class ShoppingCart:
    
    def __init__(self):
        self.items = []
    
    def add_items(self,itemName:str, itemPrice:int, itemQuantity:int):
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity
        
        self.items.append((itemName, itemQuantity, itemPrice))
        
    def remove_items(self,itemName:str):
        for item in self.items:
            if item[0] == itemName:
                self.items.remove(item)

    def calculate_total(self):
        total = 0
        
        for item in self.items:
            _,quantity, price = item
            total += quantity * price
        return total
            
    def summary(self):
        print("Shopping Cart Summary:")
        for itemName,itemQuantity,itemPrice in self.items:
           print(f"{itemName}: {itemQuantity} @ ksh {itemPrice} each")
        print(f"Total: ksh {self.calculate_total()}")
   
        
if __name__ == "__main__":
    cart:ShoppingCart = ShoppingCart()
    cart.add_items("Apple", 90, 3)
    cart.add_items("Banana", 20, 5)
    cart.add_items("Orange", 50, 2)
    
    cart.summary()