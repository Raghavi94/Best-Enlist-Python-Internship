#TASK-13:
#Classes and objects
tot_water=1000
tot_milk=1000
tot_coffee=1000
class CoffeeMachine:
   # print("---")
   # print("This is a coffee machine!")
   # print("---")
    def __init__(self,name):
        self.name=name
        self.money=0
    def resources_check(self,water,milk,coffee):
        global tot_water
        global tot_milk
        global tot_coffee
        self.water,self.milk,self.coffee=water,milk,coffee
        if tot_water >= self.water:
            if tot_milk >= self.milk:
                if tot_coffee >= self.coffee:
                    tot_water=tot_water-self.water
                    tot_milk=tot_milk-self.milk
                    tot_coffee=tot_coffee-self.coffee
                    return True
                else:
                    print("Sorry!There's no sufficient coffee powder")
                    return False
            else:
                print("Sorry!There's no sufficient milk")
                return False
        else:
            print("Sorry!There's no sufficient water")
            return False
    def payment(self):
            sal="Insert Coins" # money calculation is done here
            print("----------------------")
            quarter,dimes,nickles,pennies,=int(input("Quarter:")),int(input("Dimes:")),int(input("Nickles:")),int(input("Pennies:"))
            cus_money=0.25*quarter+0.1*dimes+0.05*nickles+0.01*pennies
            if cus_money ==self.money:
                print("Your Payment is successful")
                return True
            elif    cus_money >=self.money:
                self.money = cus_money - self.money
                print("Your payment is sucsessful")
                print(f"Collect your change ${self.money:.2f} dollars")
                return True
            else:
                print("Sorry!! You don't have enough money")
                print(f"Money refunded{cus_money:.2f}")
                return False
    def make_coffee(self):
           print(f"------Here's your {self.name}.Enjoy!------")
           return True
    def report(self,mon):
        self.mon=mon
        print("Here's the report.")
        print("---------------------------")
        print("Total water:",tot_water,"ml")
        print("Total milk:",tot_milk,"ml")
        print("Total coffee:",tot_coffee,"gm")
        print(f"Money: ${self.mon}")
      
def repo(mon):
    disp=input("Do you want the report? yes or no\t ")
    if disp in["yes","YES","Y","y"]:
        return obj.report(mon)
    else:
        pass
        

        

string=print("Hello!Welcome to STAR CAFE!!")
print("-----------------------------------")
while True:
    machine=input("Enter the code(on or off):")
    if machine=="on":
        while True:
            choice=int(input("What would you like to have? \n1.Expresso\n2.Latte\n3.Cappuccino\t"))
            if(choice==1):
                obj = CoffeeMachine("Espresso")
                repo(0)
                obj.money=3.5
                if obj.resources_check(50,225,20)==True:
                    if obj.payment()==True:
                        if obj.make_coffee()==True:
                            repo(3.5)

            elif choice==2:
                obj=CoffeeMachine("Latte")
                repo(0)
                obj.money=4.5
                if obj.resources_check(50,200,16)==True:
                   if obj.payment()==True:
                       if obj.make_coffee()==True:
                           repo(4.5)
            elif choice==3:
                obj=CoffeeMachine("Cappuccino")
                repo(0)
                obj.money=6.5
                if obj.resources_check(50,200,20)==True:
                   if obj.payment()==True:
                       if obj.make_coffee()==True:
                           repo(6.5)
            else:
                print("Sorry!!..Please Enter the correct choice")

            cont=input("Do you wanna continue: YES or NO")
            if cont in["YES","yes","Y","y"]:
                pass
            else:
                break
        a="Visit Again!!!"
        print("-------------------")

    else:
         print("Machine is switched off!")
         break
