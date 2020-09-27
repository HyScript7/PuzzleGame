import random
import time
import yaml
import os

class Game():
    def __init__(self, qlist, questions, slife, mnscore):
        QuestionsN = qlist # ["Math-1"]
        Questions = questions # {"Math-1": {"q": "How many is 3*5?", "a": "15"}}
        Life = int(slife)
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
                if random.randint(0,10) > 5:
                    print("> Luck is on your side, question removed. Mistake forgiven.")
                    QuestionsN.remove(question)
                else:
                    Life -= 1
            if len(QuestionsN) <= 0 and Life > 0 or Score >= mnscore:
                print(f"\n===== ( Game Over ) =====\nLifes: {Life}\nScore: {Score}\nRound: {Round}\n >>> You Win <<<")
                break
            elif Life <= 0:
                print(f"\n===== ( Game Over ) =====\nLifes: {Life}\nScore: {Score}\nRound: {Round}\n >>> You Lost <<<")
                break
            Round += 1
while 1:
    os.system("cls")
    with open("./colors.txt", "r") as clrf:
        colors = []
        for i in clrf.readlines():
            if not i.strip().startswith("!"):
                colors.append(i.strip())
            else:
                pass
    with open("./Questions.yaml", "r") as QFile:
        QSource = yaml.load(QFile, Loader=yaml.FullLoader)
    os.system(f"color {random.choice(colors)}")
    print("-----------------------------------------------\n HyScript7's Puzzle\n Made for a challange with Bloody_Devil\n-----------------------------------------------")
    NewGame = Game(QSource["List"], QSource["Questions"], QSource["Config"]["Lifes"], QSource["Config"]["MaxScore"])
    time.sleep(5)