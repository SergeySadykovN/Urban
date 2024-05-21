grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# ����� �������� ������ ���� �������� � ���������� �������.
# ��� ����� ��� ������������ ������ � grades.
sorted_students = sorted(students)

# ����� ������� ����� �������� � �� ������� ������.
aver_grades = {}

for i in range(len(sorted_students)):
    """�������� �� ������� ������� � ��� ������� � ������� ����� for.
i ������������ ��� ������, ����� ����� ��������������� ������ �� grades.
������� ������� ������ �������: sum(student_grades) / len(student_grades).
��������� ��� ������� � ��� ������� ������ � �������."""
    student = sorted_students[i]
    student_grades = grades[i]
    average = sum(student_grades) / len(student_grades)
    aver_grades[student] = average

print(aver_grades)
