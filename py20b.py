print("Prime Number Generation")
print("------------------------")

sn = int(input("Enter the sn: "))
en = int(input("Enter the en: "))

print("Result:")
for n in range(sn, en):
    count = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                count += 1
        if count == 0:
            print(n)
