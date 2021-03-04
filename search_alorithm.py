# Binary Search 

VALUES = [11,12,15,16,112,118,123,145]
TARGET = 11 # search value
MIN = 0
HIGH = 7 # Number of array elements - l 
FOUND = False
ANSWER = 0
MID =0

while FOUND == False and MIN <= HIGH: 
    MID = int(((MIN + HIGH) / 2))
    if VALUES[MID] == TARGET: 
        FOUND = True 
        ANSWER = MID 
    elif TARGET > VALUES[MID]: 
        MIN = MID + 1 
    else: HIGH = MID - 1
if FOUND == True:
    print(TARGET, "FOUND AT ARRAY INDEX", ANSWER)
else: 
    print(TARGET, "was not found :(")

# Sequential search 
N = [2, 9, 5, 6, 7, 8] 
X = 2
found = False 
counter = 0 
for counter in range(5):
    if N[counter] == X:
        Found = True
        print(N[counter], "found at position", counter)
if Found == False:
    print(X, "not found")
