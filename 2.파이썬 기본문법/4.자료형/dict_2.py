# 사용자 관리 프로그램
# 사용자 - 이름, 나이, 성별, 반려동물(고양이, 개, 기타)

user1 ={   
    "name": "홍길동",
    "age": 30,          
    "gender": "남자",
    "pet": {"고양이" :"코숏",
            "개":"푸들",
            "기타":"토끼"
    }    
}   
user2 = {   
    "name": "이순신",
    "age": 44,          
    "gender": "남자",
    "pet": {"고양이" :"노르웨이숲",
            "개":"진돗개",
            "기타":"물고기"
    }    
}

users = [user1, user2]
print(users)

#users의 user1의 pet중 개 정보를 변경하기 
users[0]['pet']['개'] = '시바견'
print(user1)

