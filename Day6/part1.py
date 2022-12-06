def main():
    with open('Day6/input.txt','r') as sc:
        input = sc.readlines();
    input = input[0]
    marker = False
    n = 3
    index = 3
    while not marker:
        temp = 0
        while temp<n:
            if input[index-temp] in input[index-n:index-temp]:
                break
            else:
                temp += 1
                if temp == n:
                    marker = True
            
        index+=1
    print(index)

if __name__ == "__main__":
    main()    