class Node():
    def __init__(self,x,next):
        self.x = x
        self.next = next
class LSS():
    def __init__(self):
        self.start = None
        self.end = None
    def AddNumber_first(self,x):
        self.start = Node(x, self.start)
        if self.end == None:
            self.end = self.start
    def AddNumber_last(self,x):
        if self.start == None:
            self.AddNumber_first(x)
        else:
            p = self.end
            p.next = Node(x, None)
            self.end = p.next
    def Delete_first(self):
        self.start = self.start.next
        if self.start == None:
            self.end = None
    def Delete_last(self):
        if self.end == self.start:
            self.Delete_first(self)
        p = self.start
        while p.next.next != None:
            p = p.next
        p.next = None
    def Read(self):
        if self.start == None:
            print('Empty...')
            return
        else:
            p = self.start
            while p != None:
                print(p.x, end = '\n')
                p = p.next
            print('--END--')
             
zoznam = LSS()
zoznam.AddNumber_first(20)
zoznam.AddNumber_last(78)
zoznam.AddNumber_first(10)
zoznam.AddNumber_last(45)
zoznam.Delete_first()
zoznam.Delete_last()
zoznam.Read()
