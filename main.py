from problem2 import *

company1 = Company("Apple", 1976, "Steve Jobs")
product1 = Product("iPhone", 1000, 3, company1)
product2 = Product("iPad", 800, 2, company1)


basket = Basket()
basket.add(product1)
basket.add(product2)


basket_dict = basket.to_dict()
print(basket_dict)