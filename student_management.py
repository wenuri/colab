# 학생 관리 프로그램

def input_one_student():
    name = input("학생 이름을 입력하세요 (종료하려면 'q' 입력): ")
    if name.lower() == 'q':
        return None
    
    try:
        score = int(input(f"{name}의 성적을 입력하세요: "))
        if 0 <= score <= 100:
            return (name, score)
        else:
            print("성적은 0에서 100 사이의 값이어야 합니다.")
            return input_one_student()
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
        return input_one_student()

def input_student_data():
    student = input_one_student()
    if student is None:
        return ()
    return (student,) + input_student_data()

def get_rank(student_score, all_scores):
    if not all_scores:
        return 1
    
    higher_scores = tuple(score for score in all_scores if score > student_score)
    return len(higher_scores) + 1

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

def print_ranking(ranked_students):
    if not ranked_students:
        return
    
    print("\n[학생 성적 순위]")
    print("순위\t이름\t성적")
    print("-" * 30)
    print_student_ranks(ranked_students)

def print_student_ranks(ranked_students):
    if not ranked_students:
        return
    
    student = ranked_students[0]
    print(f"{student[2]}등\t{student[0]}\t{student[1]}점")
    
    if len(ranked_students) > 1:
        print_student_ranks(ranked_students[1:])

def sort_by_score(students):
    if not students:
        return ()
    
    if len(students) == 1:
        return students
    
    pivot = students[0]
    rest = students[1:]
    
    higher = tuple(s for s in rest if s[1] > pivot[1])
    lower = tuple(s for s in rest if s[1] <= pivot[1])
    
    return sort_by_score(higher) + (pivot,) + sort_by_score(lower)

def main():
    print("=== 학생 성적 관리 프로그램 ===")
    
    # 학생 데이터 입력 받기
    students = input_student_data()
    
    if not students:
        print("입력된 학생 데이터가 없습니다.")
        return
    
    # 성적 순으로 정렬
    sorted_students = sort_by_score(students)
    
    # 석차 계산
    ranked_students = calculate_rank(sorted_students)
    
    # 결과 출력
    print_ranking(ranked_students)

if __name__ == "__main__":
    main()

#test
##test2
#test3

