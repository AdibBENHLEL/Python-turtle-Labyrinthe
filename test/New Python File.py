import turtle 

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
                for j in range(self.C):  # Iterate over columns
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



class serch:
    def __init__(self,g,l,c):
        self.graph =g
        self.explored = {}
        self.accessible = {}
        
    def succ(self,l,c):
        L=self.graph.Adjacent_Noeud(l,c)
        succ=[]
        for item in L:
            if item[2]=="True" :
                    succ.append(item)
        return succ

    def VerifEtat(self, state):
        return not (state in self.explored.keys()  or state in self.accessible.keys())
    
    def succ_valide(self,l,c):
        L_etat_valide=[]
        L=succ(l,c)
        for item in L:
            etat_a_tester=tuple(item[0],item[1])
            if VerifEtat(etat_a_tester):
                L_etat_valide.append(etat_a_tester)
        return L_etat_valide
    
                
from collections import deque
class Pile:
  def __init__(self):
    self.elements = deque()
  def pile_vide(self):
    return len(self.elements) == 0
  def empiler(self, element):
    self.elements.append(element)
  def depiler(self):
    if not self.pile_vide():
      return self.elements.pop()
    else:
      print("La pile est vide.")
  def taille_pile(self):
    return len(self.elements)
class recherche_solution:
    
    def dfs(self,etat_intiale,etat_objectif):
      p=pile()


            

g=Graphe(6,6)
for i in range (6):
    for j in range (6):
        g.Ajouter_Noueud(i, j)
print(g.Lister_Neuds())
#ligne 0
g.Ajouter_Arc(0, 0,(0,1,"True"))
g.Ajouter_Arc(0, 0,(1,0,"True"))
g.Ajouter_Arc(0, 1,(0,2,"True"))
g.Ajouter_Arc(0, 1,(1,1,"False"))
g.Ajouter_Arc(0, 2,(1,2,"False"))
g.Ajouter_Arc(0, 2,(0,3,"True"))
g.Ajouter_Arc(0, 3,(1,3,"False"))
g.Ajouter_Arc(0, 3,(0,4,"True"))
g.Ajouter_Arc(0, 4,(1,4,"False"))
g.Ajouter_Arc(0, 4,(0,5,"True"))
g.Ajouter_Arc(0, 5,(1,5,"True"))



#ligne 1
g.Ajouter_Arc(1, 0,(2,0,"True"))
g.Ajouter_Arc(1, 0,(1,1,"False"))
g.Ajouter_Arc(1, 1,(1,2,"True"))
g.Ajouter_Arc(1, 1,(2,1,"False"))
g.Ajouter_Arc(1, 2,(1,3,"False"))
g.Ajouter_Arc(1, 2,(2,2,"True"))
g.Ajouter_Arc(1, 3,(2,3,"True"))
g.Ajouter_Arc(1, 3,(1,4,"True"))
g.Ajouter_Arc(1, 4,(2,4,"False"))
g.Ajouter_Arc(1, 4,(1,5,"False"))
g.Ajouter_Arc(1, 5,(2,5,"True"))

g.Ajouter_Arc(2, 0,(2,1,"True"))
g.Ajouter_Arc(2, 0,(3,0,"True"))
g.Ajouter_Arc(2, 1,(2,2,"True"))
g.Ajouter_Arc(2, 1,(3,1,"False"))
g.Ajouter_Arc(2, 2,(2,3,"False"))
g.Ajouter_Arc(2, 2,(3,2,"False"))
g.Ajouter_Arc(2, 3,(2,4,"False"))
g.Ajouter_Arc(2, 3,(3,3,"True"))
g.Ajouter_Arc(2, 4,(2,5,"True"))
g.Ajouter_Arc(2, 4,(3,4,"False"))
g.Ajouter_Arc(2,5,(3,5,"True"))

g.Ajouter_Arc(3, 0,(3,1,"False"))
g.Ajouter_Arc(3, 0,(4,0,"True"))
g.Ajouter_Arc(3, 1,(3,2,"False"))
g.Ajouter_Arc(3, 1,(4,1,"True"))
g.Ajouter_Arc(3, 2,(3,3,"True"))
g.Ajouter_Arc(3, 2,(4,2,"True"))
g.Ajouter_Arc(3, 3,(3,4,"True"))
g.Ajouter_Arc(3, 3,(4,3,"True"))
g.Ajouter_Arc(3, 4,(3,5,"True"))
g.Ajouter_Arc(3, 4,(4,4,"False"))
g.Ajouter_Arc(3, 5,(4,5,"True"))


g.Ajouter_Arc(4, 0,(4,1,"False"))
g.Ajouter_Arc(4, 0,(5,0,"True"))
g.Ajouter_Arc(4, 1,(4,2,"True"))
g.Ajouter_Arc(4, 1,(5,1,"False"))
g.Ajouter_Arc(4, 2,(4,3,"False"))
g.Ajouter_Arc(4, 2,(5,2,"True"))
g.Ajouter_Arc(4, 3,(4,4,"False"))
g.Ajouter_Arc(4, 3,(5,3,"False"))
g.Ajouter_Arc(4, 4,(5,4,"True"))
g.Ajouter_Arc(4, 4,(4,5,"False"))
g.Ajouter_Arc(4, 5,(5,5,"False"))

g.Ajouter_Arc(5, 0,(5,1,"False"))
g.Ajouter_Arc(5, 1,(5,2,"True"))
g.Ajouter_Arc(5, 2,(5,3,"True"))
g.Ajouter_Arc(5, 3,(5,4,"True"))
g.Ajouter_Arc(5, 4,(5,5,"True"))



print(g.Lister_Arc())
print(g.Adjacent_Noeud(0,0))
print(g.AFF_GRAPHE())

g.AFF_LABYRINTHE()
S=serch(g,6,6)
print(S.succ(0,0))



