from typing import List

class Date:
    def __init__(self, s: str):
        d = s.split(".")
        self.year = int(d[0])
        self.month = int(d[1])
        self.day = int(d[2])

    # left <= right?
    def __le__(self, other):
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day <= other.day:
                    return True
        return False
    
    def __add__(self, term):
        self.month += term.duration_month
        while self.month > 12:
            self.year += 1
            self.month -= 12
        return self
    
class Term:
    def __init__(self, name: str, duration_month: int):
        self.name = name
        self.duration_month = duration_month

class Privacy:
    def __init__(self, start_date: Date, term: Term):
        self.start_date = start_date
        self.term = term

    def is_expired(self, today: Date):
        return self.start_date + self.term <= today

def solution(today: str, terms: List[str], privacies: List[str]):
    today = Date(today)

    terms_dict = {}
    for t in terms:
        t = t.split()
        terms_dict[t[0]] = Term(t[0], int(t[1]))

    result = []

    for i, privacy in enumerate(privacies):
        p = privacy.split()
        privacy = Privacy(Date(p[0]), terms_dict[p[1]])
        if privacy.is_expired(today):
            result.append(i+1)

    return result


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