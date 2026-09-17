# DOMINIQUE JILLIAN S. ANG
# 8 - SAMPAGUITA
# PAYMENT METHOD

valid_methods = ["Cash", "GCash", "Card"]

payment = input("Please enter your payment method: ").lower

if payment in valid_methods:
    print("Your payment method is ", payment)
else:
    print("Your payment method is not valid")