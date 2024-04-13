class IdGenerator:
    def __init__(self, id: str):
        self.id = id
        self.valid = ['-', '_', '.']
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    def to_lower(self):
        self.id = self.id.lower()
        return self
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    def remove_invalid(self):
        self.id = ''.join(filter(lambda x: x in self.valid or x.isalpha() or x.isnumeric(), self.id))
        return self
    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    def reduce_dots(self):
        while ".." in self.id:
            self.id = self.id.replace("..", ".")
        return self
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    def remove_first_dot(self):
        if self.id and self.id[0] == '.':
            self.id = self.id[1:]
        return self
    def remove_last_dot(self):
        if self.id and self.id[-1] == '.':
            self.id = self.id[:-1]
        return self
    def remove_first_and_last_dots(self):
        self.remove_first_dot().remove_last_dot()
        return self
    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    def set_a_if_empty(self):
        if len(self.id) == 0:
            self.id = 'a'
        return self
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    def shorten_if_long(self):
        self.id = self.id[:15]
        self.remove_last_dot()
        return self
    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    def extend_if_short(self):
        while len(self.id) <= 2:
            self.id += self.id[-1]
        return self

def solution(new_id: str):
    answer = IdGenerator(new_id)
    answer.to_lower()
    answer.remove_invalid()
    answer.reduce_dots()
    answer.remove_first_and_last_dots()
    answer.set_a_if_empty()
    answer.shorten_if_long()
    answer.extend_if_short()
    return answer.id

assert solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi"
assert solution("z-+.^.") == "z--"
assert solution("=.=") == "aaa"
assert solution("123_.def") == "123_.def"
assert solution("abcdefghijklmn.p") == "abcdefghijklmn"