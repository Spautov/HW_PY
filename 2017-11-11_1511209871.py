def ask_user():
    n = input("Enter the size of array: ")
    arr = []
    n = int(n)
    for i in range(0,n):
        st = "Enter the item number #" + str(i+1) +": "
        item = int(input(st))
        arr.append(item)
    return arr

if __name__ == '__main__':
    try:
        array = ask_user()
        print(array)

    except Exception:
        print('Error: You have entered not right data')

