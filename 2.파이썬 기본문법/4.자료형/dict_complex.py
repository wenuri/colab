# 회사 직원 정보 관리 시스템
# - 부서별 직원 정보
# - 각 직원의 상세 정보 (인적사항, 업무이력, 평가이력, 프로젝트 참여 등)
# - 급여 정보
# - 휴가 정보

# 회사 전체 정보를 담는 dictionary
company = {
    # 회사 기본 정보
    'company_info': {
        'name': '파이썬 기술 연구소',
        'founded_year': 2025,
        'address': '서울시 강남구 테헤란로 123',
        'tel': '02-123-4567',
    },
    
    # 부서 정보
    'departments': {
        'dev': {
            'name': '개발부',
            'location': '3층',
            'manager': 'DEV001',
            'employees': {
                'DEV001': {
                    'personal_info': {
                        'name': '김개발',
                        'age': 35,
                        'position': '수석 개발자',
                        'join_date': '2025-01-15',
                        'contact': {
                            'email': 'kim.dev@company.com',
                            'phone': '010-1234-5678',
                            'emergency_contact': '010-8765-4321'
                        }
                    },
                    'salary_info': {
                        'base_salary': 7000000,
                        'bonus_rate': 1.5,
                        'insurance': {
                            'health': 150000,
                            'pension': 200000,
                            'employment': 80000
                        }
                    },
                    'projects': [
                        {
                            'project_name': '클라우드 시스템 구축',
                            'role': '프로젝트 리더',
                            'period': '2025-03 ~ 2025-08',
                            'performance_rate': 95
                        },
                        {
                            'project_name': 'AI 모델 개발',
                            'role': '기술 자문',
                            'period': '2025-01 ~ 2025-02',
                            'performance_rate': 90
                        }
                    ],
                    'leave_info': {
                        'total_days': 15,
                        'used_days': 5,
                        'remaining_days': 10,
                        'leave_history': [
                            {
                                'date': '2025-05-01',
                                'type': '연차',
                                'reason': '개인 사유'
                            },
                            {
                                'date': '2025-06-15',
                                'type': '반차',
                                'reason': '병원 방문'
                            }
                        ]
                    }
                },
                'DEV002': {
                    'personal_info': {
                        'name': '이코딩',
                        'age': 28,
                        'position': '주임 개발자',
                        'join_date': '2025-03-01',
                        'contact': {
                            'email': 'lee.coding@company.com',
                            'phone': '010-2345-6789',
                            'emergency_contact': '010-9876-5432'
                        }
                    },
                    'salary_info': {
                        'base_salary': 4500000,
                        'bonus_rate': 1.2,
                        'insurance': {
                            'health': 120000,
                            'pension': 150000,
                            'employment': 60000
                        }
                    },
                    'projects': [
                        {
                            'project_name': '모바일 앱 개발',
                            'role': '프론트엔드 개발자',
                            'period': '2025-04 ~ 현재',
                            'performance_rate': 85
                        }
                    ],
                    'leave_info': {
                        'total_days': 15,
                        'used_days': 2,
                        'remaining_days': 13,
                        'leave_history': [
                            {
                                'date': '2025-04-20',
                                'type': '연차',
                                'reason': '가족 행사'
                            }
                        ]
                    }
                }
            }
        },
        'hr': {
            'name': '인사부',
            'location': '2층',
            'manager': 'HR001',
            'employees': {
                'HR001': {
                    'personal_info': {
                        'name': '박인사',
                        'age': 42,
                        'position': '인사팀장',
                        'join_date': '2025-01-01',
                        'contact': {
                            'email': 'park.hr@company.com',
                            'phone': '010-3456-7890',
                            'emergency_contact': '010-7654-3210'
                        }
                    },
                    'salary_info': {
                        'base_salary': 6000000,
                        'bonus_rate': 1.4,
                        'insurance': {
                            'health': 140000,
                            'pension': 180000,
                            'employment': 70000
                        }
                    },
                    'projects': [
                        {
                            'project_name': '2025 신입 채용',
                            'role': '채용 담당자',
                            'period': '2025-02 ~ 2025-04',
                            'performance_rate': 100
                        }
                    ],
                    'leave_info': {
                        'total_days': 20,
                        'used_days': 3,
                        'remaining_days': 17,
                        'leave_history': [
                            {
                                'date': '2025-03-10',
                                'type': '연차',
                                'reason': '건강검진'
                            }
                        ]
                    }
                }
            }
        }
    }
}

# 데이터 접근 예시
print("=== 회사 직원 정보 시스템 ===\n")

# 1. 특정 직원의 기본 정보 조회
print("1. 김개발 님의 기본 정보")
kim = company['departments']['dev']['employees']['DEV001']['personal_info']
print(f"이름: {kim['name']}")
print(f"직급: {kim['position']}")
print(f"이메일: {kim['contact']['email']}")

# 2. 부서별 관리자 정보 조회
print("\n2. 부서별 관리자 정보")
for dept_id, dept_info in company['departments'].items():
    manager_id = dept_info['manager']
    manager_info = dept_info['employees'][manager_id]['personal_info']
    print(f"{dept_info['name']} 관리자: {manager_info['name']} ({manager_info['position']})")

# 3. 프로젝트 참여 현황
print("\n3. 김개발 님의 프로젝트 현황")
kim_projects = company['departments']['dev']['employees']['DEV001']['projects']
for project in kim_projects:
    print(f"프로젝트명: {project['project_name']}")
    print(f"역할: {project['role']}")
    print(f"기간: {project['period']}")
    print(f"성과율: {project['performance_rate']}%")
    print()

# 4. 휴가 정보 분석
print("4. 부서별 평균 휴가 사용률")
for dept_id, dept_info in company['departments'].items():
    total_rate = 0
    employee_count = len(dept_info['employees'])
    for emp_id, emp_info in dept_info['employees'].items():
        leave_info = emp_info['leave_info']
        usage_rate = (leave_info['used_days'] / leave_info['total_days']) * 100
        total_rate += usage_rate
    avg_rate = total_rate / employee_count
    print(f"{dept_info['name']} 평균 휴가 사용률: {avg_rate:.1f}%")

# 5. 급여 정보 통계
print("\n5. 부서별 평균 기본급")
for dept_id, dept_info in company['departments'].items():
    total_salary = 0
    employee_count = len(dept_info['employees'])
    for emp_id, emp_info in dept_info['employees'].items():
        total_salary += emp_info['salary_info']['base_salary']
    avg_salary = total_salary / employee_count
    print(f"{dept_info['name']} 평균 기본급: {avg_salary:,.0f}원")
