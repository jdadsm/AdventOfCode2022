def main():
    with open('Day3/input.txt','r') as sc:
        input = sc.readlines();
    
    sum = 0
    for rucksack in input:
        first_compartiment = rucksack.removesuffix("\n")[:int(len(rucksack)/2)]
        second_compartiment = rucksack.removesuffix("\n")[int(len(rucksack)/2):]
        for item in first_compartiment:
            if item in second_compartiment:
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