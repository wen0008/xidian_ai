G={
    'one':{'two':1,'three':12},
    'two':{'three':9,'four':3},
    'three':{'five':5},
    'four':{'three':4,'five':13,'six':15},
    'five':{'six':4},
    'six':{}
}
X=list()
Y=['one','two','three','four','five','six']
disy={'one':0,'two':999,'three':999,'four':999,'five':999,'six':999}
distance={'one':0,'two':999,'three':999,'four':999,'five':999,'six':999}
last=dict()
while(len(Y)>0):
    s=min(disy,key=disy.get)
    X.append(Y.pop(Y.index(s)))
    del disy[s]
    for i in G[s].keys():
        if(distance[i]>distance[s]+G[s][i]):
            distance[i]=distance[s]+G[s][i]
            disy[i]=distance[s]+G[s][i]
            last[i]=s
print(distance)