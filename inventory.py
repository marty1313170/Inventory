class Product:
    product_dict = {}

    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.product_dict[name] = self 

        

    def update_stock(self, quantity):     
        choose_item = input("What item would you like to update? Buy/Sell")
        
        if choose_item in self.product_dict:
            print(f"Item found: {self.product_dict[choose_item]}")

            product = self.product_dict[choose_item]
            while True:
                choose_option = input("You can \n 1. Add Stock \n 2. Minus Stock \n 3. Exit\nChoose an option: ")

                if choose_option == "1":
                    print("Stock is updating... please wait")
                    product.quantity += 1
                    print(f"New total stock is {product.quantity}")
                elif choose_option == "2":
                    print("Stock is updating... please wait")
                    if product.quantity > 0:
                        product.quantity -= 1
                        print(f"New stock is {product.quantity}")
                    else:
                        print("Number is 0 cannot have negative stock")
                elif choose_option == "3":
                    break
                else:
                    print("invalid option ")

    def get_total_value(self, quantity, price):

        total = 0 
        
        for product in self.product_dict.values():
            total += product.price * product.quantity

            print(f"Total inventory value is {total}")
            
            return total
    
class Inventory:
    def __init__(self):
        

