def main():
    with open('Day10/input.txt','r') as sc:
        input = sc.readlines();
        
    cycle_counter = 1
    x = 1
    drawing = ""
    for line in input:
        line = line.split(" ")
        if len(line) == 1:
            if x-1 <= cycle_counter-1 <= x+1:
                drawing+="#"
            else:
                drawing+="." 
            cycle_counter+=1
        else: 
            if x-1 <= cycle_counter-1 <= x+1:
                drawing+="#"
            else:
                drawing+="." 
            cycle_counter+=1 
            if cycle_counter == 40:
                cycle_counter = 0
            if x-1 <= cycle_counter-1 <= x+1:
                drawing+="#"
            else:
                drawing+="." 
            cycle_counter+=1
            x+=int(line[1]) 
        if cycle_counter == 40:
            cycle_counter = 0
    
    res = []
    i = 0
    j = 40
    while len(drawing)>j:
        res.append(drawing[i:j])
        i+=40
        j+=40
    res.append(drawing[i:])
    
    for line in res:
        print(line)
if __name__ == "__main__":
    main()    