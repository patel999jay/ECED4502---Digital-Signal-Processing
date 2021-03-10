#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Filter Introduction
# Author: Jay Patel
# Description: FIR Filter Introduction
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class filter_taps(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Filter Introduction")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Filter Introduction")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
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

        self.settings = Qt.QSettings("GNU Radio", "filter_taps")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.transition = transition = 2000
        self.sps = sps = 2
        self.samp_rate = samp_rate = 32000
        self.lp_cutoff = lp_cutoff = 14000
        self.hp_cutoff = hp_cutoff = 2000
        self.bp_low = bp_low = 6000
        self.bp_high = bp_high = 10000
        self.sym_rate = sym_rate = samp_rate/sps
        self.lp_taps_value_no = lp_taps_value_no = print("\nThis is number of Low pass filter taps :- \t",len(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76)))
        self.lp_taps_value = lp_taps_value = print("\nThis is Low Pass coefficient : \t",firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))
        self.hp_taps_value_no = hp_taps_value_no = print("\nThis is number of High pass filter taps :- \t",len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76)))
        self.hp_taps_value = hp_taps_value = print("\nThis is High Pass coefficient : \t",firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))
        self.bp_taps_value_no_0 = bp_taps_value_no_0 = print("\nThis is number of Band pass filter taps:- \t",len(firdes.band_pass(1.0, samp_rate, bp_low, bp_high, transition, firdes.WIN_HAMMING, 6.76)))
        self.bp_taps_value = bp_taps_value = print("\nThis is Band Pass coefficient : \t", firdes.band_pass(1.0, samp_rate, bp_low, bp_high, transition, firdes.WIN_HAMMING, 6.76))
        self.LP_Filter_Taps = LP_Filter_Taps = len(firdes.low_pass(1, samp_rate, lp_cutoff, transition, firdes.WIN_RECTANGULAR, 6.76))
        self.HP_Filter_Taps = HP_Filter_Taps = len(firdes.high_pass(1, samp_rate, hp_cutoff, transition, firdes.WIN_HAMMING, 6.76))
        self.BP_Filter_Taps = BP_Filter_Taps = len(firdes.high_pass(1, samp_rate, hp_cutoff, transition, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Blocks
        ##################################################
        self._transition_range = Range(500, 15000, 100, 2000, 200)
        self._transition_win = RangeWidget(self._transition_range, self.set_transition, 'Transition width', "counter_slider", int)
        self.top_grid_layout.addWidget(self._transition_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lp_cutoff_range = Range(1000, 16000, 1000, 14000, 200)
        self._lp_cutoff_win = RangeWidget(self._lp_cutoff_range, self.set_lp_cutoff, 'LP Cutoff', "counter_slider", int)
        self.top_grid_layout.addWidget(self._lp_cutoff_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._hp_cutoff_range = Range(1000, 15000, 1000, 2000, 200)
        self._hp_cutoff_win = RangeWidget(self._hp_cutoff_range, self.set_hp_cutoff, 'HP Cutoff', "counter_slider", int)
        self.top_grid_layout.addWidget(self._hp_cutoff_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._bp_low_range = Range(1000, 8000, 1000, 6000, 200)
        self._bp_low_win = RangeWidget(self._bp_low_range, self.set_bp_low, 'BP Low-cutoff', "counter_slider", int)
        self.top_grid_layout.addWidget(self._bp_low_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._bp_high_range = Range(9000, 15000, 1000, 10000, 200)
        self._bp_high_win = RangeWidget(self._bp_high_range, self.set_bp_high, 'BP High-cutoff', "counter_slider", int)
        self.top_grid_layout.addWidget(self._bp_high_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            4096, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            4
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

        labels = ['Low-pass', 'High-pass', 'Band-pass', 'Band-reject', 'RRC',
            'Custom Low Pass Filter', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "magenta",
            "black", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [0.9, 0.9, 0.9, 0.9, 0.9,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 2, 0, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                lp_cutoff,
                transition,
                firdes.WIN_RECTANGULAR,
                6.76))
        self.high_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.high_pass(
                1,
                samp_rate,
                hp_cutoff,
                transition,
                firdes.WIN_HAMMING,
                6.76))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.band_reject_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_reject(
                1,
                samp_rate,
                bp_low,
                bp_high,
                transition,
                firdes.WIN_BLACKMAN,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                bp_low,
                bp_high,
                transition,
                firdes.WIN_HANN,
                6.76))
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_f(analog.GR_GAUSSIAN, 1, 0, 8192)
        self._LP_Filter_Taps_tool_bar = Qt.QToolBar(self)

        if None:
            self._LP_Filter_Taps_formatter = None
        else:
            self._LP_Filter_Taps_formatter = lambda x: str(x)

        self._LP_Filter_Taps_tool_bar.addWidget(Qt.QLabel('LP Filter Taps' + ": "))
        self._LP_Filter_Taps_label = Qt.QLabel(str(self._LP_Filter_Taps_formatter(self.LP_Filter_Taps)))
        self._LP_Filter_Taps_tool_bar.addWidget(self._LP_Filter_Taps_label)
        self.top_grid_layout.addWidget(self._LP_Filter_Taps_tool_bar, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._HP_Filter_Taps_tool_bar = Qt.QToolBar(self)

        if None:
            self._HP_Filter_Taps_formatter = None
        else:
            self._HP_Filter_Taps_formatter = lambda x: eng_notation.num_to_str(x)

        self._HP_Filter_Taps_tool_bar.addWidget(Qt.QLabel('HP Filter Taps' + ": "))
        self._HP_Filter_Taps_label = Qt.QLabel(str(self._HP_Filter_Taps_formatter(self.HP_Filter_Taps)))
        self._HP_Filter_Taps_tool_bar.addWidget(self._HP_Filter_Taps_label)
        self.top_grid_layout.addWidget(self._HP_Filter_Taps_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._BP_Filter_Taps_tool_bar = Qt.QToolBar(self)

        if None:
            self._BP_Filter_Taps_formatter = None
        else:
            self._BP_Filter_Taps_formatter = lambda x: eng_notation.num_to_str(x)

        self._BP_Filter_Taps_tool_bar.addWidget(Qt.QLabel('BP Filter Taps' + ": "))
        self._BP_Filter_Taps_label = Qt.QLabel(str(self._BP_Filter_Taps_formatter(self.BP_Filter_Taps)))
        self._BP_Filter_Taps_tool_bar.addWidget(self._BP_Filter_Taps_label)
        self.top_grid_layout.addWidget(self._BP_Filter_Taps_tool_bar, 4, 1, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.band_reject_filter_0, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.band_reject_filter_0, 0), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "filter_taps")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.set_BP_Filter_Taps(self._BP_Filter_Taps_formatter(len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_HP_Filter_Taps(self._HP_Filter_Taps_formatter(len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_LP_Filter_Taps(self._LP_Filter_Taps_formatter(len(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))))
        self.set_bp_taps_value(print("\nThis is Band Pass coefficient : \t", firdes.band_pass(1.0, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HAMMING, 6.76)))
        self.set_bp_taps_value_no_0(print("\nThis is number of Band pass filter taps:- \t",len(firdes.band_pass(1.0, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_hp_taps_value(print("\nThis is High Pass coefficient : \t",firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76)))
        self.set_hp_taps_value_no(print("\nThis is number of High pass filter taps :- \t",len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_lp_taps_value(print("\nThis is Low Pass coefficient : \t",firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76)))
        self.set_lp_taps_value_no(print("\nThis is number of Low pass filter taps :- \t",len(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HANN, 6.76))
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_BLACKMAN, 6.76))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_sym_rate(self.samp_rate/self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_BP_Filter_Taps(self._BP_Filter_Taps_formatter(len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_HP_Filter_Taps(self._HP_Filter_Taps_formatter(len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_LP_Filter_Taps(self._LP_Filter_Taps_formatter(len(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))))
        self.set_bp_taps_value(print("\nThis is Band Pass coefficient : \t", firdes.band_pass(1.0, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HAMMING, 6.76)))
        self.set_bp_taps_value_no_0(print("\nThis is number of Band pass filter taps:- \t",len(firdes.band_pass(1.0, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_hp_taps_value(print("\nThis is High Pass coefficient : \t",firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76)))
        self.set_hp_taps_value_no(print("\nThis is number of High pass filter taps :- \t",len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_lp_taps_value(print("\nThis is Low Pass coefficient : \t",firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76)))
        self.set_lp_taps_value_no(print("\nThis is number of Low pass filter taps :- \t",len(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))))
        self.set_sym_rate(self.samp_rate/self.sps)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HANN, 6.76))
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_BLACKMAN, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_lp_cutoff(self):
        return self.lp_cutoff

    def set_lp_cutoff(self, lp_cutoff):
        self.lp_cutoff = lp_cutoff
        self.set_LP_Filter_Taps(self._LP_Filter_Taps_formatter(len(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))))
        self.set_lp_taps_value(print("\nThis is Low Pass coefficient : \t",firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76)))
        self.set_lp_taps_value_no(print("\nThis is number of Low pass filter taps :- \t",len(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lp_cutoff, self.transition, firdes.WIN_RECTANGULAR, 6.76))

    def get_hp_cutoff(self):
        return self.hp_cutoff

    def set_hp_cutoff(self, hp_cutoff):
        self.hp_cutoff = hp_cutoff
        self.set_BP_Filter_Taps(self._BP_Filter_Taps_formatter(len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_HP_Filter_Taps(self._HP_Filter_Taps_formatter(len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.set_hp_taps_value(print("\nThis is High Pass coefficient : \t",firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76)))
        self.set_hp_taps_value_no(print("\nThis is number of High pass filter taps :- \t",len(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.samp_rate, self.hp_cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_bp_low(self):
        return self.bp_low

    def set_bp_low(self, bp_low):
        self.bp_low = bp_low
        self.set_bp_taps_value(print("\nThis is Band Pass coefficient : \t", firdes.band_pass(1.0, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HAMMING, 6.76)))
        self.set_bp_taps_value_no_0(print("\nThis is number of Band pass filter taps:- \t",len(firdes.band_pass(1.0, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HANN, 6.76))
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_BLACKMAN, 6.76))

    def get_bp_high(self):
        return self.bp_high

    def set_bp_high(self, bp_high):
        self.bp_high = bp_high
        self.set_bp_taps_value(print("\nThis is Band Pass coefficient : \t", firdes.band_pass(1.0, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HAMMING, 6.76)))
        self.set_bp_taps_value_no_0(print("\nThis is number of Band pass filter taps:- \t",len(firdes.band_pass(1.0, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HAMMING, 6.76))))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_HANN, 6.76))
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate, self.bp_low, self.bp_high, self.transition, firdes.WIN_BLACKMAN, 6.76))

    def get_sym_rate(self):
        return self.sym_rate

    def set_sym_rate(self, sym_rate):
        self.sym_rate = sym_rate

    def get_lp_taps_value_no(self):
        return self.lp_taps_value_no

    def set_lp_taps_value_no(self, lp_taps_value_no):
        self.lp_taps_value_no = lp_taps_value_no

    def get_lp_taps_value(self):
        return self.lp_taps_value

    def set_lp_taps_value(self, lp_taps_value):
        self.lp_taps_value = lp_taps_value

    def get_hp_taps_value_no(self):
        return self.hp_taps_value_no

    def set_hp_taps_value_no(self, hp_taps_value_no):
        self.hp_taps_value_no = hp_taps_value_no

    def get_hp_taps_value(self):
        return self.hp_taps_value

    def set_hp_taps_value(self, hp_taps_value):
        self.hp_taps_value = hp_taps_value

    def get_bp_taps_value_no_0(self):
        return self.bp_taps_value_no_0

    def set_bp_taps_value_no_0(self, bp_taps_value_no_0):
        self.bp_taps_value_no_0 = bp_taps_value_no_0

    def get_bp_taps_value(self):
        return self.bp_taps_value

    def set_bp_taps_value(self, bp_taps_value):
        self.bp_taps_value = bp_taps_value

    def get_LP_Filter_Taps(self):
        return self.LP_Filter_Taps

    def set_LP_Filter_Taps(self, LP_Filter_Taps):
        self.LP_Filter_Taps = LP_Filter_Taps
        Qt.QMetaObject.invokeMethod(self._LP_Filter_Taps_label, "setText", Qt.Q_ARG("QString", self.LP_Filter_Taps))

    def get_HP_Filter_Taps(self):
        return self.HP_Filter_Taps

    def set_HP_Filter_Taps(self, HP_Filter_Taps):
        self.HP_Filter_Taps = HP_Filter_Taps
        Qt.QMetaObject.invokeMethod(self._HP_Filter_Taps_label, "setText", Qt.Q_ARG("QString", self.HP_Filter_Taps))

    def get_BP_Filter_Taps(self):
        return self.BP_Filter_Taps

    def set_BP_Filter_Taps(self, BP_Filter_Taps):
        self.BP_Filter_Taps = BP_Filter_Taps
        Qt.QMetaObject.invokeMethod(self._BP_Filter_Taps_label, "setText", Qt.Q_ARG("QString", self.BP_Filter_Taps))





def main(top_block_cls=filter_taps, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
