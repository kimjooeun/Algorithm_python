# 백준 1110번

# 입력
num = input()

cnt = 0
num = str(num)
if len(num) == 1:
    num = '0'+ num

result = ''
origin_num = num
while origin_num != result:
    cnt += 1
    num_sum = int(num[0]) + int(num[1])
    if len(str(num_sum))==1:
        result = num[1] + str(num_sum)
    else:
        result = num[1] + str(num_sum)[1]
    num = result
    
# 출력
print(cnt)
