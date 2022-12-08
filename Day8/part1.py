def main():
    with open('Day8/input.txt','r') as sc:
        input = sc.readlines();

    for i in range(len(input)):
        input[i] = input[i].removesuffix("\n")
        
    size = len(input[0])
    visible = size*4 - 4
    
    for i in range(1,size-1):
        for j in range(1,size-1):
            height = input[i][j]
            if i > size//2:
                if j > size//2:
                    if check_right(input,i,j,size,height):
                        visible += 1
                        continue
                    if check_down(input,i,j,size,height):
                        visible += 1
                        continue
                    if check_up(input,i,j,height):
                        visible += 1
                        continue
                    if check_left(input,i,j,height):
                        visible += 1
                        continue
                else:
                    if check_left(input,i,j,height):
                        visible += 1
                        continue
                    if check_down(input,i,j,size,height):
                        visible += 1
                        continue
                    if check_up(input,i,j,height):
                        visible += 1
                        continue
                    if check_right(input,i,j,size,height):
                        visible += 1
                        continue
            else:
                if j > size//2:
                    if check_up(input,i,j,height):
                        visible += 1
                        continue
                    if check_right(input,i,j,size,height):
                        visible += 1
                        continue
                    if check_left(input,i,j,height):
                        visible += 1
                        continue
                    if check_down(input,i,j,size,height):
                        visible += 1
                        continue
                else:
                    if check_up(input,i,j,height):
                        visible += 1
                        continue
                    if check_left(input,i,j,height):
                        visible += 1
                        continue
                    if check_down(input,i,j,size,height):
                        visible += 1
                        continue
                    if check_right(input,i,j,size,height):
                        visible += 1
                        continue
    print(visible)

def check_left(input,i,j,height):
    for x in range(j):
        if input[i][x] >= height:
            return False
    return True

def check_right(input,i,j,size,height):
    for x in range(j+1,size):
        if input[i][x] >= height:
            return False
    return True

def check_up(input,i,j,height):
    for y in range(i):
        if input[y][j] >= height:
            return False
    return True

def check_down(input,i,j,size,height):
    for y in range(i+1,size):
        if input[y][j] >= height:
            return False
    return True

if __name__ == "__main__":
    main()    