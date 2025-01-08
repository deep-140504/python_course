print('hello world')
x = 0
while x < 5:
    print('the current value of x is {y}'.format(y = x))
    x = x + 1

ls = []
for x in[1, 2, 3]:
    for y in [4, 5, 6]:
        ls.append(x * y) #this is the one way of doing this
print(ls)
#the more optimised way of doing the same is as followed:
lst = [x * y for x in range(1, 4) for y in range(4, 7)]
print("this is lstf")
print(lst)