s= int(input("Enter start: "))
e = int(input("Enter end: "))
a =0;
p = 0;
for num in range(s, e + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if sum == num:
        a += 1
    if num > 1:
        for y in range(2, num):
            if (num % y) == 0:
                break
        else:
            p = p + 1
print(f"TOTAL ARMSTRONG NO'S ARE:{a} ")
print(f"TOTAL PRIME NO'S ARE:{p} ")
