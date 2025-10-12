# To-do list

active_list = ["a","b","c"]
dead_list = []



def add():
    a = input("enter task you want To add:- ")
    active_list.append(a)

def remove():
    r = int(input("enter the list number you want To remove:- "))
    try:
        active_list.pop(r-1)
    except (ValueError , IndexError):
         print(f"that list don't exist.\nenter list number in range(1-{len(active_list)})")
         


def check():

    print("ACTIVE TASK LIST")
    if len(active_list) == 0 :
            print("YAY!! YOU HAVE NO PENDING TASK")
    else:
        for i, items in enumerate(active_list, start=1):
            print(f"{i}) {items} [pending ...]")
   
    print("TASK YOU HAVE COMPLETED")
    if len(dead_list) == 0:
           print("nothing to show...")
    else:
        for i, items in enumerate(dead_list, start=1):
            print(f"{i}) {items} [done]")  
    
        
       
def done():
    d = int(input(f"enter the list you have completed in range(1-{len(active_list)})"))
    try:
         dead_list.append(active_list[d-1])
         active_list.pop(d-1)
         print("congratulations here is yourupdated list:-")
         check()
    except ValueError:
         print(f"invalid input .. \nenternumber in range(1-{len(active_list)})")
         
def reset():
     active_list.clear()
     dead_list.clear()

while True:
     print("\n  ----------------------------------------------")
     print("Welcome To To-do list")
     print("1. to view/check your task list enter  '1' ")
     print("2. to add task enter '2' ")
     print("3. to remove task enter '3' ")
     print("4. to mark task as done type '4' ")
     print("5. to exit menu enter '5' ")
     print("6. to reset list type '6' ")

     print("\n  ----------------------------------------------")

     try:
        choice = int(input("enter your response "))
     except ValueError:
          print("enter a valid number in range(1-6)")
          continue
     

     if choice == 1:
        check()
        input("press enter To show  main menu")
     elif choice == 2:
          add()
          input("press enter To show  main menu")
     elif choice ==3:
          remove()
          input("press enter To show  main menu")
     elif choice == 4:
          done()
          input("press enter To show  main menu")
     elif choice == 5:
          break
          input("press enter To show  main menu")
     elif choice == 6:
          reset()
          input("press enter To show  main menu")
     else:
          print("worng responce ")
          try:
             choice = int(input("enter your responce "))
          except ValueError:
             print("enter a valid number in range(1-6)")
             continue

    
    

