class Teacher(object):
    ut_count = 0
    def __init__(self, name, surname, subject, salary):
        self.name = name
        self.__surname = surname
        self.subject = subject
        self.salary = salary
        self.salares = 0
        Teacher.ut_count += 1
        self.ut_id = Teacher.ut_count

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, val):
        self.__surname = val


class TimeSheet(object):
    def __init__(self):
        self.subjects = {}
        self.teachers = []

    def calc_salary(self):
        for prep in self.teachers:
            prep.salares = int(prep.salary) * self.subjects[prep.subject]

    def add_subject(self, subj, hours):
        if subj in self.subjects.keys():
            self.subjects[subj] += hours
        else:
            self.subjects[subj] = hours


def get_prepods():
    teachers = []
    with open('teachers.txt') as f:
        for line in f:
            list_line = line.split()
            name = list_line[0]
            surname = list_line[1]
            subj = list_line[2]
            salary = list_line[3]
            teachers.append(Teacher(name, surname, subj, salary))
    return teachers


def do():
    prepods = get_prepods()
    time_sheet = TimeSheet()
    time_sheet.add_subject('physics', 36)
    time_sheet.add_subject('chemistry', 72)
    time_sheet.add_subject('mathematics', 114)
    time_sheet.add_subject('history', 96)
    time_sheet.add_subject('biology', 36)
    time_sheet.add_subject('literature', 18)
    time_sheet.add_subject('philosophy', 72)
    time_sheet.add_subject('language', 96)
    time_sheet.teachers = prepods
    time_sheet.calc_salary()
    print('%-10s %-15s %s' % ('Name', 'Surname', 'salary'))
    for prepod in prepods:
        print('%-10s %-15s %d' % (prepod.name, prepod.surname, prepod.salares))


if __name__ == '__main__':
   do()




