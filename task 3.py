import math

def isPerfectSqr(nums,X=0,Y=100):#making x = 0 and y = 100 by defualt
    perfectSquares=[]        #declaring lists to append in it
    negatives=[]
    if(X<0 or Y<X):  # some restrictions
        print("\nWrong call format\n") 
    else:
        for i in range(len(nums)): #loop through list
            if(nums[i]<0):
                negatives.insert(1,nums[i]) #filter negative numbers

            elif( int(math.sqrt(nums[i])) >= X and int(math.sqrt(nums[i])) <= Y ): #checking if in range
                sqr = int(math.sqrt(nums[i])) #storing the square root of the number as 
                                                # integers because only integers*themselves gives a perfect square

                if((sqr*sqr) == nums[i]): # ex: 3*3 = 9 -> true
                    perfectSquares.append(nums[i])
                else:
                    pass
        if(perfectSquares != []): # To print perfect squares only if available
            print(perfectSquares)
        else:
            print("No perfect Square in the given range:",X,"->",Y)
        if(negatives != []):
            print("Failed to execute: ",negatives," negative number/s")


x=[2,4,8,16,7,25,62,64,38,100,4356,-42,9,0,-8,-49]

isPerfectSqr(x,2,6)
isPerfectSqr(x,0,100)
isPerfectSqr(x,-2,10)
isPerfectSqr(x,20,10)