#1~100以内的偶数之和
# result = 0
# counter = 0
#
# while counter < 100:
#     counter += 1
#     if counter % 2 == 1:
#         continue
#     else :
#         result += counter
# print(result)

# result = 0
# counter = 0
# while counter <= 100:
#     counter += 1
#     if counter % 2 == 0 :
#         result += counter
#     else :
#         continue
# print(result)

result = 0
counter = 0
while counter < 100:
    counter += 1
    if counter % 2 == 1 :
        result += counter
    else :
        continue
print(result)