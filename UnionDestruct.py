#function for destructive union of two linked lists

def UnionDestruct(a,b):
    
    if a == None and b == None:
        return None
    else:
        if a == None and b != None:
            element = Prvek(b.x ,None)
        else:
            if b == None and a != None:
                element = Prvek(a.x ,None)
            else: 
                element = Prvek(min(a.x,b.x) ,None)
        
        
    current_element = element
    
    while (a != None) and (b != None):
        
        if a.x < b.x:
            if a.x == current_element.x:
                a = a.dalsi    
            else: 
                current_element.dalsi = Prvek(a.x,None)
                current_element = current_element.dalsi
                a = a.dalsi
                
                
        elif a.x > b.x:
            if b.x == current_element.x:
                b = b.dalsi
            else:
                current_element.dalsi = Prvek(b.x,None)
                current_element = current_element.dalsi
                b = b.dalsi
                
        elif a.x == b.x:
            if a.x != current_element.x:
                    
                current_element.dalsi = Prvek(a.x,None)
                current_element = current_element.dalsi
            a = a.dalsi
            b = b.dalsi
            
    if a == None and b != None:
        while b != None:
    
            if current_element.x < b.x:
                current_element.dalsi = Prvek(b.x, None)
                current_element = current_element.dalsi
            b = b.dalsi
    if a != None and b == None:
        while a!= None:
            if a.x > current_element.x:
                current_element.dalsi = Prvek(a.x, None)
                current_element = current_element.dalsi

            a = a.dalsi         

    return element


