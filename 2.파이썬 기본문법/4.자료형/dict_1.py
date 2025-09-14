#dictionary 사용법
#key, value 쌍으로 이루어진 자료형
#key는 중복 불가, value는 중복 가능(중복 시 마지막 값으로 저장  ) 
#key는 숫자, 문자열, 튜플만 사용 가능
#value는 모든 자료형 사용 가능
#딕셔너리 생성
#방법1: {}
#방법2: dict()  
#딕셔너리 조작
#추가: dict[key] = value
#수정: dict[key] = value
#삭제: del dict[key]
#조회: dict[key]
abc = {"name":"지은", "age" : 30} 
print(abc.get('취미','없음')) #get은 없는 key값 조회시 None이나 기본값 반환
abc['취미'] = '독서'
print(abc)

dict_1 = {} # 빈 {}는 딕셔너리, 자료가 들어가있으면 set
print(dict_1)

dict_1['name'] = '홍길동'
print(dict_1)
dict_1['age'] = 25
print(dict_1)
dict_1['age'] = 30 #수정

# dictionary를 쓰는 이유, list와 다른점
