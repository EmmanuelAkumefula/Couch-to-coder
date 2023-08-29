# card_number = int(90122345456)
# pin = (2343)
# Account_Balance = int(2000)

def start():

    print ("Welcome to ATM")
    card_number = int(90122345456)
    pin = (2343)
    Account_Balance = int(2000)
    insert_cardnumber = int(input("type in card number"))
    
    error_message = ("wrong card number please retry card number :" )

    if card_number == insert_cardnumber:
        print (verify())

    elif card_number != insert_cardnumber :
        print(error_message , insert_cardnumber)
        start()    



def verify():
      error_message_pin = ("wrong pin number please retry pin number :" )

      insert_pin = int(input("insert pin"))
      pin = (2343)
      Account_Balance = int(2000)

      


      if insert_pin == pin:
        print("Welcome Emmanuel")
        print("Your available balance is : " + str(Account_Balance) )


      elif insert_pin != pin :
        print(error_message_pin)
        verify()
    

start()





 
