import csv
import random
rnda=255 #a setting for randomness, set for reproducibility. Use None for system time

#Each cell is just an array {threshold, {weights of the previous layer}}
#basically, if sum weights of previous layer >= threshold, then we return 1.
#Sadly python makes it hard to add bools into ints, so I won't bother to do that.

def randInitialize(numPrev: int):
    
    random.seed(a=rnda) #Initialize random
    #We want the threshold to be a percent, soooo, lets make one with a randum numerator
    threshold=(random.randint(0, 100))/100

    i=0
    weights=[]
    #Now lets do the same for each nuron previous.
    while i<= numPrev:
        weights.append((random.randint(0, 100))/100)

    #Great! Now let's return these so we can use them!
    return threshold,weights
