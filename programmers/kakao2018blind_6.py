import re

def score(number, power):
    n = int(number)
    if   power == 'D': n **= 2
    elif power == 'T': n **= 3
    return n

def solution(dartResult):
    # [숫자] + [문자] + ([특수문자])
    exp = re.compile(r"(\d+)([SDT])([*#]?)")
    
    results = exp.findall(dartResult)
    scores = []
    for result in results:
        s = score(result[0], result[1])
        if result[2] == '*':
            if len(scores) > 0:
                scores[-1] *= 2
            s *= 2
        elif result[2] == '#': 
            s *= -1
        scores.append(s)

    return sum(scores)


print(solution("1S2D*3T"), 37)
print(solution("1D2S#10S"), 9)
print(solution("1D2S0T"), 3)
assert solution("1S2D*3T") == 37
assert solution("1D2S#10S") == 9
assert solution("1D2S0T") == 3
assert solution("1S*2T*3S") == 23
assert solution("1D#2S*3S") == 5
assert solution("1T2D3D#") == -4
assert solution("1D2S3T*") == 59
