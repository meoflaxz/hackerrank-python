if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

# student_marks is all the data
# student_marks[query_name] is scores associated with name
# find sum of all data, divide by number of scores that exist in that particular name
    average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(format(average_score, ".2f"))