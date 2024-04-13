def solution(n, arr1, arr2):
    answer = [""] * n
    for i in range(n):
        result = arr1[i] | arr2[i]
        for _ in range(n):
            c = '#' if result & 1 else ' '
            answer[i] = c + answer[i]
            result >>= 1
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
assert solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) == ["#####","# # #", "### #", "#  ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
assert solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]) == ["######", "###  #", "##  ##", " #### ", " #####", "### # "]