def main():
    temp_calorie = 0
    with open('Day1/input.txt','r') as sc:
        input = sc.readlines();

    calories_list = []
    for line in input:
        if line == "":
            pass
        elif line == "\n":
            calories_list.append(temp_calorie)
            temp_calorie = 0            
        else:
            temp_calorie += int(line)
    calories_list.sort()
    print(calories_list[-1]+calories_list[-2]+calories_list[-3])

if __name__ == "__main__":
    main()        