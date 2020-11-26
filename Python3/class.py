class Mobile:
    oldPhn = 'Keypad'
    newPhn = 'Touch'

    def oldNokia(self):
        print(self.oldPhn)
        
    def newPhone(self):
        print(self.newPhn)

def main():
    myMobile = Mobile()

    myMobile.newPhone()
    myMobile.oldNokia()

main()

