def main():
    highest_calorie = 0
    temp_calorie = 0
    with open('Day1/input.txt','r') as sc:
        input = sc.readlines();

    for line in input:
        if line == "":
            pass
        elif line == "\n":
            if highest_calorie<temp_calorie:
                highest_calorie = temp_calorie
            temp_calorie = 0            
        else:
            temp_calorie += int(line)
    print(highest_calorie)

if __name__ == "__main__":
    main()        