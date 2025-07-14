class Student:
    def __init__(self, id=0, name='', marks=0.0):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'ID= {self.id}, Name={self.name}, Marks={self.marks}'

class Node:
    def __init__(self, student=None):
        self.data = student
        self.link = None
    
    def create_student(self):
        id = int(input('Enter Id of the student: '))
        name = input('Enter Name of the student: ')
        marks = float(input('Enter Marks of the student: '))
        student = Student(id, name, marks)
        return student

class Queue:
    def __init__(self):
        self.front = None

    def insert(self):
        node = Node()
        student = node.create_student()
        node.data = student
        if self.front is None:
            self.front = node
            return
        node.link = self.front
        self.front = node

    def delete(self):
        if self.front is None:
            print('Queue is empty')
            return
        if self.front.link is None:
            print(f'Deleted Node data is: {self.front.data}')
            self.front = None
            return

        temp = self.front
        while temp.link.link is not None:
            temp = temp.link
        print(f'Deleted Node data is: {temp.link.data}')
        temp.link = None
