import csv
from Student import Student
from ClassSection import ClassSection

# Main method for scheduling project
# Prints each student, with how many requests were properly filled, and their schedule
# Prints A report of all the classes, stating how many students are in the class versus how many are meant to be

if __name__ == '__main__':

    # instantiates from the csv every class object
    ClassSection.instantiate()

    # begins keeping tally of the amount of students with perfect schedules
    sum = 0

    # instantiates from csv once again
    Student.add_sample_data_students()

    # loops through each individual student, printing their name, schedule, and how many of their chosen classes they are enrolled in
    for i in range(336):
        nums = 0
        Student.all_students[i].create_schedule()

        # a list of all the classes in the dictionary
        yo = list(Student.all_students[i].schedule.values())

        # loops through the schedule and checks how many are none
        for y in yo:
            if y is None:
                nums += 1

        # since the max number of classes is 8, 8 - the amount of classes they don't have is the classes they do have
        print(f'{8-nums}/{len(Student.all_students[i].requests)} Requests Filled')

        # prints student schedule and name
        print(Student.all_students[i])

        # if the number of requests and the number of classes are equal, then add an equal class to sum
        if float(8-nums)/len(Student.all_students[i].requests) == 1:
            sum += 1

    # divide sum by 336 to find percent people who have perfect schedules
    print(f'{100* sum/336} % of people have perfect schedules')

    # loops through classes and prints their data
    for sec in ClassSection.all_classes:
        for clas in ClassSection.all_classes[sec]:
            print(clas)







