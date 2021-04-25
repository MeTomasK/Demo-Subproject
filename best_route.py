
from itertools import permutations
from random import randrange

#adresses input
addresses = []
n = int(input("How many addresses? "))
for i in range(0, n):
    print ("Enter " + str(i+1) + " address:")
    ele = input()
    addresses.append(ele)
print("All addresses: " + str(addresses))

#all possible routes
comb = permutations(addresses, n)
allRoutes=[]
for i in comb:
    allRoutes.append(i)
print("Total routes: "  + str(len(allRoutes)) + "\nAll routes: " + str(allRoutes))

#adding values next to every route
allRoutesDistance=allRoutes.copy()
for i in range(len(allRoutes)):
    allRoutesDistance.insert(i*2+1, randrange(1,20))
print("All routes with distance: " + str(allRoutesDistance))

#finding best route
best=999
shortest=0
for i in range(len(allRoutes)):
    if int(allRoutesDistance[i*2+1]) < best:
        best=allRoutesDistance[i*2+1]
        shortest=allRoutesDistance[i*2]
print("Shortest route is {}, distance -  {} km". format(shortest, best))

