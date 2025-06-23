#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: native
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class test3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "test3")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.over = over = 100
        self.symb_rate = symb_rate = samp_rate/over
        self.qpsk = qpsk = [-1-1j,-1+1j,1+1j,1-1j]
        self.gain = gain = 20
        self.fc = fc = 10000
        self.bpsk = bpsk = [-1,+1]

        ##################################################
        # Blocks
        ##################################################

        self.root_raised_cosine_filter_0_1_0 = filter.interp_fir_filter_fff(
            over,
            firdes.root_raised_cosine(
                gain,
                samp_rate,
                symb_rate,
                0.5,
                (11*samp_rate)))
        self.root_raised_cosine_filter_0_1 = filter.interp_fir_filter_fff(
            over,
            firdes.root_raised_cosine(
                gain,
                samp_rate,
                symb_rate,
                0.5,
                (11*samp_rate)))
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_if(bpsk, 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_if(bpsk, 1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fc, 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fc, 1, 0, 0)
        self.analog_random_source_x_0_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000000))), True)
        self.analog_random_source_x_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 2, 1000000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_random_source_x_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.root_raised_cosine_filter_0_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.root_raised_cosine_filter_0_1_0, 0))
        self.connect((self.root_raised_cosine_filter_0_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_1_0, 0), (self.blocks_multiply_xx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_symb_rate(self.samp_rate/self.over)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(self.gain, self.samp_rate, self.symb_rate, 0.5, (11*self.samp_rate)))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(self.gain, self.samp_rate, self.symb_rate, 0.5, (11*self.samp_rate)))

    def get_over(self):
        return self.over

    def set_over(self, over):
        self.over = over
        self.set_symb_rate(self.samp_rate/self.over)

    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(self.gain, self.samp_rate, self.symb_rate, 0.5, (11*self.samp_rate)))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(self.gain, self.samp_rate, self.symb_rate, 0.5, (11*self.samp_rate)))

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(self.gain, self.samp_rate, self.symb_rate, 0.5, (11*self.samp_rate)))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(self.gain, self.samp_rate, self.symb_rate, 0.5, (11*self.samp_rate)))

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.analog_sig_source_x_0_1.set_frequency(self.fc)
        self.analog_sig_source_x_0_1_0.set_frequency(self.fc)

    def get_bpsk(self):
        return self.bpsk

    def set_bpsk(self, bpsk):
        self.bpsk = bpsk
        self.digital_chunks_to_symbols_xx_0.set_symbol_table(self.bpsk)
        self.digital_chunks_to_symbols_xx_0_0.set_symbol_table(self.bpsk)




def main(top_block_cls=test3, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
