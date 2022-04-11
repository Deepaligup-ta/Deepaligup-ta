class student():
    def marks(Self):
      
        self.english=int(input("enter the marks of english:"))
       
        self.hindi=int(input("enter the marks of hindi:"))
       
       
       self.maths=int(input("enter the marks of maths:"))
      
       self.sience=int(input("enter the marks of science"))
        
       self.sst=int(input("enter the marks of sst:"))
       
    def Percent(Self):
        self.percentage=(self.english+self.hindi+self.maths+self.science+self.sst)/5
       
        print("percentage of student is :",percentage)
    def call(self):
        print("marks of english:",self.english)
        print("marks of hindi:",self.hindi)
        print("marks of maths:",self.maths)
        print("marks of science:",self.maths)
        print("matks of sst:",self.sst)
        print("percentage of karan is :",self.percentage)

karan=student()
karan.marks()
karan.Percent()
karan.call()
        

        
        
