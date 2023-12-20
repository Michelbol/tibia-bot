

class AutoLoot:

    def __init__(self, player) -> None:
        self.player = player
    def loot(self):
        if(self.player.killMonster()):
          print('a')
