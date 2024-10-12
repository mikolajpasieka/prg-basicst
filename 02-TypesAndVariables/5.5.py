#Display the product price, discount, discounted product price, and the difference between the product price before and after the discount.
import math
price = input("Enter price:")
discount = input("Enter discount:")
discounted_product_price =int(price)-int(price)*int(discount)/100
reduction = int(price) - int(discounted_product_price)

price_r = math.ceil(int(price)*100)/100
discount_r = math.ceil(int(discount*100))/100
discounted_product_price_r = math.ceil(int(discounted_product_price*100))/100
reduction_r = math.ceil(int(reduction*100))/100

print(f"Price: {price_r}")
print(f"Discount: {discount_r} %")
print(f"Discounted product price: {discounted_product_price_r}")
print(f"Reduction: {reduction_r} ")