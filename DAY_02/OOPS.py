
#class,object,self
class cse1:
    def strength(self):
        print("The strength is 101")
        self.s=101
    def kn(self):
        print("The knowledge is good")
        self.know="good"
        
    def details(self):
        print("The current strength and knowledge")
        c_s=self.s - 10
        print(c_s,self.know)
day_2=cse1()
day_2.strength()
day_2.kn()
day_2.details()
        


#constructor
class cse1:
    def __init__(self,a,b):
        self.a1=a
        self.b1=b
        print("constructor")
    def strength(self):
        print("The strength is 101")
        self.s=101
    def kn(self,c,d):
        print("The knowledge is")
        self.know="good"
        pro=c+d
        print(pro)
    def details(self):
        print("The current strength and the knowledge")
        c_s=self.s-10
        print(c_s,self.know)
        print(self.a1+self.b1)
day_2=cse1(2,10)
day_2.strength()
day_2.kn(2,10)
day_2.details()

#===============================================================
#=========================OUTPUT================================
'''
The strength is 101
The knowledge is good
The current strength and knowledge
91 good
constructor
The strength is 101
The knowledge is
12
The current strength and the knowledge
91 good
12
'''