from typing import List, Set, Dict

def solution(id_list: List[str], report: List[str], k: int):
    Reporter = str
    Reportee = str

    # 누가 누구를 신고했는지, 신고누적횟수
    reported: Dict[Reportee: Set[Reporter]] = {}
    for r in report:
        r = r.split()
        if r[1] not in reported.keys():
            reported[r[1]] = set()
        reported[r[1]].add(r[0])
    
    answer = {id: 0 for id in id_list}
    
    for reporters in filter(lambda item: len(item) >= k, reported.values()):
        for reporter in reporters:
            answer[reporter] += 1

    return list(answer.values())



print(solution(
    ["muzi", "frodo", "apeach", "neo"], 
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 
    2))

print(solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3))

assert [2, 1, 1, 0] == solution(
    ["muzi", "frodo", "apeach", "neo"], 
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 
    2)

assert [0, 0] == solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3)