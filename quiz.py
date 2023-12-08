import random
from termcolor import colored
import os
os.system('color')
def quiz():
    score=0
    questionsRight=0
    i=0
    questionno=1
    fnames=['choose_correct_noun.csv','Identify_proper_or_common_noun.csv','write_plural_of_the_following.csv']
    for fname in fnames:
        fileName =fname
        f_name=fname.split('_')
        s = ' '.join(f_name)
        print(colored(s[:-4],'yellow'))
        quizFile = open(fileName,"r")
        quizData = quizFile.readlines()
        random.shuffle(quizData)
        i=i+len(quizData)
        
        for i in range(len(quizData)):
            x = quizData[i].strip()
            data = x.split(",")        
            question = data[0]
            choice=data[1]
            CorrectAnswer = data[2]
        
            print("Question #",questionno,question)
            choice_list=choice.split('-')
            k=len(choice_list)
          
            for z in range(0,k):
                if choice_list[z]!='':          
                    print((z+1),'-',choice_list[z])
          
            answer = input("What is your answer? ")
            if answer.upper() == CorrectAnswer.upper():
                print(colored("Correct!",'green'))
                score=score+1
                questionsRight=questionsRight+1
                questionno = questionno+1

            else:
                print(colored("Incorrect.",'red'))
                print(colored("Correct answer should be: "+CorrectAnswer,'blue'))
                questionno = questionno+1
        
            
    totalScore = (score / (questionno-1)) * 100
    print(colored("You got "+str(score)+" questions right and a score of "+str(totalScore)+"%.",'yellow'))
          
          
          
          
          
quiz()