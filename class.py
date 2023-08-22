class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def add(self, name, username, password):
        self.append({name, username, password})

    def display(self):
        print(f'이름 : {self.name}     ID : {self.username}     PW : {self.password}')

class Post:
    def __init__(self, title, content):
        self.title = title
        self.author = Member.__name__
        self.content = content
        
    def display(self):
        print(f'제목 : {self.title} / 작성자 : {self.author} / 내용 : {self.content}')

members = []

Member('홍길동', '아이디', '비밀번호')

mem = Member

print(mem)
print(members)