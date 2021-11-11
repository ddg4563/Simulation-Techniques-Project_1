#A python file that contains definitions for the classes to be used in the program 

class Customer:
    def __init__(self, startedWaiting):
        self.startedWaiting = startedWaiting

    


class CheckOutLane:
    def __init__(self):
        self.numCustomers = 0
        self.customerQueue = []

    def dequeueCustomer():
        return self.customerQueue.pop(0)

    def queueCustomer(customer):
        return self.customerQueue.append(customer)



class Model:
    def __init__(self):
        self.totalTime = 0.0
        self.eventQueue = []

    def dequeueCustomer():
        return self.eventQueue.pop(0)

    def queueCustomer(event):
        return self.eventQueue.append(event)
    
    def processEvents(customer, lanes, event):
        return

