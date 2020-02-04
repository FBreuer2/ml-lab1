import lib.monkdata as m
import lib.dtree as d

t=d.buildTree(m.monk1, m.attributes)
print('MONK-1 Train: ', d.check(t, m.monk1))
print('MONK-1 Test: ', d.check(t, m.monk1test))



t=d.buildTree(m.monk2, m.attributes)
print('MONK-2 Train: ', d.check(t, m.monk2))
print('MONK-2 Test: ', d.check(t, m.monk2test))

t=d.buildTree(m.monk3, m.attributes)
print('MONK-3 Train: ', d.check(t, m.monk3))
print('MONK-3 Test: ', d.check(t, m.monk3test))