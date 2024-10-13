#Display the product price, discount, discounted product price, and the difference between the product price before and after the discount.
price = input("Enter price:")
discount = input("Enter discount:")
discounted_product_price =float(price)-round((float(price)*float(discount)/100), 2 )
reduction = float(price) - float(discounted_product_price)

discounted_product_price_r = round( discounted_product_price, 2)
reduction_r = round (reduction, 2)

print(f"Price: {price}")
print(f"Discount: {discount} %")
print(f"Discounted product price: {discounted_product_price_r}")
print(f"Reduction: {reduction_r} ")