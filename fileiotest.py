#so uhh erm login typa thingy lmao
#yo future me or anyone reading this, add something to check if bdays are valid, like if they match actual dates
import csv
accounts = {}
def start():
    with open("accounts.csv") as file:
      file1 = csv.reader(file)
      for x in file1:
        username = x[0].strip()
        date = x[1].strip()
        age = int(x[2].strip())

        accounts[username] = {
          "birthday": date,
          "age": age
        }
    while True:
      newornot = input("Do you have an existing account? (Y/N):  ").upper().strip()
      if newornot in ["Y", "N"]:
         break
      else:
        print("Invalid input.")
    if newornot == "Y":
     oldacc()
    if newornot == "N":
     newacc()
      
      
def newacc():
   while True:
        checkacc = input("Enter a username here: ").lower().strip()
        if checkacc in accounts:
          print("Account already exists.")
          continue
        confirm = input(f"Is {checkacc} correct? (Y/N): ").upper().strip()
        if confirm in ["Y", "N"]:
          if confirm == "Y":
            break
          else:
            continue
        else:
          print("Invalid input.")
   main(checkacc, False)

def oldacc():
  while True:
    accexists = input("Enter your account name here: ").lower().strip()
    if accexists in accounts:
      main(accexists, True)
      break
    else:
      print("Account not found. Please check input.")  
       
def main(accname, state):
  if state == False:
   bday = input("Enter your birthday (MM/DD/YY): ")
   while True:
    try:
     age = str(input("Enter your age: "))
     break
    except TypeError:
     print("Please input a number.")
   with open("accounts.csv", "a") as file:
    file.write(f"{accname}")
    file.write(f", {bday}")
    file.write(f", {age}\n")
    print(f"Welcome {accname}!")
    print("Account successfully created.")
  if state == True:
    print(f"Welcome back {accname}!")
    #placeholder, do smth here lmao

start()