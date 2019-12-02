f = open("input.txt", "r")
nums = f.read().split("\n")
f.close()

total = 0

for num in nums:
    if num != "":
        integer = int(num)
        total += integer // 3 - 2

print total

