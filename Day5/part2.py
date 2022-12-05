def main():
    with open('Day5/input.txt','r') as sc:
        puzzle_start = ""
        line = ""
        while(line != "\n"):
            puzzle_start += line
            line = sc.readline()
        input = sc.readlines();
    puzzle_start = puzzle_start.removesuffix("\n").split("\n")
    for i in range(len(puzzle_start)):
        temp = []
        j = 1
        while j < len(puzzle_start[i]):
            temp.append(puzzle_start[i][j])
            j += 4
        puzzle_start[i] = temp
    puzzle_start = puzzle_start[:-1]
    
    init_pos = []
    for i in range(len(puzzle_start[0])):
        init_pos.append([])
    
    for i in range(len(puzzle_start)-1,-1,-1):
        for j in range(len(puzzle_start[i])):
            if puzzle_start[i][j] != " ":
                init_pos[j].append(puzzle_start[i][j])
            
    
    for i in range(len(input)):
        input[i] = input[i].split(" ")
        input[i] = (input[i][1],input[i][3],input[i][5])
        
    for line in input:
        temp = []
        for i in range(int(line[0])):
            temp = [init_pos[int(line[1])-1].pop()] + temp
        init_pos[int(line[2])-1] += temp

    res = ""
    for i in range(len(init_pos)):
        res+=(init_pos[i].pop())
    
    print(res)
    
    

if __name__ == "__main__":
    main()    