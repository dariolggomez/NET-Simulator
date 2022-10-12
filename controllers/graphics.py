# -*- coding: utf-8 -*-
"""
This is the main file to launch pyqtgraph-spectrographer.
"""

from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
from services.receptor import MicrophoneRecorder
from time import perf_counter
from PySide2 import QtCore
from PySide2.QtCore import Slot, Qt, Signal
from threading import Thread

class GraphicsController(QtCore.QObject):
    __mainWindow = None
    update_waveform_signal = Signal(object)
    set_curve_data_signal = Signal(list)
    set_curve_pos_signal = Signal(int)
    set_fttCurve_data_signal = Signal(list)
    def __init__(self, parent) -> None:
        super().__init__()
        self.__mainWindow = parent
        self.default_pen = pg.mkPen(width=1, color='y')
        self.default_pen.setStyle(Qt.PenStyle.SolidLine)
        self.createDefinitions()
        self.createWaveformPlot()
        self.createFftPlot()
        self.create_spectrogram_graphic()
        self.connectSignals()
        # pg.setConfigOptions(useOpenGL=True)
        # pg.setConfigOption('enableExperimental', True)

    def connectSignals(self):
        self.update_waveform_signal.connect(self.__mainWindow.update_board_waveform)
        self.set_curve_data_signal.connect(self.set_curve_data)
        self.set_curve_pos_signal.connect(self.set_curve_pos)
        self.set_fttCurve_data_signal.connect(self.set_fftCurve_data)

    def generatePgColormap(self, cm_name):
        """Converts a matplotlib colormap to a pyqtgraph colormap."""
        colormap = plt.get_cmap(cm_name)
        colormap._init()
        lut = (colormap._lut * 255).view(np.ndarray)  # Convert matplotlib colormap from 0-1 to 0 -255 for Qt
        return lut

    def createDefinitions(self):
        sfmt = QtGui.QSurfaceFormat()
        sfmt.setSwapInterval(0)
        QtGui.QSurfaceFormat.setDefaultFormat(sfmt)
        self.CHUNKSIZE = 1024
        self.SAMPLE_RATE = 44100
        self.TIME_VECTOR = np.arange(self.CHUNKSIZE) / self.SAMPLE_RATE
        self.N_FFT = 1024
        self.FREQ_VECTOR = np.fft.rfftfreq(self.N_FFT, d=self.TIME_VECTOR[1] - self.TIME_VECTOR[0])
        self.WATERFALL_FRAMES = int(250 * 2048 // self.N_FFT)
        self.TIMEOUT = 151
        self.fps = None
        self.EPS = 1e-8
        self.ptr = 0
        self.last_time = perf_counter()
        self.running = False
        self.first_run = True
    
    def startMicrophone(self):
        self.recorder = MicrophoneRecorder(sample_rate=self.SAMPLE_RATE, chunksize=self.CHUNKSIZE)
        self.recorder.start()

    # win = pg.GraphicsLayoutWidget(show=True)
    # win.resize(1000, 600)
    # win.setWindowTitle('pyqtgraph spectrographer')

    def createWaveformPlot(self):
        self.waveform_plot = pg.PlotWidget(title="Forma de Onda")
        self.waveform_plot.showGrid(x=False, y=True)
        self.waveform_plot.enableAutoRange('x', True)
        self.waveform_plot.setMouseEnabled(x=False, y=True)
        # waveform_plot.setXRange(TIME_VECTOR.min(), TIME_VECTOR.max())
        self.waveform_plot.setYRange(-2 ** 15, 2 ** 15 - 1)
        self.waveform_plot.setLabel('left', "Señal", units='A.U.')
        self.waveform_plot.setLabel('bottom', "Tiempo", units='s')
        self.curve = self.waveform_plot.plot(pen=self.default_pen, skipFiniteCheck=True)
        self.__mainWindow.ui.waveform_layout.addWidget(self.waveform_plot)

    def start_waveform_updater_thread(self):
        updater_thread = Thread(target=self.update_waveform)
        updater_thread.daemon = True
        updater_thread.start()

    def update_waveform(self):
        self.frames = self.recorder.get_frames()
        if len(self.frames) == 0:
            self.data = np.zeros((self.recorder.chunksize,), dtype=np.int32)
        else:
            self.data = self.frames[-1]
            # self.curve.setData(x=self.TIME_VECTOR*100, y=self.data)
            values = [self.TIME_VECTOR*100, self.data]
            self.set_curve_data_signal.emit(values)
            # t_end = perf_counter()
            if(self.frames[0][0] != 0):
                self.ptr += self.TIMEOUT
            # if(t_end - self.last_time >= 0.5):
            # self.last_time = perf_counter()
            # self.curve.setPos(self.ptr, 0)
            self.set_curve_pos_signal.emit(self.ptr)
            values_dict = {"x": (self.TIME_VECTOR*100).tolist(),
                           "y": self.data.tolist(),
                           "ptr": self.ptr}
            self.update_waveform_signal.emit(values_dict)

    def set_curve_data(self, values):
        self.curve.setData(x=values[0], y=values[1])

    def set_curve_pos(self, value):
        self.curve.setPos(value, 0)
    
    @Slot()
    def startAll(self):
        self.startMicrophone()
        self.startWaveform()
        self.start_fft_plot()
        self.start_spectrogram()
        self.running = True
    
    @Slot()
    def stopAll(self):
        if self.running:
            self.stopWaveform()
            self.stop_fft_plot()
            self.stop_spectrogram()
            self.recorder.stop = True
            self.running = False

    def startWaveform(self):
        self.waveformTimer = QtCore.QTimer()
        self.waveformTimer.timeout.connect(self.start_waveform_updater_thread)
        self.waveformTimer.start(self.TIMEOUT)
    
    def stopWaveform(self):
        self.waveformTimer.stop()

    def createFftPlot(self):
        self.fft_plot = pg.PlotWidget(title='Transformada de Fourier')
        self.fft_curve = pg.PlotCurveItem(pen=self.default_pen, skipFiniteCheck=True)
        self.fft_plot.addItem(self.fft_curve)
        self.fft_plot.autoRange()
        self.fft_plot.setMouseEnabled(x=False, y=True)
        self.fft_plot.showGrid(x=True, y=True)
        self.fft_plot.setXRange(self.FREQ_VECTOR.min(), self.FREQ_VECTOR.max())
        # self.fft_plot.setYRange(20 * np.log10(2 ** 11 * self.CHUNKSIZE) - 100, 20 * np.log10(2 ** 11 * self.CHUNKSIZE))
        self.fft_plot.setLabel('left', "Amplitud", units='A.U.')
        self.fft_plot.setLabel('bottom', "Frecuencia", units='Hz')
        self.__mainWindow.ui.fft_transform_layout.addWidget(self.fft_plot)
        self.waterfall_data = deque(maxlen=self.WATERFALL_FRAMES)
    
    def start_fft_updater_thread(self):
        fft_updater_thread = Thread(target=self.update_fft)
        fft_updater_thread.daemon = True
        fft_updater_thread.start()

    def update_fft(self):
        if self.first_run:
            self.data = np.zeros((self.recorder.chunksize,), dtype=np.int32)
            self.first_run = False
        if self.data.max() > 1:
            X = np.abs(np.fft.rfft(np.hanning(self.data.size) * self.data, n=self.N_FFT))
            magn = 20 * np.log10(X + self.EPS)
            # self.fft_curve.setData(x=self.FREQ_VECTOR, y=magn)
            values = [self.FREQ_VECTOR, magn]
            self.set_fttCurve_data_signal.emit(values)
            # self.fft_plot.enableAutoRange('y', True)
            self.waterfall_data.append(np.log10(X + 1e-12))

    def set_fftCurve_data(self, values):
        self.fft_curve.setData(x=values[0], y=values[1])
        self.fft_plot.enableAutoRange('y', True)

    def start_fft_plot(self):
        self.timer_fft = QtCore.QTimer()
        self.timer_fft.timeout.connect(self.start_fft_updater_thread)
        self.timer_fft.start(self.TIMEOUT)

    def stop_fft_plot(self):
        self.timer_fft.stop()

    # win.nextRow()
    def create_spectrogram_graphic(self):
        # image_data = np.random.rand(20, 20)
        self.waterfall_plot = pg.PlotWidget(title='Waterfall plot', colspan=2)
        self.waterfall_plot.setLabel('left', "Frecuencia", units='Hz')
        self.waterfall_plot.showAxis('bottom', False)
        # waterfall_plot.setLabel('bottom', "Time", units='s')
        self.waterfall_plot.setXRange(0, self.WATERFALL_FRAMES * self.TIME_VECTOR.max())
        # waterfall_plot.enableAutoRange('x', True)
        self.waterfall_image = pg.ImageItem()
        self.waterfall_plot.addItem(self.waterfall_image)
        # waterfall_image.setImage(image_data)
        lut = self.generatePgColormap('jet')
        self.waterfall_image.setLookupTable(lut)
        tr = QtGui.QTransform()
        tr.scale((self.CHUNKSIZE / self.SAMPLE_RATE), self.FREQ_VECTOR.max() * 2. / self.N_FFT)
        # set scale: x in seconds, y in Hz
        self.waterfall_image.setTransform(tr)
        self.__mainWindow.ui.spectrogram_layout.addWidget(self.waterfall_plot)


    def update_waterfall(self):
        arr = np.c_[self.waterfall_data]
        if arr.size > 0:
            if arr.ndim == 1:
                arr = arr[:, np.newaxis]
            max = arr.max()
            min = max / 10
            self.waterfall_image.setImage(arr, levels=(min, max), autoLevels=False)
            now = perf_counter()
            dt = now - self.last_time
            self.last_time = now
            if self.fps is None:
                self.fps = 1.0/dt
            else:
                s = np.clip(dt*3., 0, 1)
                self.fps = self.fps * (1-s) + (1.0/dt) * s
            self.waterfall_plot.setTitle('%0.2f fps' % self.fps)

    def start_spectrogram(self):
        self.timer_waterfall = QtCore.QTimer()
        self.timer_waterfall.timeout.connect(self.update_waterfall)
        self.timer_waterfall.start(self.TIMEOUT)
    
    def stop_spectrogram(self):
        self.timer_waterfall.stop()

    # if __name__ == '__main__':
    #     import sys

    #     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    #         pg.exec()
