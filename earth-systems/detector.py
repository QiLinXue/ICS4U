class Detector:
    '''Object which holds each detector object
    
    Attributes:
        xpos {float} -- the x position of the detector
        ypos {float} -- the y position of the detector
        radius {float} -- the radius of the detector
        min_quake {float} -- the minimum magnitude it can pick up
    '''

    def __init__(self,xpos,ypos,radius,min_quake):
        '''Iniializes each detector object
        
        Arguments:
            xpos {float} -- the x position of the detector
            ypos {float} -- the y position of the detector
            radius {float} -- the radius of the detector
            min_quake {float} -- the minimum magnitude it can pick up
        '''

        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.min_quake = min_quake