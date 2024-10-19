#Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.


try:
    temp = int(input("Enter temp in Farenheit: "))
    celcius = (temp - 32) * 5/9
except ValueError:
    print("That isn't a valid number. Please try again.")
else:
    print(f"{temp} degrees Farenheit is {celcius} degrees Celcius.")
finally:
    print("Thanks for using the Weather Forecasting app.")
    

