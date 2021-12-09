'''timer'''
import time

def pd():
    
    answer1 = input("Answer 1: (0 or 1)")
    
    '''for technical purposes'''
    time.sleep(5)
    
    answer2 = input("Answer 2: (0 or 1)")

    '''main_algorithm'''
    if (answer2 == "0") and (answer1 == "0"):
        print("both free")
    if (answer2 == "0") and (answer1 == "1"):
        print ("you free, the other in jail")
    if (answer2 == "1") and (answer1 == "1"):
        print("both jail")
    if (answer2 == "1") and (answer1 == "0"):
        print("you jail, the other free")
    pass
        
'''function call'''
pd()
