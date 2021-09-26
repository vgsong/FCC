class Category:
  def __init__(self, name):
      self.name = name
      self.ledger = []
      self.spentotal = []

  def __str__(self):
      ledgerDescription = []
      ledgerAmounts = []

      ledgerDescription.append([x['description'][0:23] for x in self.ledger])
      ledgerAmounts.append(["{:.2f}".format(x['amount']) for x in self.ledger])
      finalStr = f'{self.name.center(30, "*")}\n'

      for x in range(0,len(ledgerAmounts[0])):
          finalStr += f'{ledgerDescription[0][x].ljust(23)}{ledgerAmounts[0][x].rjust(7)}\n'

      finalStr += f'Total: {sum([x["amount"] for x in self.ledger])}'
      return finalStr

  def check_funds(self, amt):
      if amt > sum([x['amount'] for x in self.ledger]):
          return False
      else:
          return True

  def deposit(self, amt, desc=''):
      self.ledger.append({'amount':amt,'description':desc})

  def withdraw(self, amt, desc=''):
      if self.check_funds(amt) == False:
          return False
      else:
          self.ledger.append({'amount': float(-amt), 'description': desc})
          return True

  def get_balance(self):
      return sum([x['amount'] for x in self.ledger])

  def transfer(self,amt, totransfer):
      if self.check_funds(amt) == False:
          return False
      else:
          self.ledger.append({'amount': float(-amt), 'description': f'Transfer to {totransfer.name}'})
          totransfer.ledger.append({'amount': float(amt), 'description': f'Transfer from {self.name}'})
          return True





def create_spend_chart(categories):
  def get_perspent(cat,totalout):
      result =0
      for x in range(0,len(cat.ledger)):
          result += sum([x['amount'] for x in cat.ledger if x['amount'] < 0])

      result = -int((result/totalout))
      return int(str(result)[0])

  def get_total_spent(allist):
      totalSpent = 0
      for x in range(0,len(allist)):
          totalSpent += sum([x['amount'] for x in allist[x].ledger if x['amount'] < 0])

      return -totalSpent

  # provides dashes amount based on total count of items in categories
  def get_dashes(cat):
      result = '    -'
      for x in range(0, len(cat)):
          result += '---'
      return result

  # separates from word to letters for self.name of each category
  def sep_categories(cat):
      result = []
      for x in range(0, len(cat)):
          result.append(list(cat[x].name))
      return result

  # returns the len of the self.name with the longest string length
  def max_len_list(cat):
      max_len = 0
      temp_len = 0
      for x in range(0, len(cat)):
          temp_len = len(cat[x])
          if max_len < temp_len:
              max_len = temp_len

      return max_len

  #  CONSTANTS
  # All goes into finalStr ---------
  finalStr = 'Percentage spent by category' + '\n'  # The header of the final string
  yList = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
  dashes = get_dashes(categories)
  # ---------------------------

  tempNameList = sep_categories(categories)
  finalNameList = ['   ' for x in range(0, max_len_list(tempNameList))]
  totalout = 0

  # END CONSTANTS

  # debug.print area --------------------------
  # print(tempNameList)
  # print(dashes)
  # print(len(finalNameList))
  totalout = get_total_spent(categories)
  # print(totalout)
  # print(len(categories))
  # END OF debug.print area ----------------------------

  for x in range(0, len(categories)):
      catWithdraw = -sum([x['amount'] for x in categories[x].ledger if x['amount'] < 0])
      numberCircles = int((catWithdraw/totalout)*10)
      vezes = 10 - numberCircles

      while vezes > 0:
          categories[x].spentotal.append('   ')
          vezes -=1
      while 0 <= numberCircles:
          categories[x].spentotal.append(' o ')
          numberCircles -=1

  # print(categories[0].spentotal, categories[1].spentotal, categories[2].spentotal)

  # for x in range(0, len(categories)):
  #     # print(categories[x].ledger)
  #     i = 0
  #     add_blanks = 10 - get_perspent(categories[x],totalout)

  #     while add_blanks > 0:
  #         categories[x].spentotal.append('   ')
  #         add_blanks -= 1

  #     while i <= get_perspent(categories[x],totalout):
  #         categories[x].spentotal.append('o ')
  #         i += 1

  for x in range(0,len(categories[-1].spentotal)):
    categories[-1].spentotal[x] += ' '


  for x in range(0, len(categories)):
      for y in range(0, 11):
          yList[y] += categories[x].spentotal[y]

  for x in range(0, 11):
      if x == 10:
          finalStr += f'{yList[x]}'
          break;
      finalStr += f'{yList[x]}\n'

  for x in range(0,len(tempNameList)):
      for y in range(0, len(finalNameList)):
          if len(tempNameList[x]) > y:
              finalNameList[y] += f'  {tempNameList[x][y]}'
          else:
              finalNameList[y] += '   '

  finalStr += f'\n{dashes}\n'

  for x in range(0,len(finalNameList)-1):
      finalStr +=  finalNameList[x] + '  \n'

  finalStr += finalNameList[-1] + '  '

  print(finalNameList[-1])

  return finalStr
