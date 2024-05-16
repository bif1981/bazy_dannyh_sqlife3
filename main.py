# Создайте базу данных students.db
# В базе данных должны существовать 2 таблицы: students и grades
# В таблице students должны присутствовать следующие поля: id, name, age
# В таблице grades должны присутствовать следующие поля: id, student_id, subject, grade
# # Так же нужно создать класс University со следующими атрибутами и методами:
# name - имя университета
# add_student(name, age) - метод добавления студента.
# add_grade(student_id, subject, grade) - метод добавления оценки.
# get_students(subject=None) - метод для возврата списка студентов в формате [(Ivan, 26, Python, 4.8), (Ilya, 24,
# PHP, 4.3)], где subject, если не является None(по умолчанию) и если такой предмет существует, выводит студентов
# только по этому предмету.
# Описание полей:
# id - в обоих таблицах обязательно PRIMARY KEY
# name - STR
# age - INT
# subject - STR
# grade - FLOAT
# и самое интересное student_id - INT (или внешний ключ)
#
# Внешний ключ - это данное в поле указывающее на id в другой таблице, оно может быть реализовано следующей командой в
# SQL: FOREIGN KEY (student_id) REFERENCES students(id), при создании таблицы.
# При этом поле student_id - существует как INT.
#
# Пример работы кода:
#
# Код:
# u1 = University('Urban')
#
# u1.add_student('Ivan', 26) # id - 1
# u1.add_student('Ilya', 24) # id - 2
#
# u1.add_grade(1, 'Python', 4.8)
# u1.add_grade(2, 'PHP', 4.3)
#
# print(u1.get_students())
# print(u1.get_students('Python'))
#
# Консоль:
# [(Ivan, 26, Python, 4.8), (Ilya, 24, PHP, 4.3)]
# [(Ivan, 26, Python, 4.8)]
#
# Примечание:
# Перед отправкой полной версии БД на GitHub сделайте при помощи вашего класса University и соответствующих объектов
# минимум 8 записей, где у каждого студента будет минимум по 2 зачёт (значит студентов будет 4).
#
# Пришлите ссылку на репозиторий GitHub со следующими файлами:
# Файл базы данных с расширением .db
# Файл(-ы) с классом University и соответствующим(-и) объектами (на которых тестировали).
#
# Помните, что веткой по умолчанию (default) должна быть выбрана та, где находятся необходимые файлы.

import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()


cursor.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name STR, age INT)")
cursor.execute("CREATE TABLE grades(id INTEGER PRIMARY KEY, student_id, subject STR, grade FLOAT)")


class University:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()

    # Метод добавления студентов
    def add_student(self, name, age):
        self.cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    # Метод добавления оценок
    def add_grade(self, student_id, subject, grade):
        self.cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)",
                            (student_id, subject, grade))
        self.conn.commit()

    # Метод для возврата списка студентов
    def get_students(self, subject=None):
        if subject:
            self.cursor.execute("SELECT students.name, students.age, grades.subject, grades.grade FROM students "
                                "JOIN grades ON students.id = grades.student_id WHERE grades.subject = ?",
                                (subject,))
        else:
            self.cursor.execute("SELECT students.name, students.age, grades.subject, grades.grade FROM students JOIN "
                                "grades ON students.id = grades.student_id")
            self.conn.commit()
        students_data = self.cursor.fetchall()
        self.conn.commit()
        for row in students_data:
            if students_data:
                return students_data
            print(students_data)
            print(row)

        self.conn.commit()
        cursor.close()

    def __del__(self):
        self.conn.close()


u1 = University('Urban')

u1.add_student('Ivan', 26)  # id - 1
u1.add_student('Ilya', 24)  # id - 2
u1.add_student('Kolya', 30)  # id - 3
u1.add_student('Tolya', 28)  # id - 4

u1.add_grade(1, 'Python', 4.8)
u1.add_grade(2, 'PHP', 4.3)
u1.add_grade(1, 'PHP', 4.3)
u1.add_grade(2, 'Python', 4)
u1.add_grade(3, 'PHP', 5)
u1.add_grade(3, 'Python', 4.5)
u1.add_grade(4, 'PHP', 4.7)
u1.add_grade(4, 'Python', 4.9)

print(u1.get_students())
print(u1.get_students('Python'))
