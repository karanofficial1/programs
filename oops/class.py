# area of circle
class AreaOfCircle():
    PI = 3.14
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
       
        self.radius = radius

    def area_circle(self):
            print(f"Area of cirle: { self.PI * self.radius**2}")

try:
    area = AreaOfCircle(-5)
    area.area_circle()
except ValueError as e:
    print(f"Validation Error: {e}")



class Shop():
    def __init__(self, product_name, price, qty):
        self.product_name = product_name
        self.price = price
        self.qty = qty

    def total_price(self):
        if self.price < 1:
            print("Price could not be less than 1.")
        elif self.qty < 1:
            print("Quantity could not be less than 1")
        else:
            print(f"The product is {self.product_name} and it's total price is Rs.{ self.price * self.qty } ")

book_name = input("Enter Your book name: ")
book_price=  float(input("Enter price of book: "))
book_qty = int(input("Enter quantity of books: "))
book = Shop(book_name, book_price, book_qty)
book.total_price()