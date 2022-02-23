def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    if int(in_num) > 21:
        n = (int(in_num) - 21) * 2 
    if int(in_num) < 21:
        n = 21 - int(in_num)
    print('Result:', abs(n))

calculateAbsolute()

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateAbsolute()