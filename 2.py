# Ask user to enter the weather
weather = input("Enter the weather (autumn or spring): ")

# Check the weather using if-else
if weather == "autumn":
    print("The weather is cool and leaves are falling,")
elif weather == "spring":
    print("The weather is warm and flowers are blooming.")
else:
    print("Please enter either 'autumn' or 'spring'.")