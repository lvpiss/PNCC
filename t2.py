#-*- coding:utf8 -*-
listport = [19215,33088,23717,36433,19215, 19215, 23717, 19215, 19215, 33088, 19215, 36433, 19215, 33088, 19215, 23717, 36433, 36433, 36433, 36433, 19215, 19215, 19215, 19215, 36433, 36433, 36433, 36433, 19215, 19215, 19215, 23717, 19215, 19215, 36433, 23717, 19215, 33088, 33088, 33088, 19215, 19215, 33088, 19215, 19215, 33088, 19215, 33088, 19215, 33088, 19215, 36433, 36433, 36433, 36433, 36433, 19215, 19215, 36433, 19215, 19215, 19215, 33088, 19215, 19215, 33088, 19215, 23717, 19215, 33088, 19215, 23717, 19215, 19215, 19215, 19215, 19215, 19215, 33088, 23717, 19215, 19215, 33088, 19215]

r1 = listport[0]
r2 = listport[1]
r3 = listport[2]
r4 = listport[3]

listrand = [r1,r2,r3,r4]

listabd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = 0
dictabd = {}
for l1 in listrand:
	for l2 in listrand:
		for l3 in listrand:
			for l4 in listrand:
				if x < 26:
					dictabd[listabd[x]] = [l1,l2,l3,l4]
				x = x + 1
dictabd[' '] = [r4,r4,r4,r4]
print(dictabd)

print(dictabd[' '])

l = len(listport)
i = 0

ll = l / 4
print(ll)

covertm = []
while i < ll:
	listport[i] = []
	listport[i].append(listport[4*i])
	listport[i].append(listport[4*i+1])
	listport[i].append(listport[4*i+2])
	listport[i].append(listport[4*i+3])
	for x in listabd:
		if dictabd[x] == listport[i]:
			listport[i] = x
			covertm.append(x)
		pass
	print('listport[',i,']:',listport[i])
	i = i + 1
	pass

print(covertm)