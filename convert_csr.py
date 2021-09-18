import igraph as ig
from igraph import Graph



name='star1000.txt'
file1 = open(name, 'r')
Lines = file1.readlines()
file1.close()
count=0
to =[]
fromm =[]
for line in Lines:
    count += 1
    if(count!=1):
            l=line.split()
            to.append(int(l[0])-1)
            fromm.append(int(l[1])-1)

edge=count-1
vertex=max(max(to)+1,max(fromm)+1)
print(vertex)

g = Graph(edges=list(zip(to,fromm)))
print(g.summary(verbosity=0))
print(g.vcount())
print(g.ecount())

name=name.split(".")[0]

r=[]
A=g.get_adjacency_sparse()
print(A)
file1 = open(name+'csr_coloff.txt', 'w')
for i in range(len(A.nonzero()[0])):
    if i%1000==0:
        print(i)
    r.append(A.nonzero()[0][i])
    file1.write(str(A.nonzero()[1][i])+"\n")
file1.close()
 

#craete row ptr
row_ptr=[]
row_ptr.insert(0,g.ecount()*2)
#next time do it with cpp vectors
for i in range(g.vcount()-1,0,-1):
    if i%1000==0:
        print(i)   
    try:
        val=r.index(i)
        row_ptr.insert(0,val)
    except:
        row_ptr.insert(0,val)

row_ptr.insert(0,0)

file1 = open(name+'csr_rowptr.txt', 'w')
for i in row_ptr:    
    file1.write(str(i)+"\n")

file1.close()



#print(row_ptr)
# 2 in case of undirected
#file1.writelines(s)

