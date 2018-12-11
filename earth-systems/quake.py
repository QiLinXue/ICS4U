import math

class Quake:
    '''Quake object that defines each earthquake
    
    Attributes:
        xpos {float} -- x location of epicenter
        ypos {float} -- y location of epicenter
        period {float} -- the time between successive quakes at same location
        power {float} -- the magnitude of the quake
        decay {float} -- the rate at which the magnitude decreases per second
        speed {float} -- the speed at which the radius increases per second
        radius {float} -- the radius of the affected areas
    '''

    def __init__(self,xpos,ypos,period,power,decay,speed):
        '''Initialize quake object
        
        Arguments:
            xpos {float} -- x location of epicenter
            ypos {float} -- y location of epicenter
            period {float} -- the time between successive quakes at same location
            power {float} -- the magnitude of the quake
            decay {float} -- the rate at which the magnitude decreases per second
            speed {float} -- the speed at which the radius increases per second
        '''

        self.xpos = xpos
        self.ypos = ypos
        self.period = period
        self.power = power
        self.decay = decay
        self.speed = speed
        self.radius = 0

    def update(self):
        '''Updates the radius and power of earthquake
        '''
        
        # NOTE Due to unclear instructions, the period of the earthquake was not designed properly and based off the UML could not be completed exactly according to the wishes of Colonel Sir Macaulay. 
        # However, after some R&D, it was discovered that the difference between the periods are so miniscule that over a long period of time, it will not greatly affect the area.
        # We apologize for the inconvenience and if necessary, we will be able to edit this part of the code

        if self.period < 0:
            self.power -= self.decay
            self.radius += self.speed
        else:
            self.period -= 1
    
    def checkDetector(self,detector):
        '''Checks if the earthquake is detected by anything
        
        Arguments:
            detector {Detector[]} -- a list of the detectors
        
        Returns:
            boolean -- whether or not the earthquake is detected
        '''

        for z in detector:
            if z.min_quake <= self.power:
                return False
            actual_dist = math.hypot(self.xpos-z.xpos,self.ypos-z.ypos)
            needed_dist = self.radius + z.radius

            if actual_dist <= needed_dist:
                return True
            else:
                return False