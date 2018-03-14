import selectquery as sq
from collections import deque
f = open('./haha.txt', 'w')

node_init = '2'

listnode = deque(node_init)

count = 1
while (True):
    if len(listnode) == 0:
        break
    nodecurrent = str(listnode.popleft())

    print "From: " + nodecurrent

    if count < 100:
        listnode_from_nodecurrent = sq.linking(nodecurrent)
        for id in listnode_from_nodecurrent:
            print " to: " + str(id)
            f.write(str(nodecurrent) + '\t' + str(id))
            f.write('\n')
        listnode.extend(listnode_from_nodecurrent)
    else:
        listnode_from_nodecurrent = sq.linking(nodecurrent)
        for id in listnode_from_nodecurrent:
            print " to: " + str(id)
            f.write(str(nodecurrent) + '\t' + str(id))
            f.write('\n')

    count = count + 1

