# SET 기본 사용법
# - 중복을 허용하지 않는다.
# - 순서가 없다.
# - 인덱싱으로 접근할 수 없다.
# - 집합 연산을 지원한다. (합집합, 교집합, 차집합)
# - 서로 다른 자료형끼리 전환가능(리스트, 튜플, 문자열을 set으로 변환할 수 있다)
# - set은 변경 가능(mutable)하다.
# - set은 변경 불가능(immutable)한 frozenset이 있다.
# - set은 {}로 표현한다.
# - set은 set()으로 생성한다.
# - set은 요소를 추가할 때 add() 메서드를 사용한다.
# - set은 요소를 제거할 때 remove() 메서드를 사용한다.
# - set은 요소를 제거할 때 discard() 메서드를 사용한다.
# - set은 요소를 모두 제거할 때 clear() 메서드를 사용한다.
# - set은 요소의 개수를 셀 때 len() 함수를 사용한다.

# 1. 기본적인 set 생성
fruits = {'apple', 'banana', 'orange', 'apple'}  # 중복된 'apple'은 자동으로 제거됨
print("1. 기본 set:", fruits)  # 중복이 제거된 set 출력

# 2. 다른 자료형으로부터 set 생성
list_to_set = set([1, 2, 2, 3, 3, 3])  # 리스트로부터 set 생성
tuple_to_set = set((4, 5, 5, 6, 6, 6))  # 튜플로부터 set 생성
string_to_set = set("hello")  # 문자열로부터 set 생성
print("2. 리스트로부터:", list_to_set)
print("   튜플로부터:", tuple_to_set)
print("   문자열로부터:", string_to_set)  # 중복된 'l'이 제거되고 순서가 무작위

# 3. set 조작하기
numbers = {1, 2, 3}
print("\n3. 초기 set:", numbers)

# add() 메서드로 요소 추가
numbers.add(4)
print("   요소 추가 후:", numbers)

# remove()와 discard()의 차이
numbers.remove(4)  # 존재하지 않는 요소를 remove하면 KeyError 발생
print("   remove 후:", numbers)

numbers.discard(5)  # 존재하지 않는 요소를 discard해도 에러가 발생하지 않음
print("   discard 후:", numbers)

# 4. 집합 연산
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("\n4. set1:", set1)
print("   set2:", set2)

# 합집합
union_set = set1 | set2  # set1.union(set2)와 동일
print("   합집합:", union_set)

# 교집합
intersection_set = set1 & set2  # set1.intersection(set2)와 동일
print("   교집합:", intersection_set)

# 차집합
difference_set = set1 - set2  # set1.difference(set2)와 동일
print("   차집합:", difference_set)

# 5. frozenset 사용
frozen = frozenset([1, 2, 3])
print("\n5. Frozenset:", frozen)
# frozen.add(4)  # 이 줄을 실행하면 AttributeError 발생 (변경 불가)

# 6. set의 크기
numbers = {1, 2, 3, 4, 5}
print("\n6. Set의 크기:", len(numbers))

# 7. set 비우기
numbers.clear()
print("   Set 비운 후:", numbers)    
