# Kyle Dela Pena
# 2038252

numbers = input().split()
answer = []

for num in numbers:
    num = int(num)
    if num >= 0:
        answer.append(num)

answer.sort()
for num in answer:
    print(num, end=" ")