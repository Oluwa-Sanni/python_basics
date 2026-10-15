print("This will be executed first")

for _ in range(5):
    print("This will execute five times")
    print("This will also execute five times")
print("now we are outside the loop")

z = ("This will be executed first")
print(z.count("e"))
print(z.index("e"))

for name in ["Babs", "John", "Bob", "Mosh", "Sarah"]:
    print("Hello", name , "Please come to the meeting at 3pm")


values = [2, 4, 6]
result = 1

for num in values:
    result = result * num

print(num)
print(result)


text_file = open("file.txt", "w")
for num in range(10):
    square = num * num
    text_file.write(str(square) + "\n")
text_file.close()


olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

new_file = open("olympian.txt", "w")
new_file.write("Name, Age, Sport")
new_file.write("\n")
for oly in olympians:
    row_input = "{}, {}, {}\n".format(oly[0], oly[1], oly[2])
    new_file.write(row_input)
    new_file.write("\n")
new_file.close()

import csv
with open("olympian.txt", "r") as new_file:
    reader = csv.reader(new_file)
    headers = next(reader)
    print(headers)
    for row in reader:
       if row[4].strip() == "Cycling":
           print(f"{row[0]}, {row[1]}, {row[3]}")