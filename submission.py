def sort(tup): 
    return(sorted(tup, key = lambda x: x[1]))  

def min_diff(tup, n):
    start = 0
    end = 0
    diff = 9999999999
    n-=1

    for i in range (0,len(tup)-n):
        if tup[i+n][1]-tup[i][1] <= diff:
            diff = tup[i+n][1]-tup[i][1]
            start = i
            end = i+n

    return [start, end, diff]

lst = [('Fitbit Plus', 7980),('IPods', 22349),('MI Band', 999),('Cult Pass' ,2799),('Macbook Pro' ,229900),('Digital Camera' ,11101),('Alexa',9999),('Sandwich Toaster', 2195),('Microwave Oven', 9800),('Scale' ,4999)]
lst = sort(lst)
dist_goodies = min_diff(lst, 4)
print("The goodies selected for distribution are: ")
for i in range(dist_goodies[0], dist_goodies[1]+1):
    print(lst[i][0]+":"+str(lst[i][1]))

print("And the difference between the chosen goodie with highest price and the lowest price is "+str(dist_goodies[2]))
