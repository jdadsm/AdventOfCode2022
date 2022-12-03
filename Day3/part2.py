def main():
    with open('Day3/input.txt','r') as sc:
        input = sc.readlines();
    
    sum = 0
    first_rucksacks = []
    second_rucksacks = []
    third_rucksacks = []
    for i in range(int(len(input)/3)):
        first_rucksacks.append(input[i*3].removesuffix("\n"))
        second_rucksacks.append(input[i*3+1].removesuffix("\n"))
        third_rucksacks.append(input[i*3+2].removesuffix("\n"))
    
    for i in range(int(len(input)/3)):
        for item in first_rucksacks[i]:
            if item in second_rucksacks[i] and item in third_rucksacks[i]:
                char_value = ord(item)
                if item.islower():
                    char_value -= 96
                else:
                    char_value -= 38
                sum += char_value
                break
    print(sum)

if __name__ == "__main__":
    main()    