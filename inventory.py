class Product:
    
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity    

    def update_stock(self, amount):     
        if self.quantity + amount < 0:
             print("Stock cannot be a negative")
        else:
            self.quantity += amount
              
    def get_total_value(self):
         return self.price * self.quantity
    
    def __str__(self):
        return f"ID: {self.product_id} | {self.name} ({self.price}) | Stock: {self.quantity}"

    
class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def restock(self,product_id, amount):
        get_product = self.products[product_id]
        get_product.quantity += amount

    def sell_product(self, product_id, amount):
        get_product = self.products[product_id]
        if get_product.quantity > 0 :
            get_product.quantity -= amount

    def display_all(self):
        for indiv_product in self.products.values():
            print(indiv_product)

        


if __name__ == "__main__": 
    
        inventory = Inventory() 

        while True:
              print("\n 1. Add new product \n 2. View all Inventory \n 3. Update Product Stock (Buy/Sell) \n 4.Exit")

              pick = input("Pick a option")

              if pick == "1":
                    
                poduct_id = input("Enter ID: ")
                name = input("Enter name: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
            
                product = Product(poduct_id, name, price, quantity)
                inventory.add_product(product)

              elif pick == "2":
                 inventory.display_all()

              elif pick == "3":
                   product_id = input("Product ID?")
                   buy_sell = input("Would you buy/sell").lower()
                   amount= int(input("Input quantity"))       
                   if buy_sell == "buy":
                      inventory.sell_product(product_id, amount)
                   elif buy_sell == "sel;":
                      inventory.sell_product(product_id, amount)
                   else:
                       print("nope pick another mate")

              elif pick == "4":
                  print("cya")
                  break
              
              else:
                  print("invalid my guy")
                  

            
 





  


        