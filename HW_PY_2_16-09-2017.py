class subscriber:
    def __init__(self, name=''):
        self.name = name

    def enter_name(self,name=''):
        self.name = name

    def enter_home_phone(self, phone):
        self.home_phone = phone

    def enter_work_phone(self, phone):
        self.work_phone = phone

    def enter_mobile_phone(self, phone):
        self.mobile_phone = phone

    def enter_inform(self, inform):
        self.inf = inform
telbook = []

def add_new():
    new = subscriber()
    new_data = input('Enter name: ')
    new.enter_name(new_data)
    new_data = input('Enter phone of home: ')
    new.enter_home_phone(new_data)
    new_data = input('Enter phone of work: ')
    new.enter_work_phone(new_data)
    new_data = input('Enter phone of mobile: ')
    new.enter_mobile_phone(new_data)
    new_data = input('Enter additional information: ')
    new.enter_inform(new_data)
    telbook.append(new)

def show_all():
    i = 1
    for sub in telbook:
        print('№',i, sub.name, sub.home_phone, sub.work_phone, sub.mobile_phone, sub.inf)
        i +=1

def delete(i):
    i -=1
    if (i>=len(telbook)) and (i<0):
        print('The subscriber with such number doesn\'t exist')
        return
    telbook.pop(i)

def find(st):
    i = 1
    for sub in telbook:
        if st == sub.name:
            print('№',i, sub.name, sub.home_phone, sub.work_phone, sub.mobile_phone, sub.inf)
        i +=1

if __name__ == '__main__':
    select = ' '
    while select != 'n':
        print('1 - to add the new subscriber')
        print('2 - to remove the subscriber')
        print('3 - search of the subscriber')
        print('4 - to show all subscribers')
        print('n - exit \n')
        select = input()
        if select == '1':
            add_new()
        elif select == '2':
            num = input('Enter serial number of the deleted subscriber')
            num = int(num)
            delete(num)
        elif select == '3':
            str = input('Enter a name of the required subscriber')
            find(str)
        elif select == '4':
            show_all()
