print("WELCOME TO KAUN BANEGA CROREPATI")
name = input("\nEnter your name : ")

questions = [
    ["What is the purpose of 'break' in a loop?", 
     "Skip iteration", 
     "Exit loop", 
     "Repeat loop", 
     "Declare variable", 
     2],

    ["Which force opposes motion?", 
     "Friction", 
     "Gravity", 
     "Normal force", 
     "Tension", 
     1],

    ["What is the symbol for gold?", 
     "Ag", 
     "Au", 
     "Hg", 
     "Pb", 
     2],

    ["What does 'git commit' do?", 
     "Stage changes", 
     "Push changes", 
     "Save changes", 
     "Create branch", 
     3],

    ["What is the unit of force?", 
     "Newton", 
     "Joule", 
     "Pascal", 
     "Watt", 
     1],

    ["What is the output of `5 % 2`?", 
     "2", 
     "2.5", 
     "1", 
     "3", 
     3],

    ["What is the process of water turning to ice?", 
     "Melting", 
     "Freezing", 
     "Boiling", 
     "Sublimation", 
     2],

    ["What does 'return' do in a function?", 
     "Exit function", 
     "Return value", 
     "Call function", 
     "Declare variable", 
     2],

    ["What is the largest planet?", 
     "Earth", 
     "Saturn", 
     "Jupiter", 
     "Uranus", 
     3],

    ["What is the chemical symbol for oxygen?", 
     "O", 
     "O2", 
     "H2O", 
     "CO2", 
     1],

    ["What is the purpose of an array?", 
     "Store data", 
     "Perform math", 
     "Create loops", 
     "Define functions", 
     1],

    ["What is the speed of light?", 
     "300 m/s", 
     "300,000 km/s", 
     "1500 m/s", 
     "100 km/h", 
     2],

    ["What is the process of a solid turning to gas?", 
     "Melting", 
     "Freezing", 
     "Sublimation", 
     "Deposition", 
     3],

    ["What is the smallest unit of life?", 
     "Cell", 
     "Molecule", 
     "Tissue", 
     "Organ", 
     1],

    ["What does 'git push' do?", 
     "Stage changes", 
     "Save changes", 
     "Upload changes", 
     "Create branch", 
     3],

    ["What is the chemical formula for water?", 
     "H2", 
     "O2", 
     "H2O", 
     "CO2", 
     3],

    ["What is the purpose of a loop?", 
     "Repeat code", 
     "Skip code", 
     "Exit code", 
     "Declare variable", 
     1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, 10000000, 75000000]
money = 0
for i in range(0, len(questions)):

  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]} is {question[0]}")
  print(f"\na. {question[1]}\nb. {question[2]}")
  print(f"c. {question[3]}\nd. {question[4]} ")
  reply = int(input("\nEnter your answer (1-4) or 0 to quit: " ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 5):
      money = 10000
    elif(i == 10):
      money = 320000
    elif(i == 15):
      money = 7500000
    elif(i == 17):
      money = 75000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")