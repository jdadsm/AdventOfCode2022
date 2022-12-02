def main():
    with open('Day2/input.txt','r') as sc:
        input = sc.readlines();
    
    score = 0
    for line in input:
        line = line.removesuffix("\n").split(" ")
        if line[0] == "A": # Rock
            if line[1] == "X": # Lose
                score += 3
            elif line[1] == "Y": # Draw
                score += 3
                score += 1
            elif line[1] == "Z": # Win
                score += 6
                score += 2
        elif line[0] == "B": # Paper
            if line[1] == "X": # Lose
                score += 1
            elif line[1] == "Y": # Draw
                score += 3
                score += 2
            elif line[1] == "Z": # Win
                score += 6
                score += 3
        elif line[0] == "C": # Scissors
            if line[1] == "X": # Lose
                score += 2
            elif line[1] == "Y": # Draw
                score += 3
                score += 3
            elif line[1] == "Z": # Win
                score += 6
                score += 1
    print(score)
if __name__ == "__main__":
    main()        