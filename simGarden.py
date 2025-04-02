import matplotlib.pyplot as plt
import numpy as np
from GardenFinal import *
import pandas as pd
import matplotlib.patches as patches

def getSubgrid(t, pos):
    rmin = pos[0]-1
    rmax = pos[0]+2
    cmin = pos[1]-1
    cmax = pos[1]+2
    print(rmin, rmax, cmin, cmax)
    sub = t[rmin:rmax,cmin:cmax]
    return sub

try:
    colours=pd.read_csv("garden4.csv", header = None)
    terrain = colours.to_numpy()
except:
    print("Invalid")

def main():
    LIMITS = (terrain.shape)
    print("\nWelcome to the Secret Garden...\n")
    antinput = input("Enter the number of ants you want(number between 0-20)...")
    bflyinput = input("Enter the number of Butterflies you want(number between 0-5)...")
    bfly1input = input("Enter the number of Butterflies[1] you want(number between 0-10)...")
    ladybirdinput = input("Enter the number of Ladybirds you want(number between 0-10)...")
    fishinput = input("Enter the number of Fish you want(number between 0-10)...")
    print("LIMITS ARE:",LIMITS)
    plt.figure(figsize=(10,10))
    ax = plt.axes()
    ax.set_aspect("equal")

    #terrain = np.zeros(LIMITS)
    ants=[]
    fishes=[]
    rainds=[]
    

    
    x0s=[]
    y0s=[]
    for i in range(terrain.shape[0]):
        for j in range(terrain.shape[1]):
            if terrain[i,j] == 0:
                x0s.append(i)
                y0s.append(j)

    
    b10x = []
    b10y = []
    for t in range(42):
        for v in range(72):
            if (terrain[t,v] == 6) :
                b10x.append(t)
                b10y.append(v)
    

    l0x = []
    l0y = []
    for j in range(42):
        for m in range(100):
            if (terrain[j,m] == 6.6) :
                l0x.append(j)
                l0y.append(m)

    fruits=[]
    fruits1=[]
    fruits2=[]

    bflys=[]
    for k in range(int(bflyinput)):
        if len(b10x)>=5:
            bflypos=np.random.randint(len(b10x))
            bflyx = b10x[bflypos]
            bflyy = b10y[bflypos]
            bfly = Butterfly2(f"B{k+1}",(bflyx,bflyy))
            bflys.append(bfly)

    bflys1=[]    
    for u in range(int(bfly1input)):     
        bfly1 = Butterfly1(f"C{u+1}", (7,8+7*u))
        bflys1.append(bfly1)

    
    # for b in range(4):     
    #     lbird2 = Ladybird(f"C{b+1}", (23,74+4*b))
    #     lbirds2.append(lbird2)
    #     lbird2.stepChange(getSubgrid(terrain, lbird2.getPos()))
            
    
    lbirds=[]
    for n in range(int(ladybirdinput)):
        if len(l0x)>=5:
            lbirdspos=np.random.randint(len(l0x))
            lbirdx = l0x[lbirdspos]
            lbirdy= l0y[lbirdspos]
            lbird = Ladybird(f"L{n+1}",(lbirdx,lbirdy))
            lbirds.append(lbird)
        
    for time in range(90):
        colormap = plt.colormaps.get_cmap('terrain_r')
        if time>=70:        
            plt.imshow(terrain, cmap=colormap, vmax = 9)
        else:        
            plt.imshow(terrain, cmap=colormap, vmax = 10)
        
        for x in range(int(antinput)):
            if len(x0s)>=5:
                antpos=np.random.randint(len(x0s))
                antx = x0s[antpos]
                anty = y0s[antpos]
                ant = Ant(f"A{x+1}", (antx,anty))
                ants.append(ant)
                ants[x].plotMe(ax, LIMITS)
                dig_pos = ants[x].getPos()
                if terrain[dig_pos] == 1:
                    terrain[dig_pos] = 0  # Change it to 0
        
        for f in range(int(fishinput)):
            fish = Fish(f"H{f+1}", (46,74+3*f))
            fishes.append(fish)
            fish.stepChange(getSubgrid(terrain, fish.getPos()))
            fishes[f].plotMe(ax, LIMITS)

        for fish in fishes:
            #print("\nFishes ##################")
            fish.stepChange(getSubgrid(terrain, fish.getPos()))
            # print(fish.pos)
    #       lbird.plotMe(ax, LIMITS) 

        for o in range(4):
            fruit = Fruits(f"H{o+1}", (22,8+8*o),"#FFFF00")
            fruits.append(fruit)
            fruit.stepChange(getSubgrid(terrain, fruit.getPos()))
            fruits[o].plotMe(ax, LIMITS)

        for o in range(3):
            fruit1 = Fruits(f"H{o+1}", (29,22+8*o),"#FFFF00")
            fruits1.append(fruit1)
            fruit1.stepChange(getSubgrid(terrain, fruit1.getPos()))
            fruits1[o].plotMe(ax, LIMITS)

        for o in range(3):
            fruit2 = Fruits(f"H{o+1}", (25,45+8*o),"#FFFF00")
            fruits2.append(fruit2)
            fruit2.stepChange(getSubgrid(terrain, fruit2.getPos()))
            fruits2[o].plotMe(ax, LIMITS)

        
        for bfly1 in bflys1:
            if 0 <= time <= 15:
                bfly1.stepChange(getSubgrid(terrain, bfly1.getPos()))
            elif 16 <= time <= 41:
                bfly1.avoidRain()
            elif 42<=time <= 65:
                bfly1.comingOut()
            elif time>=66:
                bfly1.stepChange(getSubgrid(terrain, bfly1.getPos()))

            bfly1.plotMe(ax, LIMITS)
            
        for bfly in bflys:
            bfly.lifecyclebfly()
            if bfly.age>=18:
                bfly.stepChange(terrain) 
            bfly.plotMe(ax, LIMITS)

        for lbird in lbirds:
            lbird.lifecyclelbird()
            if lbird.age>=13:
                lbird.stepChange(terrain) 
            lbird.plotMe(ax, LIMITS)
            if time>=40: 
                lbirds.remove(lbird)
                
        if 0<=time<=80:
            for ant in ants:
                ant.lifecycleant()
                if ant.age > 5:
                    ant.stepChange()

        if 20<=time<=45: 
            for r in range(11):
                raind = Rain(f"c{r+1}", (0,random.randint(0,100)), '#00006699')
                rainds.append(raind)
            for drops in rainds:
                if time>=55:
                    rainds.remove(drops)

        for raind in rainds:
            # print("\nRain ##################")
            raind.stepChange(getSubgrid(terrain, raind.getPos()),terrain)
            raind.plotMe(ax, LIMITS)
            #print(raind.lifespan)

        
        for fruit in fruits:
            for bfly in bflys:
                if fruit.getPos() == bfly.getPos():
                    fruits.remove(fruit)
        for fruit1 in fruits1:
            for bfly in bflys:
                if fruit1.getPos() == bfly.getPos():
                    fruits1.remove(fruit1)
        for fruit2 in fruits2:
            for bfly in bflys:
                if fruit2.getPos() == bfly.getPos():
                    fruits2.remove(fruit2)
            
        for fruit in fruits:
            for bfly1 in bflys1:
                if fruit.getPos() == bfly1.getPos():
                    fruits.remove(fruit)
        for fruit1 in fruits1:
            for bfly1 in bflys1:
                if fruit1.getPos() == bfly1.getPos():
                    fruits1.remove(fruit1)
        for fruit2 in fruits2:
            for bfly1 in bflys1:
                if fruit2.getPos() == bfly1.getPos():
                    fruits2.remove(fruit2)

        plt.title(f"Garden Timestep:{time+1}", fontsize="18")
        plt.grid()
        #plt.show()
        plt.pause(0.2)
        plt.cla()
        #plt.close()

if __name__ == "__main__":
    main()
