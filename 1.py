N = int(input("enter a integer"))
sumodd = 0
sumeven = 0
for i in range(1, N + 1):
    if (i % 2 == 1):
        sumodd = sumodd + i

    else:
        sumeven += i

print("Sum of the odd numbers:", sumodd)
print("Average of even numbers",sumeven / N)