import csv


class ClassSection:

    # same method to all previous instantiates
    @classmethod
    def instantiate(cls):
        with open('sample class data.csv', 'r') as f:
            reader = csv.DictReader(f)
            print(f)
            items = list(reader)
            for item in items:
                ClassSection(
                    class_name=str(item.get('name')),
                    teacher=str(item.get('teacher')),
                    period=str(item.get('period')),
                    class_size=int(item.get('class size'))
                )

    # list of all classes in dictionary form with their values being set to an empty list
    all_classes = {
        'Humanities 9: English': [],
        'Advanced English Language Learning': [],
        'Honors Humanities 12': [],
        'Humanities 12': [],
        'ADV.SEM: Comparative Religion': [],
        'Humanities 9: History': [],
        'American Studies: English': [],
        'ADV.SEM: 21st Century Citizenship': [],
        'Humanities 10': [],
        'ADV.SEM: State-building & Post-Colonial Societies': [],
        'Honors European History': [],
        'Continuing Studies in Ceramics': [],
        'Foundations of Ceramics': [],
        'Foundations of Painting & 2D Design': [],
        'Philharmonic Strings': [],
        'Saints Chorale': [],
        'Music Theory': [],
        'AP Music Theory': [],
        'Concert Choir': [],
        'Foundations of Drawing & 2D Design': [],
        'Continuing Studies in Drawing  Painting & 2D Design': [],
        'Continuing Studies in Digital Media Arts': [],
        'Foundations of Digital Media Arts': [],
        'Continuing Studies in Theatre Arts': [],
        'Theatre Arts': [],
        'Dramatic Literature and Writing': [],
        'Study Skills': [],
        'Life Skills': [],
        'Honors Integrated Mathematics 2': [],
        'Integrated Mathematics 4': [],
        'AP Calculus AB': [],
        'Integrated Mathematics 3': [],
        'Integrated Mathematics 2': [],
        'Integrated Mathematics 1': [],
        'Economics': [],
        'Honors Integrated Mathematics 3': [],
        'Computer Science Principles': [],
        'Honors Data Structures': [],
        'Honors Software Engineering': [],
        'AP Calculus BC': [],
        'Honors Differential Equations': [],
        'AP Statistics': [],
        'AP Chemistry': [],
        'Advanced Biology': [],
        'ADV.SEM: BioTechnology and Ethics': [],
        'ADV.SEM: Enviro. Studies & Research': [],
        'Advanced Chemistry': [],
        'AP Physics C': [],
        'Advanced Physics': [],
        'AP Spanish Language': [],
        'Honors Spanish 2': [],
        'Honors Spanish 3': [],
        'Honors Spanish 5: Adv. Literature/Honors Spanish 6: Lit Film Current Evts': [],
        'Spanish 2': [],
        'Spanish 1': [],
        'Spanish 3': [],
        'Honors French 3': [],
        'French 3': [],
        'AP French Language': [],
        'French 4/5/H': [],
        'Spanish 4/5': [],
        'French 1': [],
        'Latin 4/5': [],
        'French 2': [],
        'ADV.SEM: Entrepreneurship': [],
    }

    # intializer for all class objects
    def __init__(self, class_name, teacher, period, class_size):
        self.class_name = class_name
        self.teacher = teacher
        self.period = period
        self.class_size = class_size
        self.roster = []
        self.people_in_class = 0
        self.all_classes[class_name].append(self)

    # returns class information in readable format, including the amount of epople currently enrolled in the class
    def __repr__(self):
        return f'{self.class_name} - {self.teacher} - {self.period}: {self.people_in_class}/{self.class_size} students'

    # adds students to the class by adding to roster and increasing the number of people in the class
    def add_student(self, student):
        self.people_in_class += 1
        self.roster.append(student)


