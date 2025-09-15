print("Prime Number Checking")
print("----------------------")

n = int(input("Enter the number: "))
print("Result:")
count=0
for i in range(2, n):
        if n % i == 0:
            count += 1
            if count == 0:
                print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
