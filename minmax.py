import pygame 
import math
import time
width=1300
length=760
win=pygame
win=pygame.display.set_mode((1450,800))
pygame.display.set_caption("GUI")
COLOR=(100,100,100)
GRAY=(150,150,150)
values = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
class Node():
    def __init__(self,x,y,radius, color, left, right, value,Max, depth,p):
        # la position du nœud dans l’interface graphique:
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.left=left
        self.right=right
        self.value=value
        self.Max=Max
        self.depth= depth
        self.p=p

    def getLoc(self):
        return (self.x,self.y)  

    def getColor(self):
        return self.color    

    def getRaduis(self):
        return self.radius

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, left):
        self.left=left

    def setRight(self, right):
        self.right=right

    def getMAX(self):
        return self.Max

    def setMAX(self, Max):
        self.Max=Max  

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value=value 

    def getDepth(self):
        return self.depth
    def getpere(self):
        return self.p

    def setpere(self, p):
        self.p=p

#La fonction qui va créer un arbre binaire dont tous les nœuds sont initialement vides:
def create_nodes(levels):
    nodes=[]
    values = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
    finalTot=2**(levels-1)
    diameter=(width//finalTot)/2.5
    radius=diameter
    for lvl in range(levels):
        #MIN MAX:
        if(lvl%2==0): Max = False
        else:Max = True
        #totlvl <- 1,2,4,8,16
        totlvl=2**lvl
        start =(width//totlvl)/2
        for node in range(totlvl):
            #ef __init__(self,x,y,radius, color, left, right):
            if(lvl==4):
              nodes.append(Node((start+((width//totlvl)* node)),((length//levels)*lvl+(length//levels/2)),radius,COLOR,None,None,values[node],Max, lvl,None)) 
            else:
                nodes.append(Node((start+((width//totlvl)* node)),((length//levels)*lvl+(length//levels/2)),radius,COLOR,None,None,None,Max,lvl,None))

    for i in range(len(nodes)):
        if 2*i+1<len(nodes) and nodes[2*i+1]:
            nodes[i].setLeft(nodes[2*i+1])    
            nodes[2*i+1].setpere(nodes[i])   
        if 2*i+2<len(nodes) and nodes[2*i+2]:
            nodes[i].setRight(nodes[2*i+2])  
            nodes[2*i+2].setpere(nodes[i])
    

    return nodes

def draw_circles(levels,nodes):
    for node in nodes:
        pygame.draw.circle(win,node.getColor(),node.getLoc(),node.getRaduis())
        #getValue
        #font = pygame.font.Font('freesansbold.ttf',25)
        #text = font.render(f"{node.getMAX()}", True, (255,255,255))
        #win.blit(text,node.getLoc())


def draw_lines(nodes):
    for node in nodes:
        if node.getLeft()!=None:
            pygame.draw.line(win,(COLOR),node.getLoc(),node.getLeft().getLoc(),5)
        if node.getRight()!=None:   
            pygame.draw.line(win,(COLOR),node.getLoc(),node.getRight().getLoc(),5) 
  

def draw(levels,nodes):
    draw_lines(nodes)
    draw_circles(levels,nodes) 
    font = pygame.font.Font('freesansbold.ttf',15)
    for i in range(2**(levels-1)): 
      pygame.draw.rect(win,(30,30,30),[(((width//16)/4)+(width//16)*i),750,((width//16)/2),((width//16)/2)]) 
      text = font.render(f"{values[i]}", True, (255,255,255))
      win.blit(text,(((((width//16)/4)+(width//16)*i)+(((width//16)/1.75)/4)),(750+(((width//16)/1.75)/3.75))))

    for i in range(levels):
        if(i%2==0):
            text = font.render("MIN", True, COLOR)
            win.blit(text,(1330,((length//levels)*i+10+(length//levels/3))))
        else:
            text = font.render("MAX", True, COLOR)   
            win.blit(text,(1330,((length//levels)*i+10+(length//levels/3))))


    pygame.display.update()

def MiniMax(node, depth):
        time.sleep(1)
        if (depth == 0):
            pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
            pygame.display.update()
            MiniMax(node.getLeft(),node.getDepth()+1)
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getRight().getLoc(),5)
            pygame.display.update()
            MiniMax(node.getRight(),node.getDepth()+1)
            L=node.getLeft()
            R=node.getRight()
            if(node.getMAX()==True):
                if(node.value==None):
                    if(R.getValue()>L.getValue()):
                        node.value=R.value
                        drawPath(node,R,L)
                    else:
                        node.value=L.value
                        drawPath(node,L,R)
            else:  
                if(node.value==None):
                    if(R.getValue()<L.getValue()):
                        node.value=R.value
                        drawPath(node,R,L)
                    else:
                        node.value=L.value
                        drawPath(node,L,R)
            
            pygame.draw.circle(win,(150,0,0),node.getLoc(),node.getRaduis())
            font = pygame.font.Font('freesansbold.ttf',20)
            text = font.render(f"{node.value}", True, (255,255,255))
            win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))            
            pygame.display.update()                    
            
        else:
            if(depth == 4):
                pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(f"{node.value}", True, (255,255,255))
                win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))
                pygame.display.update()

            else:
                pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
                pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
                pygame.display.update()
                MiniMax(node.getLeft(),node.getDepth()+1)
                pygame.draw.line(win,(0,0,150),node.getLoc(),node.getRight().getLoc(),5)
                pygame.display.update()
                MiniMax(node.getRight(),node.getDepth()+1)
                L=node.getLeft()
                R=node.getRight()
                if(node.getMAX()==True):
                    if(node.value==None):
                         if(R.getValue()>L.getValue()):
                            node.value=R.value
                            drawPath(node,R,L)
                         else:
                            node.value=L.value
                            drawPath(node,L,R)
                else:  
                    if(node.value==None):
                         if(R.getValue()<L.getValue()):
                            node.value=R.value
                            drawPath(node,R,L)

                         else:
                            node.value=L.value
                            drawPath(node,L,R)
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(f"{node.value}", True, (255,255,255))
                win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))
                pygame.display.update()
             
def drawPath(node,W,L):
    #W : winner en rouge
    #L : loser en blue
    pygame.draw.line(win,( 0,0,150),node.getLoc(),L.getLoc(),5)
    pygame.draw.line(win,(150,0,0),node.getLoc(),W.getLoc(),5)
    pygame.draw.circle(win,(150,0,0),W.getLoc(),node.getRaduis())
    pygame.draw.circle(win,(0,0,150),L.getLoc(),node.getRaduis())
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(f"{W.value}", True, (255,255,255))
    win.blit(text,((W.x-(W.radius/4)),(W.y-(W.radius/4))))
    text = font.render(f"{L.value}", True, (255,255,255))
    win.blit(text,((L.x-(W.radius/4)),(L.y-(W.radius/4))))
      
def NegaMax(node, player, depth):
        time.sleep(1)
        if (depth == 0):
            pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
            pygame.display.update()
            NegaMax(node.getLeft(),-1*player,node.getDepth()+1)
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getRight().getLoc(),5)
            pygame.display.update()
            NegaMax(node.getRight(),-1*player,node.getDepth()+1)
            L=node.getLeft()
            R=node.getRight()
            if(node.value==None):
                if((-1*R.getValue())>(-1*L.getValue())):
                    node.value=-1*R.value
                    drawPath(node,R,L)
                else:
                    node.value=-1*L.value
                    drawPath(node,L,R)

            
            pygame.draw.circle(win,(150,0,0),node.getLoc(),node.getRaduis())
            font = pygame.font.Font('freesansbold.ttf',20)
            text = font.render(f"{node.value}", True, (255,255,255))
            win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))            
            pygame.display.update()                    
            time.sleep(500000)
        else:
            if(depth == 4):
                if(player==-1):node.value=-1*node.value
                pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(f"{node.value}", True, (255,255,255))
                win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))
                pygame.display.update()

            else:
                pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
                pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
                pygame.display.update()
                NegaMax(node.getLeft(),-1*player,node.getDepth()+1)
                pygame.draw.line(win,(0,0,150),node.getLoc(),node.getRight().getLoc(),5)
                pygame.display.update()
                NegaMax(node.getRight(),-1*player,node.getDepth()+1)
                L=node.getLeft()
                R=node.getRight()
                if(node.value==None):
                         if((-1*R.getValue())>(-1*L.getValue())):
                            node.value=-1*R.value
                            drawPath(node,R,L)
                         else:
                            node.value=-1*L.value
                            drawPath(node,L,R)
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(f"{node.value}", True, (255,255,255))
                win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))
                pygame.display.update()
             

def NegaMaxAlphaBetaPruning(node, player, depth, alpha, beta):
        time.sleep(1)
        if (depth == 0):
            pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
            drawAlphaBeta(node,alpha,beta,(node.x)-23,(node.y-(node.radius*2)),(node.x)-23,(node.y-(node.radius*2)+14))
            pygame.display.update()
            NegaMaxAlphaBetaPruning(node.getLeft(),-1*player,node.getDepth()+1,-beta, -alpha)
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getRight().getLoc(),5)
            pygame.display.update()
            NegaMaxAlphaBetaPruning(node.getRight(),-1*player,node.getDepth()+1,-beta, -alpha)
            L=node.getLeft()
            R=node.getRight()
            if(node.value==None):
                if((-1*R.getValue())>(-1*L.getValue())):
                    node.value=-1*R.value
                    drawPath(node,R,L)
                else:
                    node.value=-1*L.value
                    drawPath(node,L,R)

            
            pygame.draw.circle(win,(150,0,0),node.getLoc(),node.getRaduis())
            font = pygame.font.Font('freesansbold.ttf',20)
            text = font.render(f"{node.value}", True, (255,255,255))
            win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))            
            pygame.display.update()                    
            time.sleep(500000)
        else:
            if(depth == 4):
                if(player==-1):node.value=-1*node.value
                pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(f"{node.value}", True, (255,255,255))
                win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))
                font = pygame.font.Font('freesansbold.ttf',12)
                text = font.render(f"alpha={alpha}", True, (0,0,255),GRAY)
                win.blit(text,((node.x)-23,(node.y+(node.radius*2)-27)))
                text = font.render(f"beta={beta}", True, (0,0,255),GRAY)
                win.blit(text,((node.x)-23,(node.y+(node.radius*2)-14)))
                pygame.display.update()

            else:
                pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
                pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
                pygame.display.update()
                NegaMaxAlphaBetaPruning(node.getLeft(),-1*player,node.getDepth()+1,-beta, -alpha)
                pygame.draw.line(win,(0,0,150),node.getLoc(),node.getRight().getLoc(),5)
                pygame.display.update()
                NegaMaxAlphaBetaPruning(node.getRight(),-1*player,node.getDepth()+1,-beta, -alpha)
                L=node.getLeft()
                R=node.getRight()
                if(node.value==None):
                         if((-1*R.getValue())>(-1*L.getValue())):
                            node.value=-1*R.value
                            drawPath(node,R,L)
                            drawAlphaBeta(node,alpha,beta,(node.x)-23,node.y-(node.radius*2)-15,(node.x)-23,(node.y-(node.radius*2)))
                         else:
                            node.value=-1*L.value
                            drawPath(node,L,R)
                            drawAlphaBeta(node,alpha,beta,(node.x)-23,node.y-(node.radius*2)-15,(node.x)-23,(node.y-(node.radius*2)))
                font = pygame.font.Font('freesansbold.ttf',20)
                text = font.render(f"{node.value}", True, (255,255,255))
                win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))
                pygame.display.update()
             
    
def drawAlphaBeta(node,alpha,beta,xa,ya,xb,yb):
    font = pygame.font.Font('freesansbold.ttf',12)
    text = font.render(f"alpha={alpha}", True, (0,0,255))
    win.blit(text,((xa,ya)))
    text = font.render(f"beta={beta}", True, (0,0,255))
    win.blit(text,((xb,yb)))




    

pygame.init()
win.fill(GRAY)
pygame.display.update()
levels=5
nodes= create_nodes(5)
draw(levels,nodes)
positive_infinity= float('inf')
negative_infinity= float('-inf')
while(True):
   
   # time.sleep(5)
    draw(levels,nodes)
    MiniMax(nodes[0],0)

    #if(nodes[0].getMAX()==True):
        #NegaMaxAlphaBetaPruning(nodes[0],1,0,positive_infinity,negative_infinity)
    #else:
        #NegaMaxAlphaBetaPruning(nodes[0],-1,0,positive_infinity,negative_infinity)

