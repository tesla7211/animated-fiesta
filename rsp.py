'''
**과제 내용:**

1. 플레이어와 컴퓨터가 참여하는 가위바위보 게임을 만드세요.
2. 게임은 다음 순서로 진행됩니다.
    - 플레이어가 가위, 바위, 보 중 하나를 입력합니다.
    - 컴퓨터도 무작위로 가위, 바위, 보 중 하나를 선택합니다.
    - 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정합니다.
    - 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지를 알려줍니다.
    - 게임을 반복하거나 종료할 수 있는 기능을 추가하세요.

**추가 도전 과제:**

1. 게임의 승, 패, 무승부 횟수를 기록하고, 게임 종료 시에 플레이어에게 통계를 제공하세요.
2. 플레이어가 입력할 때 대소문자를 구분하지 않도록 프로그램을 개선하세요.
3. 플레이어가 게임을 반복하고 싶을 경우, 게임 재시작 여부를 묻고 그에 따라 게임을 초기화하거나 종료하는 기능을 추가하세요.



랜덤으로 1~3 출력
1가위 2바위 3보

사용자 가위 바위 보 입력

컴퓨터와 비교후 승패 출력
0전 0승 0패 0무

재시작 여부 문의
게임초기화 여부

필요 변수 체크

crsp = 컴퓨터 가위바위보 값
ursp = 사용자 가위바위보 값
rmenu = 메뉴 선택
rwin = 승리 횟수
rlose = 패배 횟수
rdraw = 무승부 횟수
rcount = 게임 횟수
rclear = 전적 초기화


'''

import random

class Gameplay:

    def welcome(self):
        print('')
        print('')
        print('')
        print('🎃 : ✨가위 바위 보 게임에 오신것을 환영합니다✨')
        print('')

    def menu(self):
        print('')
        print('')
        print('[1]👉[게임 시작]')
        print('[2]👉[전적 초기화]')
        print('[3]👉[완전 종료]')
        print('')

    def clear(self):
        print('')
        print("🎃 : 전적 초기화 완료")

    def err(self):
        print('')
        print('🎃 : ✨다시 입력하세요✨')

    def showme(self):
        print(f'현재 스코어 :   {rcount}전  {rwin}승  {rdraw}무  {rlose}패  ')

    def uwin(self):
        print('🎃 : 당신의 승리')

    def ulose(self):
        print('🎃 : 당신의 패배')

    def udraw(self):
        print('🎃 : 아쉬운 무승부')

    def txt(self):
        print('  🤞    ✊   ✋    📴')
        print('가위   바위   보  종료')
        print('  1     2    3    4')
        print('  R     S    P    E')
        print('')

mylist = {
    '가위':1, '바위':2, '보':3, '종료':4,
    'R':1, 'S':2, 'P':3, 'E':4
}

ursp = 0                                    #사용자 가위바위보 값
rrsp = 0                                    #사용자 가위바위보 값 변환
rmenu = 0                                   #메뉴 선택
rwin = 0                                    #승리 횟수
rlose = 0                                   #패배 횟수
rdraw = 0                                   #무승부 횟수
rcount = 0                                  #게임 횟수
rstart = 0

game = Gameplay()
game.welcome()

while True:
    game.showme()
    game.menu()
    rmenu = input('메뉴를 선택하세요 :  ')
    print('')
    if rmenu.isdigit() == 0 :
        game.err()
    else:
        rmenu = int(rmenu)

        if rmenu not in range(1,4) :
            game.err()
        elif rmenu == 3:
            print('프로그램 종료')
            break                               #메인 화일문 종료
        elif rmenu == 2:
            game.clear()
            rcount = 0
            rwin = 0
            rlose = 0
            rdraw = 0
        elif rmenu == 1:
            while rstart == 0:
                crsp = random.randint(1, 3)
                game.txt()

                while True:
                    ursp = input('🤞   ✊   ✋중 당신의 선택은 ⁉  :    ')

                    if ursp.isdigit() == 1:
                        rrsp = int(ursp)

                    if ursp in mylist:
                        rrsp = mylist[ursp]

                    if rrsp in range(1, 5):
                        print('')
                        if rrsp == 1:
                            print('당신의 선택은 :  🤞')
                            if crsp == 1:
                                print('상대의 선택은 :  🤞')
                                game.udraw()
                                rdraw += 1
                            if crsp == 2:
                                print('상대의 선택은 :  ✊')
                                game.ulose()
                                rlose += 1
                            if crsp == 3:
                                print('상대의 선택은 :  ✋')
                                game.uwin()
                                rwin += 1
                        if rrsp == 2:
                            print('당신의 선택은 :  ✊')
                            if crsp == 1:
                                print('상대의 선택은 :  ✊')
                                game.udraw()
                                rdraw += 1
                            if crsp == 2:
                                print('상대의 선택은 :  ✋')
                                game.ulose()
                                rlose += 1
                            if crsp == 3:
                                print('상대의 선택은 :  🤞')
                                game.uwin()
                                rwin += 1
                        if rrsp == 3:
                            print('당신의 선택은 :  ✋')
                            if crsp == 1:
                                print('상대의 선택은 :  ✋')
                                game.udraw()
                                rdraw += 1
                            if crsp == 2:
                                print('상대의 선택은 :  🤞')
                                game.ulose()
                                rlose += 1
                            if crsp == 3:
                                print('상대의 선택은 :  ✊')
                                game.uwin()
                                rwin += 1
                        if int(rrsp) == 4:
                            print('')
                            print('- 📴 게임을 종료합니다 -')
                            print('')
                            rstart = 1
                            break
                        print('')
                        rcount += 1
                        game.showme()
                        print('')
                        print('')

                    if rrsp not in range(1, 4):
                        game.err()
                        continue