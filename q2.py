
# Q2

# Replace the content of this function with your own algorithm
# inputs: 
#   n: the number of members in your team
#   W: weight limit of each vehicle used for deliveries.
#   packages: 2D list [[packageID, reward, weight], [packageID, reward, weight], ...]
# returns:
#   2D list of package IDs to represent n sets of packages. 
#   e.g. if n = 2, this is a possible solution: [["P001", "P003"], ["P010"]]


# packages=[['P000', 110, 40], ['P001', 150, 60], ['P002', 70, 30], ['P003', 80, 40], ['P004', 30, 20], ['P005', 5, 5]]
# n=2
# W=75


def select_packageSets(n, W, packages):
    packages_ratio=packages 
    #greedy approach: creates a list of package with ratios to be sorted by reward/weight O(P)
    for i,v in enumerate(packages_ratio):
        temp_reward=v[1]
        temp_weight=v[2]
        temp_value=temp_reward/temp_weight
        temp_value=round(temp_value,2)
        v.append(temp_value)
    # sorting O(NLogN) with lambda
    packages_ratio.sort(key=lambda x: -x[3])
    
    #O(N)
    track_weight = [0 for i in range(n)]
    track_reward = [0 for i in range(n)]
    track_output = [[] for i in range(n)]
    
    # O(P*N)
    for package, reward, weight, ratio in packages_ratio: 
        #initialize as -1 if package weight exceeds everyones limit the package will be skipped
        current_index = -1
        #initialize reward for every package loop
        current_lowest_reward = 9999999

        for i in range(n):
            #loops through each person & checks if weight & finds the person with the lowest reward 
            if ((track_weight[i] + weight <= W) and (track_reward[i] < current_lowest_reward)):
                current_index = i
                current_lowest_reward = track_reward[i]

        # appends to trackers & output if there is an package that is under someones weight limit
        if current_index !=-1:
            #updating
            track_output[current_index].append(package) 
            track_reward[current_index] += reward 
            track_weight[current_index] += weight
            
    return track_output


# select_packageSets(n, W, packages)






# you may insert other functions here, but all statements must be within functions
# before submitting to red, check that there are no print statements in your code. Nothing should be printed when your code runs.

