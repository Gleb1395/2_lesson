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
        return self.group

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True
gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!