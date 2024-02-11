class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise ValueError('Студентов больше 10')

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