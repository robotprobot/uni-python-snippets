pwd = "ATOTALLYSECUREPASSWORD"

while 1==1:
    userentered = input("Please enter password: ").upper()
    if userentered == pwd:
      print("Password accepted!")
      print("""
      Welcome back User!
      
      There has been no events whilst you were away.
      """)
      break;
    else:
        print("Incorrect password. Try again.")