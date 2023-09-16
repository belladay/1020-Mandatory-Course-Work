from engi1020.arduino.api import *
from time import sleep
import numpy as np
from datetime import *
import matplotlib.pyplot as plt

# when script is run, arduino checks if button is pressed until it is pressedw

# create an arbitrary value before the infinite loop starts

oled_clear()
oled_print('Press the button to turn on the device')
rgb_lcd_colour(0,0,0)

v = 1

#create a list of all the light readings each day (max len of list is the number of seconds in a day, but for this project
#since it is being done on a smaller scale, it will be the number of light readings for a minute (60s)

r = []

# clear txt file
open("readings.txt","w").close()


while True:
    if digital_read(6) == True:
        on = True
    else:
        continue
    while on == True:
        l = analog_read(6)
        
# add light reading to list

        
        #open text file   
        with open("readings.txt","a") as f:
            #using datetime create a time string and write it into the txt file
            time = datetime.now()
            time_str = time.strftime("%H:%M:%S")
            f.write(time_str)
            f.write('\t')
            #write the light level into the text file
            f.write(str(l))
            f.write('\n')
        
                

# create a function that converts light sensor readingg to brightness level
        def bright(l):
            b = ((755-l)/755)*255
            return b

# b is the light level of the rgb
# using our defined function, change the brightness of the rgb lcd
        
        sleep(1)
# pressing a button changes an aribitrary value from 1-3

        if digital_read(6) == True:
            if v < 3:
                v += 1
            else: v = 1
# determine brightness level
        b = bright(l)
# convert to integer whole number so the rgb function will understand
        b = int(b)
        
# using values of v and b, change the rgb lcd
# note v represents the colour of the light (1-3),(red,green,blue)
# note b represents the brightness of the light

        if v == 1:
            oled_clear()
            oled_print('light is red, brightness is:')
            oled_print(b)
            rgb_lcd_colour(b,0,0)
            
        elif v == 2:
            oled_clear()
            oled_print('light is purple, brightness is:')
            oled_print(b)
            rgb_lcd_colour((int(b/2)),0,(int(b/2)))
            
            
        elif v == 3:
            oled_clear()
            oled_print('light is blue, brightness is:')
            oled_print(b)
            rgb_lcd_colour(0,0,b)
        
        if analog_read(0) == 1023:
            #exit inside loop
            on = False
    
    #graph
            
    x=[]
    y=[]
    f = open("readings.txt","r")
    for line in f.readlines():
        line_r = line.split("\t")
        x.append(datetime.strptime(line_r[0],"%H:%M:%S"))
        y.append(int(line_r[1]))
     
    plt.plot_date(x, y, label = "Light Level", linestyle="solid")
    #plt.plot(y, label = "Y")
   
    plt.xlabel('Time')
    plt.ylabel('Light level')
    plt.legend()
    plt.show()
            
