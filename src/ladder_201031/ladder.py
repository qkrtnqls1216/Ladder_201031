import random;

def ladder(): 
    person = []
    select = int(input ("조원의 수 입력해 주세요:"))

    for i in range(select):
        name = input(f"조원 {i + 1}의 이름을 입력하세요:")
        person.append(name)
    choice = random.choice(person)
    print("발표자:", choice)
    # print(person)
