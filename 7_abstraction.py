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
hiding unnecessary info and showing only essential info

'''