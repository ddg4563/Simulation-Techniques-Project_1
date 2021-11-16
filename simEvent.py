#python file to create and handle customer events
import simClasses


def customerReadyToCheckOut(lanes, time):
    #When ready to enter a check-out lane, a customer selects the lane with the shortest line; if more than one line is 
    #of the shortest length, then one of those lanes is selected at random.
    
    #loop through the check out lanes and assign customer to shortest lane
    shortestLane = lanes[0]
    for l in range(len(lanes)):
        if l.numCustomers < shortestLane.numCustomers:
            shortestLane = l

    arrivalTime = 0 #needs inverseTransform technique
    #create a new customer and set its started waiting time
    shortestLane.queueCustomer(simClasses.Customer(arrivalTime))
    laneChosen = shortestLane.laneNumber
    

    return (customerNumber, arrivalTime, laneChosen)




def customerProcessed(customerProcessedNumber, lanes, time):
    #dequeue the  customer and update the time and statistics
    customer = None
    laneleft = 0
    #go through all lanes to find customer
    for l in range(len(lanes)):
        for c in l:
            if c.customerNumber == customerProcessedNumber:
                customer = l.pop(0)
                laneleft = l.laneNumber
    
    processTime = 0 #needs inverseTransform technique
                    
    return (customerNumber, processTime, laneLeft)




