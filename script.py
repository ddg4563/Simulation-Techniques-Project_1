#!/usr/bin/python

import sys
import random
import simClasses

print '\nNumber of arguments: ', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

rngseed = int(sys.argv[1])
duration = int(sys.argv[2])
numlanes = int(sys.argv[3])
car = int(sys.argv[4])
csr = int(sys.argv[5])

lanes = []

    
# run simulation and write to log file
try:

    with open("log", "r+") as f:
        #create lane queues
        for i in range(numlanes):
            lanes.append(simClasses.CheckOutLane(i))

        #create model
        checkOutLanesModel = simClasses.Model()

        #a customer number counter
        customerNumber = 1
        while checkOutLanesModel.totalTime < duration:
            
            #add customer ready to check out events to the event queue according to the customer arrival rate

            #add customer processed events to the event queue according to customer service rates

            #determine customer arrival time using inverse-transform equation

            #create a new customer and set its started waiting time and customerNumber

            #process a event and print log output to log file
            print()

except IOError as e:
    print(e)      
