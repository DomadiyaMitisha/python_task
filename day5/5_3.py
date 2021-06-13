import math
class cal3:
    k=0
    i=0
    s=0
    
    def __init__(self , k , i , s ):
        self.k=k
        self.i=i
        self.s=s

    def callinterest(self):
        self.interest= self.k*(1.0 + (self.i*self.s))
        
    def display(self):
        print("the simple interest is : " , self.interest )

call=cal3(44.33,90,20)
call.callinterest()
call.display()
