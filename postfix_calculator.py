
import sys

def operation(a,b,symbol):
    if symbol == "+":
        return a+b
    if symbol == "-":
        return a-b
    if symbol == "*":
        return a*b
    if symbol == "/":
        return a//b
    
def calculate(data):
    data = data.strip().split()
    
    ops = ["+","-","/","*"]
    index_list = []
    for i in range(len(data)):
        for j in range(len(ops)):
            if data[i] == ops[j]:
                index_list.append(i)
    
    while True:
        try:
            answer =(operation(int(data[min(index_list)-2]),int(data[min(index_list)-1]),data[min(index_list)]))
        
        
            data[min(index_list)] = answer
            data.pop(min(index_list)-1)
            data.pop(min(index_list)-2)
            index_list.pop(0)
            
            
            if len(index_list) == 0:
                ans = data[0]
                return ans
                break

            for i in range(len(index_list)):
                index_list[i] -= 2
                
        except Exception as e:
            if type(e) == ZeroDivisionError:
                return "Zero division"
            else: 
                print
                return "Malformed expression"
    
    
for line in sys.stdin:
    if len(line.strip().split()) > 0:
        print(calculate(line))

