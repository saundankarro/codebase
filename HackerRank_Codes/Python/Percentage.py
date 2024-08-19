if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for k,v in student_marks.items():
        marks_len = sum(1 for w in v if query_name)
    print(f"Looking up the percentage of {query_name}'s marks...")


    avg = sum(student_marks[query_name])/marks_len

    output = f"{avg:.2f}"
    print(output)