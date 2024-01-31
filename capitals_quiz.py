print("Welcome to the World Capitals Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()  

print("Okay! Let's play :)")
score = 0

answer = input("What is the capital of France? ")

if answer.lower() == "paris": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")
  
answer = input("What is the capital of the United States of America? ")

if answer.lower() == "washington, d.c.": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")
  
answer = input("What is the capital of Germany? ")

if answer.lower() == "berlin": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")
  
answer = input("What is the capital of Italy? ")

if answer.lower() == "rome": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")

answer = input("What is the capital of Spain? ")

if answer.lower() == "madrid": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")

answer = input("What is the capital of Portugal? ")

if answer.lower() == "lisbon": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")

answer = input("What is the capital of Russia? ")

if answer.lower() == "moscow": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")
  
answer = input("What is the capital of the United Kingdom? ")

if answer.lower() == "london": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")
  
answer = input("What is the capital of Ireland? ")

if answer.lower() == "dublin": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")
  
answer = input("What is the capital of Brazil? ")

if answer.lower() == "brasilia": 
  print("Correct!")
  score += 1 
else: 
  print("Incorrect!")
  
print("You got " + str((score / 10) * 100) + "%.")