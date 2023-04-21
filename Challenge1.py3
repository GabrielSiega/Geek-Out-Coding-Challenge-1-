#made by: Gabriel S.#
#date: 21 Apr 2023#
    
    #Conditions: 
        
        #Write a program that does the following:   

        #Loop through all the numbers between 1 to 50 and print ‘Geek’ and ‘Out’
        #for numbers divisible by 3 and 5 respectively. If that number is divisible
        #by both 3 and 5, print ‘GeekOut’ instead! If the number is not divisible by
        #either 3 or 5, just print the current number.  
        
        #Conditions: 
        # 1. If the numbers are divisible by 3 print "Geek"
        # 2. If the numbers are divisible by 5 print "Out"
        # 3. If the numbers are divisible by both 3 and 5 "GeekOut"
        
       
for i in range(1, 51): #integers available is no.'s 1-50
    
    if i % 3 == 0 and i % 5 == 0:  #If the no. is divisible by both 3 & 5
        print("number:",(i),'(GeekOut)')
    elif i % 3 == 0:               #If the no. is divisible by 3 only
        print("number:",(i),'(Geek)')
    elif i % 5 == 0:               #If the no. is divisible by 5 only
        print("number:",(i),'(Out)')
    else:
        print("number:",(i))
        
