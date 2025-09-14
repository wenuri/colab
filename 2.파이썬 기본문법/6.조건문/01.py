# 조건문 예시   
score = 85
if score >= 90:  #true 면 :아래실행하고 끝남
    grade = 'A'
elif score >= 80:
    grade = 'B' 
else:
    grade = 'C'
print(f"점수: {score}, 학점: {grade}") #f"{}"로 {}안에 변수 넣기 가능
print("점수:", score, "학점:", grade)


if True:
    print("항상 실행되는 문장")

print("if와 상관없는 문장")
# 들여쓰기 중요, 공백 4칸 권장

list_1 = [1,2,3,4,5]
if 4 in list_1:
    print("4가 list_1에 있음")


dict_1 = {'name' : '이지아', 'age' : 30}
if 'age' in dict_1: # valeue가 아닌 key값이 기준이어야함
    print("age가 dict_1에 있음")

#중첩 조건문 - 들여쓰기 라인이 맞아야함 주의할것!
# if 조건문1:
#     if 조건문2:
#         실행문1
#     else:
#         실행문2
# else:#
#예시
num = 15
if num % 2 == 0: #짝수
    if num % 3 == 0:
        print("2와 3의 공배수")
    else:
        print("2의 배수")   

if num % 2 == 0 and num % 3 == 0:
    print("2와 3의 공배수") 

