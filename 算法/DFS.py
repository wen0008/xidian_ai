G={
    'a':['b','g'],
    'b':['a','c','f'],
    'c':['b','d','e'],
    'd':['c','e'],
    'e':['c','d'],
    'f':['b','g'],
    'g':['a','f','h'],
    'h':['g','i','j'],
    'i':['h','j'],
    'j':['h','i'],
}
start='a'
unvisited=list()
visited=list()
for k in G.keys():
    unvisited.append(k)

def dfs(g,G,unvisited,visited):
    visited.append(unvisited.pop(unvisited.index(g)))
    for k,v in G.items():
        
        i=0
        while(i<len(G[g])):
            if(G[g][i] in unvisited):
                dfs(G[g][i],G,unvisited,visited)
            i+=1
        i=0        

for k,v in G.items():
    if(k in unvisited):
        dfs(k,G,unvisited,visited)
    
print(visited)