'''
This program is used to validate a Credit Card Number (CCN) using a Check Digit(CD)
For this example, we will use LUHN's algorithm to check the 

1. Prefix must be MAstercard or Visa only
2. Length of CCN must be 16 digits
3. Check Digit (CD) must be valid - use LUHN's algo.


Luhns Algo.
    
    checkdigit format - uses LUHN's algorithm - modulo = even number
    remainder principle

    Step 1. working from the right, for each even number position: 2,4,6,
            etc: multiply by 2
        Step 1a. if the total is a two digit number, add the two digits together
                e.g 46 => 4+6 = 10 = this is known as the "digital root"
        Step 1b. Add this value to a running total for even numbers

    Step 2: add odd position values to running total
    Step 4: round up to nearest 10, so 53 rounded -> 60, difference is 7
    Step 5: this is the checkdigit

'''

# functions defined here
def fn_luhn(CCNumber):
    CDNumber = CCNumber[0:15]#This is the CC number without the last dgit(check digit)
    CD = CCNumber[15]#This is the CC Check digit
    CDeven = CDNumber[0:15:2]
    CDodds = CDNumber[1:15:2] 
    CDoddstotal = 0
    CDeventotal = 0
    CDtotal  = 0

    
    for x in CDeven:#This for loop get the even position numbers total

        x = int(x)
        x = x*2
        if x > 9:
            x = x - 9
        CDeventotal = CDeventotal + x

        
    for x in CDodds:#This for loop get the odd position numbers total
        
        x = int(x)
        CDoddstotal = CDoddstotal + x

    CDtotal = CDeventotal + CDoddstotal

    checkdigit_totalcalc = 0
    

    while  checkdigit_totalcalc < CDtotal:#This while loop gets the next multiple of 10 of the total number 
        checkdigit_totalcalc = checkdigit_totalcalc + 10

    luhns_result = checkdigit_totalcalc - CDtotal#This finds the result of luhns
    
        
        
    if int(CD) == int(luhns_result):
        print("Valid Credit Card Number!")

    else:
        print("Check digit is invalid - CC number invalid!")
    
        
        




# main program starts here




while True:
    CCNumber = input("Insert Credit Card number here ---->")
    if CCNumber.isdigit():#This validates if the credit card is numbers
        print("Validating number of digits...")
        
        if len(CCNumber) == 16:
            
            print("Number of digits is Valid!")

            if CCNumber[0:2] in ["50", "51", "52", "53", "54", "55"]:#This validates if the prefix is mastercard
                print ("Mastercard!")
                break
        
       
        

            elif CCNumber[0:1] == "4":#This validates if the prefix is visa

                print("Visa!")
                break
        
        


            else:
                print("No prefix detected - Invalid CC number!")
            
        elif len(CCNumber) > 16 or len(CCNumber) < 16:#This validates the number of digits in the cc nr is 16
            print("Number of digits is Invalid - Invalid CC number!")

        
    else:
        print("Invalid input - number expected")



    



fn_luhn(CCNumber)#Use function

    
    

    
               
            
        
    










    
