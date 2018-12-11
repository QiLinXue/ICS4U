====================================================================
For the detectionUnits.txt file, it is set up as follows:

x,y,detection-radius,min-tremor,min-quake

Where x is the x position of the alarm
      y is the y position of the alarm
      detection-radius is the radius that it can detect an earthquake
      min-tremor is the minimum value on the Richter scale it can detect as the initial tremor


====================================================================
For the earthquakeLocations file, is is set up as follows:

x,y

Where x is the x position of the earthquake's centre
      y is the y position of the earthquake's centre


====================================================================
For the simulation file, is set up as follows:

1st line = minimum earthquake value on the Richter scale to be detected

Beyond the first line:

x,y,waiting-period,initial-power,wave-degredation-speed,wave-speed

Where x is the x position of the earthquake's centre
      y is the y position of the earthquake's centre
      waiting-period is the amount of time (in seconds) until the next earthquake can be sent from the same location (if necessary)
      initial-power is the initial intensity of the earthquake on the Richter scale
      wave-degredation-speed is how fast the wave degrades per second
      wave-speed growth-rate is how fast (in pixels / second) the earthquake spreads in all directions - e.g. if this was 1, it would increase the radius of the shockwave by 1 pixel / second.





There are 3 sample files provided - when you are ready to complete testing, you will use the fileGenerator to build your own custom files for this project.