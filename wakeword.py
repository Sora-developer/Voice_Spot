# import pvporcupine
# from pvrecorder import PvRecorder

# class WakeWordDetector:
#     def __init__(self, access_key, keyword="computer"):
#         self.porcupine = pvporcupine.create(
#             access_key=access_key,
#             keywords=[keyword] 
#         )
        
#         self.recorder = PvRecorder(device_index=-1, frame_length=self.porcupine.frame_length)
#         self.is_listening = False

#     def start(self):
#         print("Wake word detector running… say your wake word.")
#         self.recorder.start()
#         self.is_listening = True

#         while self.is_listening:
#             pcm = self.recorder.read()
#             keyword_index = self.porcupine.process(pcm)

#             if keyword_index >= 0:
#                 return True 

#     def stop(self):
#         self.is_listening = False
#         self.recorder.stop()
#         self.porcupine.delete()


import pvporcupine
from pvrecorder import PvRecorder
import threading

class WakeWordDetector:
    def __init__(self, access_key, keyword="computer", on_detect=None):
        self.porcupine = pvporcupine.create(
            access_key=access_key,
            keywords=[keyword]
        )
        self.recorder = PvRecorder(device_index=-1, frame_length=self.porcupine.frame_length)

        self.is_running = False
        self.thread = None
        self.on_detect = on_detect  # callback (function)

    def start(self):
        if self.is_running:
            return
        
        print("Wake-word listening started.")
        self.is_running = True
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def stop(self):
        print("Wake-word listening stopped.")
        self.is_running = False

    def _run(self):
        self.recorder.start()

        while self.is_running:
            pcm = self.recorder.read()
            result = self.porcupine.process(pcm)

            if result >= 0:
                print("Wake word detected!")
                if self.on_detect:
                    self.on_detect()  # call into app
            
        self.recorder.stop()

    def delete(self):
        self.stop()
        self.porcupine.delete()
