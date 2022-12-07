from system import *

def main():
    with open('Day7/input.txt','r') as sc:
        input = sc.readlines();

    curr_dir = None
    root = Dir(None,"/")
    
    for i in range(len(input)):
        string = input[i].removesuffix("\n").split(" ")
        if string[0] == "$":
            if string[1] == "cd":
                if string[2] == "/":
                    curr_dir = root
                elif string[2] == "..":
                    curr_dir = curr_dir.root
                else:
                    for dir in curr_dir.dirs:
                        if dir.name == string[2]:
                            curr_dir = dir
                            break
            elif string[1] == "ls":
                continue
        elif string[0] == "dir":
            curr_dir.add_dir(Dir(curr_dir,string[1]))
        else:
            curr_dir.add_file(File(input[i].removesuffix("\n")))
    
    print(getSum(root))
        
def getSum(root_dir):        
    sum = 0
    if root_dir.dir_size() <= 100000:
        sum += root_dir.dir_size()
    for dir in root_dir.dirs:
        sum += getSum(dir)
    return sum
    
if __name__ == "__main__":
    main()    