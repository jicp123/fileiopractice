#so uhh erm login typa thingy lmao
#yo future me or anyone reading this, add something to check if bdays are valid, like if they match actual dates
import csv
accounts = {}
def start():
    with open("accounts.csv") as file:
      file1 = csv.reader(file)
      for x in file1:
        username = x[0].strip()
        dob = x[1].strip()
        age = int(x[2].strip())

        accounts[username] = {
          "birthday": dob,
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
        print(accounts)
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
      
   with open("accounts.csv", "a") as file:
    file.write(f"{checkacc}\n")
   main(checkacc)

def oldacc():
  while True:
    accexists = input("Enter your account name here: ").lower().strip()
    if accexists in accounts:
      main(accexists)
      break
    else:
      print("Account not found. Please check input.")  
       
def main(accname):
  print(f"Welcome {accname}!")

start()