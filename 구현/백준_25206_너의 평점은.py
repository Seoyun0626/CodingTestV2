dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
score = 0
total_grade = 0
for _ in range(20):
    name, grade, alphabet = map(str, input().split())
    if alphabet == "P":
        continue
    else:
        score += (float(grade) * dict[alphabet])
        total_grade += float(grade)
result = score / total_grade
print((round(result, 6)))

