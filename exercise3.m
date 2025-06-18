clear;          % Clear the workspace
close all;      % Close all figure windows
clc;            % Clear the command window

% bertool

%% Parameters
T = 0.1;            % Symbol period (in seconds)
over = 10;          % Oversampling factor
a = 0.5;            % Roll-off factor (between 0 and 1)
A = 10;              % Half duration of the pulse in symbol periods (positive integer)
Ts = T/over;        % Sampling period (symbol period divided by oversampling factor)
Fs = 1/Ts;          % Sampling frequency (inverse of the sampling period)
N = 1e6;          % Number of symbols to simulate

%% Transmitter
b = (sign(randn(N,1))+1)/2;   % Generate random bits (0 or 1), using a Gaussian distribution
symbols = 2*b-1;               % Map bits to symbols (-1 for bit 0, +1 for bit 1)

% Upsampling: Increase the symbol rate by the oversampling factor
X_delta = Fs*upsample(symbols, over);  % Upsample the symbols by the oversampling factor
time = linspace(0, N*T, N*over);       % Time vector for the upsampled signal

% Create a square root raised cosine pulse (using custom function 'srrc_pulse')
[phi, t] = srrc_pulse(T, over, A, a);  % Generate SRRC pulse based on parameters

% phi = ones(1, over); % Simple rectangular pulse
% t = -T/2:Ts:T/2; 

% Convolution at the transmitter: shape the symbols using the SRRC pulse
X = conv(phi, X_delta)*Ts;          % Convolve the upsampled symbols with the pulse
X_time = time(1)+t(1):Ts:time(end)+t(end)-Ts;  % Time vector after convolution

% % Define sampling times: Sample the received signal at integer multiples of symbol period
% sample_times = (0:N-1)*T;          % From 0 to the end with step size T (symbol period)
% idx = ismember(round(X_time,2), round(sample_times,2)) > 0;  % Find the indices where the times match
% X_sampled = X(idx);

%% Receiver with the same SRRC pulse

% Create the same square root raised cosine pulse for the receiver
[h1, h1_time] = srrc_pulse(T, over, A, a);

% h1 = ones(1, over); % Simple rectangular pulse
% h1_time = -T/2:Ts:T/2; 

% Convolution at the receiver: apply the pulse shaping filter to the received signal
Y = conv(X, h1)*Ts;                % Convolve the transmitted signal with the receiver's filter
Y_time = X_time(1)+h1_time(1):Ts:X_time(end)+h1_time(end);  % Time vector after convolution

%% Calculate bit error rate (BER)

% Define sampling times: Sample the received signal at integer multiples of symbol period
sample_times = (0:N-1)*T;          % From 0 to the end with step size T (symbol period)
idx = ismember(round(Y_time,2), round(sample_times,2)) > 0;  % Find the indices where the times match
Y_sampled = Y(idx);                      % Extract the sampled received signal

% Eb = (max(abs(Y_sampled))^2)*T;
msv = (max(abs(Y_sampled))^2);
% Define range of noise variances (sigma represents the standard deviation of the noise)
sigma = sqrt(msv):-0.001:sqrt(msv/10);                  % Noise standard deviation values
N0 = sigma.^2;                   % Noise power spectral density (variance)
SNR = msv./(N0);                     % Eb/N0 values for different noise levels
SNR_dB = 10*log10(SNR);           % Eb/N0 in decibels

% Initialize error counter to store BER values for each noise level
BER = zeros(size(sigma));  % Preallocate for Bit Error Rate (BER) values
% Loop over each noise level (different sigma values)
for i = 1:length(sigma)
    s = sigma(i);          % Get the current noise standard deviation

    % Generate Gaussian noise with standard deviation 's'
    noise = sqrt(N0(i)/2)*randn(size(Y));  % Create noise with the specified standard deviation

    % Add noise to the received signal
    Y_noisy = Y+noise;          % Noisy received signal
    Y_sampled = Y_noisy(idx);     % Sample noisy signal 

    % Decision Rule: Detect symbols based on the sign of the sampled signal
    detected_symbols = sign(Y_sampled);  % Map the received samples to symbols (-1 or +1)

    % Compare detected symbols with the original transmitted symbols
    errors = sum(detected_symbols ~= symbols);      % Count the number of errors

    % Compute Bit Error Rate (BER) for the current noise level
    BER(i) = errors/length(symbols);  % Ratio of errors to total number of symbols
end

% Theoretical BER for BPSK using the Q-function (standard formula for BPSK in AWGN)
BER_theory = qfunc(sqrt(2*SNR));  % Q-function approximation for BPSK

%% Plot the results
% bertool
% figure;  % Create a new figure
hold on;
semilogy(SNR_dB, BER_theory,"g-square", "DisplayName","Theoretical","LineWidth",2);  % Plot theoretical BER for BPSK
semilogy(SNR_dB, BER, "r*", "DisplayName", "Experimental","LineWidth",2);  % Plot BER vs. SNR (log scale for BER)
grid on;  % Enable grid on the plot
title("Bit Error Rate vs SNR");  % Set plot title
xlabel("SNR (dB)");  % X-axis label
ylabel("BER");        % Y-axis label
legend();