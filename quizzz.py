sample_question = ["who is virat kholi?" , "how many alphabet are there in english excluding vowels?" , "when did INDIA got freedom from british rule?","is python good language?"]
sample_answer_1 = ["writer", "elephant","cricketer", "prime minister"]
sample_answer_2 = ["26", "5","21", "98"]
sample_answer_3 = ["1947", "1950","1946","2014"]
sample_answer_4 = ["yes" , "no","can't say", "it depends on demand"]


for question in sample_question:

    print(question)
    
    if question == "who is virat kholi?"  :
        print("choose your answer :-")
        for otp in sample_answer_1:
            print(otp)
        answer = input("type your ans carefully ")
        if answer == "cricketer":
            print("correct answer", "you won RS.500")
        else:
            print("you lost fool")
            break



    if question == "how many alphabet are there in english excluding vowels?" :
        print("choose your answer :-")
        for otp in sample_answer_2:
            print(otp)
        answer = input("type your ans carefully ")
        if answer == "21":
            print("correct answer", "you won RS.1500")
        else:
            print("you lost fool")
            break

    if question == "when did INDIA got freedom from british rule?" :
        print("choose your answer :-")
        for otp in sample_answer_3:
            print(otp)
        answer = input("type your ans carefully ")
        if answer == "1947":
            print("correct answer", "you won RS.3000")
        else:
            print("you lost fool")
            break
 
    if question =="is python good language?" :
        print("choose your answer :-")
        for otp in sample_answer_4:
            print(otp)
        answer = input("type your ans carefully ")
        if answer == "yes":
            print("correct answer", "you won RS.6000")
        else:
            print("you lost fool")
            break