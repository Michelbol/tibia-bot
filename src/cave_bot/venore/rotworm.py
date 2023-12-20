from cave_bot.walk import Walk

class Rotworm:

    commands = [
        Walk.up,
        Walk.up,
        Walk.left,
        Walk.left,
        Walk.left,
        Walk.left,
        Walk.up,
        Walk.left,
        Walk.up
    ]

    def __init__(self, player) -> None:
        self.walk = Walk()
        self.player = player
        self.active = True
    
    def script(self):
        iteration = 0

        while(self.active):
            if(self.player.attacking == False):
                self.commands[iteration]()
                iteration = iteration+1



    