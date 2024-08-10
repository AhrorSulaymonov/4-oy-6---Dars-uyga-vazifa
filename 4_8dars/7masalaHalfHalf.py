A = int(input("Ani kiriting: "))
B = int(input("Bni kiriting: "))
count = 0
while A> 2 * B:
    A /= 2
    count += 1
print(count)