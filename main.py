import random
Question = 1
Score = 0
while Question <= 10:
    apple1 = random.randint(1,12)
    apple2 = random.randint(1,12)
    print("Question",Question)
    if Question % 2 == 0:
        if apple1 < apple2:
            apple1, apple2 = apple2, apple1
        print(f"{apple1} 🍎 × {apple2} 🍎 = ?")
    else:
         print(f"{apple1} 🍎 ÷ {apple2} 🍎 = ?")
    ans = int(input(""))
    if Question % 2 == 0:
        if ans == apple1 * apple2:
            print("Correct!")
            Score += 1
        else:
            print("Incorrect!")
            print("The answer is", apple1 * apple2)
    else:
          if ans == apple1 / apple2:
              print("Correct!")
              Score += 1
          else:
              print("Incorrect!")
              print("The answer is", apple1 / apple2)
    Question += 1
            
print("================")
print("Score =", Score, "/10!")  
print("================")    
if Score == 10:
  print("Superstar! 😆🎖")
elif Score >= 5:
    print("Ah! you're a banger! 🤩👊")
else:
    print("It's hard, but you can do this! 🥹")