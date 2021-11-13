#A python file that contains definitions for the classes to be used in the program 
import simEvent


# A classs to define the customer entity
class Customer:
    def __init__(self, startedWaiting):
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
    def __init__(self):
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
    
    def processEvents(customer, lanes, event):
        if event.getCustomerReadyToCheckOut():
            customerReadyToCheckOut(customer, lanes, self.totalTime, self.eventQueue)
        elif event.getcustomerProcessed():
            customerProcessed(customer, lanes, self.totalTime, self.eventQueue)

        return

