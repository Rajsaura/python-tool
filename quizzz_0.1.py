#quizzz game using loops 


questions = [
    ["who is virat kholi?" , "writer","author","cricketer" , "elephant" , 3],
    ["who is srk" , "writer","actor","cricketer" , "elephant" , 2],
    ["how many throphy did KKR won in IPL" , "2","3","none" , "5" , 2],
    ["when did INDIA won indepence?" , "1947","1950","1945" , "2014" , 1],
    ["how many alphabet are there in english excluding vowels?" , "5","26","21" , "49" , 3],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Leo Tolstoy", "Charles Dickens", "Mark Twain", 1],
    ["What is the chemical symbol for water?", "H2O", "O2", "CO2", "NaCl", 1],
    ["Which number is a prime number?", "4", "6", "9", "7", 4],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["In which year did World War II end?", "1945", "1939", "1918", "1950", 1],
    ["Which language is used to style web pages?", "HTML", "JQuery", "CSS", "XML", 3],
    ["What is the boiling point of water in Celsius?", "90°C", "100°C", "110°C", "120°C", 2],
    ["Who discovered gravity?", "Albert Einstein", "Isaac Newton", "Galileo Galilei", "Nikola Tesla", 2]
]

levels = [500 ,1000, 2000, 5000, 10000, 50000, 100000, 250000, 500000,500000, 5000000, 1000000,2000000,35000000, 70000000]


for i, question in enumerate(questions):
    print(f"Q{i+1}: {question[0]}")

    print(question[0])

    print(f"a.{question[1]}                     b.{question[2]}")
    print(f"c.{question[3]}                     d.{question[4]}")
    ans = int(input("enter the option(a as 1 , b as 2 & so on..) :- "))

    if ans == question[5]:
        print(f"correct answer!! .  you won {levels[i]}")
        input("press enter for next question!")
    else:
        print("you lost fool!!!")
        if i <= 4 and i < 8:
            print(f"you won only {levels[4]}")
        elif i <= 8 and i < 10:
            print(f"you won only {levels[8]}")
        elif i <= 10 and i < 12:
            print(f"you won only {levels[10]}")
        elif i >= 12 :
            print(f"you won only {levels[12]}")
        break


