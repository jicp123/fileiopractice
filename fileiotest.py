#so uhh erm login typa thingy lmao
#1 - user is asked if login or new acc
#2 - in new acc, make new file according to username, then in login user uses name to access that file u feel me
#3 - in making new acc user is asked to input info bout themselves js for shits n giggles then save
#4 - yeah

#in checking if account exists try to put filenames in a list?? idk
#need way to check if account already exists 
#ok so not list, i make a database w all accounts and yeahhh
accounts = []
def start():
    with open("accounts.txt") as file:
      for x in file:
        accounts.append(x.strip())
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
        confirm = input(f"Is {checkacc} correct? (Y/N): ").upper().strip()
        if confirm in ["Y", "N"]:
          if confirm == "Y":
            break
          else:
            continue
        else:
          print("Invalid input.")
      
   with open(f"{checkacc}.txt", "a") as _:
      with open("accounts.txt", "a") as file:
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