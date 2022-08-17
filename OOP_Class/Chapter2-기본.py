'''
class는 oop의 원칙을 따르는 설계도다.
class자체는 쿠키틀이다.
쿠키틀을 활용하여 뽑는다.
instance란? OOP의 원칙을 따른 설계도로 나온 실제 세상의 물건이다.

4가지 원리
캡슐화

    class model1(nn.Module):

        def __init__(self, num_layers = None)....:

        def forward(self, x)....

            return out

이런식으로 잔뜩 만들고 나서... 모델 실제로 정의할 떄는?

model = model1(num_layers = ...)이런식으로 기능을 숨길 수 있다.

상속
자식 class는 부모 class를 물려 받을 수 있다. 여기에 overwriting을 통해 새로운 기능을 추가할 수 있다.
class model(nnn.Module):...
model이란 class는 nn.Module이란 부모 class를 물려 받았다는 뜻이다.

다형성
class에서 만든 객체는 부품화가 가능하다.
예) model = model1()한다음...이걸 함수에 넣든 또다른 class에 넣을 수 있다.

추상화
불필요한 정보는 숨기고 필요한 정보만을 표현한다.

class customdataset(Dataset):
    def __init__(self,):

    def __len__(self):

여기서 필요한 데이터셋 길이 알려고
data1 = customdataset()한다음
data1.__len__()로 필요한 길이를 알 수 있다.
'''
