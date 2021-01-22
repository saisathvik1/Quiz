"""
You can add your questions that are related and the 
questions that I mention here are sample! 
"""

# Global Variables
QandA = {"What is capital if India?":"C",
"Who is the current President of India?":"A",
"Who is the current President of US":"B",
"Who is the current captain of India team?":"B"}
questions = list(QandA.keys())
options = [["A. Kolkata","B. Hyderabad","C. New Delhi"],
["A. Ram Nath Kovind","B. Narendra Modi","C. Imran Khan"],
["A. Trump","B. Joe Biden","C. Obama"],
["A. MS Dhoni","B. Virat Kohli","C. Ajinkya Rahane"]]

def new_game():
    score = 0
    print("Welcome to Quiz game!")
    for i in range(len(questions)):
        print("-"*15)
        print(questions[i])
        for j in options[i]:
            print(j)
        ans = input("Enter A or B or C:  ")

        if ans.lower()==QandA[questions[i]].lower():
            print("Correct Answer!")
            score+=1
        else:
            print("Wrong Answer!")
    return score


score = new_game()
print("-"*15)
if score >= 2:
    print(f"You passed🥳 Your score is {score}")
else:
    print(f"You failed😢 Your score is {score}")
