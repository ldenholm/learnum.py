###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: LD
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import os

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename) -> dict[str, int]:
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    # Read file from disk:
    cows = {}
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        for line in f:
            (key, val) = line.split(",")
            cows[str(key)] = int(val)
    
    return cows

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cowsCopy = sorted(cows.items(), key=lambda x:x[1])
    print('cows dict remains untouched', cows)
    print('descending list sorted cowsCopy', cowsCopy)
    currentTrip = []
    trips = []
    tripTotalWeight = 0
    # Note we need to sort the list in such a way that each time we append to the list we choose
    # a locally optimal solution. This is the definition of greedy.
    for i in range(len(cowsCopy)):
        if (tripTotalWeight + cowsCopy[i][1]) <= limit:
            currentTrip.append(cowsCopy[i][0])
            tripTotalWeight += cowsCopy[i][1]
        else:
            # Trip total weight exceed the limit
            trips.append(currentTrip)
            # need to create a new list otherwise it only ever appends the one memory location to trips
            currentTrip = []
            # Reset total weight and trip list
            tripTotalWeight = 0 + cowsCopy[i][1]
            currentTrip.append(cowsCopy[i][0])
            # Edge case for final trip:
            if i == (len((cowsCopy)) -1):
                trips.append(currentTrip)
    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    tripPartitions = []
    for partition in get_partitions(cows.keys()):
        tripPartitions.append(partition)
    
    acceptableTrips = tripPartitions.copy()
    # rm invalid partitions that exceed the weight bound
    for tp in tripPartitions:
        # list of trips so iterate through each trip and calculate the weight
        for trip in tp:
            # sum and use current cow in trip as the key to access value in dict
            total = sum([cows.get(cow) for cow in trip])
            if total > limit:
                acceptableTrips.remove(tp)
                break
    # return the smallest length partition
    return (min(acceptableTrips, key=len), acceptableTrips)
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    # Load data
    cows = load_cows("ps1_cow_data.txt")
    print('Original cows', cows)

    # Test greedy
    start = time.time()
    trips = greedy_cow_transport(cows)
    ms = (time.time() - start) * 1000
    print("trips: ", trips, 'num of trips: ', len(trips), '\nTime to run: ', ms)

    start = time.time()
    optimal_trip, acceptableTrips = brute_force_cow_transport(cows)
    ms = (time.time() - start) * 1000
    print("optimal trip: ", optimal_trip, '\nTime to run: ', ms, 'total num of acceptable trips, ', len(acceptableTrips))

    pass

compare_cow_transport_algorithms()