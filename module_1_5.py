grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_avv = [sum(grades[0])/len(grades[0]),
                sum(grades[1])/len(grades[1]),
                sum(grades[2])/len(grades[2]),
                sum(grades[3])/len(grades[3]),
                sum(grades[4])/len(grades[4])]
students = list(students)
students.sort()
book_of_students = {students[0]: grades_avv[0],
                    students[1]: grades_avv[1],
                    students[2]: grades_avv[2],
                    students[3]: grades_avv[3],
                    students[4]: grades_avv[4]}
print(book_of_students)
