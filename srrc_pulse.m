function [pulse, time] = srrc_pulse(T, over, A, beta)
% Input:
%   T:  Nyquist parameter or symbol period  (positive real number)                  
%   over: positive integer equal to T/T_s (oversampling factor)              
%   A:  half duration of the pulse in symbol periods (positive integer)             
%   beta:  roll-off factor (real number between 0 and 1)    
% Output:
%   phi: truncated SRRC pulse, with parameter T, roll-off factor a, and duration 2*A*T                         %
%   t:   time axis of the truncated pulse

Ts = T/over; 

% Create time axis
time = (-A*T:Ts:A*T) + 10^(-8); % in order to avoid division by zero problems at t=0.

num = cos((1+beta)*pi*time/T) + sin((1-beta)*pi*time/T) ./ (4*beta*time/T);
denom = 1-(4*beta*time./T).^2;
pulse = 2*beta/(pi*sqrt(T)) * num ./ denom;

end
