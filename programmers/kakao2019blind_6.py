def solution(N, stages):
    clear = [0] * N
    reach = [0] * (N+1)

    for stage in stages:
        reach[stage-1] += 1
        for i in range(stage-1):
            clear[i] += 1
    failure_rate = [reach[i] for i in range(N)]
    for i in range(N):
        if reach[i]+clear[i] != 0:
            failure_rate[i] /= (reach[i]+clear[i])
    failure_rate = sorted(enumerate(failure_rate), key=lambda s: s[1], reverse=True)

    return list(map(lambda x: x[0]+1, failure_rate))

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
assert solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3,4,2,1,5]
print(solution(4, [4,4,4,4,4]))
assert solution(4, [4,4,4,4,4]) == [4,1,2,3]
print(solution(5, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
assert solution(5, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]