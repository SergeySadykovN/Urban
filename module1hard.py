grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# чтобы получить список имен учеников в алфавитном порядке.
# Это нужно для соответствия оценок в grades.
sorted_students = sorted(students)

# будем хранить имена учеников и их средние оценки.
aver_grades = {}

for i in range(len(sorted_students)):
    """Проходим по каждому ученику и его оценкам с помощью цикла for.
i используется как индекс, чтобы брать соответствующие оценки из grades.
Считаем среднюю оценку ученика: sum(student_grades) / len(student_grades).
Добавляем имя ученика и его среднюю оценку в словарь."""
    student = sorted_students[i]
    student_grades = grades[i]
    average = sum(student_grades) / len(student_grades)
    aver_grades[student] = average

print(aver_grades)
