from threading import Lock, Condition
class Foo:
    def __init__(self):
        self.cv = Condition()
        self.num = 0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.cv:
            while self.num!=0:
                self.cv.wait()
            printFirst()
            self.num+=1
            self.cv.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()