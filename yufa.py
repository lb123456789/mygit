"""
words = ["this","is","an","ex","parrot" ]
for word in words:
    print(word)

numbers = [1,2,1,2,2,3,3,5,6,]
for number in numbers:
    print(number)

for number1 in range(1,100):
    print(number1)


# 迭代字典

d = {"X": 1, "Y": 2, "Z": 3}
for key in d:
    print(key, "correponds to", d[key])

# 并行迭代
name = ["ddf1", "ddf2", "ddf3", "ddf4"]
ages = [1, 2, 3, 4]
for i in range(len(name)):
    print(name[i], "is", ages[i], "years old")
    if name[i] is "ddf3":
        break

# while循环

x = 1
while x <= 100:
    print(x)
    x += 1



def power(x, n):
    if n==0:
        return 1

    else:
        return x* power(x,n-1)
print(power(2, 3))
"""
