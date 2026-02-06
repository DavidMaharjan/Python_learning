class shopping_cart:
    def __init__(self):
        self.cart= []
    def __add__(self,itm):
        self.cart.append(itm)
    def __len__(self):
        return len(self.cart)
    def remove(self,itm):
        if itm in self.cart:
            self.cart.remove(itm)
        else:
            return "Item not in cart"
    def _get_cart__(self):
        return self.cart
    
    def contains(self,itm):
        return itm in self.cart
    def clear_cart(self):
        self.cart.clear()
        
cart = shopping_cart()
cart.__add__("apple")   
cart.__add__("banana")
print(cart._get_cart__())
print(len(cart))
print(cart.contains("apple"))
print(cart.contains("orange"))  
cart.remove("banana")
print(cart._get_cart__())
cart.clear_cart()
print(cart._get_cart__())
    
        