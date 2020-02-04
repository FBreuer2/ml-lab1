import lib.dtree as dtree

import lib.monkdata as m

def getInfo(setName, set):
    for i in range(6):
        print(setName, ' and attribute ', str(i+1), ' has information gain of ', dtree.averageGain(set, m.attributes[i]))


#print('m1 a5=1', dtree.mostCommon(dtree.select(m.monk1, m.attributes[4], 1)))
#print('m1 a5=2', dtree.mostCommon(dtree.select(m.monk1, m.attributes[4], 2)))
#print('m1 a5=3', dtree.mostCommon(dtree.select(m.monk1, m.attributes[4], 3)))

# first part
#getInfo('m1 a5=1', dtree.select(m.monk1, m.attributes[4], 1))
#getInfo('m1 a5=2', dtree.select(m.monk1, m.attributes[4], 2))

#getInfo('m1 a5=3', dtree.select(m.monk1, m.attributes[4], 3))

#getInfo('m1 a5=2 and a6=1', dtree.select(dtree.select(m.monk1, m.attributes[4], 3), m.attributes[5], 1))
#getInfo('m1 a5=2 and a6=2', dtree.select(dtree.select(m.monk1, m.attributes[4], 3), m.attributes[5], 2))

print(dtree.buildTree(m.monk1, m.attributes, 2))
print(dtree.buildTree(m.monk2, m.attributes, 2))
print(dtree.buildTree(m.monk3, m.attributes, 2))