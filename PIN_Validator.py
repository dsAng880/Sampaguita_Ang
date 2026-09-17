# DOMINIQUE JILLIAN S. ANG
# 8 - SAMPAGUITA
# PIN VALIDATOR

pin = input("Enter PIN: ")

if len(pin) == 6 and pin.isdigit():
    print("PIN is valid")
else:
    print("PIN is not valid")