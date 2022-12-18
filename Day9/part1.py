import math

def main():
    with open('Day9/input.txt','r') as sc:
        input = sc.readlines();
    curr_pos_head = [0,0]
    tail = Tail([0,0])
    visited = {}
    visited[str(tail.coord)] = 1
    for line in input:
        line = line.removesuffix("\n").split(" ")
        direction = line[0]
        times = line[1]
        for i in range(int(times)):
            if direction == "U":
                curr_pos_head[1] += 1
            elif direction == "D":
                curr_pos_head[1] -= 1
            elif direction == "R":
                curr_pos_head[0] += 1
            elif direction == "L":
                curr_pos_head[0] -= 1
            tail.update_coord(curr_pos_head)
            if str(tail.coord) not in visited:
                visited[str(tail.coord)] = 1
    
    
    print(len(visited.keys()))

class Tail:
    def __init__(self,coord):
        self.coord = coord
    
    def update_coord(self,head_coords):
        updated = False
        if abs(self.coord[0]-head_coords[0]) > 1:
            updated = True
            if self.coord[0] > head_coords[0]:
                self.coord = [head_coords[0]+1,head_coords[1]]
            else:
                self.coord = [head_coords[0]-1,head_coords[1]]
        if abs(self.coord[1]-head_coords[1]) > 1:
            updated = True
            if self.coord[1] > head_coords[1]:
                self.coord = [head_coords[0],head_coords[1]+1]
            else:
                self.coord = [head_coords[0],head_coords[1]-1]
        return updated
        
if __name__ == "__main__":
    main()    