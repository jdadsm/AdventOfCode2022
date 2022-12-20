import math
import numpy

def main():
    with open('Day11/input.txt','r') as sc:
        input = sc.readlines();

    rounds = 10000
    
    monkeys = []
    
    temp_items = []
    temp_op = []
    temp_test = []
    for line in input:
        if line.find("Starting items:")!=-1:
            temp_items = line.strip().removeprefix("Starting items:").removesuffix("\n").split(",")
            temp_items = [eval(i) for i in temp_items]
        elif line.find("Operation:")!=-1:
            line = line.strip().removeprefix("Operation:").removesuffix("\n")
            if line.find("*")!=-1:
                temp_op.append("*")
                line = line.split("*")
                if line[-1]==(" old"):
                    temp_op.append("old")
                else:
                    temp_op.append(int(line[-1]))
            elif line.find("+")!=-1:
                temp_op.append("+")
                line = line.split("+")
                if line[-1]==(" old"):
                    temp_op.append("old")
                else:
                    temp_op.append(int(line[-1]))
            else:
                print("Operator not found")
        elif line.find("Test:")!=-1:
            temp_test.append(int(line.split(" ")[-1]))
        elif line.find("If")!=-1:
            temp_test.append(int(line.split(" ")[-1]))
        if len(temp_test) == 3:
            monkeys.append(Monkey(temp_items,temp_op,temp_test))
            temp_items = []
            temp_op = []
            temp_test = []
    
    modulo = 1
    for monkey in monkeys:
        modulo = modulo * monkey.test[0]
        
    for i in range(rounds):
        if i == 20:
            print(20)
        if i%100==0:
            print(i)
        for monkey in monkeys:
            i = 0
            length = len(monkey.items)
            if length == 0:
                continue
            while True:
                if i == length:
                    break
                monkey.items[0] = operation(monkey.op,monkey.items[0],modulo)
                monkey.inspections += 1
                throw_to = test(monkey.test,monkey.items[0])
                monkeys[throw_to].items.append(monkey.items.pop(0))
                i += 1
    
    monkeys.sort(key = lambda monkey:monkey.inspections)
    print(monkeys[-1].inspections*monkeys[-2].inspections)

def operation(monkey_op,item,modulo):
    if type(monkey_op[1]) == str:
        if monkey_op[0] == "+":
            item = item*2
        else:
            item = item*item
    else:
        if monkey_op[0] == "+":
            item += monkey_op[1]
        else:
            item = item*monkey_op[1]
    return item%modulo

def test(monkey_test,item):
    if item % monkey_test[0] == 0: 
            return monkey_test[1]
    return monkey_test[2]
    
class Monkey:
    def __init__(self,items,op,test):
        self.items = items
        self.op = op
        self.test = test
        self.inspections = 0
                
if __name__ == "__main__":
    main()  