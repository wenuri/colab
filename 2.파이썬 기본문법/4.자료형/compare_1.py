# 비교 연산자 (true, false)
a = 10
b = 20      
print("a == b :", a == b)   # 같음
print("a != b :", a != b)   # 다름  
print("a > b :", a > b)     # 큼
print("a < b :", a < b)     # 작음
print("a >= b :", a >= b)   # 크거나 같음
print("a <= b :", a <= b)   # 작거나 같음
print()

# is, is not
list1 = [1,2,3] 
list2 = [1,2,3]

list2 = list1
print("list1 is list2 :", list1 is list2)     # list1과 list2는 동일 객체
print("list1 ==  list2 :", list1 == list2)     # list1과 list3는 동일 객체 아님

# in , not in    설
print(10 in list1)


# 논리 연산자(and, or, not)
x = True
y = False
print("x and y :", x and y)  # x, y 모두 참일 때 참
print("x or y :", x or y)    # x, y 중 하나만 참이어도 참
print("not x :", not x)      # x가 거짓일 때 참
print("not y :", not y)      # y가 거짓일 때 참
print()


a = 89
print(a > 5 and a < 10)  # False    
print(a < 5 or a >= 65)   # True

kor = 0 ; eng = 0 ; math = 0 ; avg = 0
avg > 60 and kor >= 40 and eng >= 40 and math >= 40 # 평균과 하나라도 과락이 있는경우

# 처음이 false면 뒤에꺼는 안봄, 처음이 true고 or면 뒤에꺼는 안봄, 그러므로 처음에 결과가 빨리나오는걸 배치하는게 좋음   