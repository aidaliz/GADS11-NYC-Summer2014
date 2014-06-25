### CLASSES
import code

class Car():
    def __init__(self, model='Ford', num_wheels=4):
        self.model = model
        if num_wheels <0:
            print 'num wheels must be >=0'
            self.num_wheels = 0
        else:
            self.num_wheels = num_wheels

        self.running = False
    def start(self):
        if self.running != True:
            print 'The car started!'
            self.running = True
        else:
            print 'The car is already running!'
    def stop(self):
        if self.running == True:
            print 'The car stopped!'
            self.running = False
        else:
            print 'The car was not running!'

ford = Car(num_wheels=-4)
nissan = Car(model = 'Nissan')
code.interact(local=locals())
ford.running
ford.start()
ford.running
nissan.running
nissan.stop()
