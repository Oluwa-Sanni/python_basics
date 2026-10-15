import math

print("Hello World!")
print("*" * 10)

x = 1
course = "Python\"s Programming"
print(len(course))
print(course[0])
print(course[0:3])
print(course)

x = input("x: ")
y = int(x) + 2
print(f"x: {x}, y: {y}")

temperature = 27
if temperature > 30:
    print("It is warm outside")
    print("Drink Water")
elif temperature > 25:
    print("Ideal temperature")
    print("Go outside with Sun glasses")
else:
    print("It is freezing outside") 
print("Done")


txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")