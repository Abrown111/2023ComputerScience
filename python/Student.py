from ClassSection import ClassSection
import csv
import random


class Student:
    # holds a list of all students
    all_students = []

    # initializes the student objects
    def __init__(self, name, grade, advisor, requests):
        self.name = name
        self.grade = grade
        self.advisor = advisor
        self.requests = requests

        # schedule dictionary
        self.schedule = {
            'Q1/3 P1' : None,
            'Q1/3 P2' : None,
            'Q1/3 P3' : None,
            'Q1/3 P4' : None,
            'Q2/4 P1' : None,
            'Q2/4 P2' : None,
            'Q2/4 P3' : None,
            'Q2/4 P4' : None
        }
        self.all_students.append(self)

    def create_schedule(self):
        # worked = []
        # loops through the classes, inputting requests
        for requests in self.requests:
            for classes in ClassSection.all_classes[requests]:

                # if the amount of people in the class is less than the calss size and the student has the period open
                if classes.class_size > classes.people_in_class and self.schedule[classes.period] is None:
                    # worked.append(True)

                    # add the student to the class and add the class to the schedule
                    classes.add_student(self)
                    self.schedule[classes.period] = classes
                    break
            # worked.append(False)
        # return worked

    def __repr__(self):
        # returns name and schedule
        return f'{self.name}: \n\t' \
               f'Period 1 (1/3): {self.schedule["Q1/3 P1"]}\n\t' \
               f'Period 2 (1/3): {self.schedule["Q1/3 P2"]}\n\t' \
               f'Period 3 (1/3): {self.schedule["Q1/3 P3"]}\n\t' \
               f'Period 4 (1/3): {self.schedule["Q1/3 P4"]}\n\t' \
               f'Period 1 (2/4): {self.schedule["Q2/4 P1"]}\n\t' \
               f'Period 2 (2/4): {self.schedule["Q2/4 P2"]}\n\t' \
               f'Period 3 (2/4): {self.schedule["Q2/4 P3"]}\n\t' \
               f'Period 4 (2/4): {self.schedule["Q2/4 P4"]}\n\t' \

    @classmethod
    def add_sample_data_students(cls):
        # instantiates student data from csv
        # opens csv file as type read and creates a dictionary with all objects. Then, converts this dictionary into a list
        with open('sample student data no names.csv', 'r') as f:
            reader = csv.DictReader(f)
            print(f)
            items = list(reader)

        # loops through the items in the csv file
        # takes the items associated with the header name and creates student, automatically adding them to the list of students
        for item in items:
            request = []
            for i in range(9):
                if item.get(f'req{i+1}') is not '':
                    request.append(item.get(f'req{i+1}'))
            Student(
                name=item.get('name'),
                grade=item.get('grade'),
                advisor=item.get('advisor'),
                requests=request
            )






