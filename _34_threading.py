__author__ = 'royalfiish'

import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = Messenger()
y = Messenger()