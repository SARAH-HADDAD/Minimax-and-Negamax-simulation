import pygame 
import time
import button

# Create game window
width=1300
length=760
win=pygame.display.set_mode((1450,800))
pygame.display.set_caption("GUI")
# Game variables
COLOR=(100,100,100)
GRAY=(150,150,150)
RED=(150,0,0)
BLUE=(0,0,150)
BLACK=(0,0,0)
values = [10, 5, 7, 11, 12, 8, 9, 8, 5, 12, 11, 12, 9, 8, 7, 10]
menu_state = "main"
# Load button images
Min_img=pygame.image.load("images/MIN.png")
Max_img=pygame.image.load("images/MAX.png")
MiniMax_img=pygame.image.load("images/MiniMax.png")
NegaMax_img=pygame.image.load("images/NegaMax.png")
NegaMaxWithAlphaBeta_img=pygame.image.load("images/NegaMax with Alpha-Beta Pruning.png")
# Create button instances
Min_button=button.Button((1400/2)-(MiniMax_img.get_width()/2),800/3,Min_img,1)
Max_button=button.Button((1400/2)-(MiniMax_img.get_width()/2),(800*2)/3,Max_img,1)
MiniMax_button=button.Button((1400/2)-(MiniMax_img.get_width()/2),800/4,MiniMax_img,1)
NegaMax_button=button.Button((1400/2)-(NegaMax_img.get_width()/2),800/2,NegaMax_img,1)
NegaMaxWithAlphaBeta_button=button.Button((1400/2)-(NegaMaxWithAlphaBeta_img.get_width()/2),(760*3)/4,NegaMaxWithAlphaBeta_img,1)
class Node():
    def __init__(self,x,y,radius, color, left, right, value, depth,p,alpha,beta):
        # la position du nœud dans l’interface graphique:
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.left=left
        self.right=right
        self.value=value
        self.depth= depth
        self.p=p
        self.alpha=alpha
        self.beta=beta


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
    positive_infinity= float('inf')
    negative_infinity= float('-inf')
    for lvl in range(levels):
        #totlvl <- 1,2,4,8,16
        totlvl=2**lvl
        start =(width//totlvl)/2
        for node in range(totlvl):
            #ef __init__(self,x,y,radius, color, left, right):
            if(lvl==4):
              nodes.append(Node((start+((width//totlvl)* node)),((length//levels)*lvl+(length//levels/2)),radius,COLOR,None,None,values[node], lvl,None,negative_infinity,positive_infinity)) 
            else:
                nodes.append(Node((start+((width//totlvl)* node)),((length//levels)*lvl+(length//levels/2)),radius,COLOR,None,None,None,lvl,None,negative_infinity,positive_infinity))

    for i in range(len(nodes)):
        if 2*i+1<len(nodes) and nodes[2*i+1]:
            nodes[i].setLeft(nodes[2*i+1])    
            nodes[2*i+1].p=(nodes[i])   
        if 2*i+2<len(nodes) and nodes[2*i+2]:
            nodes[i].setRight(nodes[2*i+2])  
            nodes[2*i+2].p=(nodes[i])
    

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
  

def draw(levels,nodes,player):
    draw_lines(nodes)
    draw_circles(levels,nodes) 
    font = pygame.font.Font('freesansbold.ttf',15)
    for i in range(2**(levels-1)): 
      pygame.draw.rect(win,(30,30,30),[(((width//16)/4)+(width//16)*i),750,((width//16)/2),((width//16)/2)]) 
      text = font.render(f"{values[i]}", True, (255,255,255))
      win.blit(text,(((((width//16)/4)+(width//16)*i)+(((width//16)/1.75)/4)),(750+(((width//16)/1.75)/3.75))))
    #Display min max   
    minmax=player
    font = pygame.font.Font('freesansbold.ttf',25)
    for i in range(levels):
        if(minmax==1):
            text = font.render("MAX", True, COLOR)
            win.blit(text,(1330,((length//levels)*i+10+(length//levels/3))))
        else:
            text = font.render("MIN", True, COLOR)   
            win.blit(text,(1330,((length//levels)*i+10+(length//levels/3))))
        minmax=-minmax    
    pygame.display.update()
def drawPath(node,W,L):
    #W : winner en rouge
    #L : loser en blue
    pygame.draw.line(win,(0,0,150),node.getLoc(),L.getLoc(),5)
    pygame.draw.line(win,(150,0,0),node.getLoc(),W.getLoc(),5)
    pygame.draw.circle(win,(150,0,0),W.getLoc(),node.getRaduis())
    pygame.draw.circle(win,(0,0,150),L.getLoc(),node.getRaduis())
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(f"{W.value}", True, (255,255,255))
    win.blit(text,((W.x-(W.radius/4)),(W.y-(W.radius/4))))
    text = font.render(f"{L.value}", True, (255,255,255))
    win.blit(text,((L.x-(W.radius/4)),(L.y-(W.radius/4))))
def drawBestPath(node,W):
    #W : winner en rouge
    if(node.getLeft()==W): 
        L=node.getRight()
    else:
        L=node.getLeft()
    #W : winner en rouge
    #L : loser en blue
    pygame.draw.line(win,(0,0,150),node.getLoc(),L.getLoc(),5)
    pygame.draw.line(win,(150,0,0),node.getLoc(),W.getLoc(),5)
    pygame.draw.circle(win,(150,0,0),W.getLoc(),node.getRaduis())
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(f"{-W.value}", True, (255,255,255))
    win.blit(text,((W.x-(W.radius/4)),(W.y-(node.radius/4))))
    if(L.value!=None):
        pygame.draw.circle(win,(0,0,150),L.getLoc(),node.getRaduis())
        text = font.render(f"{-L.value}", True, (255,255,255))
        win.blit(text,((L.x-(L.radius/4)),(L.y-(node.radius/4))))
def DisplayAlpha(alpha,Color,node):
    x=node.x-23
    if(node.depth==4):
        y=node.y+((node.radius*2)-27)
    else:
        if(node.depth==0):
            y=(node.y-(node.radius*2))
        else:
            y=node.y-(node.radius*2)-15
    font = pygame.font.Font('freesansbold.ttf',12)
    if(alpha==negative_infinity or alpha==positive_infinity):
        text = font.render(f"α={alpha} ", True, Color,GRAY)
    else:  text = font.render(f"α={alpha}    ", True, Color,GRAY)
    win.blit(text,((x,y)))
    pygame.display.update()

def DisplayBeta(beta,Color,node):
    x=node.x-23
    if(node.depth==4):
        y=node.y+((node.radius*2)-14)
    else:
        if(node.depth==0):
            y=(node.y-(node.radius*2)+14)
        else:
            y=node.y-(node.radius*2)   
    font = pygame.font.Font('freesansbold.ttf',12)
    if(beta==negative_infinity or beta==positive_infinity):
        text = font.render(f"β={beta} ", True, Color,GRAY)
    else:  text = font.render(f"β={beta}    ", True, Color,GRAY)
    win.blit(text,((x,y)))
    pygame.display.update()


    

def DisplayValue(node,Color):
     pygame.draw.circle(win,Color,node.getLoc(),node.getRaduis())
     font = pygame.font.Font('freesansbold.ttf',20)
     if(node.value!=None):
        text = font.render(f"{node.value}", True, (255,255,255))
        win.blit(text,((node.x-(node.radius/4)),(node.y-(node.radius/4))))
     pygame.display.update()

def MiniMax(node, depth,player):
        if(depth==4):
           DisplayValue(node,BLUE)
           time.sleep(0.7)
        else:
            pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
            MiniMax(node.getLeft(),node.getDepth()+1,-player)
            time.sleep(0.7)
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getRight().getLoc(),5)
            MiniMax(node.getRight(),node.getDepth()+1,-player)
            time.sleep(0.7)
            L=node.getLeft()
            R=node.getRight()
            if(player==1):
                if(R.getValue()>L.getValue()):
                    node.value=R.value
                    drawPath(node,R,L)
                else:
                    node.value=L.value
                    drawPath(node,L,R)
            else:  
                if(R.getValue()<L.getValue()):
                    node.value=R.value
                    drawPath(node,R,L)
                else:
                    node.value=L.value
                    drawPath(node,L,R)     
            DisplayValue(node,RED)
            time.sleep(0.7)                                    

def NegaMax(node,depth,player):
        if(depth==4):
           if(player==-1):node.value=-1*node.value
           DisplayValue(node,BLUE)
           time.sleep(0.7)
        else:
            pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getLeft().getLoc(),5)
            NegaMax(node.getLeft(),node.getDepth()+1,-player)
            time.sleep(0.7)
            pygame.draw.line(win,(0,0,150),node.getLoc(),node.getRight().getLoc(),5)
            NegaMax(node.getRight(),node.getDepth()+1,-player)
            time.sleep(0.7)
            L=node.getLeft()
            R=node.getRight()
            if((-1*R.getValue())>(-1*L.getValue())):
                node.value=-1*R.value
                drawPath(node,R,L)
            else:
                node.value=-1*L.value
                drawPath(node,L,R)
            DisplayValue(node,RED)
            time.sleep(0.7) 


def NegaMaxAlphaBetaPruning(node,depth,player,alpha,beta):
    if depth == 0:
        if(player==-1):node.value = - node.value      
        #// Display the values of alpha and beta
        DisplayAlpha(alpha,BLUE,node)
        DisplayBeta(beta,BLUE,node)
        #// Display the current node’s value and mark it as explored
        DisplayValue(node,BLUE)  
        pygame.display.update()

    else:
        #Mark the current node as explored
        pygame.draw.circle(win,(0,0,150),node.getLoc(),node.getRaduis())
        #Display the values of alpha and beta
        DisplayAlpha(alpha,BLUE,node)
        DisplayBeta(beta,BLUE,node)
        DisplayValue(node,BLUE)
        pygame.display.update()
        listChildren = [node.left, node.right]
        bestValue =float('-inf')
        bestPath = None
        for child in listChildren:
            #// Mark the link between the current node and the child node as explored
            pygame.draw.line(win,(0,0,150),child.p.getLoc(),child.getLoc(),5)
            NegaMaxAlphaBetaPruning(child,depth-1,-player,-beta,-alpha)
            if(child.value!=None):
                child.value = - child.value
                if child.value > bestValue:
                    bestValue = child.value
                    bestPath = child
                    child.p.value=bestValue
                if bestValue > alpha:
                    alpha = bestValue
                    #// Display the new value of alpha
                    DisplayAlpha(alpha,RED,node)
                    DisplayBeta(beta,BLUE,node)
                if beta <= alpha:
                    break
                node.value = bestValue
                print(node.depth,node.value,bestPath.value)
                #// Display the best path and the current node’s value
                drawBestPath(node,bestPath) 
                DisplayValue(node,RED)  




pygame.init()
pygame.display.update()
levels=5
nodes= create_nodes(5)
player=1
win.fill(GRAY)
pygame.display.update()
positive_infinity= float('inf')
negative_infinity= float('-inf')
while(True):

   #MiniMax(nodes[0],0)
   # time.sleep(5)
   draw(levels,nodes,1)
   listChildren=[]
   NegaMaxAlphaBetaPruning(nodes[0],4,1,negative_infinity,positive_infinity)
   time.sleep(50)

        

    
      

  

               

  
        
            
                


