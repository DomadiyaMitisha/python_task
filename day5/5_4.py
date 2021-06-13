class cal5:
    n=0
        
    def setdata(self):
        self.n=int(input("Enter the number :"))
    
    def display(self):
        ans =self.n**2
        print("The square of the number is : " , ans)

sum=cal5()
sum.setdata()
sum.display()