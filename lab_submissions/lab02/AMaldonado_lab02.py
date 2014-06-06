class Car():
    def __init__(self, model='Ford', wheels = 4): 
        self.model = model			
        self.running = False
        self.wheels = wheels
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
   
   #Creates a new method called num_wheels which tells you the number of wheels of the car
   #and returns an error message if the number of wheels is less than 0.
    def num_wheels(self):
    	if self.wheels < 0:
    		print 'A car cannot have negative wheels'
    		self.wheels = 0
    	else:
    		print 'The car has %d wheels' % self.wheels	        