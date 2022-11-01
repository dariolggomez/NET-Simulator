import pyaudio
import numpy as np
import threading
import atexit


class MicrophoneRecorder(object):
    
    def __init__(self, p, sample_rate=44100, chunksize=1024):
        self.sample_rate = sample_rate
        self.chunksize = chunksize
        self.p = p
        self.stream = None
        self.lock = threading.Lock()
        self.stop = False
        self.frames = []
        atexit.register(self.close)

    def listaudiodevices():
        miclist = []
        indices = []
        
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            try:
                if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                    miclist.append(p.get_device_info_by_index(i).get('name'))
                    indices.append(i)
                    #cdict = p.get_device_info_by_index(i)
                    #for ckey in cdict:
                    #    print(f"{ckey}: {cdict[ckey]}\n")
            except OSError:
                pass
        
        return miclist,indices,p
            
    def create_stream(self, input_index):
        if self.stream is not None:
            self.stream.close()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.sample_rate,
                                  input=True,
                                  output=False,
                                  frames_per_buffer=self.chunksize,
                                  input_device_index=input_index,
                                  start=False,
                                  stream_callback=self.new_frame)

    def new_frame(self, data, frame_count, time_info, status):
        data = np.frombuffer(data, 'int16')
        with self.lock:
            self.frames.append(data)
            if self.stop:
                return None, pyaudio.paComplete
        return None, pyaudio.paContinue

    def get_frames(self):
        with self.lock:
            frames = self.frames
            self.frames = []
            return frames

    def start(self):
        self.stream.start_stream()

    def close(self):
        with self.lock:
            self.stop = True
        if self.stream is not None:
            self.stream.close()
        self.p.terminate()


if __name__ == '__main__':
    # short recording to test that everything works as expected
    import time
    import matplotlib.pyplot as plt

    recorder = MicrophoneRecorder()
    recorder.start()
    print('recording')
    time.sleep(1)
    frames = recorder.get_frames()
    recorder.close()
    fig, ax = plt.subplots()
    ax.plot(frames[-1])
    plt.show()
