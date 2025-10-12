#Student record system

students = []

def add():

    print("To create new Student ID enter the following data:-")
    name = input("Enter the name of the student:- ")
    
    try:
        adm_no = int(input("Enter student adm no.:-"))
    except ValueError:
        print("Invalid adm no.")
        return
    try:
        standard = int(input("Enter the class student study (in nunbers like - 1,2... ):-"))
    except ValueError:
        print("Enter a valid value ")
        return
    
    section = input("Enter the section student study in ( A,B,C,D):- ")
    if section in ["A", "B", "C", "D"]:
        section_1 = section
    else:
        print("Invalid section...")    
        return

    student = {
        "NAME" : name,
        "ADMISSION NUMBER" : adm_no,
        "CLASS" : f"{standard}-{section_1}",
        "'PERFORMANCE'" : { },
    }
    
    students.append(student)


def remove():
    try:
        r = int(input("Enter the student ID you want to remove "))
        if r >0 and r + 1 < len(students):
            print(f"do you want to delete STUDENT ID -{r}")
            confom_test = input("yes or no")
            if confom_test.strip().lower() == "yes":
                students.pop(r-1)
            elif confom_test.strip().lower() == "no":
                print("No data was deleted...")
            else:
                print("Invalid input value")
        else:
            print(f"enter a valid value in range (1-{len(students)})")
    except ValueError:
        print(f"enter a valid value in range (1-{len(students)})")


def view():
    try:
        for i , val in enumerate(students,start=1):
            print(f"{i}) {val['NAME']}")
    except NameError:
        print("Nothing to show...")


def profile():
    try:
        p = int(input("Enter the Student ID whose profile you want to see:- "))
        if 1 <= p <= len(students):
            student = students[p-1]
            print(f"a) name : {student['NAME']}")
            print(f"b) adm no: {student['ADMISSION NUMBER']}")
            print(f"c) class: {student['CLASS']}")
            print("d) 'performance':")
            perf = student['PERFORMANCE']
            print(f"   i) physics : {perf['PHYSICS'] if perf['PHYSICS'] != '' else 'No marks yet'}")
            print(f"  ii) chemistry : {perf['CHEMISTRY'] if perf['CHEMISTRY'] != '' else 'No marks yet'}")
            print(f" iii) maths : {perf['MATHS'] if perf['MATHS'] != '' else 'No marks yet'}")
        else:
            print(f"Enter a value in range (1-{len(students)})")
    except ValueError:
        print(f"Enter a valid number in range (1-{len(students)})")





def marks_add():
    try:
        s = int(input("Enter the student ID you want to edit:-"))
        print("enter subject whose marks you want to add in list:-")
        print("a) PHYSICS       ")
        print("b) CHEMISTRY")
        print("c) MATHS ")

        add_input = input("a,b,c")
        try:
            if add_input.strip().lower() == "a":
                students[s-1]['PERFORMANCE']['PHYSICS'] = int(input("Enter marks in physics:-"))
            elif add_input == "b":
                students[s-1]['PERFORMANCE']['CHEMISTRY'] = int(input("Enter marks in chemistry:-"))
            elif add_input == "c":
                students[s-1]['PERFORMANCE']['MATHS'] = int(input("Enter marks in maths:-"))
            else:
                print("invlid data ....")
        except ValueError:
            print("Enter a valid subjectt ID...")
    except  (ValueError , IndexError):
        print(f"Enter the value in range (1-{len(students)})")


def reset():
    print("Do you want to reset all data?")
    reset_test = input("yes or no")
    if reset_test.strip().lower() == "yes":
        students.clear()
    elif reset_test.strip().lower() == "no":
        print("no data was erased...")
    else:
        print("invalid data type")



while True:
    print("--------------------------------------------------------")
    print("STUDENT MANAGEMENT DATABASE\n\n")
    print("choose the action you want to perform:-")
    print("1)TO veiw student list")
    print("2)to add/create new Student ID")
    print("3)to view profile of student")
    print("4)to add/update marks of student")
    print("5)to remove a Student ID")
    print("6)reset")
    print("7)Exit")

    try:
        m = int(input("Enter your action number... "))
    except ValueError:
        print("invalid data entered...")

    if m == 1:
        print("--------------------------------------------------------")
        view()
        next = input("press enter to continue..")
    elif m == 2:
        print("--------------------------------------------------------")
        add()
        next = input("press enter to continue..")
    elif m == 3:
        print("--------------------------------------------------------")
        profile()
        next = input("press enter to continue..")
    elif m == 4:
        print("--------------------------------------------------------")
        marks_add()
        next = input("press enter to continue..")
    elif m == 5 :
        print("--------------------------------------------------------")
        remove()
        next = input("press enter to continue..")
    elif m == 6 :
        print("--------------------------------------------------------")
        reset()
        next = input("press enter to continue..")
    elif m == 7:
        print("--------------------------------------------------------")
        
        break
    else:
        print(f"Enter value in range(1-7)")

    print("--------------------------------------------------------")
  
