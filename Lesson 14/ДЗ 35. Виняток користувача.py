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


class StudentException(Exception):
    def __init__(self, message, num):
        super().__init__()
        self.message = message
        self.num = num

    def get_exception_message(self):
        return f'{self.message}\n{self.num}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise StudentException('Студентов больше 10', f'Количество допустимых студентов {len(self.group)}')

    def delete_student(self, last_name):
        student_remove = self.find_student(last_name)
        if student_remove:
            self.group.remove(student_remove)

    def find_student(self, last_name):
        for element in self.group:
            if last_name in str(element):
                return element
        return None

    def __str__(self):
        for student in self.group:
            all_students = student
            return f'Number:{self.number}\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 21, 'Liza', 'Taylor', 'AN146')
st4 = Student('Female', 22, 'Liza', 'Taylor', 'AN147')
st5 = Student('Male', 23, 'Liza', 'Taylor', 'AN148')
st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN149')
st7 = Student('Male', 23, 'Liza', 'Taylor', 'AN140')
st8 = Student('Male', 25, 'Liza', 'Taylor', 'AN151')
st9 = Student('Female', 23, 'Liza', 'Taylor', 'AN152')
st10 = Student('Male', 21, 'Liza', 'Taylor', 'AN153')
st11 = Student('Male', 21, 'Liza', 'Taylor', 'AN153')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
try:
    gr.add_student(st11)  # ValueError
except StudentException as e:
    print(e.get_exception_message()) # Достигнут минимум
