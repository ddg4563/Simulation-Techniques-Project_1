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
    
    def setCustomerReadyToCheckOut(self, value):
        if type(value) == bool:
            self.customerReadyToCheckOut = value
    def getCustomerReadyToCheckOut(self):
        return self.customerReadyToCheckOut

    def setcustomerProcessed(self, value):
        if type(value) == bool:
            self.customerProcessed = value
    def getcustomerProcessed(self):
        return self.customerProcessed


# A class to define the CheckOutLane entity
class CheckOutLane:
    def __init__(self, laneNumber):
        self.laneNumber = laneNumber
        self.numCustomers = 0
        self.customerQueue = []

    def dequeueCustomer(self):
        return self.customerQueue.pop(0)

    def queueCustomer(self, customer):
        self.customerQueue.append(customer)
        self.numCustomers += 1



# A class to define the system of the simulation
class Model:
    def __init__(self):
        self.totalTime = 0.0
        self.eventQueue = []

    def dequeueEvent(self):
        return self.eventQueue.pop(0)

    def queueEvent(self, event):
        self.eventQueue.append(event)
    
    def processEvents(self, customerNumber, lanes, event, time, car, csr):
        #print(self,customerNumber,lanes, event, time)
        if event.getCustomerReadyToCheckOut():
            print(lanes, self.totalTime, car)
            return simEvent.customerReadyToCheckOut(lanes, self.totalTime, car)
        elif event.getcustomerProcessed():
            return simEvent.customerProcessed(customerNumber, lanes, time, csr)

    
    def printLog(self, file, customerNumber, lane, time, eventType):
        logStr = ""
        try:
            if event.getCustomerReadyToCheckOut():
                logStr = ""
            elif event.getcustomerProcessed():
                logStr = ""
            file.write(logStr)

        except IOError as e:
            print(e)            

