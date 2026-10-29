def tosin():
    print("Hello, This is Tosin")
    print("I am python programmer")

print("This is my first function")
tosin()


def most_freq_letters(s):
    freq = letter_count(s)
    return most_common(freq)

def letter_count(str):
    ##file = open("olympians.txt", "r")
    ##words = file.read()
    count = {}
    for word in str:
        if word not in count:
            count[word] = 0
        count[word] += 1
    ##file.close()
    return count

def most_common(dic):
    ks = dic.keys()
    common = list(ks)[0]
    for k in ks:
        if dic[k] > dic[common]:
            common = k
    return common

##with open("olympians.txt", "r") as file:
  ##  words = file.read()

##print("Most frequent letter is: " + str(most_freq_letters(words)))

print("Most frequent letter is: " + most_freq_letters("sssdfghguhkjhkljkjlkjkhgfttrrswdazaqawaqaaxcvooonhjvc"))