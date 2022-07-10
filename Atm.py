class ATM(object):
  def __init__(self, cardNum, pin, bal = 0):
    self.cardNum = cardNum
    self.pin = pin
    self.bal = bal
  def cashWithdrawl(self, amount):
    g = 3
    while g > 0:
      q = input('Pin:')
      if q == self.pin:
        if self.bal >= amount:
          self.bal-=amount
        else:
          print('You don\'t have enough money')
        break
      else:
        print('Incorrect pin. Please try again.')
      g -= 1
      if g == 0:
        print('Could not withdraw money.')
  def seeBalance(self):
    print('Your balance is',str(self.bal))
  def deposit(self, amount):
    g = 3
    while g > 0:
      q = input('Pin:')
      if q == self.pin:
        self.bal+=amount
        break
      else:
        print('Incorrect pin. Please try again.')
      g -= 1
      if g == 0:
        print('Could not deposit money.')
atm = ATM(1234, '1234')
atm.seeBalance()
atm.deposit(500)
atm.seeBalance()
atm.cashWithdrawl(300)
atm.seeBalance()