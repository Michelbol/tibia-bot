from cave_bot.walk import Walk

class SwampTroll:

    commands = [
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.right,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.left,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
        Walk.up,
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