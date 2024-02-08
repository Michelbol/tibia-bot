from tkinter import *
from program import Program
from views.preview_config import PreviewConfig
from macros.auto_eat import AutoEat
from macros.auto_healer import AutoHealer
from macros.auto_printer import AutoPrinter

class MainView:

    view = None


    def configureAutoEat(self):
        self.program.settings['autoEat'] = self.enableAutoEat.get()

    def configureAutoAttack(self):
        self.program.settings['autoAttack'] = self.enableAutoAttack.get()

    def configureAutoHealing(self):
        self.program.settings['autoHealing'] = self.enableAutoHealing.get()
    
    def configureAutoLoot(self):
        self.program.settings['autoLoot'] = self.enableAutoLoot.get()

    def execute(self):
        self.program = Program()
        previewConfig = PreviewConfig()
        view = Tk()
        view.geometry('800x600')
        view.title('Tibia bot')

        start = Label(view, text='Configure seu bot antes de iniciar o programa')
        start.grid(column=0, row=0, padx=0, pady=0)

        printHotkeyLabel = Label(view, text="PrintScreenHotkey: "+str(AutoPrinter.HOTKEY_TO_PRINT))
        printHotkeyLabel.grid(column=2, row=0, padx=0, pady=0)

        startButton = Button(view, text="Iniciar Bot", command=self.program.start)   
        startButton.grid(column=0, row=5)

        showViewConfiguration = Button(view, text="Configurações do Bot", command=previewConfig.preview)
        showViewConfiguration.grid(column=1, row=5)

        showViewConfiguration = Button(view, text="Start CaveBot", command=self.program.startCaveBot)
        showViewConfiguration.grid(column=2, row=5)

        self.enableAutoEat = BooleanVar()
        checkboxAutoEat = self.createCheckbox(view, 'Enable AutoEat('+str(AutoEat.hotkeyToEat)+')', self.enableAutoEat, self.configureAutoEat)
        checkboxAutoEat.grid(column=0,row=1)


        self.enableAutoAttack = BooleanVar()
        checkboxAutoAttack = self.createCheckbox(view, 'Enable AutoAttack', self.enableAutoAttack, self.configureAutoAttack)
        checkboxAutoAttack.grid(column=1,row=1)

        self.enableAutoHealing = BooleanVar()
        checkboxAutoHealing = self.createCheckbox(view, 'Enable AutoHealing(Mana:'+str(AutoHealer.hotkeyToFillMana)+' Life:'+str(AutoHealer.hotkeyToHealLife)+')', self.enableAutoHealing, self.configureAutoHealing)
        checkboxAutoHealing.grid(column=2,row=1)

        self.enableAutoLoot = BooleanVar()
        checkboxAutoLoot = self.createCheckbox(view, 'Enable AutoLoot', self.enableAutoLoot, self.configureAutoLoot)
        checkboxAutoLoot.grid(column=3,row=1)
        view.mainloop()

    def createCheckbox(self, view, title, var, command):
        return Checkbutton(view, text=title,variable=var, onvalue=True, offvalue=False, command=command)