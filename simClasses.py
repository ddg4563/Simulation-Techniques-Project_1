#A python file that contains definitions for the classes to be used in the program 
import simEvent


# A classs to define the customer entity
class Customer:
    customerNumber = 0
    def __init__(self, startedWaiting):
        Customer.customerNumber += 1
        self.custNum = Customer.customerNumber
        self.startedWaiting = startedWaiting


# A class to define the events in the simulation model
# the two event are a customer ready to check out event
# and a customer processed event
# these events are added to the model's event queue and then 
# handled by the model's processEvent function
class CustomerEvent:
    def __init__(self):
        self.customerReadyToCheckOut = False
        self.customerProcessed = False
    
    def setCustomerReadyToCheckOut(value):
        if type(value) == bool:
            self.customerReadyToCheckOut = value
    def getCustomerReadyToCheckOut():
        return self.customerReadyToCheckOut

    def setcustomerProcessed(value):
        if type(value) == bool:
            self.customerProcessed = value
    def getcustomerProcessed():
        return self.customerProcessed


# A class to define the CheckOutLane entity
class CheckOutLane:
    def __init__(self, laneNumber):
        self.laneNumber = laneNumber
        self.numCustomers = 0
        self.customerQueue = []

    def dequeueCustomer():
        return self.customerQueue.pop(0)

    def queueCustomer(customer):
        return self.customerQueue.append(customer)



# A class to define the system of the simulation
class Model:
    def __init__(self):
        self.totalTime = 0.0
        self.eventQueue = []

    def dequeueEvent():
        return self.eventQueue.pop(0)

    def queueEvent(event):
        return self.eventQueue.append(event)
    
    def processEvents(customerNumber, lanes, event, time):
        if event.getCustomerReadyToCheckOut():
            return customerReadyToCheckOut(lanes, self.totalTime)
        elif event.getcustomerProcessed():
            return customerProcessed(customerNumber, lanes, time)

    
    def printLog(file, customerNumber, lane, time, eventType):
        logStr = ""
        try:
            if event.getCustomerReadyToCheckOut():
                logStr = ""
            elif event.getcustomerProcessed():
                logStr = ""
            file.write(logStr)

        except IOError as e:
            print(e)            

