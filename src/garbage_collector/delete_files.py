import os

class DeleteFiles:

    def deleteFilesInFolder(path):
        dir = os.listdir(path) 
        for file in dir:
            if(file == '.gitkeep'):
                continue
            os.remove(path+file)
