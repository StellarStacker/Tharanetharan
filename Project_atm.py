import time
class Authenticate:
    def __init__(self):
        self.Pin_map={1234:1920010000010001,4532:1920010000010002,4321:19200100001000003}
        self.Name_map={1920010000010001:"Akash B",1920010000010002:"Bharath P",19200100001000003:"Monika A"}
        self.bal_map={1920010000010001:1000.0,1920010000010002:1000.0,19200100001000003:1000.0}
        print("\n")
        print("\t\t\t\t\tWELCOME TO SRM ATM","\n")
        print("-"*100,"\n")
        print("Please insert your card...","\n")
        time.sleep(2)
        self.pin=int(input("Enter your pin : " ))
        self.auth()
    def auth(self):
        if(self.pin in self.Pin_map.keys()):
                print("\n\t**Please wait while your pin is being verified**","\n")
                time.sleep(1)
                print("\t\t\tLogin successfull","\n")
                print("-"*100,"\n")
                user_map=self.pin
                p=self.Atm_func(self.Name_map,self.Pin_map,user_map,self.bal_map,self)
                p.choice_list()
        else:    
            print("Incorrect pin","\n")
            self.logout() 
    def auth_pin(self,test_pin):
        if(test_pin==self.pin):
            return True
        else:
            return False               
    def logout(self,):
        print("\t\tLogout successfull","\n") 
    class Atm_func():
        def __init__(self,namemap,pinmap,user_map,bal_map,Authclass):
            self.namemap=namemap
            self.pinmap=pinmap
            self.user_map=user_map
            self.bal_map=bal_map
            self.Authclass=Authclass
            self.Accountnumber=self.pinmap[(user_map)]
            self.user_name=namemap[self.Accountnumber]
            self.balance=self.bal_map[self.Accountnumber]
        def choice_list(self):
             self.Repeat=True
             while(self.Repeat==True):
                print("\tWelcome :",self.user_name,"\n")
                print("  1.Deposit")
                print("  2.Withdraw")
                print("  3.Balance Enquiry")
                print("  4.Change Pin")
                print("  5.View Profile")
                print("  6.Exit")
                print()
                try:
                    ch=int(input("Enter your choice : "))
                except ValueError:
                    print("Invalid choice")
                    self.choice_list()
                finally:
                    print()
                if(ch==1):
                    self.deposit()
                elif(ch==2):
                    self.withdraw() 
                elif(ch==3):
                    self.display()   
                elif(ch==4):
                    self.change_pin() 
                elif(ch==5):
                    self.viewprofile()
                elif(ch==6):
                    self.exit()
                else:
                    time.sleep(0.6)
                    print("Wrong choice")
                    self.Repeat=False
                    self.Authclass.logout()    
        def deposit(self):     
            print("\t\t Welcome to deposition corner","\n")
            time.sleep(2)
            d=eval(input("Enter the amount you want to deposit : "))
            print()
            if(d>0):
                self.balance+=d
                self.bal_map[self.Accountnumber]+=d
                print("\tPlease wait while your cash is being deposited","\n")
                time.sleep(2)
                print("  Amount deposited successfully","\n")
                time.sleep(0.5)
            else:
                print("Kindly enter amount greater than zero","\n")
                time.sleep(0.6)
        def withdraw(self):
            print("\t\tWelcome to Withdrawal corner","\n")
            time.sleep(1.5)
            print("  Available denominations : 100 , 200 , 500 , 2000","\n")
            w=eval(input("Enter the amount in multiples denominations below : "))
            print()
            if(w<=self.balance):
                print("Please wait while your transaction is in process..")
                time.sleep(1.5)
                print("Withdrawal success","\n")
                self.balance-=w
                time.sleep(0.4)
            elif(w>=self.balance):
                time.sleep(1)
                print("Insufficient balance","\n")
                time.sleep(0.5)
                self.Authclass.logout()
            else:
                time.sleep(1)
                print("Invalid operation")
                self.Repeat=False
                time.sleep(0.4)
                self.Authclass.logout()    
        def display(self):
            print("Please wait your transaction is being processed..")
            time.sleep(1.5) 
            print("Name : ",self.user_name,"\n")
            print("AccountNumber : ",self.Accountnumber,"\n")
            print("Balance : ",self.balance,"\n")
        def change_pin(self):
            print("**WELCOME TO PIN CHANGE**")
            Acc_no=int(input("Enter your account number : "))
            if(self.pinmap[self.Authclass.pin]==Acc_no):
                print("....Please wait while your details are being verified...")
                time.sleep(1.5)
                self.old_pin=int(input("Enter the old pin : "))
                time.sleep(0.4)
                if(self.Authclass.pin==self.old_pin):
                    self.new_pin=int(input("Enter the new pin : "))
                    time.sleep(0.2)
                    print("**Please wait while your transaction is being processed**","\n")
                    k=self.pinmap.keys()
                    if(self.new_pin not in k):
                        if(self.old_pin in k):
                            self.old_pin=self.new_pin
                            time.sleep(1.5)
                            print("Pin change sucessfull")
                            time.sleep(0.2)
                            self.Repeat=False
                            self.Authclass.logout()
                            temp_pin=int(input("Enter your pin : "))
                            if(temp_pin==self.old_pin):
                                time.sleep(0.5)
                                self.Authclass.auth()
                            else:
                                time.sleep(0.1)
                                print("Internal error occured")
                            
                        else:
                            print("Kindly valid new pin")
                            time.sleep(1.5)
                            self.Repeat=False     
                    else:
                        self.Repeat=False
                        print("Pin already exists") 
            else:
                time.sleep(2.0)
                print("Invalid data entered")
                self.Authclass.logout()
        def exit(self):
            time.sleep(0.2)
            print("\t\t Thankyou for using SRM ATM")
            time.sleep(1)
            self.Repeat=False
        def viewprofile(self):
            time.sleep(1.5)
            t=int(input("Enter the your pin : "))
            print()
            print("...please wait while your transaction is being processed...","\n")
            time.sleep(1)
            if(self.Authclass.auth_pin(t)): 
                print("Username : ",self.user_name,"\n")
                print("Account Number : ",self.Accountnumber,"\n")
		print("Branch name :  Kattankulathur","\n")
                print("Bank Name : SRM BANK OF INDIA","\n")
                time.sleep(3)
                self.Repeat=False
            else:
                print("Kindly enter valid pin","\n")    
                time.sleep(1)
                self.Repeat=False
ob=Authenticate() 
#one line added