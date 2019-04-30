def solution(participant, completion):
    participant.sort()
    completion.sort()
    for index in range(len(completion)) :
        if participant[index]  != completion[index] :
            return participant[index]
    return participant[len(completion)]


participant = ["leo","kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))
