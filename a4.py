from lib import dtree

import lib.monkdata as m

for i in range(6):
    print('MONK-1 attribute ', str(i+1), ' has information gain of ', dtree.averageGain(m.monk1, m.attributes[i]))

for i in range(6):
    print('MONK-2 attribute ', str(i+1), ' has information gain of ', dtree.averageGain(m.monk2, m.attributes[i]))

for i in range(6):
    print('MONK-3 attribute ', str(i+1), ' has information gain of ', dtree.averageGain(m.monk3, m.attributes[i]))