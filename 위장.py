# 풀이 1
from collections import Counter
def solution(clothes):
    answer = 0
    counter_each_category = Counter([cat for _, cat in clothes])
    
    print(counter_each_category)
    all_possible = 1
    for key in counter_each_category:
        all_possible *= (counter_each_category[key] + 1)
        
    return all_possible -1
    
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

# 풀이 2
from functools import reduce
from collections import Counter
def solution(clothes):
    cnt = Counter([data for _, data in clothes])
    print(cnt.values())
    return reduce(lambda a,b: (a+1)*(b+1)-1, cnt.values())
