class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'First name: {self.first_name}, last name: ' \
               f'{self.last_name}, age: {self.age}, gender: {self.gender} '


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'First name: {self.first_name}, last name: {self.last_name}, ' \
               f'id student: {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        tmp_set = self.group.copy()
        student_remove = self.find_student(last_name)
        for element in tmp_set:
            if str(student_remove) in str(element):
                self.group.remove(student_remove)

    def find_student(self, last_name):
        tmp_set = self.group.copy()
        for element in tmp_set:
            if last_name in str(element):
                return element
        return None


    def __str__(self):
        for student in self.group:
            all_students = student
            return f'Number:{self.number}\n {all_students} '