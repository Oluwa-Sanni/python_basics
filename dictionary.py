file = open("olympians.txt", "r")
words = file.read()
count = 0
for word in words:
    if word == "a":
        count += 1
print("a:" + str(count) + " times")
file.close()


file = open("olympians.txt", "r")
words = file.read()
count = {}
for word in words:
    if word not in count:
        count[word] = 0
    count[word] += 1
print(count)
file.close()


file = open("olympians.txt", "r")
words = file.read()
count = {}
count["a"] = 0
count["e"] = 0
for word in words:
    if word == "a":
        count[word] = count[word] + 1
    elif word == "e":
        count[word] = count[word] + 1
print("a: " + str(count["a"]) + " times")
print("e: " + str(count["e"]) + " times")
file.close()



file = open("olympians.txt", "r")
words = file.read()
count = {}
for word in words:
    if word not in count:
        count[word] = 0
    count[word] += 1
print("k: " + str(count["k"]) + " times")
print("t: " + str(count["t"]) + " times")
file.close()


file = open("olympians.txt", "r")
words = file.read()
count = {}
for word in words:
    if word not in count:
        count[word] = 0
    count[word] += 1

for y in count:
    print(y + ": " + str(count[y]) + " times")
file.close()