from threading import *
import os

class MouseCursorThread(Thread):
    def run(self):
        os.system("python mouse-cursor-control.py")
        return

class VoiceThread(Thread):
    def run(self):
        os.system("python voice.py")
        return

t1=MouseCursorThread()
t2=VoiceThread()
t1.start()
t2.start()
