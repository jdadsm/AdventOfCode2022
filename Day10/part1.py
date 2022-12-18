def main():
    with open('Day10/input.txt','r') as sc:
        input = sc.readlines();
        
    cycle_counter = 1
    x = 1   
    signal_strengths = []
    interesting_cycle = 20
    for line in input:
        line = line.split(" ")
        if len(line) == 1:
            cycle_counter+=1
            if cycle_counter == interesting_cycle:
                signal_strengths.append(cycle_counter*x)
                interesting_cycle+=40
        else: 
            cycle_counter+=1
            if cycle_counter == interesting_cycle:
                signal_strengths.append(cycle_counter*x)
                interesting_cycle+=40    
            x+=int(line[1]) 
            cycle_counter+=1 
            if cycle_counter == interesting_cycle:
                signal_strengths.append(cycle_counter*x)
                interesting_cycle+=40
    print(sum(signal_strengths))
if __name__ == "__main__":
    main()    