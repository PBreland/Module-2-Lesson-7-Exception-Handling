#Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.


try:
    temp = int(input("Enter temp in Farenheit: "))          #Task 1: Asking the user to input a number.
    celcius = (temp - 32) * 5/9                          #Task 2: Writing a formula for converting farenheit to celcius.
except ValueError:
    print("That isn't a valid number. Please try again.")
else:                                                       #Task 3: Implimenting an else block.
    print(f"{temp} degrees Farenheit is {celcius} degrees Celcius.")
finally:                                            #Task 4: Adding a Finally Block.
    print("Thanks for using the Weather Forecasting app.")
    

