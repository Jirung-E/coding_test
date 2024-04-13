def solution(new_id: str):
    step1 = lambda s: s.lower()
    
    valid = ['-', '_', '.']
    step2 = lambda s: ''.join(filter(lambda x: x in valid or x.isalpha(), s))

    step3 = lambda s: None


    answer = step2(step1(new_id))
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"), "bat.y.abcdefghi")
print(solution("z-+.^."), "z--")
print(solution("=.="), "aaa")
print(solution("123_.def"), "123_.def")
print(solution("abcdefghijklmn.p"), "abcdefghijklmn")