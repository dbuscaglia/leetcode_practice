import threading


class ZeroEvenOdd(object):

    def __init__(self, n):
        self.n = n
        self.i = 0

        self.lock_zero = threading.Lock()
        self.lock_odd = threading.Lock()
        self.lock_even = threading.Lock()

        self.lock_odd.acquire()
        self.lock_even.acquire()

    def zero(self, printNumber):
        for _ in range(self.n):
            self.lock_zero.acquire()
            printNumber(0)

            if self.i % 2 == 0:
                self.lock_odd.release()
            else:
                self.lock_even.release()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.lock_even.acquire()
            printNumber(i)
            self.i = i
            self.lock_zero.release()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.lock_odd.acquire()
            printNumber(i)
            self.i = i
            self.lock_zero.release()