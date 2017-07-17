import random

class Player:
  def __init__(self,num,name,coin):
    self.num = num
    self.name = name
    self.coin = coin
    self.card = []
  def noThanks(self):
    self.coin -= 1
  def takeIt(self,nowCoin,nowCard):
    self.coin += nowCoin
    self.card.append(nowCard)
  def getScore(self):
    score = 0
    self.card.sort()
    nCard = list(self.card)
    while nCard != []:
      cur = nCard[0]
      isDone = True
      for i in range(len(nCard)):
        if cur+i != nCard[i]:
          score += cur
          nCard = nCard[i:]
          isDone = False
          break
      if isDone:
        score += cur
        break
    score -= self.coin
    return score

class Board:

  def __init__(self):
    self.deck = list(range(3,36))
    self.p = [Player(0,"test",0)]

  def getNextPlayer(self):
    if self.nowPlayer + 1 > self.numOfPlayer:
      return int((self.nowPlayer+1)%self.numOfPlayer)
    return self.nowPlayer+1

  def setNextPlayer(self):
    self.nowPlayer = self.getNextPlayer()

  def checkCon(self):
    if self.nowCard-1 in self.p[self.nowPlayer].card or \
      self.nowCard + 1 in self.p[self.nowPlayer].card:
      return True
    return False

  def comAction(self):
    com = self.p[self.nowPlayer]
    self.showStatus()
    if com.coin == 0:
      com.takeIt(self.nowCoin,self.nowCard)
      self.nowCoin = 0
      self.nowCard = self.openCard()
    else:
      if self.checkCon():
        com.takeIt(self.nowCoin,self.nowCard)
        self.nowCoin = 0
        self.nowCard = self.openCard()
      else:
        if self.nowCard < 15:
          com.takeIt(self.nowCoin,self.nowCard)
          self.nowCoin = 0
          self.nowCard = self.openCard()
        else:
          com.noThanks()
          self.nowCoin += 1

  def ready(self,numOfPlayer,eachCoins,exceptCards):

    self.numOfPlayer = numOfPlayer
    self.exceptCards = exceptCards
    nowPlayer, nowCoin, nowCard, exceptCards = 0, 0, 0, 0
    for i in range(1, numOfPlayer + 1):
      self.p.append(Player(i, "test", eachCoins))

    self.nowPlayer = 1
    self.nowCoin = 0
    self.nowCard = 0

    # 카드 순서 초기화 및 설정
    # 3~35의 숫자 배열 중 exceptCards개를 랜덤으로 제거하고, 그걸 다시 랜덤으로 배열
    for i in range(self.exceptCards):
      r = random.randrange(33 - i)
      self.deck.pop(r)
    random.shuffle(self.deck)
    self.nowCard = self.openCard()

  def showStatus(self):
    print("\n=== Now Player: %d ===" %(self.nowPlayer))
    print("Now Card: %d   Now Coin: %d   Card Remain: %d" % (self.nowCard, self.nowCoin, len(self.deck)))
    for i in range(1,self.numOfPlayer+1):
      print("[P%d] coin: %d, card: %s, score: %d" %(i,self.p[i].coin,sorted(self.p[i].card),self.p[i].getScore()))

  def playerAction(self):
    pl = self.p[self.nowPlayer]
    self.showStatus()

    try:
      c = int(input("Choose your action. (1: No Thanks, 2: Take It)\n"))
    except:
      print("Oops!  That was no valid number.  Try again...\n")
    if pl.coin == 0:
      print("You don't have any coin. You must take this card.")
      c = 2

    if c == 1:
      pl.noThanks()
      self.nowCoin += 1
    else:
      pl.takeIt(self.nowCoin,self.nowCard)
      self.nowCoin = 0
      self.nowCard = self.openCard()

  def action(self):
    """
    if self.nowPlayer == 1:
      self.playerAction()
    else:
      self.comAction()
    """
    self.comAction()
    #input()
    self.nowPlayer = self.getNextPlayer()

  def openCard(self):
    return self.deck.pop(0)

  def calScore(self):
    winner = 0
    minScore = 987654321
    for n in range(1,self.numOfPlayer+1):
      if minScore > self.p[n].getScore():
        minScore = self.p[n].getScore()
        winner = n
    return winner

class Game:
  def __init__(self,numOfGames):
    self.numOfGames = numOfGames
  def start(self):
    b = Board()
    b.ready(5, 7, 6)
    while b.deck != []:
      b.action()
    # 결과 얻는 루틴
    winner = b.calScore()

    print("Winner is %d" %winner)

"""
g = Game(1)
g.start()
"""

