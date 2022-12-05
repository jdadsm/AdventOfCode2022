def main():
    with open('Day4/input.txt','r') as sc:
        input = sc.readlines();

    count = 0
    for line in input:
        pairs = line.removesuffix("\n").split(",")
        first = pairs[0].split("-")
        second = pairs[1].split("-")
        if int(first[0])<=int(second[0]) and int(first[1])>=int(second[1]):
            count += 1
        elif int(first[0])>=int(second[0]) and int(first[1])<=int(second[1]):
            count += 1
    print(count)

if __name__ == "__main__":
    main()    