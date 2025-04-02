import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import random
import pandas as pd

colours=pd.read_csv("garden4.csv", header = None)
terrain = colours.to_numpy()

def flipCoords(rcpos,LIMITS):
    y = rcpos[0]
    x = rcpos[1]
    return (x,y)

class Ant():
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.age = 0
        self.lifecycleant()        

    def lifecycleant(self):
        self.age += 1
        self.size = 0.5
        self.colour = "black"
        self.latest_move = None  # Store the last move made by the ant
        self.latest_pos = None  # Store the previous position

        age = self.age

        if -1 <= age <= 4:
            self.size = 0.15
            self.colour = "red"
        elif 5 <= age <= 15:
            self.size = 0.35
            self.colour = "orange"
        elif age <= 30:
            self.size = 0.5
            self.colour = "brown"

    def getPos(self):
        return self.pos
    
    
    def dead_End(self, move):
        new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])

        if (45 <= new_pos[0] <= 77) and (0 <= new_pos[1] <= 103):
            terrain_value = terrain[new_pos]
            if terrain_value == 1:
                terrain[new_pos] = 0
                return True

        return False

    def stepChange(self):
        validMoves = [(1,0), (-1,0), (0,1), (0,-1), (0,0)]

        if self.latest_pos:
            tunnel_move = (self.latest_pos[0] - self.pos[0], self.latest_pos[1] - self.pos[1])
            if tunnel_move in validMoves:
                validMoves.remove(tunnel_move)

        if len(validMoves) > 0:
            move = random.choice(validMoves)

            if self.dead_End(move):
                # If it's a dead end, the move is already handled
                return

            new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])

            while not (((new_pos[0]) <= 77 and (new_pos[0]) >= 45) and
                       ((new_pos[1]) <= 103 and (new_pos[1]) >= 0) and
                       (terrain[new_pos] == 0)):
                move = random.choice(validMoves)

                if self.dead_End(move):
                    # If it's a dead end, the move is already handled
                    return

                new_pos = (self.pos[0] + move[0], self.pos[1] + move[1])

            self.latest_pos = self.pos
            self.latest_move = move
            self.pos = new_pos

    def dig(self, terrain):
        p , q = self.pos
        if terrain[p,q] == 1:
            terrain[p,q]== 0

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

class Butterfly1():
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.size = 0.8
        self.target_pos = None  
        self.colour = "orange"      

    def getPos(self):
        return self.pos
    
    def stepChange(self,subgrid):
        validMoves = [(1,-1),(1,1),(-1,1),(-1,-1),(1,0), (-1,0), (0,1), (0,-1), (0,0)]
        print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            while not(((self.pos[0] + move[0])<=38 and (self.pos[0] + move[0])>=5) and ((self.pos[1] + move[1])<=60 and (self.pos[1] + move[1])>=0)):
                move = random.choice(validMoves)
                print("error")
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])

    def avoidRain(self):
        validMoves = [(1,0),(2,0),(1,1),(1,-1),(0,0)]
        print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            while not(((self.pos[0] + move[0])<=38 and (self.pos[0] + move[0])>=5) and ((self.pos[1] + move[1])<=60 and (self.pos[1] + move[1])>=0)):
                move = random.choice(validMoves)
                # print("error")
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])

    

    def comingOut(self):
        validMoves = [(-1,0),(-2,0),(0,1),(-1,1),(-1,-1)]
        print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            while not(((self.pos[0] + move[0])<=38 and (self.pos[0] + move[0])>=5) and ((self.pos[1] + move[1])<=60 and (self.pos[1] + move[1])>=0)):
                move = random.choice(validMoves)
                # print("error")
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])
    

    def plotMe(self, ax,LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color = self.colour)
        ax.add_patch(circle1)

