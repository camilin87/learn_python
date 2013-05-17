#! /usr/bin/env python

import sys
import time
import threading
import random

class BGCounter(threading.Thread):

    def __init__(self, mult):
        threading.Thread.__init__(self)
        self.__mult__ = mult
        self.daemon = True
        self.should_stop = False
        self.__rnd_mult__ = random.randrange(1, 21, 1)

    def run(self):
        total = 0
        i = 0
        while not self.should_stop:
            total += i * self.__mult__
            print 'counter {0} => {1}'.format(self.__mult__, total)
            i += 1
            if i % self.__rnd_mult__ == 0:
                #time.sleep(1)
                print 'pause on thread {0}'.format(self.__mult__)



def main(args):
    l_threads = []
    num_threads = 10

    for n in range(0, num_threads):
        worker = BGCounter(n + 1)
        l_threads.append(worker)
        worker.start()


    #this is a way to stop the threads
    while len(l_threads) > 0:
        try:
            l_threads = [t.join(1) for t in l_threads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            for t in l_threads:
                t.should_stop = True



if __name__ == '__main__':
    main(sys.argv)
