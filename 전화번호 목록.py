# 풀이 1
def solution(phone_book):
    phone_book = list(map(str, phone_book))

    first = phone_book[0]

    answer =[]
    for i in phone_book:
        if first == i:
            continue
        elif first == i[0:len(first)] or i == first[0:len(i)]:
            answer.append("False")
        else:
            answer.append("True")
    if "False" in answer:
        return False
    else:
        return True

# 풀이 2
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in (phone_book[i+1]):
                return False
    return answer
