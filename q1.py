



# Replace the content of this function with your own algorithm
# inputs: 
#   W: weight limit of the vehicle used for deliveries.
#   packages: 2D list [[packageID, reward, weight], [packageID, reward, weight], ...]
# returns:
#   1D list of package IDs to represent a package selection. e.g. ["P001", "P003, "P010]

def select_packageSet(W, packages):
    n=len(packages)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    output=[]
    val = [package[1] for package in packages]
    wt = [package[2] for package in packages]
    input_total_wt=int(sum(wt))
    if input_total_wt>W:
        # generate 2d list of with columns being the weights 
        for i in range(n +1): 
            for w in range(W + 1): 
                    if i == 0 or w == 0: 
                        K[i][w] = 0
                    elif wt[i-1] <= w: 
                        K[i][w] = max(K[i-1][w], val[i-1] + K[i-1][w-wt[i-1]]) 
                    else: 
                        K[i][w] = K[i-1][w] 
        #Making the decisions 
        optimal_value=K[len(K)-1][-1]
        # going in reverse hence the counter for the index 
        for i in range(len(K)-1,-1,-1):
            if K[i][W] != K[i-1][W] and K[i][W]!=0:
                output.append(packages[i-1][0])
                W-=packages[i-1][2]
        return output
    else:
        # return all packages  if knapsack problem doesn not exist 
        for i,v in enumerate(packages):
            output.append(v[0])
        return output


            




# print(select_packageSet(W, packages))

