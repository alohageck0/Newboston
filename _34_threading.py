__author__ = 'royalfiish'

import threading
import time

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())
            time.sleep(0.5)

x = Messenger(name='First thread')
y = Messenger(name='Second thread')
x.start()
y.start()
