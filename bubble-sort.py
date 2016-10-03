import random
import datetime
bubbles = []
for count in range(0,101):
    random_nunber = round(random.random()*100)
    bubbles.append(random_nunber)
print bubbles

def bubble_sort(list):
    for stage in range(0,len(list)-1):
        for index in range(0,len(list)-1):
            if list[index] > list[index + 1]:
                (list[index], list[index + 1]) = (list[index + 1], list[index])
        print list
    print list
t1 = datetime.datetime.now()
bubble_sort(bubbles)
t2 = datetime.datetime.now()
print "time before: ", t1
print "time after: ", t2
print "Total time to sort list = ", t2 - t1
