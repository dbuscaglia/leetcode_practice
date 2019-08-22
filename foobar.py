from threading import Lock

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.fooLock = Lock()
        self.barLock = Lock()

        self.barLock.acquire()


    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.fooLock.acquire()
            printFoo()
            self.barLock.release()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printBar() outputs "bar". Do not change or remove this line.

            self.barLock.acquire()
            printBar()
            self.fooLock.release()