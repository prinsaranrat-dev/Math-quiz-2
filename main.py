import random
Question = 1
Score = 0
while Question <= 10:
    pizza1 = random.randint(1,12)
    pizza2 = random.randint(1,12)
    print("Question",Question)
    if Question % 2 == 0:
        if pizza1 < pizza2:
            pizza1, pizza2 = pizza2, pizza1
        print(f"{pizza1} 🍕 × {pizza2} 🍕 = ?")
    else:
         print(f"{pizza1} 🍕 ÷ {pizza2} 🍕 = ?")
    ans = int(input(""))
    if Question % 2 == 0:
        if ans == pizza1 * pizza2:
            print("Correct!")
            Score += 1
        else:
            print("Incorrect!")
            print("The answer is", pizza1 *pizza2)
    else:
          if ans == pizza1 / pizza2:
              print("Correct!")
              Score += 1
          else:
              print("Incorrect!")
              print("The answer is", pizza1 / pizza2)
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