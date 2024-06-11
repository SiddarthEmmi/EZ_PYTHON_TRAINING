'''
QUESTION:
Create a class CarShowRoom in which 
-->Create a function in name CarCompany which will allow user to select a car company 
which will allow user to select a car company out of diaplayed companies. If the user
enters any random car company he/she should be asked to re-entry.
-->According to the car company selected the user should be re-directed to selecting 
the models of thst company.Out of the given list if anything other then model he/she
should re-enter
-->Now, after selecting the model the user should be re-directed through selecting 
the varient(petrol/deisel)
-->According to the car company model and varient a price should be calculated to 
which SGST & CGST are added to make it the total price.
NOTE: SGST & CGST are common for all the cars.
'''

class carshowroom:
    def __init__(self):
        self.cgst = 200000
        self.sgst = 100000
        self.insurance = 200000
    def company(self):
        while True:
            print("Toyota,Mercedes")
            self.n=input("Enter the car company: ")
            if self.n=="Toyota":
                print("Welcome to Toyo")
                self.model()
                break
            elif self.n=="Mercedes":
                print("Welcome to merc")
                self.model()
                break
            else:
                print("Enter valid company: ")
    def model(self):
        if self.n=="Toyota":
            while True:
                print("Select from Fortuner and LC")
                self.choice = input("Enter the car model: ")
                if self.choice == "Fortuner":
                    self.price(self.choice)
                    break
                elif self.choice == "LC":
                    self.price(self.choice)
                    break
                else:
                    print("Enter Valid")
        elif self.n=="Mercedes":
            while True:
                print("Select from amg and gw")
                self.choice = input("Enter the car model: ")
                if self.choice == "amg":
                    self.price(self.choice)
                    break
                elif self.choice == "gw":
                    self.price(self.choice)
                    break
                else:
                    print("Enter Valid")
    def price(self,choice):
        if choice == "Fortuner":
            self.p = 5000000
        elif choice == "LC":
            self.p = 1000000
        elif choice == "amg":
            self.p = 24432874
        elif choice == "gw":
            self.p = 843726837
        tot_p = self.p+self.sgst+self.cgst+self.insurance
        print(tot_p)
        
c = carshowroom()
c.company()

#==============================================================================
#====================================OUTPUT====================================
'''
Toyota,Mercedes
Enter the car company: Toyota
Welcome to Toyo
Select from Fortuner and LC
Enter the car model: Fortuner
5500000


Toyota,Mercedes
Enter the car company: Mercedes
Welcome to merc
Select from amg and gw
Enter the car model: gw
844226837


Toyota,Mercedes
Enter the car company: Tata
Enter valid company: 
Toyota,Mercedes
Enter the car company: Toyota
Welcome to Toyo
Select from Fortuner and LC
Enter the car model: Innova
Enter Valid
Select from Fortuner and LC
Enter the car model: Fortuner
5500000
'''