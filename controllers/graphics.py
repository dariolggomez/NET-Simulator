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
from PySide2.QtCore import Slot

class GraphicsController():
    __mainWindow = None
    def __init__(self, parent) -> None:
        self.__mainWindow = parent
        self.createDefinitions()
        self.createWaveformPlot()

    def generatePgColormap(cm_name):
        """Converts a matplotlib colormap to a pyqtgraph colormap."""
        colormap = plt.get_cmap(cm_name)
        colormap._init()
        lut = (colormap._lut * 255).view(np.ndarray)  # Convert matplotlib colormap from 0-1 to 0 -255 for Qt
        return lut

    def createDefinitions(self):
        self.CHUNKSIZE = 1024
        self.SAMPLE_RATE = 48000
        self.TIME_VECTOR = np.arange(self.CHUNKSIZE) / self.SAMPLE_RATE
        self.N_FFT = 1024
        self.FREQ_VECTOR = np.fft.rfftfreq(self.N_FFT, d=self.TIME_VECTOR[1] - self.TIME_VECTOR[0])
        self.WATERFALL_FRAMES = int(250 * 2048 // self.N_FFT)
        self.TIMEOUT = int(self.TIME_VECTOR.max() * 1000)
        self.fps = None
        self.EPS = 1e-8
        self.ptr = 0
        self.last_time = perf_counter()
    
    def startMicrophone(self):
        self.recorder = MicrophoneRecorder(sample_rate=self.SAMPLE_RATE, chunksize=self.CHUNKSIZE)
        self.recorder.start()

    # win = pg.GraphicsLayoutWidget(show=True)
    # win.resize(1000, 600)
    # win.setWindowTitle('pyqtgraph spectrographer')

    def createWaveformPlot(self):
        self.waveform_plot = pg.PlotWidget(name="Forma de Onda")
        self.waveform_plot.showGrid(x=True, y=True)
        self.waveform_plot.enableAutoRange('x', True)
        # waveform_plot.setXRange(TIME_VECTOR.min(), TIME_VECTOR.max())
        self.waveform_plot.setYRange(-2 ** 15, 2 ** 15 - 1)
        self.waveform_plot.setLabel('left', "Señal", units='A.U.')
        self.waveform_plot.setLabel('bottom', "Tiempo", units='s')
        self.curve = self.waveform_plot.plot(pen='y')
        self.__mainWindow.ui.waveform_layout.addWidget(self.waveform_plot)


    def update_waveform(self):
        self.frames = self.recorder.get_frames()
        if len(self.frames) == 0:
            self.data = np.zeros((self.recorder.chunksize,), dtype=np.int64)
        else:
            self.data = self.frames[-1]
            self.curve.setData(x=self.TIME_VECTOR*100, y=self.data)
            if(self.frames[0][0] != 0):
                self.ptr += self.TIMEOUT
                self.curve.setPos(self.ptr, 0)
    @Slot()
    def startWaveform(self):
        self.startMicrophone()
        self.waveformTimer = QtCore.QTimer()
        self.waveformTimer.timeout.connect(self.update_waveform)
        self.waveformTimer.start(self.TIMEOUT)
    @Slot()
    def stopWaveform(self):
        self.waveformTimer.stop()

    # fft_plot = win.addPlot(title='FFT plot')
    # fft_curve = fft_plot.plot(pen='y')
    # fft_plot.enableAutoRange('xy', False)
    # fft_plot.showGrid(x=True, y=True)
    # fft_plot.setXRange(FREQ_VECTOR.min(), FREQ_VECTOR.max())
    # fft_plot.setYRange(20 * np.log10(2 ** 11 * CHUNKSIZE) - 100, 20 * np.log10(2 ** 11 * CHUNKSIZE))
    # fft_plot.setLabel('left', "Amplitude", units='A.U.')
    # fft_plot.setLabel('bottom', "Frequency", units='Hz')

    # waterfall_data = deque(maxlen=WATERFALL_FRAMES)


    # def update_fft():
    #     global data, fft_curve, fft_plot
    #     if data.max() > 1:
    #         X = np.abs(np.fft.rfft(np.hanning(data.size) * data, n=N_FFT))
    #         magn = 20 * np.log10(X + EPS)
    #         fft_curve.setData(x=FREQ_VECTOR, y=magn)
    #         waterfall_data.append(np.log10(X + 1e-12))


    # timer_fft = QtCore.QTimer()
    # timer_fft.timeout.connect(update_fft)
    # timer_fft.start(TIMEOUT)

    # win.nextRow()

    # image_data = np.random.rand(20, 20)
    # waterfall_plot = win.addPlot(title='Waterfall plot', colspan=2)
    # waterfall_plot.setLabel('left', "Frequency", units='Hz')
    # waterfall_plot.showAxis('bottom', False)
    # # waterfall_plot.setLabel('bottom', "Time", units='s')
    # waterfall_plot.setXRange(0, WATERFALL_FRAMES * TIME_VECTOR.max())
    # # waterfall_plot.enableAutoRange('x', True)
    # waterfall_image = pg.ImageItem()
    # waterfall_plot.addItem(waterfall_image)
    # waterfall_image.setImage(image_data)
    # lut = generatePgColormap('jet')
    # waterfall_image.setLookupTable(lut)
    # tr = QtGui.QTransform()
    # tr.scale((CHUNKSIZE / SAMPLE_RATE), FREQ_VECTOR.max() * 2. / N_FFT)
    # # set scale: x in seconds, y in Hz
    # waterfall_image.setTransform(tr)


    # def update_waterfall():
    #     global waterfall_data, waterfall_image, last_time, fps, waterfall_plot
    #     arr = np.c_[waterfall_data]
    #     if arr.size > 0:
    #         if arr.ndim == 1:
    #             arr = arr[:, np.newaxis]
    #         max = arr.max()
    #         min = max / 10
    #         waterfall_image.setImage(arr, levels=(min, max))
    #         now = perf_counter()
    #         dt = now - last_time
    #         last_time = now
    #         if fps is None:
    #             fps = 1.0/dt
    #         else:
    #             s = np.clip(dt*3., 0, 1)
    #             fps = fps * (1-s) + (1.0/dt) * s
    #         waterfall_plot.setTitle('%0.2f fps' % fps)


    # timer_waterfall = QtCore.QTimer()
    # timer_waterfall.timeout.connect(update_waterfall)
    # timer_waterfall.start(TIMEOUT)

    # if __name__ == '__main__':
    #     import sys

    #     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    #         pg.exec()
