

class CashRegister:
    def __init__(self, discount=0):
        
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
       
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            'item': item,
            'price': price,
            'quantity': quantity
        })

    def apply_discount(self):
       
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        
        self.total = self.total * (100 - self.discount) / 100
        
        if float(self.total).is_integer():
            total_str = str(int(self.total))
        else:
            total_str = str(self.total)
        print(f"After the discount, the total comes to ${total_str}.")

    def void_last_transaction(self):
       
        if not self.previous_transactions:
            print("No transaction to void.")
            return
        last = self.previous_transactions.pop()
       
        self.total -= last['price'] * last['quantity']
       
        for _ in range(last['quantity']):
            if last['item'] in self.items:
                self.items.remove(last['item'])