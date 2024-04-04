from typing import List


def dayStrToDays(day: str) -> int:
    d = list(map(int, day.split('.')))
    return d[0] * 28*12 + d[1] * 28 + d[2]


def solution(today: str, terms: List[str], privacies: List[str]):
    today = dayStrToDays(today)
    
    terms_dict = {}
    for term in terms:
        t = term.split()
        terms_dict[t[0]] = int(t[1])

    answer = []

    for i, privacy in enumerate(privacies):
        p = privacy.split()
        if dayStrToDays(p[0]) + terms_dict[p[1]]*28 <= today:
            answer.append(i+1)

    return answer

assert [1, 3] == solution(
    "2022.05.19",
    ["A 6", "B 12", "C 3"],
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
)

assert [1, 4, 5] == solution(
    "2020.01.01",
    ["Z 3", "D 5"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
)