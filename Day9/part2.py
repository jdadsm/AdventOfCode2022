import math

def main():
    with open('Day9/input.txt','r') as sc:
        input = sc.readlines();
    curr_pos_head = [0,0]
    tails = []
    n_tails = 9
    for i in range(n_tails):
        tails.append(Tail([0,0]))
    visited = {}
    visited[str(tails[-1].coord)] = 1
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
            temp_head = curr_pos_head
            for tail in tails:
                if tail.update_coord(temp_head):
                    while tail.update_coord(temp_head):
                        pass
                else:
                    break
                temp_head = tail.coord
            if str(tails[-1].coord) not in visited:
                visited[str(tails[-1].coord)] = 1
    
    print(len(visited.keys()))

class Tail:
    def __init__(self,coord):
        self.coord = coord
    
    def update_coord(self,head_coords):
        updated = False
        distance = math.hypot(self.coord[0]-head_coords[0],self.coord[1]-head_coords[1])
        if distance > 2**(1/2):
            updated = True
            if head_coords[0] == self.coord[0]:
                if head_coords[1] > self.coord[1]:
                    self.coord[1] += 1
                else:
                    self.coord[1] -= 1
            elif head_coords[1] == self.coord[1]:
                if head_coords[0] > self.coord[0]:
                    self.coord[0] += 1
                else:
                    self.coord[0] -= 1
            elif head_coords[0] > self.coord[0] and head_coords[1] > self.coord[1]:
                self.coord = [self.coord[0]+1,self.coord[1]+1]
            elif head_coords[0] > self.coord[0] and head_coords[1] < self.coord[1]:
                self.coord = [self.coord[0]+1,self.coord[1]-1]
            elif head_coords[0] < self.coord[0] and head_coords[1] > self.coord[1]:
                self.coord = [self.coord[0]-1,self.coord[1]+1]
            elif head_coords[0] < self.coord[0] and head_coords[1] < self.coord[1]:
                self.coord = [self.coord[0]-1,self.coord[1]-1]         
        return updated
        
if __name__ == "__main__":
    main()    