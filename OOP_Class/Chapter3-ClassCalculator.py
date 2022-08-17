#하나의 계산기를 만들 예정 속성도 나눔
#계산기에는 사칙연산이 요구

def add_two(a, b):
    return a + b

def sub_two(a, b):
    return a - b

def mul_two(a, b):
    return a * b

def dic_two(a, b):
    return a / b


'''
이 함수들을 하나로 묶을 수 없을까?
상태, 속성으로 나눌 수 있다고 느끼는 순간! class가 사용 가능해진다. 
'''

class calculator():
    #init은 생성자라고 부른다. class가 메모리에 올라올 때 (class가 인스턴스를 만들 때) 즉시 실행
    #class란 빵틀로 instance란 빵을 만들었을 때 제일 먼저 실행(빵에서 연기가 나기?)
    def __init__(self, a, b): #빵에 재료를 넣는 느낌?
        self.a = a
        self.b = b
    #계산기의 4가지 행위를 하나의 class에 정의
    def add_two(self):
        #instance를 지칭하는 인자인 self가 필요하다.
        return self.a + self.b #인스턴스 안의 네임스페이스에서 접근이 가능해진다.
        #instance안의 namespace(공간에서) self.a가 a를 가리키며, self.b는 b를 가리킨다.

    def sub_two(self):
        return self.a - self.b

    def mul_two(self):
        return self.a * self.b

    def div_two(self):
        return self.a / self.b

cal1 = calculator(3, 4)
'''
메모리에 cal1이란 객체가 올라왔다. self는 cal1을 가리키며 3은 a가 4는 b가 가리키게 된다. 
cal1.a = 3, cal1.b는 4를 가리키게 된다. 
왜?? 생성자라는 함수는 메모리에 올라오는 순간 즉시 실행이 되며, 생성자의 인자로 넘어가게 된다. 
cal1은 namespace라는 공간이 생겼다. 여기에는 a, b, add_two, sub_two, div_two, mul_two가 존재한다.
.을 찍으면 안의 공간에 접근이 가능하다. 
더하기라는 공간에 가려면?
cal1.add_two()
a라는 공간에 가려면? cal1.a
b라는 공간은? cal1.b
'''
print(cal1.a)
print(cal1.b)
print(cal1.add_two())
'''

def add_two(self)에서 self는 cal1을 가리키게 된다. 이것을 instance method라고 한다.
instance method들은 앞에 인자가 필요하며, 인자들은 .찍힌 instance를 가리킨다. (__init__에서 정의한 변수)

설계도 하나로 만든 instance들은 독립적이다. 
'''
cal1 = calculator(3, 4)
cal2 = calculator(1, 1)
#cal1과 cal2는 서로 다른 객체이다.
print(cal2.a)
print(cal2.b)

'''
요소를 바꿀 수 있다. 
'''
cal1.a = 100
print(cal1.add_two())
#namespace (self.a)가 바뀌는 순간 바뀐다. 인스턴스 변수가 공유가 된다.


