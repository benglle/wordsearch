from multiprocessing.sharedctypes import Value
import random as r
from colorama import Fore

class wordsearch:
    
    def __init__(self,difficulty,dimension,words,dev):
        self.difficulty = difficulty
        self.dimension = dimension
        self.words = words
        self.dev = dev
        
    def pquery(self):
        if self.dev == True:
            return ["TESTING" for x in range(5)]
        else:
            words = []
            try:
                n = int(input("n of words: "))
                if n < 1 or n >= self.dimension/2: self.pquery()
            except ValueError:
                print("you need to input an integer")
                self.pquery()
            for i in range(n):
                word = input(f"Word number {i+1}: ")
                words.append(word)
            return words

    def check_difficulty(self):
        if self.difficulty != None:
            reverse = r.randint(1,100)
            if 10*self.difficulty > reverse:
                return True
            else: return False
        #add diagonal gen chances based off increased difficulty
    
    def validate_pos(self, x, y, d, di, arr):
        print("I HAVE BEEN CALLED")
        w = d/2
        if w%2 != 0:
            w+=0.5
        w=int(w)
        v1,e1 = (x-w),(y-w)
        flag = False
        if di == "x":
            lst = []
            for c in range(d):
                lst.append(((v1+c),y))
        elif di == "y":
            lst = []
            for c in range(d):
                lst.append((x,(e1+c)))
        new_lst = []
        for a in arr:
            for x in a:
                new_lst.append(x)
        for y in lst:
            if y in new_lst:
                flag = True
        if flag == True: return False
        else: return True

    def construct_table(self):
        table = [[] for x in range(self.dimension)]
        alphabet = [j for j in "abcdefghijklmnopqrstuvwxyz"]#upper()
        for t in table:
            for c in range(self.dimension):
                t.append(r.choice(alphabet))
        n = self.dimension
        arr=[]
        if self.words == None:
            words = self.pquery()
        for w in words:
            direction = r.choice(["x","y"])
            found = False
            while found==False:
                x=y=r.randint(0,n)
                d = len(w)/2
                if d%2 != 0:
                    d+=0.5
                d=int(d)
                v1,v2 = (x-d),(x+d)
                e1,e2 = (y-d),(y+d)
                if direction=="x":
                    if v1 >= 0 and v2 <= n:
                        g = self.validate_pos(x,y,len(w),direction,arr)
                        if g == True: found = True
                if direction=="y":
                    if e1 >= 0 and e2 <= n:
                        g = self.validate_pos(x,y,len(w),direction,arr)
                        if g == True: found = True
            if direction=="x":
                a = self.check_difficulty()
                lst = []
                for c in range(len(w)):
                    if a: table[y][v1+c] = w[-(c+1)]
                    else: table[y][v1+c] = w[c]
                    pos=(v1+c,y)
                    lst.append(pos)
                arr.append(lst)
            if direction=="y":
                a = self.check_difficulty()
                lst = []
                for c in range(len(w)):
                    if a: table[e1+c][x] = w[-(c+1)]
                    else: table[e1+c][x] = w[c]
                    pos=(x,(e1+c))
                    lst.append(pos)
                arr.append(lst)

        return table
def print_table(table):
    for t in table:
        for x in t:
            if x.isupper():
                print(Fore.RED + f"{x}  ",end='')
            else:
                print(Fore.BLUE + f"{x}  ",end='')
        print()
    print("\n\n")

myTable = wordsearch(5,20,None,True)
table = myTable.construct_table()
print_table(table)
