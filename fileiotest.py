#so uhh erm login typa thingy lmao
#yo future me or anyone reading this, add something to check if bdays are valid, like if they match actual dates
import csv
import re
accounts = {}
bday_pattern = r"^[0-9]{2}/[0-9]{2}/[0-9]{2}$"
age_pattern = r"^[0-9]{2}$"
def start():
    with open("accounts.csv") as file:
      file1 = csv.DictReader(file)
      for x in file1:
        username = x["name"].strip()
        date = x["dob"].strip()
        age = int(x["age"].strip())

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
   while True:
    bday = input("Enter your birthday (MM/DD/YY): ")
    if re.match(bday_pattern, bday):
      break
    else:
      print("Invalid birthday format, Please follow MM/DD/YY")
   while True:
     age = str(input("Enter your age: "))
     if re.match(age_pattern, age):
       break
     else:
       print("Invalid input.")
   with open("accounts.csv", "a") as file:
     file.write(f"{accname}")
     file.write(f",{bday}") 
     file.write(f",{age}\n")  
     print(f"Welcome {accname}!")
     print("Account successfully created.")
  elif state == True:
    print(f"Welcome back {accname}!")
    #placeholder

start()
