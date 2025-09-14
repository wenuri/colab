# Python 데이터 타입 가이드

## 목차
1. [튜플(Tuple)](#1-튜플tuple)
2. [집합(Set)](#2-집합set)
3. [실전 응용: 학생 관리 프로그램](#3-실전-응용-학생-관리-프로그램)

## 1. 튜플(Tuple)

### 1.1 튜플의 기본 특성
- **정의**: 튜플은 불변(immutable)한 순서가 있는 데이터 구조
- **생성 방법**: `()` 또는 `tuple()`을 사용
- **특징**:
  - 중복 허용
  - 순서 있음
  - 인덱싱 가능
  - 요소 변경 불가능

### 1.2 튜플 연산
```python
tutple_1 = (1, 2, '안녕', 3, 4, 5, 6, 7, 8, 9, 10)
tutple_2 = (3, '반가워', 4)

# 연결
print(tutple_1 + tutple_2)  # 튜플 연결

# 메서드
print(tutple_1.count(3))    # 특정 값의 개수 세기

# 슬라이싱
print(tutple_1[2:5])        # 일반 슬라이싱
print(tutple_1[-3::-1])     # 역방향 슬라이싱
```

### 1.3 튜플의 장점
1. 데이터 보호: 변경 불가능하여 안전
2. 성능: 리스트보다 메모리 효율적
3. 딕셔너리 키로 사용 가능

## 2. 집합(Set)

### 2.1 Set의 기본 특성
- **정의**: 중복을 허용하지 않는 순서 없는 컬렉션
- **생성 방법**: `{}` 또는 `set()`
- **주요 특징**:
  - 중복 불허
  - 순서 없음
  - 인덱싱 불가
  - 집합 연산 지원

### 2.2 Set 조작
```python
# 기본 생성
set1 = {1, 2, 3, 4, 5}

# 요소 추가/제거
set1.add(6)        # 요소 추가
set1.remove(6)     # 요소 제거 (없으면 에러)
set1.discard(6)    # 요소 제거 (없어도 에러 없음)

# 집합 연산
set1 = {1, 3, 5, 7}
set2 = {5, 7, 9, 11}

print(set1 & set2)  # 교집합
print(set1 | set2)  # 합집합
print(set1 - set2)  # 차집합
```

### 2.3 Set의 활용
1. 중복 제거
2. 집합 연산
3. 멤버십 테스트 (in 연산자)

### 2.4 변환과 응용
```python
# 다른 자료형으로부터 변환
list_to_set = set([1, 2, 2, 3, 3, 3])
tuple_to_set = set((4, 5, 5, 6, 6, 6))
string_to_set = set("hello")

# set을 리스트로 변환 (인덱싱 필요시)
set1 = {1, 2, 3}
list1 = list(set1)
```

## 3. 실전 응용: 학생 관리 프로그램

### 3.1 프로그램 구조
- 튜플을 활용한 데이터 관리
- 재귀적 접근을 통한 데이터 처리
- 순수 함수형 프로그래밍 스타일

### 3.2 주요 기능
1. 학생 데이터 입력
2. 성적 기반 정렬
3. 석차 계산
4. 결과 출력

### 3.3 코드 하이라이트
```python
def input_student_data():
    student = input_one_student()
    if student is None:
        return ()
    return (student,) + input_student_data()

def calculate_rank(students):
    if not students:
        return ()
    
    scores = tuple(student[1] for student in students)
    first_student = students[0]
    rest_students = students[1:]
    
    current_rank = get_rank(first_student[1], scores[1:])
    ranked_student = (first_student[0], first_student[1], current_rank)
    
    if not rest_students:
        return (ranked_student,)
    
    return (ranked_student,) + calculate_rank(rest_students)
```

### 3.4 프로그램의 특징
- 불변성(Immutability) 유지
- 순수 함수형 접근
- 재귀적 문제 해결
- 데이터 무결성 보장

## 결론
Python의 튜플과 집합은 각각 고유한 특성과 용도를 가지고 있으며, 적절한 상황에서 활용하면 효율적인 프로그래밍이 가능합니다. 특히 튜플의 불변성과 집합의 중복 제거 특성은 데이터 무결성과 처리에 있어 큰 장점을 제공합니다.
