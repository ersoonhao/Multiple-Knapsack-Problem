# <Your Team ID>
# <Team members' names>

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
    # print(packages)
  # TODO: edit this function's body
  # return [[P001, P003], [P011, P007], [P004, P005, P006], [P012]]
  # number of packages was originally n i renamed it to number of packages  
    number_of_packages=len(packages)
    # print(packages)
    # track_weight=[[W] for lst in range(n)] 
    # track_reward=[[] for lst in range(n)]
    # print(track_weight)
    initial_w=W
    W=round((n*W)*1.5)   # additional slack for extra packages. 
    output=[]
    assignment_track = [[[],0] for lst in range(n)] #generates a list of
    # print(assignment_track)

    # tracks rewards
    index_track=[]

    for i in range(n):
        index_track.append([i,0])
    # print(index_track)
        

    K = [[0 for x in range(W + 1)] for x in range(number_of_packages + 1)]
    best_sets=[]
    val = [package[1] for package in packages]
    # print(val)
    wt = [package[2] for package in packages]
    input_total_wt=int(sum(wt))

    # Multiple Knapsack problem exists
    # hm this means that sum of all packages is smaller than W * 1.5 
    # if input_total_wt<W:
       
    
    for i in range(number_of_packages +1): 
        for w in range(W + 1): 
                if i == 0 or w == 0: 
                    K[i][w] = 0
                elif wt[i-1] <= w: 
                    K[i][w] = max(K[i-1][w], val[i-1] + K[i-1][w-wt[i-1]]) 
                else: 
                    K[i][w] = K[i-1][w] 
    
    
    optimal_value=K[len(K)-1][-1]


    for i in range(len(K)-1,-1,-1):

        if K[i][W] != K[i-1][W] and K[i][W]!=0:
            best_sets.append(packages[i-1])
            W-=packages[i-1][2]
    

    # append by ratio & sort by reward/weight
    for i,v in enumerate(best_sets):
        temp_reward=v[1]
        temp_weight=v[2]
        temp_value=temp_reward/temp_weight
        temp_value=round(temp_value,2)
    
        v.append(temp_value)
    best_sets.sort(key=lambda x: -x[3])
    # print(best_sets)
    # print(best_sets)
    
    # [[0, 0], [1, 0]]
# [['P000', 110, 40, 2.75], ['P001', 150, 60, 2.5], ['P002', 70, 30, 2.33], ['P003', 80, 40, 2.0], ['P004', 30, 20, 1.5], ['P005', 5, 5, 1.0]]
    # assigning sets to each individal
    
    # assignment_track packages & weight   [[[], [0]], [[], [0]]]
    # index_track index & rewards [[0, 0], [1, 0]]
    

    counter=0 
    while counter<len(best_sets):

        index_track.sort(key=lambda x: -x[1],reverse=True)

        for i,sorted_index_track in enumerate(index_track):

            current_index=sorted_index_track[0]
            #check weight
            if((assignment_track[current_index][1])+(best_sets[counter][2])<initial_w):
                assignment_track[current_index][0].append(best_sets[counter][0])
                assignment_track[current_index][1]+=best_sets[counter][2]

                #update index with reward
                index_track[i][1]+=best_sets[counter][1]
                counter+=1
                break
        else:
            # when you can't fit in this set 
            counter+=1
    
    for i,v in enumerate(assignment_track):
        output.append(v[0])
            
    #     print(counter)
    # print(assignment_track)
    # print(index_track)


    return output

# test=[]
# test.append(1)
# test.append(2)
# test.pop(0)
# test.append(1)
# print(test)    
            
# print(select_packageSets(n, W, packages))        
                    
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,13, 13, 13],
# [0, 0, 0, 0, 0, 0, 0, 13, 15, 15, 15, 15, 15, 15, 15, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28],
# [0, 0, 0, 0, 0, 0, 0, 13, 15, 16, 16, 16, 16, 16, 16, 28,29, 31, 31, 31, 31, 31, 31, 31, 44, 44, 44],
# [0, 0, 0, 0, 0, 0, 0, 13, 15, 16, 16, 23, 23, 23, 23, 28, 29, 31, 36, 38, 39, 39, 39, 39, 44, 44, 51],
# [0, 0, 0, 0, 0, 0, 0, 13,15, 16, 16, 23, 24, 24, 24, 28, 29, 31, 36, 38, 39, 40, 40, 47, 47, 47, 51]]   
            













# you may insert other functions here, but all statements must be within functions
# before submitting to red, check that there are no print statements in your code. Nothing should be printed when your code runs.

