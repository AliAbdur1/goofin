class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    

    def __str__(self):
        return self.name + ":" + str(self.price)
    
    def __repr__(self):
        return str(self)
    
class VendingMachine:
    def __init__(self, password):
        self.balance = 0
        self.password = password
        self.items = []

    def add_item(self, name, price, password):
        if self.password != password:
            print("Password was incorrect")
            return
        item = Item(name, price)
        self.items.append(item)

    def purchase_item(self, index, pay):
        if index < 0 or index >= len(self.items):
            print("Invalid index")
            return None, pay
        item = self.items[index]
        if item.price > pay:
            return None, pay
        else:
            self.balance += item.price
            change = pay - item.price
            del self.items[index]
            return item, change
        
    def __str__(self):
        info = "Vending Machine Balance: " + str(self.balance) + "\n"
        for item in self.items:
            info += repr(item) + "\n"
        return info


#TEST CODE
my_password = "cheessauce"
wrong_password = "monkey"

vm = VendingMachine(my_password)

vm.add_item("Twix", 1.25, my_password)
vm.add_item("Doritos", 1.25, my_password)
vm.add_item("Gum", .25, my_password)
vm.add_item("Sniggers", 1.25, wrong_password) #incorrect password
vm.add_item("Twix", 1.25, my_password)

print("\nBefore:")
print(vm)

print("\nAfter:")
print(vm.purchase_item(1, 1.50))
print(vm.purchase_item(3, 1.50))
print(vm)

