grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
book_of_students = {students[0]: grades[0],
                    students[1]: grades[1],
                    students[2]: grades[2],
                    students[3]: grades[3],
                    students[4]: grades[4]}
print(book_of_students)
print(students[1])
print(grades[1])
