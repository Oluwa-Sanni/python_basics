weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"Weight in Kg: {converted}")
else:
    converted = weight / 0.45
    print(f"Weight in Lbs: {converted}")


i = 1
while i <= 100:
    print(i)
    i += 50



numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)
