i = 1  

while i <= 10: 

    print(i) 

    i += 1  


print("\n new line \n")


a = 2 

while a <= 20: 

    print(a) 

    a += 2 


print("\n new line \n")


b = 10  

while b >= 0: 

    print (b)

    b -= 1


print("\n new line \n")

###############################
###############################


# now we need to add the sum of the first n(natural numbers together!)
# so the first thing to start off with is the starting point which is i = 1

sum = 1    # here we need another tool so we can save up our 

sigma = 0

while sum <= 100: 

    sigma += sum

    sum += 1

print (sigma)



############################### 

# now find the biggest number inside a list in python 

numbers = [12, 45, 7, 89, 23, 56]  

                                 # good way of thinking 
                                 # let's align a number index to the biggest one  
                                 # then let the program kinda do the others for us like 
                                 # comparing all the components and priting out the 
                                 # biggest index 

