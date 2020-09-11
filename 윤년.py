# 백준 2753번

num = int(input())

result = 0
if num % 4 ==0 and num % 100 != 0 or num % 400 == 0:
    result = 1
    
print(result)
