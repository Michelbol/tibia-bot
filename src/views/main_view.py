from tkinter import *
from program import Program
from views.preview_config import PreviewConfig

class MainView:

    view = None

    def execute(self):
        program = Program()
        previewConfig = PreviewConfig()
        view = Tk()
        view.geometry('400x400')
        view.title('Tibia bot')
        something = Entry(view)
        something.grid(column=0,row=2)
        start = Label(view, text='Configure seu bot antes de iniciar o programa')
        start.grid(column=0, row=0, padx=0, pady=0)
        startButton = Button(view, text="Iniciar Bot", command=program.start)   
        startButton.grid(column=0, row=1)

        showViewConfiguration = Button(view, text="Configurações do Bot", command=previewConfig.preview)
        showViewConfiguration.grid(column=0, row=2)
        view.mainloop()
        