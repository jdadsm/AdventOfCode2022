def main():
    with open('Day8/input.txt','r') as sc:
        input = sc.readlines();

    for i in range(len(input)):
        input[i] = input[i].removesuffix("\n")
        
    size = len(input[0])
    highest_scenic_score = 0
    for i in range(1,size-1):
        for j in range(1,size-1):
            height = input[i][j]
            temp = check_left(input,i,j,height)*check_right(input,i,j,size,height)*check_up(input,i,j,height)*check_down(input,i,j,size,height)
            if temp > highest_scenic_score:
                highest_scenic_score = temp
    print(highest_scenic_score)

def check_left(input,i,j,height):
    for x in range(j-1,-1,-1):
        if input[i][x] >= height:
            break
    return j-x

def check_right(input,i,j,size,height):
    for x in range(j+1,size):
        if input[i][x] >= height:
            break
    return x-j

def check_up(input,i,j,height):
    for y in range(i-1,-1,-1):
        if input[y][j] >= height:
            break
    return i-y

def check_down(input,i,j,size,height):
    for y in range(i+1,size):
        if input[y][j] >= height:
            break
    return y-i

if __name__ == "__main__":
    main()    