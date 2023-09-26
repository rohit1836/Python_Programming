import random,string
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digit = string.digits
symbols = string.punctuation
all = upper + lower + digit + symbols

temp = ""
for i in range(8,16):
    temp = random.choice(all) + temp
print(temp)


