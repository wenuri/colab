# Python 프로그래밍 문법 가이드

## 목차
1. [데이터 타입과 기본 문법](#1-데이터-타입과-기본-문법)
2. [조건문](#2-조건문)
3. [비교 연산자와 논리 연산자](#3-비교-연산자와-논리-연산자)
4. [데이터 구조](#4-데이터-구조)
5. [실전 프로그래밍 예제](#5-실전-프로그래밍-예제)

## 1. 데이터 타입과 기본 문법

### 1.1 기본 데이터 타입
- 숫자형 (int, float)
- 문자열 (str)
- 불리언 (bool)
- None

### 1.2 문자열 포매팅
```python
name = "김철수"
age = 25
# f-string 사용
print(f"이름: {name}, 나이: {age}")
# 일반 포매팅
print("이름: %s, 나이: %d" % (name, age))
```

## 2. 조건문

### 2.1 기본 if 문
```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
print(f"점수: {score}, 학점: {grade}")
```

### 2.2 중첩 조건문
```python
num = 15
if num % 2 == 0:  # 짝수
    if num % 3 == 0:
        print("2와 3의 공배수")
    else:
        print("2의 배수")

# 동일한 조건을 논리 연산자로 표현
if num % 2 == 0 and num % 3 == 0:
    print("2와 3의 공배수")
```

## 3. 비교 연산자와 논리 연산자

### 3.1 비교 연산자
```python
a = 10
b = 20
print("a == b :", a == b)   # 같음
print("a != b :", a != b)   # 다름
print("a > b :", a > b)     # 큼
print("a < b :", a < b)     # 작음
print("a >= b :", a >= b)   # 크거나 같음
print("a <= b :", a <= b)   # 작거나 같음
```

### 3.2 논리 연산자
```python
x = True
y = False
print("x and y :", x and y)  # 둘 다 참이어야 참
print("x or y :", x or y)    # 하나만 참이어도 참
print("not x :", not x)      # 참/거짓 반전
```

### 3.3 멤버십 연산자
```python
list_1 = [1, 2, 3, 4, 5]
print(4 in list_1)          # True
print(6 not in list_1)      # True
```

## 4. 데이터 구조

### 4.1 튜플(Tuple)
```python
# 튜플 기본 특성
# - 중복 허용
# - 순서 있음
# - 인덱싱 가능
# - 변경 불가능(immutable)

tuple_1 = (1, 2, '안녕', 3, 4, 5)
print("슬라이싱:", tuple_1[2:5])
print("역순:", tuple_1[::-1])
```

### 4.2 집합(Set)
```python
# Set 특성
# - 중복 불허
# - 순서 없음
# - 집합 연산 지원

set1 = {1, 3, 5, 7}
set2 = {5, 7, 9, 11}

# 집합 연산
print("교집합:", set1 & set2)
print("합집합:", set1 | set2)
print("차집합:", set1 - set2)
```

### 4.3 딕셔너리(Dictionary)
```python
# Dictionary 특성
# - 키-값 쌍으로 데이터 저장
# - 키는 중복 불가, 값은 중복 가능
# - 키는 변경 불가능한 타입만 가능

# 기본 사용법
user = {
    "name": "홍길동",
    "age": 30,
    "skills": ["Python", "JavaScript"]
}

# 데이터 접근
print(user["name"])
print(user.get("hobby", "없음"))  # 기본값 지정 가능

# 데이터 추가/수정
user["hobby"] = "독서"
```

### 4.4 복잡한 데이터 구조 예제
```python
# 중첩된 dictionary 구조
employee = {
    "personal_info": {
        "name": "김개발",
        "age": 35,
        "position": "수석 개발자",
        "contact": {
            "email": "kim.dev@company.com",
            "phone": "010-1234-5678"
        }
    },
    "projects": [
        {
            "name": "클라우드 시스템 구축",
            "role": "프로젝트 리더",
            "period": "2025-03 ~ 2025-08"
        }
    ]
}
```

## 5. 실전 프로그래밍 예제

### 5.1 학생 성적 관리 프로그램
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
    current_rank = get_rank(first_student[1], scores[1:])
    ranked_student = (first_student[0], first_student[1], current_rank)
    
    return (ranked_student,) + calculate_rank(students[1:])
```

### 5.2 회사 직원 정보 관리
```python
# 부서별 평균 급여 계산
for dept_id, dept_info in company['departments'].items():
    total_salary = 0
    employee_count = len(dept_info['employees'])
    for emp_id, emp_info in dept_info['employees'].items():
        total_salary += emp_info['salary_info']['base_salary']
    avg_salary = total_salary / employee_count
    print(f"{dept_info['name']} 평균 기본급: {avg_salary:,.0f}원")
```

## 프로그래밍 스타일 가이드

### 1. 코드 구조화
- 함수를 사용하여 코드 모듈화
- 관련 기능끼리 그룹화
- 적절한 들여쓰기 사용 (4칸 공백 권장)

### 2. 변수 명명 규칙
- 소문자와 언더스코어 사용
- 의미있는 이름 사용
- 일관된 명명 규칙 유지

### 3. 주석 작성
- 코드의 목적과 동작 설명
- 복잡한 로직에 대한 설명 추가
- 주석은 간단명료하게

## 결론
이 가이드는 Python의 기본적인 문법과 데이터 구조, 그리고 실전 프로그래밍 예제를 다루고 있습니다. 각 섹션의 예제 코드를 직접 실행해보면서 학습하면 더 효과적인 이해가 가능합니다.
