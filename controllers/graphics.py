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
from time import perf_counter, time
from PySide2 import QtCore
from PySide2.QtCore import Slot, Qt, Signal
from threading import Thread, Timer

class GraphicsController(QtCore.QObject):
    __mainWindow = None
    update_board_waveform_signal = Signal(object)
    update_board_fft_signal = Signal(object)
    update_board_spectrogram_signal = Signal(object)
    set_curve_data_signal = Signal(list)
    set_curve_pos_signal = Signal(int)
    set_fttCurve_data_signal = Signal(list)
    set_waterfall_image_signal = Signal(list)
    set_waterfall_fps_signal = Signal(float)
    def __init__(self, parent) -> None:
        super().__init__()
        self.__mainWindow = parent
        self.default_pen = pg.mkPen(width=1, color='y')
        self.default_pen.setStyle(Qt.PenStyle.SolidLine)
        self.createDefinitions()
        self.add_input_devices()
        self.createWaveformPlot()
        self.createFftPlot()
        self.create_spectrogram_graphic()
        self.connectSignals()
        # pg.setConfigOptions(useOpenGL=True)
        # pg.setConfigOption('enableExperimental', True)

    def connectSignals(self):
        self.update_board_waveform_signal.connect(self.__mainWindow.update_board_waveform)
        self.update_board_fft_signal.connect(self.__mainWindow.update_board_fft)
        self.update_board_spectrogram_signal.connect(self.__mainWindow.update_board_spectrogram)
        self.set_curve_data_signal.connect(self.set_curve_data)
        self.set_curve_pos_signal.connect(self.set_curve_pos)
        self.set_fttCurve_data_signal.connect(self.set_fftCurve_data)
        self.set_waterfall_image_signal.connect(self.setWaterfallImage)
        # self.set_waterfall_fps_signal.connect(self.setWaterfallPlotFps)

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
        self.TIMEOUT = 21
        self.fps = None
        self.EPS = 1e-8
        #identifying connected devices
        self.audiosources,self.audiosourceIDs,self.PyAudioObject = MicrophoneRecorder.listaudiodevices()
        self.recorder = MicrophoneRecorder(p=self.PyAudioObject, sample_rate=self.SAMPLE_RATE, chunksize=self.CHUNKSIZE)
        # self.recorder.stream.stop_stream()
        self.ptr = 0
        self.last_time = 0.0
        self.t_end = 0.0
        self.running = False
        self.first_run = True

    def add_input_devices(self):
        for device in self.audiosources:
            self.__mainWindow.ui.input_devices.addItem(device)
    
    def startMicrophone(self):
        self.recorder.start()

    @Slot()
    def startAll(self):
        self.__mainWindow.ui.start_btn.setEnabled(False)
        self.source_index = self.audiosourceIDs[self.__mainWindow.ui.input_devices.currentIndex()]
        self.recorder.create_stream(self.source_index)
        self.startMicrophone()
        self.startDataRetrieving()
        self.startWaveformUpdate()
        self.start_fft_data_processing()
        self.start_fft_update()
        self.start_spectrogram()
        self.running = True
    
    @Slot()
    def stopAll(self):
        if self.running:
            self.__mainWindow.ui.start_btn.setEnabled(True)
            self.stopWaveformDataRtv()
            self.stopWaveformUpdate()
            self.stop_fft_processing()
            self.stop_fft_plot()
            self.stop_spectrogram()
            self.recorder.stream.stop_stream()
            self.running = False

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

    # def start_waveform_updater_thread(self):
    #     updater_thread = Thread(target=self.retrieve_waveform_data)
    #     updater_thread.daemon = True
    #     updater_thread.start()

    def retrieve_waveform_data(self):
        self.frames = self.recorder.get_frames()
        if len(self.frames) == 0:
            self.data = np.zeros((self.recorder.chunksize,), dtype=np.int32)
        else:
            self.data = self.frames[-1]
            # self.curve.setData(x=self.TIME_VECTOR*100, y=self.data)
            self.waveform_values = [self.TIME_VECTOR*100, self.data]
            self.t_end = time()
            if(self.frames[0][0] != 0):
                self.ptr += (self.t_end - self.last_time)
            # if(t_end - self.last_time >= 0.5):
            self.last_time = time()
            # self.curve.setPos(self.ptr, 0)
            self.waveform_values_dict = {"x": (self.TIME_VECTOR*100).tolist(),
                           "y": self.data.tolist(),
                           "ptr": self.ptr}
        self.waveformDataTimer = Timer(self.TIMEOUT/1000, function=self.retrieve_waveform_data)
        self.waveformDataTimer.daemon = True
        self.waveformDataTimer.start()

    def update_waveform(self):
        self.set_curve_data_signal.emit(self.waveform_values)
        self.set_curve_pos_signal.emit(self.ptr)
        self.update_board_waveform_signal.emit(self.waveform_values_dict)
        self.waveformTimer = Timer((self.TIMEOUT+100)/1000, function=self.update_waveform)
        self.waveformTimer.daemon = True
        self.waveformTimer.start()

    def set_curve_data(self, values):
        self.curve.setData(x=values[0], y=values[1])

    def set_curve_pos(self, value):
        self.curve.setPos(value, 0)
    
    def startDataRetrieving(self):
        # self.waveformTimer = QtCore.QTimer()
        self.last_time = time()
        self.waveformDataTimer = Timer(self.TIMEOUT/1000, function=self.retrieve_waveform_data)
        # self.waveformTimer.timeout.connect(timerCallback)
        self.waveformDataTimer.daemon = True
        self.waveformDataTimer.start()

    def startWaveformUpdate(self):
        self.waveformTimer = Timer((self.TIMEOUT+100)/1000, function=self.update_waveform)
        self.waveformTimer.daemon = True
        self.waveformTimer.start()

    def stopWaveformUpdate(self):
        self.waveformTimer.cancel()
    
    def stopWaveformDataRtv(self):
        self.waveformDataTimer.cancel()

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
    
    # def start_fft_updater_thread(self):
    #     fft_updater_thread = Thread(target=self.update_fft)
    #     fft_updater_thread.daemon = True
    #     fft_updater_thread.start()

    def process_fft_data(self):
        if self.first_run:
            self.data = np.zeros((self.recorder.chunksize,), dtype=np.int32)
            self.first_run = False
        if self.data.max() > 1:
            X = np.abs(np.fft.rfft(np.hanning(self.data.size) * self.data, n=self.N_FFT))
            magn = 20 * np.log10(X + self.EPS)
            # self.fft_curve.setData(x=self.FREQ_VECTOR, y=magn)
            self.values = [self.FREQ_VECTOR, magn]
            self.valuesBoardFFt = [self.FREQ_VECTOR.tolist(), magn.tolist()]
            # self.fft_plot.enableAutoRange('y', True)
            data = np.log10(X + 1e-12)
            self.waterfall_data.append(data)
            self.update_board_spectrogram_signal.emit(data.tolist())
        self.timer_fft_processing = Timer((self.TIMEOUT+80)/1000, function=self.process_fft_data)
        self.timer_fft_processing.daemon = True
        self.timer_fft_processing.start()

    def set_fftCurve_data(self, values):
        self.fft_curve.setData(x=values[0], y=values[1])
        self.fft_plot.enableAutoRange('y', True)

    def update_fft_plot(self):
        self.set_fttCurve_data_signal.emit(self.values)
        self.update_board_fft_signal.emit(self.valuesBoardFFt)
        self.update_fft_timer = Timer((self.TIMEOUT+200)/1000, function=self.update_fft_plot)
        self.update_fft_timer.daemon = True
        self.update_fft_timer.start()

    def start_fft_data_processing(self):
        self.timer_fft_processing = Timer((self.TIMEOUT+80)/1000, function=self.process_fft_data)
        # self.timer_fft.timeout.connect(self.start_fft_updater_thread)
        self.timer_fft_processing.daemon = True
        self.timer_fft_processing.start()

    def start_fft_update(self):
        self.update_fft_timer = Timer((self.TIMEOUT+200)/1000, function=self.update_fft_plot)
        self.update_fft_timer.daemon = True
        self.update_fft_timer.start()

    def stop_fft_processing(self):
        self.timer_fft_processing.cancel()

    def stop_fft_plot(self):
        self.update_fft_timer.cancel()

    # win.nextRow()
    def create_spectrogram_graphic(self):
        # image_data = np.random.rand(20, 20)
        self.waterfall_plot = pg.PlotWidget(title='Espectrograma', colspan=2)
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
            values = [arr,min,max]
            # self.waterfall_image.setImage(arr, levels=(min, max), autoLevels=False)
            self.set_waterfall_image_signal.emit(values)
            # now = perf_counter()
            # dt = now - self.last_time
            # self.last_time = now
            # if self.fps is None:
            #     self.fps = 1.0/dt
            # else:
            #     s = np.clip(dt*3., 0, 1)
            #     self.fps = self.fps * (1-s) + (1.0/dt) * s
            # self.waterfall_plot.setTitle('%0.2f fps' % self.fps)
            # self.set_waterfall_fps_signal.emit(self.fps)
        self.timer_waterfall = Timer((self.TIMEOUT+1000)/1000, function=self.update_waterfall)
        self.timer_waterfall.daemon = True
        self.timer_waterfall.start()

    def setWaterfallImage(self, values):
        self.waterfall_image.setImage(values[0], levels=(values[1], values[2]), autoLevels=False)

    # def setWaterfallPlotFps(self, fps):
    #     self.waterfall_plot.setTitle('%0.2f fps' % fps)

    def start_spectrogram(self):
        self.timer_waterfall = Timer((self.TIMEOUT+1000)/1000, function=self.update_waterfall)
        # self.timer_waterfall.timeout.connect(self.update_waterfall)
        self.timer_waterfall.daemon = True
        self.timer_waterfall.start()
    
    def stop_spectrogram(self):
        self.timer_waterfall.cancel()

    # if __name__ == '__main__':
    #     import sys

    #     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    #         pg.exec()
