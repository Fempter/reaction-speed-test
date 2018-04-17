import time
#from math import sqrt
import RPi.GPIO as GPIO
from random import randint as rd

def my_handler():
        GPIO.output(22,False)
        t2 = time.time()
        tc = t2-t1
        t.append(tc)
        print tc

def mean(lst):
        sum = 0
        for i in range(len(lst)):
            sum += lst[i]
        return (sum/len(lst))

def stddev(lst):
        sum = 0
        mn = mean(lst)
        for i in range(len(lst)):
            sum += (lst[i]-mn)**2
        return (sum/(len(lst)-1))**(0.5)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

file_name = raw_input('Podaj imie: ')
file_out = open(file_name+'.txt', 'w')

t = []
n = 20

#GPIO.add_event_detect(18,GPIO.FALLING,callback=my_handler,bouncetime=300)

for i in xrange(n):
        GPIO.output(22,False)
        GPIO.output(15,True)
        print'Przygotuj sie'
        time.sleep(2)
        GPIO.output(15,False)

        time.sleep(rd(1,10))
        t1 = time.time()
        GPIO.output(22,True)

        GPIO.wait_for_edge(18,GPIO.FALLING)
        my_handler()
        file_out.write('%f \t'% (t[i]))
        print t
        
file_out.write('\n%f\t%f'% (mean(t),stddev(t)))

print mean(t)
print stddev(t)

GPIO.cleanup()
