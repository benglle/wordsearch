from random import randint, choice
from colorama import Fore

class wordsearch:

    def __init__(self,words,difficulty,dev):
        self.words = words
        self.difficulty = difficulty
        self.dev = dev
        
    def get_words(self):
        i, words = 0, []
        if self.dev==True:
            words = ["TESTING" for x in range(5)]
        else:
            print("enter 'i' to stop")
            while True:
                f=False
                w = input(f"enter word number {i+1}: ")
                if w=="i" and i>1: break
                elif f==False and w != "": 
                    words.append(w)
                    i+=1
        return words

    def validate_pos(self,arr,set):
        j=False
        for s in set:
            if s in arr:
                j=True
                break
        if j: return False
        else: return True

    def get_difficulty(self):
        if self.difficulty != None:
            reverse = randint(1,100)
            if 10*self.difficulty > reverse:
                return True
            else: return False

    def construct(self):
        if self.words == None: words = self.get_words()
        t = [len(j) for j in words]
        t.sort()
        total=0
        for a in t:
            total+=a
        longest_word = max(words,key=len)
        dimension = round(len(longest_word)*1.2+(total/len(words)+len(words)/2))
        alphabet = [a for a in "abcdefghijklmnopqrstuvwxyz"]
        table = [[] for m in range(dimension)]
        for t in table:
            for c in range(dimension):
                t.append(choice(alphabet))
        arr=[]
        for w in words:
            c=choice(["x","y","xy","yx"])#x = -, y = |, xy = \, yx = /
            f=True
            f1=True
            while f: #find a valid pos to place word on table
                l = len(w)
                diff = self.get_difficulty()
                while f1:
                    x=randint(0,dimension-1)
                    y=randint(0,dimension-1)
                    if c=="x" or c=="y" or c=="xy":
                        if x+l < dimension and y+l < dimension:
                            f1=False
                    elif c=="yx":
                        if x+l < dimension and y-l > 0:
                            f1=False
                f1=True
                set = []
                if c=="x":
                    for z in range(l):
                        pos = (x+z,y)
                        set.append(pos)
                    if self.validate_pos(arr,set): 
                        f=False
                        for z in range(l):
                            if diff: table[y][x+z] = w[-(z+1)]
                            else: table[y][x+z] = w[z]
                if c=="y":
                    for z in range(l):
                        pos = (x,y+z)
                        set.append(pos)
                    if self.validate_pos(arr,set): 
                        f=False
                        for z in range(l):
                            if diff: table[y+z][x] = w[-(z+1)]
                            else: table[y+z][x] = w[z]
                if c=="xy":
                    for z in range(l):
                        pos = (x+z,y+z)
                        set.append(pos)
                    if self.validate_pos(arr,set): 
                        f=False
                        for z in range(l):
                            if diff: table[y+z][x+z] = w[-(z+1)]
                            else: table[y+z][x+z] = w[z]
                if c=="yx":
                    for z in range(l):
                        pos = (x+z,y-(z+1))
                        set.append(pos)
                    if self.validate_pos(arr,set): 
                        f=False
                        for z in range(l):
                            if diff: table[y-(z+1)][x+z] = w[-(z+1)]
                            else: table[y-(z+1)][x+z] = w[z]
            for s in set:
                arr.append(s)
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
table = wordsearch(None,5,False)#difficulty between 1 - 10, increases chances of reverse
myTable = table.construct()
print_table(myTable)
