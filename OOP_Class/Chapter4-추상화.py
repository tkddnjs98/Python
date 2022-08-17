#추상화
'''
공통의 속성과 행위를 하나로 묶는 것
'''

'''
siri 
name:siri
code = 20220816
hi
error
2+3
'''
siri_name = "siri"

siri_code = 20220816

def siri_say_hi():
    print("Hi! My Name is siri")

def siri_add_cal():
    return 2+3

def siri_die():
    print("Error")

'''
jarvis
name:jarvis
code = 20220817
hi
error
10+7, 2+4
destroy
'''

jarvis_name = "jarvis"

jarvis_code = 20220817

def jarvis_say_hi():
    print("Hi! My Name is jarvis")

def jarvis_add_cal():
    return 2+3

def jarvis_die():
    print("Destroy")

'''
이렇게 반복되는 공통점들을 하나로 묶는 것이 추상화이다!
'''

class Robot():
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def hi(self):
        print(f"Hi! My Name is {self.name}!")
        return 00

    def cal_add(self, a, b):
        print(f"{a}+{b}는 {a+b}입니다!")
        return 00

    def die(self):
        print(f"{self.name} is destroyed!")
        return 00


siri  = Robot('siri', 20220816)
jarvis = Robot('jarvis', 20220817)
bixby = Robot('bixby', 20220818)

siri.name
siri.hi()
siri.cal_add(2, 3)
siri.die()
jarvis.name

'''
Robot은 class 명 
def __init__ 인스턴스가 생성될 떄 초기화가 되는 함수(인스턴스 생성되면 제일 먼저 생성)
__init__에 self.는 각각의 instance를 뜻한다.
key-value형식으로 저장
self.name 이 key "siri"는 value
이런 self.변수를 instance 변수라고 한다.

jarvis = jarvis.hi()와 siri.hi()는 다르다. 독립적이다. 
hi(), cal_add()를 인스턴스 메서드라고 부른다. 
'''

#Robot을 만들어서 instance를 끊어봤다.
#찍어낼 떄마다 인스턴스의 개수를 알고 싶으면??
#Robot이라는 큰 공간이 존재하며 Robot이란 class로 각각의 instance를 찍었음
#각각의 instace들은 독립적인 공간이 있다. hi()등등
#class 공간 / class라는 공간에서 instance각각이 공유하는 변수와 메소드를 정의할 수 있다.
#이것이 classmethod라고 한다.

class Robot1():

    #인스턴스들이 공유하는 변수 Robot의 인구를 설정 / 인스턴스를 생성할 때마다 robot이 몇개 있는지 알고 싶음
    #class 공간에서 인스턴스들이 공유하는 변수와 메소드가 있다. 이걸 classmethod라고 한다.
    population = 0

    def __init__(self, name, code): #생성자 함수--> 인스턴스가 생성될 때 초기화(실행)가 되는 함수, self는 각각의 instance를 뜻한다.
        #각각의 인스턴스안에 공간이 있는데 self.name이란 key와 name이란 변수가 value가 저장되어있다.
        self.name = name #인스턴스 변수
        self.code = code
        #instance가 생성될 때마다 Robot의 인구에 1을 더한다.
        Robot1.population += 1 #Robot1이란 공간에 1을 더한다.

    #siri.hi() siri안에 있는 hi()함수에 접근
    def hi(self):
        print(f"Hi! My Name is {self.name}!")
        return 00

    def cal_add(self, a, b):
        print(f"{a}+{b}는 {a+b}입니다!")
        return 00

    def die(self):
        print(f"{self.name} is destroyed!")
        Robot1.population -= 1 #die 실행 될때마다
        if Robot1.population < 1:
            print(f"Oh No! The last one {self.name} is destroyed!")
        else:
            print(f"There are still {Robot1.population} robots working")
        return 00

    @classmethod  #인스턴스끼리 공유하는 클래스메소드 데코레이터
    def how_many(cls):
        print(f"We have {cls.population} robots") #cls.population을 넣음으로써 클래스 변수를 넣은 것을 볼 수 있다.
        return 00




Robot1.population
siri11 = Robot1("aa", 222)
Robot1.population

siri22 = Robot1("bb", 222)
Robot1.population

#Robot이란 class namespace안에 존재하는 변수들이 있고 변수들은 instance들이 공유한다.
#인스턴스 각각안에 class로 데이터를 찍어낸다.

#instance 변수와 instance mothod vs class 변수와 class method
#16분
siri22.how_many()

siri11.die()
siri22.die()
