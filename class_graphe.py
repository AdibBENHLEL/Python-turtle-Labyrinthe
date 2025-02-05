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
            i=0
            for j in range(1,self.C): 
                print("i am in",i,j)
                t.penup()
                t.goto(j* size, -i * size)
                t.pendown()
                t.goto((j+1) * size,-i * size)
            # bottom walls
            i=self.L  
            for j in range(self.C-1):
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
    def __init__(self, g):
        self.graph = g
        self.explored = {}#teste bien avec (1,0):2 État déjà exploré ou accessible ; rest[(0, 1)]
        self.accessible = {}
        
    def succ(self,state):
        l,c=state
        L = self.graph.Adjacent_Noeud(l, c)
        succ = []
        for item in L:
            if item[2] == "True":
                succ.append(item)
        return succ
    
    def VerifEtat(self, state):
        return state in self.explored.keys() or state in self.accessible.keys()
    
    def succ_valide(self,state):
        L_etat_valide = []
        L = self.succ(state)
        for item in L:
            etat_a_tester = (item[0], item[1])
            if not self.VerifEtat(etat_a_tester):
                L_etat_valide.append(etat_a_tester)
            else:
                print("État déjà exploré ou accessible")
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
  def aff_pile(self):
      return (self.elements)


from collections import deque

class File:
    def __init__(self):
        self.elements = deque()
    
    def queue_vide(self):
        return len(self.elements) == 0
    
    def enfiler(self, element):
        self.elements.append(element)
    
    def defiler(self):
        if not self.queue_vide():
            return self.elements.popleft()
        else:
            print("La queue est vide.")
    
    def taille_queue(self):
        return len(self.elements)
    
    def aff_queue(self):
        return self.elements



class recherche_solution:
    
    def __init__(self, g,etat_intiale,etat_objectif):
        self.g=g
        self.etat_intiale=etat_intiale
        self.etat_objectif=etat_objectif
    
    def aff_path(self, dic):
        t = turtle.Turtle()
        t.speed(0)  # Set the drawing speed to the fastest
        size = 50  # Set the size of each cell (adjust as needed)
        col = "#ADD8E6"  # Set the color
        t.fillcolor(col)
        t.begin_fill()
        t.penup()
        t.goto(5.5, 6)  # make the pointer at (0,0) the beginning
        t.pendown()
        t.color("red")  # Change the color of the line to red
        for index in range(len(dic) - 1):
            courant, source = list(dic.values())[index], list(dic.keys())[index]
            
            (i, j), (i_source, j_source) = courant, source
            if (j_source == j and (i_source == i + 1 or i_source == i - 1)):
                t.penup()
                t.goto((j + 0.5) * size, -i_source * size)
                t.pendown()
                t.goto((j + 0.5) * size, -i * size)
            elif (i_source == i and (j_source == j + 1 or j_source == j - 1)):
                t.penup()
                t.goto(j_source * size, -(i + 0.5) * size)
                t.pendown()
                t.goto(j * size, -(i + 0.5) * size)  
        turtle.write("solution founded ", align="right")
    
    
    def DFS(self):
        S = serch(g)
        p = Pile()
        etat_courant = self.etat_intiale
        p.empiler(etat_courant)
        S.explored[self.etat_intiale] = None
        
        while not p.pile_vide():
            for item in S.succ_valide(etat_courant):
                p.empiler(item)
                S.accessible[item] = etat_courant
            etat_courant_new = p.depiler()
            S.explored[etat_courant_new] = etat_courant
            etat_courant = etat_courant_new
            
            if etat_courant == self.etat_objectif:
                print("Path trouvé:")
                fwdPath = {}
                cellule = self.etat_objectif
                while cellule != (0, 0):
                    try:
                        fwdPath[S.accessible[cellule]] = cellule  #cle:accesible valeur:source 
                        cellule = S.accessible[cellule]
                    except:
                        print('nexiste pas!')
                        return False
                print(fwdPath)    
                return fwdPath
        print("No solution found for this labyrinth.")
    
    
    
    
    
    def BFS(self):
        S = serch(g)
        F= File()
        etat_courant = self.etat_intiale
        F.enfiler(etat_courant)
        S.explored[self.etat_intiale] = None
        
        
        while not F.queue_vide():
            for item in S.succ_valide(etat_courant):
                F.enfiler(item)
                S.accessible[item] = etat_courant
            
            etat_courant_new = F.defiler()
            S.explored[etat_courant_new] = etat_courant
            etat_courant = etat_courant_new
            if (etat_courant == self.etat_objectif):
                
                print("Path trouvé:")
                print(len(S.explored))
                fwdPath = {}
                cellule = self.etat_objectif
                while cellule != (0, 0):
                    try:
                        fwdPath[S.accessible[cellule]] = cellule  #cle:accesible valeur:source 
                        cellule = S.accessible[cellule]
                    except:
                        print('nexiste pas!')
                        return False
                print(fwdPath)    
                return fwdPath
        print("No solution found for this labyrinth.")
        




def reset_labyrinth_visualization():
    turtle.resetscreen() 
def reset_labyrinth(g):
    # Clear the dictionary holding the graph information
    g.dic.clear()

resultat=False
while not resultat :
    #Ajouter_Noueud
    g=Graphe(6,6)
    for i in range (6):
        for j in range (6):
            g.Ajouter_Noueud(i, j)
    print(g.Lister_Neuds())


    # Randomly add walls
    for i in range(6):
        for j in range(6):
            if j < 5:
                    if random.choice([True, False]):
                        g.Ajouter_Arc(i, j, (i, j + 1, "True"))
                    else:
                        g.Ajouter_Arc(i, j, (i, j + 1, "False"))
            if i < 5:
                    if random.choice([True, False]):
                        g.Ajouter_Arc(i, j, (i + 1, j, "True"))
                    else:
                        g.Ajouter_Arc(i, j, (i + 1, j, "False"))
    print(g.AFF_GRAPHE())
    

    R=recherche_solution(g,(0,0),(5,5))
    path=R.DFS()
    
    if path :
        g.AFF_LABYRINTHE()
        R.aff_path(path)
        break
    else :
         resultat=False
         reset_labyrinth_visualization()
         reset_labyrinth(g)