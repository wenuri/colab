# 리스트 연산자
# set은 리스트같은 자료형을 쓰다가 두값사이 값을 비교하는등 특정연산을 하고싶을때 바꿔쓰고 다시 원래자료형으로 변환하는 식으로 많이 사용


list_1 = [1,2,3]
list_2 = [4,5,6]
 
print("1. 리스트 더하기:", list_1 + list_2)  # 리스트 연결
print("2. 리스트 반복:", list_1 * 2)     # 리스트 반복

list_1.extend(list_2)
print('list_1 = ', list_1)
print('list_2 * 3= ', list_2 * 3)

list_1.append(list_2)
print('list_1 = ', list_1)
print('list_2 * 3= ', list_2 * 3)

print(list_1[6][1])

#문자열

str_1 = '안녕'
str_2 = '반가워'    
print(str_1 + str_2)
#set
set_1 = {1,2,3,4,1,2,3,5,6  }
print('set_1 = ', set_1)
#set에서 특정위치 단일값에 접근하려면
print(list(set_1)[2])

set_1 = {1,3,5,7}
set_2 = {5,7,9,11}
#교집합
print("set_1 & set_2 = ", set_1 & set_2)
print("set_1.intersection(set_2) = " , set_1.intersection(set_2))

#합집합
print("set_1 | set_2 = ", set_1 | set_2)
print("set_1.union(set_2) = ", set_1.union(set_2))

#차집합
print("set_1 - set_2 = ", set_1 - set_2)    
print("set_1.difference(set_2) = ", set_1.difference(set_2))
print("set_2 - set_1 = ", set_2 - set_1)