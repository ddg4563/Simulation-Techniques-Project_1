
import sys
import random

print('\nNumber of arguments: ', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

rngseed = int(sys.argv[1])
duration = int(sys.argv[2])
numlanes = int(sys.argv[3])
car = int(sys.argv[4])
csr = int(sys.argv[5])

#setup rng seed
random.seed(rngseed)

#setup lanes
lanes = []
for i in range(numlanes):
    lanes.append([])

# functions to handle events
def customerReadyToCheckOut(customerNumber,lanes, time, car):
    #When ready to enter a check-out lane, a customer selects the lane with the shortest line; if more than one line is 
    #of the shortest length, then one of those lanes is selected at random.
    
    #loop through the check out lanes and assign customer to shortest lane
    shortestLane = lanes[0]
    laneChosen = 0
    for i in range(len(lanes)):
        if len(lanes[i]) < len(shortestLane):
            shortestLane = lanes[i]
            laneChosen = i  

    #use inverse transform exponetial distibution to get the arrival time of customers
    if customerNumber == 1:
        arrivalTime = 0.0
    else:
        arrivalTime = random.expovariate(car)
        arrivalTime += time

    #add customer's arrival time to lane queue
    lanes[laneChosen].append(arrivalTime)
    
    

    return (arrivalTime, laneChosen)


def customerProcessed(lanes, laneChosen, csr):
    #get the lane that the customer is exiting
    laneLeft = laneChosen
    
    
    #use inverse transform exponetial distibution to get process time of the customer
    processTime = random.expovariate(csr) 
    processTime += lanes[laneChosen].pop(0)
    return (processTime, laneLeft)


#system variables for the main loop
lanesChosen = []    #a queue for which lanes that the customers were added to
totalTime = 0.0     # the total time of the simulation
totalCustomers = 1  #total number of customers in the simulation
numberOfCustomersProcessed = 1  #total number of customers processed in the simulation

for i in range(duration): #main loop
    for r in range(car): # process customer arrival events according to customer arrival rate 
        atime, lChosen = customerReadyToCheckOut(totalCustomers,lanes, totalTime, car) # call customerReadyToCheckOut to get the arrival time and lane chosen
        lanesChosen.append(lChosen) # add the lane chosen to the lanesChosen queue
        totalTime += atime #update the total simulation time
        print("Time: " + str(totalTime) + " Customer " + str(totalCustomers) +  " enters check-out lane " + str(lChosen+1)) # print output
        # write output to a log file
        try:
            with open("log", "a+") as f:
                f.write("Time: " + str(totalTime) + " Customer " + str(totalCustomers) +  " enters check-out lane " + str(lChosen+1) + "\n")
        except IOError as e:
            print(e)    
        totalCustomers +=1 #update total number of customers
    
    for p in range(csr): # process customer serviced events according to customer service rate 
        lChosen = lanesChosen.pop(0) # get the lane that the current customer who is being processed was added to. the customer being processed corresponds to the numberOfCustomersProcessed variable 
        pTime, lLeft = customerProcessed(lanes, lChosen, csr) #call the customerProcessed function and get the process time and the lane that was left
        totalTime += pTime #update total time
        print("Time: " + str(totalTime) +  " Customer " + str(numberOfCustomersProcessed) + " exits check-out lane " + str(lLeft+1))    #print output
        
        # write output to a log file
        try:
            with open("log", "a+") as f:
                f.write("Time: " + str(totalTime) +  " Customer " + str(numberOfCustomersProcessed) + " exits check-out lane " + str(lLeft+1) + "\n")
        except IOError as e:
            print(e)

        numberOfCustomersProcessed += 1 #update the total number of customers processed
    

    if totalTime >= duration: # exit loop when finished
        break
        

