#Created by Bjorn Eriksson

#Missed discussion about how to import custom files, study that solo.

################ Day 1:   #####################

#Building a dog park

class DogPark:
    def __init__(self, name):
        self.name = name
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)
    
    def show_dogs(self):
        for dog in self.dogs:
            print(dog.get_name())

    def change_dog_name(self, old_name, new_name):
        for dog in self.dogs:
            if dog.get_name() == old_name:
                dog.set_name(new_name)

    def find_dog(self, dog_name):
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                dog.speak()
    
    def call_dog(self, dog_name):
        #Remove dog from list of dogs.
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                self.dogs.remove(dog_name)

    
            
'''



'''


class Dog:
    def __init__(self, name, size, breed ='Unknown'): #Alyways put any optinal variables in the back.
        self.name = name
        self.breed = breed
        self.size = size
        
    #getters
    def get_name(self):
        return self.name
    def get_breed(self):
        return self.breed
    def get_size(self):
        return self.size
    #setters
    def set_name(self, new_name):
        self.name = new_name
    def set_breed(self, new_breed):
        self.breed = new_breed
    def set_size(self, new_size):
        self.size = new_size

    def speak(self):
        if self.size == 1:
            print('yip!')
        elif self.size == 2:
            print('bark')
        elif self.size == 3:
            print('woof')


'''
park1 = DogPark("Bark Zone")

park1.add_dog(Dog("Fluffy", 1, ))
park1.add_dog(Dog("Spot", 2, "Lab"))
park1.add_dog(Dog("Rover", 3, "Mastiff"))
park1.add_dog(Dog("Spike", 3, ))

park1.show_dogs()
park1.call_dog("Spot")
park1.show_dogs()

#park1.find_dog("Rover")
#park1.find_dog("Spot")
#park1.find_dog("Fluffy")
'''

################### Day 2:   ########################

#write a class for a bank account. Bank account should have an owner and a balance, and should be able to
# -Deposit money
# - Withdraw money

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    #getters
    def get_owner(self):
        return self.owner
    def get_balance(self):
        return self.balance
    #setters
    def set_owner(self,new_owner):
        self.owner = new_owner
    def set_balance(self,new_balance):
        self.balance = new_balance
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= withdraw_amount
            print(f"Here is your {withdraw_amount}")
    
    def __str__(self):
        msg = ''
        msg += f'owner: {self.owner}, balance: {self.balance}'
        return msg
    def __add__(self, other_account):
        new_owner = f'{self.get_owner()} & {other_account.get_owner()}'
        new_balance = self.get_balance() + other_account.get_balance()
        new_account = BankAccount(new_owner, new_balance)
    def __eq__(self, other):
        """ Let's assume this bank only allows one account per user"""
        return self.get_owner() == other.get_owner()

        
matt_acc = BankAccount('Matt')
matt_acc.deposit(100)
matt_acc.deposit(50)

ashley_acc = BankAccount("Ashley", 500)

joint_acc = matt_acc + ashley_acc


















































