#!/usr/bin/python

import sys
import random
import simClasses

print('\nNumber of arguments: ', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

rngseed = int(sys.argv[1])
duration = int(sys.argv[2])
numlanes = int(sys.argv[3])
car = int(sys.argv[4])
csr = int(sys.argv[5])

lanes = []


# run simulation and write to log file
try:

    with open("log", "a+") as f:
        #create lane queues
        for i in range(numlanes):
            lanes.append(simClasses.CheckOutLane(i))

        #create model
        checkOutLanesModel = simClasses.Model()

        #a customer number counter
        customerProcessedNumber = 1
        # create initial customer event
        e = simClasses.CustomerEvent()
        e.setCustomerReadyToCheckOut(True)
        checkOutLanesModel.queueEvent(e)
        #checkOutLanesModel.queueEvent(simClasses.CustomerEvent().setCustomerReadyToCheckOut(True))
        
        print(checkOutLanesModel.eventQueue)
        while checkOutLanesModel.eventQueue:

            #dequeue a event
            e = checkOutLanesModel.dequeueEvent()
            print(e)
            # process the event
            if e:
                custNum, time, lane = checkOutLanesModel.processEvents(customerProcessedNumber, lanes, e, checkOutLanesModel.totalTime, car, csr)

            #update customer processed counter if customer processed event ocurred
            if e.getcustomerProcessed():
                customerProcessedNumber += 1
            
            #print log output to log file
            checkOutLanesModel.printLog(custNum, lane, time, e)

            #update total time
            checkOutLanesModel.totalTime += time


            #add customer ready to check out events to the event queue according to the customer arrival rate
            for i in range(car):
                checkOutLanesModel.queueEvent(simClasses.CustomerEvent().setCustomerReadyToCheckOut(True))
            
            #add customer processed events to the event queue according to customer service rates
            for i in range(csr):
                checkOutLanesModel.queueEvent(simClasses.CustomerEvent().setcustomerProcessed(True))


            
            if checkOutLanesModel.totalTime >= duration:
                break
            


            

except IOError as e:
    print(e)      


#print statistics to a statistics file