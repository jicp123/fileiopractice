#so uhh erm login typa thingy lmao
#1 - user is asked if login or new acc
#2 - in new acc, make new file according to username, then in login user uses name to access that file u feel me
#3 - in making new acc user is asked to input info bout themselves js for shits n giggles then save
#4 - yeah

#in checking if account exists try to put filenames in a list?? idk
#uhm soooooooo hehe 
#new test

accounts = []

def start():
    while True:
      newornot = input("Do you have an existing account? (Y/N):  ").upper().strip()
      if newornot in ["Y", "N"]:
         break
      else:
         print("Invalid input.")
    if newornot == "Y":
     while True:
      try:
        checkacc = str(input("Input account name here: ").lower().strip())
        break
      except ValueError:
        print("Input a valid account name.")
     #add file thingy here
        
