class OutOfStockError(Exception):
    pass
class PaymentFailedError(Exception):
    pass
class InvalidAddressError(Exception):
    pass
class Order:
    def __init__(self,stock,payment_status,address):
        self.stock = stock
        self.payment_status = payment_status
        self.address = address
    def place_order(self):
        try:
            if self.stock <= 0:
                raise OutOfStockError("product unavalid")
            if not self.payment_status:
                raise PaymentFailedError("payment is failed")
            if self.address.strip() =="":
                raise InvalidAddressError("add")
            print("Order placed successfully")
        except OutOfStockError as e:
            print(e)
        except PaymentFailedError as e:
            print(e)
        except InvalidAddressError as e:
            print(e)
stock = int(input("enter stock:"))
payment = input("Payment successful (yes/no):").lower()
address = input("enter the address")
payment_status = payment =="yes"
obj = Order(stock, payment_status,address)
obj.place_order()