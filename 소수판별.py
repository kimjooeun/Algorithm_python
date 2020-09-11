user_input = input()

answer = False
for i in range(2, 10):
    if int(user_input) == 2:
        answer = True
        break
    if len(user_input) == 1 and int(user_input) % 2 == 1:
        answer = True
    if int(user_input) % i == 0:
        answer = False

print(answer)
