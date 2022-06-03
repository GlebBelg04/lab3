import configparser
from dataclasses import dataclass
@dataclass
class Player:
    id: int
    name: str

@dataclass
class PlayerMobile(Player):
    os:str
player1=Player(101,"Vasya")
player2=PlayerMobile(101,"Vasya","Android")
print(player1)
print(player2)
 #-------------------------------------------------
test = configparser.ConfigParser()
test.read('test.ini')

print(test['DEFAULT']['NAME'])

print(test['DEFAULT']['AGE'])

print(test['BASE']['IP'])

#---------------------------------------------------
import pickle

class NAME():
    def __init__(self):
        self.info = OtherClass(option=1)

        @staticmethod
        def unpickle():
            with file('test.ini', 'rb') as f:
                return pickle.load(f)
    data = NAME.unpickle()

    def pickle(self):
        f = file('test.ini', 'wb')
        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        f.close()

    def unpickle(self):
        f = file('test.ini', 'rb')
        pickle.load(f)
        f.close()


class OtherClass():
    def __init__(self, option):
        self.property = option * 2


mydata = NAME(option=5)

mydata.pickle()
