import snap
import networkx as nx
import matplotlib as plt

with open('./link_db.txt', 'r') as f:
    data = f.readlines()
# print "Data:"
# print data
X = []
for da in data:
    vidu = da.split()
    linkto = {
        'id_from': vidu[0],
        'id_to': vidu[1]
    }
    X.append(linkto)

G = snap.TNGraph.New()
listNode = []

for node in X:
    x = int(node['id_from'])
    y = int(node['id_to'])
    if x not in listNode:
        G.AddNode(x)
        listNode.append(x)
    if y not in listNode:
        G.AddNode(y)
        listNode.append(y)
    G.AddEdge(x, y)

PRankH = snap.TIntFltH()
snap.GetPageRank(G, PRankH)



# sort node
ranks = "ranks.txt"
ranks_file = open('./' + ranks, 'w+')
rank_node = []
for item in PRankH:
    ranks_file.write(str(item) + '  ' + str(round(PRankH[item],4)) + '\n')
    rank_node.append((float(round(PRankH[item],4)),int(item)))
    # print item, PRankH[item]
ranks_file.close()
print rank_node
rank_node.sort()
rank_node.reverse()
output_file = "sort_rank.txt"
print('ghi kq sort ra  file ....')
with open(output_file, 'w+') as f:
	for pagerank, pageid in rank_node:
		f.write(str(pagerank) + '\t' + str(pageid) + '\n')
