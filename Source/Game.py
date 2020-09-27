import random
import time
import yaml
import os

with open("./colors.txt", "r") as clrf:
    colors = []
    for i in clrf.readlines():
        if not i.strip().startswith("!"):
            colors.append(i.strip())
        else:
            pass

class Game():
    def __init__(self, qlist, questions):
        QuestionsN = qlist # ["Math-1"]
        Questions = questions # {"Math-1": {"q": "How many is 3*5?", "a": "15"}}
        Life = 5
        Round = 1
        Score = 0
        WinScore = len(QuestionsN)
        while 1:
            print(f"\n-----------------------------\nLifes: {Life}\nScore: {Score}\nRound: {Round}\n-----------------------------")
            question = random.choice(QuestionsN)
            print(Questions[question]["q"])
            print("-----------------------------")
            inp = input("> ")
            if inp == Questions[question]["a"]:
                print("\n===== ( Correct ) =====")
                Score += 1
                QuestionsN.remove(question)
            else:
                print("\n===== ( Incorrect ) =====")
                Life -= 1
            if Score >= WinScore:
                print(f"\n===== ( Game Over ) =====\nLifes: {Life}\nScore: {Score}\nRound: {Round}\n >>> You Win <<<")
                break
            elif Life <= 0:
                print(f"\n===== ( Game Over ) =====\nLifes: {Life}\nScore: {Score}\nRound: {Round}\n >>> You Lost <<<")
                break
            Round += 1
while 1:
    with open("./Questions.yaml", "r") as QFile:
        QSource = yaml.load(QFile, Loader=yaml.FullLoader)
    os.system(f"color {random.choice(colors)}")
    print("-----------------------------------------------\n HyScript7's Puzzle\n Made for a challange with Bloody_Devil\n-----------------------------------------------")
    NewGame = Game(QSource["List"], QSource["Questions"])
    time.sleep(5)