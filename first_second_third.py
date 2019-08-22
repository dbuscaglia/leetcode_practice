class Foo(object):
    def __init__(self):
        self.lock_state_machine = [False, False, False]


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock_state_machine[0] = True

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while not self.lock_state_machine[0]:
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        
        printSecond()
        self.lock_state_machine[1] = True
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while not self.lock_state_machine[1] or not self.lock_state_machine[0]:
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.lock_state_machine[2] = True