#矩形迷宫地图，1为墙壁，0为可通行格
map=[
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,1,0,0,1,1,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]
road=list()
i=0
while(i<len(map)):
    road.append(map[i][:])
    i+=1
open=list()
close=list()
class Grid():
    """迷宫格子"""
    def __init__(self,x,y):
        self.x=x  #纵坐标
        self.y=y  #横坐标
        self.father=None
        self.g=0  #起点到当前格子的路程
        self.h=0  #当前格子到终点的路程(不考虑障碍)
        self.f=0  #f=g+h
    def get_grid(self):
        return((self.x,self.y))      

start=Grid(0,0)
end=Grid(4,6)   

def grid_pass(grid,map):
    """检查格子是否存在且可通行"""
    exist=True
    if(grid.x>=len(map) or grid.x<0):
        exist=False
    elif(grid.y>=len(map[grid.x]) or grid.y<0):
        exist=False    
    elif(map[grid.x][grid.y]==1):
        exist=False    
    return(exist)    
#print(grid_pass(grid(1,3),map))

def find_next(grid,map):
    """找当前格子可到达的格子,记录父节点"""
    next=list()
    gup=Grid(grid.x-1,grid.y)
    gdown=Grid(grid.x+1,grid.y)
    gleft=Grid(grid.x,grid.y-1)
    gright=Grid(grid.x,grid.y+1)
    if(grid_pass(gup,map)):
        next.append(gup)
    if(grid_pass(gdown,map)):
        next.append(gdown)
    if(grid_pass(gleft,map)):
        next.append(gleft)
    if(grid_pass(gright,map)):
        next.append(gright)
    i=0
    while(i<len(next)):
        next[i].father=grid    
        i+=1
    return(next)                

def find_minf(open):
    """找出open中f值最小的格子"""
    i=0
    min=0
    while(i<len(open)):
        if(open[i].f<open[min].f):
            min=i
        i+=1
    return(min)        

def is_end(open,end):
    """判断终点是否在open表里"""
    r=False
    i=0
    while(i<len(open)):
        if(open[i].x==end.x and open[i].y==end.y):
            r=True
        i+=1    
    return(r)    

# A*算法过程
open.append(start)
next=list()
while(True):
    now_grid=open[find_minf(open)]
    close.append(open.pop(open.index(now_grid)))
    next=find_next(now_grid,map)
    i=0
    while(i<len(next)):
        if((next[i] not in open)and (next[i] not in close)):
            next[i].g=now_grid.g+1
            next[i].h=((end.x-next[i].x)**2)**0.5+((end.y-next[i].y)**2)**0.5
            next[i].f=next[i].g+next[i].h    
            open.append(next[i])
            i+=1
    i=0
    if(is_end(open,end)):
        end.father=now_grid
        break

#显示路径
now_grid=end
while(True):
    road[now_grid.x][now_grid.y]=2
    now_grid=now_grid.father
    if(road[start.x][start.y]==2):
        break
i=0
while(i<len(road)):
    print(road[i])
    i+=1   