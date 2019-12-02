f = open("input.txt", "r")
nums = f.read().split("\n")
f.close()

total = 0

for num in nums:
    if num != "":
        integer = int(num)
        while integer > 6:
            integer = integer // 3 - 2
            total += integer
print total

