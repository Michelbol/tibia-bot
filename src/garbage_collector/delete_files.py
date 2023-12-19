import os

class DeleteFiles:

    def deleteFilesInFolder(path):
        dir = os.listdir(path) 
        for file in dir:
            if(file == '.gitkeep'):
                continue
            os.remove(path+file)


    def deleteFilesInFolderButNotLastOne(path):
        dir = os.listdir(path) 
        for file in dir:
            if(file == '.gitkeep'):
                continue
            if(file == sorted(dir)[-1]):
                continue
            os.remove(path+file)