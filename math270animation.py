import matplotlib.pyplot as plt
import numpy as np
import math
from AnimationClassStudents import Matrix

# create 2d figure of square house and triangle roof
#  first row is x coordinates, second row is y cooridnates
#  trace all vertices of the figure
house = np.matrix(' 0.  4.  7.  9. 10. 9. 7. 4. 0. -4. -7. -9. -10. -9. -7. -4. 0;'
                  ' 20. 19. 17. 14 10. 6. 3. 1. 0.  1   3.  6.  10. 14.    17. 19. 20')
Mh = Matrix(house)

# initialize plotting system
plt.ion()

# translate animate
# clear screen on each plot
# pause for less than 1/32 seconds
Mh = Matrix(house)
Mh.scale(1, 1.8)
Mh.translate(0, -2)
Mh.plot()
plt.pause(1.0)
for _ in range(3):
    speed = 15 #Smaller is faster
    squishiness = 0.8 #From 0 to 1, where 1 is very squishy
    segmentLength = 40/(((speed+1)**2 - (speed+1))/2)
    for i in range(speed):
        Mh.translate(0, -(i+1) * segmentLength)  # Simulating acceleration
        Mh.rotate(math.pi/(speed), about='center')
        Mh.plot(clrfig=1)
        plt.pause(1 / 40)
    for i in range(speed//10 + 1):
        Mh.translate(0,40)
        Mh.scale(1/(1 - 3*squishiness/speed), 1 - (squishiness/(speed/5)))
        Mh.translate(0,-40)
        Mh.plot(clrfig=1)
        plt.pause(1 / 40)
    for i in range(speed//10 + 1):
        Mh.translate(0,40)
        Mh.scale(1 - 3*squishiness/speed, 1/(1-(squishiness/(speed/5))))
        Mh.translate(0,-40)
        Mh.plot(clrfig=1)
        plt.pause(1 / 40)
    for i in range(speed):
        i = speed - i
        Mh.translate(0, i * segmentLength)  # Simulating acceleration
        Mh.rotate(math.pi / (speed), about='center')
        Mh.plot(clrfig=1)
        plt.pause(1 / 40)


for i in range(20):
    Mh.rotate(math.pi/(16*(i+1)), about = 'center')
    Mh.shear(-30/(i+1), 0)
    Mh.translate(i*2, 0)
    Mh.plot(clrfig=1)
    plt.pause(1/30)


plt.pause(1)
print("Luke Winter")



