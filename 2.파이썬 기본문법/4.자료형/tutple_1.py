#tuple 기본 사용법 -list는 범용적, 순서, 변경, 중복가능, set 은 중복불가, 집합연산, tuple은 변경불가
# - 중복을 허용한다.
# - 순서가 있다.
# - 인덱싱으로 접근할 수 있다.
# - 서로 다른 자료형끼리 전환가능(리스트, 튜플, 문자열을 tuple로 변환할 수 있다)
# - tuple은 변경 불가능(immutable)하다. (요소 추가, 제거, 변경 불가)
# - tuple은 ()로 표현한다.          
# - tuple은 tuple()으로 생성한다.   

tutple_1 = (1,2,'안녕',3,4,5,6,7,8,9,10)
tutple_2 = (3,'반가워',4)
print("tutple_1 + tutple_2 = ", tutple_1 + tutple_2)
print("tutple_count(31) = ", tutple_1.count(3))
#슬라이싱
print("tutple_1[2:5] = ", tutple_1[2:10])
print("len(tutple_1) = ", len(tutple_1))
print("tuple의 마지막값까지 = " , tutple_1[3:len(tutple_1)])
print("tuple의 역방향 = " , tutple_1[-3: :-1])
print("tuple의 역방향 = " , tutple_1[-3: :-2])
print("tuple의 역방향 = " , tutple_1[: :-1])  #오름차순, 내림차순 정렬때 사용

