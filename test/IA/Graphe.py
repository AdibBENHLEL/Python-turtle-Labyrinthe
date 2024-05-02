import turtle 
import random
class Graphe():
        def __init__(self,L,C):
            self.L=L
            self.C=C
            self.dic={}
        def Ajouter_Noueud(self,i,j):
            if (i<self.L and j<self.C):
                    self.dic[(i,j)]=[]
             
        def Ajouter_Arc(self,l,c,T):
                self.dic[(l,c)].append(T)
                self.dic[T[:2]].append((l,c,T[2]))
        def Lister_Neuds(self):
            return self.dic.keys()
        def Lister_Arc(self):
            return self.dic.values()
        def Adjacent_Noeud(self,l,c):
            return self.dic[(l,c)]
        def AFF_GRAPHE(self):
            return self.dic
        def AFF_LABYRINTHE(self):
            t = turtle.Turtle()
            t.speed(-20)  # Set the drawing speed to the fastest
            size = 50 # Set the size of each cell (adjust as needed)
            
            t.penup()
            t.goto(-self.C * size / 2, self.L * size / 2)
            t.pendown()
            
            # Draw top and bottom walls
            for i in [0,self.L]:  # Iterate over top and bottom rows
                for j in range(1,self.C):  # Iterate over columns
                    print("i am in",i,j)
                    t.penup()
                    t.goto(j* size, -i * size)
                    t.pendown()
                    t.goto((j+1) * size,-i * size)
            
            # Draw left and right walls
            for j in [0,self.C]:  # Iterate over left and right columns
                for i in range(self.L):  # Iterate over rows
                    t.penup()
                    t.goto(j * size,-i * size)
                    t.pendown()
                    t.goto(j* size,-(i+1) * size)
            
            # Draw only the horizontal walls
            for j in range(0,6):  # Iterate over columns
                for i in range(0,6):  # Iterate over rows
                    if ((i+1, j, "False") in self.Adjacent_Noeud(i,j)):
                        print("mure found")
                        t.penup()
                        t.goto(j* size, -(i+1)* size)
                        t.pendown()
                        t.goto((j+1)* size, -(i+1) * size)
            
            t.hideturtle()  # Hide the turtle
            # Draw only the vertical walls
            for i in range(0,6):  # Iterate over columns
                for j in range(0,6):  # Iterate over rows
                    if ((i, j+1, "False") in self.Adjacent_Noeud(i,j)):
                        print("mure found")
                        t.penup()
                        t.goto((j+1)* size, -i* size)
                        t.pendown()
                        t.goto((j+1)* size, -(i+1) * size)
            
            t.hideturtle()  # Hide the turtle