class Character:

    def __init__(self) -> None:
        self.maxLife = None
        self.currentLife = None
        self.maxMana = None
        self.currentMana = None
        self.level = None
        self.experience = None
        self.soulPoints = None
        self.capacity = None
        self.speed = None
        self.food = None
        self.stamina = None
        self.magicLevel = None
        self.fist = None
        self.club = None
        self.sword = None
        self.axe = None
        self.distance = None
        self.shielding = None
        self.fishing = None
        self.vocation = None


    def calcLifeByLevel(self):
        if(self.vocation == 'knight'):
            return (self.level-8)*15+185
        if(self.vocation == 'paladins'):
            return (self.level-8)*10+185
        if(self.vocation == 'sorcerer' or self.vocation == 'druid'):
            return self.level*5+185
        return self.level*5+145
    
    def calcManaByLevel(self):
        if(self.vocation == 'paladins'):
            return (self.level-8)*15+90
        if(self.vocation == 'sorcerer' or self.vocation == 'druid'):
            return (self.level-8)*30+90
        # knight and others
        return self.level*5+50