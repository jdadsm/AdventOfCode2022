class Dir:
    def __init__(self,root,name):
        self.root = root
        self.name = name
        self.dirs = []
        self.files = []
        
    def add_dir(self,dir):
        self.dirs.append(dir)

    def add_file(self,file):
        self.files.append(file)        
        
    def dir_size(self):
        size = 0
        for dir in self.dirs:
            size += dir.dir_size()
        for file in self.files:
            size += file.size
        return size
    
class File:
    def __init__(self,filestring):
        file = filestring.split(" ")
        size,filename = file[0],file[1]
        self.filename = filename
        self.size = int(size)
    