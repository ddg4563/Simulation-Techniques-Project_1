#python file to create and handle customer events
import simClasses
import math
import random

def customerReadyToCheckOut(lanes, time, car):
    #When ready to enter a check-out lane, a customer selects the lane with the shortest line; if more than one line is 
    #of the shortest length, then one of those lanes is selected at random.
    
    #loop through the check out lanes and assign customer to shortest lane
    shortestLane = lanes[0]
    for l in lanes:
        if l.numCustomers < shortestLane.numCustomers:
            shortestLane = l

    arrivalTime = (-1/car) * math.log(random.randrange(time, time + 1)) #needs inverseTransform technique
    #create a new customer and set its started waiting time
    customer = simClasses.Customer(arrivalTime)
    shortestLane.queueCustomer(customer)
    laneChosen = shortestLane.laneNumber
    

    return (customer.customerNumber, arrivalTime, laneChosen)




def customerProcessed(customerProcessedNumber, lanes, time, csr):
    #dequeue the  customer and update the time and statistics
    customer = None
    laneLeft = 0
    #go through all lanes to find customer
    for l in range(len(lanes)):
        for c in l:
            if c.customerNumber == customerProcessedNumber:
                customer = l.pop(0)
                laneLeft = l.laneNumber
    
    processTime = (-1/csr) * math.log(random.randrange(time, time +1)) #needs inverseTransform technique
                    
    return (customer.customerNumber, processTime, laneLeft)




