#Decorator
def smile():
    print("^^")

def cry():
    print("ㅜㅜ")

def angry():
    print("\/")

'''
이런식으로 이모티콘을 만든다고 가정
'''


smile()
angry()
cry()

'''
런칭하려는데 갑자기 저작권 표시가 필요하다고 지적
'''

'''
def smile():
    print("copy right 123456789abcdefghijk...")
    print("^^")

def cry():
    print("copy right 123456789abcdefghijk...")
    print("ㅜㅜ")

def angry():
    print("copy right 123456789abcdefghijk...")
    print("\/")
'''
'''
힘들게 copyright를 생성하다가 아이디어가 생김! 이모티콘을 그리기 전에 copyright를 찍어주는 함수를 생성하자! 
'''

def copyright(func):
    def new_func():
        print(1)
        print("copy right 123456789abcdefghijk...")
        func()
        print(2)

    return new_func

'''

새로운 형식의 함수를 정의
먼저 copyright 글귀가 실햄됨
함수가 실행이 됨
실행 종료

이런식으로 진행
'''

print(111111)
smile = copyright(smile)
angry = copyright(angry)
cry = copyright(cry)


"after 재정의"
smile()
angry()
cry()

'''
이렇게 굳이 변수를 다시 할당할 필요가 없다!
'''
print("Using Decorator")

@copyright
def smile():
    print("^^")

smile()

'''
결론: 함수를 다시 정의하고 꾸밀려고 데코레이터를 만든다.

def 데코레이터 이름(고치고 싶은 함수):
    def 새롭게 정의하는 함수()
    새로운 형식을 실행 (print를 한다든지...)
    고치고 싶은 함수를 실행()
    return 새롭게 정의하는 함수
    
이런식으로 만든뒤....
함수위에다가 @데코레이터 이름  이런식으로 붙이면 끝! 
'''