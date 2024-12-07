# student.py
from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call parent class initializer
        self.knowledge = []  # Initialize with an empty list for knowledge
    
    def learn(self, knowledge_string):
        # Add a knowledge string to the student's list of knowledge
        self.knowledge.append(knowledge_string)
