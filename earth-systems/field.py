class Field:
    '''An object that holds a simulation field object

    Attributes:
        detectors {Detector[]} -- a list of the detectors needed
        quakes {Quake[]} -- a list of the quakes in the simulation
    '''

    def __init__(self,detectors,quakes):
        '''Initilaizes the simulation field
        
        Arguments:
            detectors {Detector[]} -- a list of the detectors needed
            quakes {Quake[]} -- a list of the quakes in the simulation
        '''

        self.detectors = detectors
        self.quakes = quakes
        self.time = 0
    
    def run(self):
        '''A function that iterates over time 
        until the final earthquake is detected
        '''

        # from main import min_magnitude

        while len(self.quakes) > 0:
            self.time += 1
            

            for i in self.quakes:
                i.update()
                if i.power <= 3 or i.power <= 0:
                    # print("%s died" % i.xpos)
                    self.quakes.remove(i)
                    if(len(self.quakes) == 0):
                        print("Final earthquake died at %s seconds" % self.time)
                if i.checkDetector(self.detectors):
                    self.quakes.remove(i)
                    if(len(self.quakes) == 0):
                        print("Final earthquake detected at %s seconds" % self.time)
                    break