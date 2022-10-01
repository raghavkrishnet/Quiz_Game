class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompt = [
    "Ques1: Which of the following is correct with respect to OOP concept in Python? \n(a) Objects are real world entities while classes are not real. \n(b) Classes are real world entities while objects are not real. \n(c) Both objects and classes are real world entities. \n(d) Both object and classes are not real. \n\nAns: ",

    "\nQues2: In python, what is method inside class? \n(a) attribute \n(b) object \n(c) argument \n(d) function \n\nAns: ",

    "\nQues3: What kind of data structures are used for manipulating data in Pandas? \n(a) list and dataFrame \n(b) set and dataFrame \n(c) Series and dataFrame \n(d) series and list \n\nAns: ",

    "\nQues4: Is Python case sensitive when dealing with identifiers? \n(a) No \n(b) Yes \n(c) Machine Development \n(d) None of the above mentioned \n\nAns: ",
    
    "\nQues5: Which of the following is the correct extension of the Python file? \n(a) .python \n(b) .pl \n(c) .py \n(d) .p \n\nAns: ",
    
    "\nQues6: Is Python code compiled or interpreted? \n(a) Python code is both compiled and interpreted \n(b) Python code is neithercompiled nor interpreted \n(c) Python code is only compiled \n(d) Python code is only interpreted \n\nAns: ",
    
    "\nQues7: All keywords in Python are in _________ \n(a) Capitalized \n(b) lower case \n(c) UPPER CASE \n(d) None of the mentioned \n\nAns: ",
    
    "\nQues8: What will be the value of the following Python expression? \n 4 + 3 % 5 \n(a) 7 \n(b) 2 \n(c) 4 \n(d) 1 \n\nAns: ",
    
    "\nQues9: Which of the following is used to define a block of code in python language? \n(a) Indentation \n(b) Key \n(c) Brackets \n(d) All of the above mentioned \n\nAns: ",
    
    "\nQues10: Which keyword is used for function in Python langauge? \n(a) Function \n(b) Def \n(c) Fun \n(d) Define \n\nAns: "
]

questions = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"d"), 
    Question(question_prompt[2],"c"), 
    Question(question_prompt[3],"a"), 
    Question(question_prompt[4],"c"), 
    Question(question_prompt[5],"b"), 
    Question(question_prompt[6],"d"), 
    Question(question_prompt[7],"a"), 
    Question(question_prompt[8],"a"), 
    Question(question_prompt[9],"b") 
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        
    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)