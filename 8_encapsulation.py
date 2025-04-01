class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def strt(self):
        self.clutch=True
        self.acc=True
        print("car started...")

car1=Car()
car1.strt()

'''
this is encapsulation

wrapping data and function into single unit(object)

------------
|  data    |
|    +     |    <==  capsule
| function |
------------
**************************************************
------------
|  data    |  (Private variables, e.g., `__name`, `__marks`)
|    +     |  <==  Capsule (Class hides data and exposes controlled access)
| function |  (Public methods, e.g., `get_name()`, `set_marks()`)
------------


'''