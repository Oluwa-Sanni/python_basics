age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


for w in words[:]:
    if len(w) > 4:
        words.insert(0, w)
        print (words)



for i in range(5, 20):
    print(i)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print (list (range(5)))