class Butterfly2():
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.age = 0
        self.lifecyclebfly()

    def lifecyclebfly(self):
        self.age += 1
        self.size = 0.9
        self.colour = "pink"

        age = self.age

        if 0 <= age <= 3:
            self.size = 0.2
            self.colour = "black"
        elif 4 <= age <= 8:
            self.size = 0.4
            self.colour = "green"
        elif 9<= age <=16:
            self.size =  0.6
            self.colour = "brown"       

    def getPos(self):
        return self.pos

    def stepChange(self,subgrid):
        validMoves = [(1,-1),(1,1),(-1,1),(-1,-1),(1,0), (-1,0), (0,1), (0,-1), (0,0)]
        print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            try:
                while not(((self.pos[0] + move[0])<=40 and (self.pos[0] + move[0])>=15) and ((self.pos[1] + move[1])<=60 and (self.pos[1] + move[1])>=0)):
                    move = random.choice(validMoves)
            except:    
                print("error")
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])

    
    def plotMe(self, ax,LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

class Ladybird():    
    def __init__(self, name, pos):
        self. name = name
        self. pos = pos
        self.age = 0

    def lifecyclelbird(self):
        self.age += 1
        self.size = 0.4
        self.colour = "red"

        age = self.age

        if 0 <= age <= 6:
            self.size = 0.2
            self.colour = "yellow"
        elif 7 <= age <= 12:
            self.size = 0.3
            self.colour = "brown"
        elif 13<= age<= 20:
            self.size = 0.4
            self.colour ="red"

    def getPos (self):
        return self. pos

    def stepChange (self, subgrid):
        validMoves = [(-1,0), (-1,1), (-1,-1), (0,0),(0,1),(0,-1)]
        print (validMoves)
        if len (validMoves)>0:
            move = random. choice (validMoves)
            while not(((self.pos[0]+move[0])>=17 and (self.pos[0]+move[0])<=45) and ((self.pos[1]+move[1])<=95 and (self.pos[1]+move[1])>=70)):
                move = random. choice (validMoves)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)

class Fish():
    size = 1
    
    def __init__(self, name, pos):
        self. name = name
        self. pos = pos
        self.colour = "orange"

    def getPos (self):
        return self. pos

    def stepChange (self, subgrid):
        validMoves = [(1,1), (1,-1), (-1,1), (-1,-1), (0,0)]
        print (validMoves)
        if len (validMoves)>0:
            move = random. choice (validMoves)
            while not(((self.pos[0]+move[0])>=45 and (self.pos[0]+move[0])<=49) and ((self.pos[1]+move[1])<=96 and (self.pos[1]+move[1])>=73)):
                move = random. choice (validMoves)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = patches.Wedge(XYpos, self.size,-30,10, color = self.colour)
        ax.add_patch(circle1)


class Rain():
    def __init__(self, name, pos, colour):
        self.name = name
        self.pos = pos
        self.colour = '#00006699'
        self.size = 0.2

    def getPos(self):
        return self.pos

    def stepChange(self,subgrid,map): 
        validMoves = [(1,0),(2,0),(3,0)]
        print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            newpos = (self.pos[0] + move[0],  self.pos[1] + move[1]) 
            if newpos[0] <= 43 :
                self.pos = newpos
            else:
                newpos = (43,newpos[1]+10)
                if newpos[1] < 90:
                    self.pos = newpos

    def plotMe(self, ax,LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)


class Fruits():
    def __init__(self,name,pos,colour):
        self.name = name
        self.pos = pos
        self.colour = "#FFFF00"
        self.size = 0.3

    def getPos(self):
        return self.pos
    
    def stepChange(self,subgrid):
        validMoves = [(1,-1),(1,1),(-1,1),(-1,-1),(1,0), (-1,0), (0,1), (0,-1), (0,0)]
        print(validMoves)
        if len(validMoves) > 0:
            move = random.choice(validMoves)
            while not(((self.pos[0] + move[0])<=34 and (self.pos[0] + move[0])>=18) and ((self.pos[1] + move[1])<=60 and (self.pos[1] + move[1])>=0)):
                move = random.choice(validMoves)
                print("error")
            self.pos = (self.pos[0] + move[0],  self.pos[1] + move[1])
    
    def plotMe(self, ax, LIMITS):
        XYpos = flipCoords(self.pos, LIMITS)
        circle1 = plt.Circle(XYpos, self.size, color=self.colour)
        ax.add_patch(circle1)
