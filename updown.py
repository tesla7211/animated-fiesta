import random   # ramdom 모듈 불러오기

class Gameplay:

    def welcome(self):
        print('')
        print('🎃 : ✨업다운 게임에 오신것을 환영합니다✨')
        print('')

    def menu(self):
        print('')
        print('[1]👉[게임 시작]')
        print('[2]👉[랭킹 확인]')
        print('[3]👉[완전 종료]')
        print('')

    def chk(self):
        print("🎃 : 랭킹 기록을 위해 개인정보 수집에 동의하십니까?")
        print("🎃 : [1]동의⭕  [2]미동의❌")

    def start(self):
        print('')
        print('')
        print('------------게임시작------------')
        print('...(*￣０￣)ノ💨 🎲 ')
        print('')
        print('')

rstb1 = range(1,4)
rstb2 = range(1,3)
rank1 = {"김무명":40, "이무명":30, "박무명":20, "최무명":10}

game = Gameplay()
game.welcome()

while True:                                     # 메뉴 반복 시작

    game.menu()                                     # 메뉴 출력
    stb1 = int(input("메뉴 번호를 입력하세요 :      "))       # 메뉴 입력창

    if stb1 not in rstb1:                           # 메뉴 선택 무결성 검사
        print('📢 옳바른 번호를 입력해주세요!!')
        continue
    elif stb1 == 2:                           # 랭킹 확인
        for name, count in rank1.items():
            print(f'👉{name} : {count}회')
    elif stb1 == 3:                           # 완전 종료
        print('완전 종료 완료!')
        break
    else:
        while True:                                     # 게임 반복
            rnum = random.randint(1, 100)             # 정답 생성
            num = 0                                       # 입력값 초기화
            try1 = 0                                        # 카운트 초기화
            answer = 0

            game.start()
            while answer == 0:                                  # 정답 반복 시작
                num = int(input("🎃 정답은? :   "))                  # 정답 입력
                try1 += 1                                           # 카운트 증가
                print('')
                print('')
                if num < rnum:                                      # UP
                    print('🎃 : 🔼UP🔼')
                    continue
                if num > rnum:                                      # DOWN
                    print('🎃 : 🔽DOWN🔽')
                    continue
                if num == rnum:                                         # 정답
                    if try1 == 1:                                           # 1회
                        print("🎃 : 축하합니다! 🎊 첫 시도로 맞추셨네요?")
                    if try1 >= 2:                                           # 1회 초과
                        print(f'🎃 : 축하합니다, 🎉{try1}번 시도해 맞추셨네요?')
                    while True:  # 랭크 기록
                        game.chk()
                        check1 = int(input('💻 입력하기  :  '))
                        if check1 not in rstb2:
                            print('숫자 1 혹은 2를 입력해주세요')
                            continue
                        if check1 in rstb2:
                            if check1 == 1:
                                print("🎃 : 이름을 알려주세요")
                                rname = 'rname 체크포인트'
                                rname = str(input('이름 :   '))
                                if rname != 'rname 체크포인트':
                                    rank1[rname] = try1
                                elif rname == 'rname 체크포인트':
                                    print('rname 오류 발생')
                                print('🎃 : 성공적으로 저장되었습니다 💾!')
                            if check1 == 2:
                                print('🎃 : 개인정보 제공 미동의, 초기화면으로 돌아갑니다.')
                                print('')
                        break
                    answer += 1
            break