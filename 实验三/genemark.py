import pandas as pd
#open the gtf file
f = open('genemark.gtf','r+')
initdata = f.readlines()
f.close()
#open the blast result
f = open('prores','r')
indexdata = f.readlines()
f.close()

data = []
for x in initdata:
	data.append(x.split('\t'))

for x in data:
	x[8] = x[8].split(' ')

target = []
for x in indexdata:
	target.append(x.split('\t'))
data[0][8][1][1:-2]

#add the query name to the list
for x in data:
	for y in target:
		if x[8][1][1:-2] == y[0]:
			x.append(y[1])
			break

for x in data:
	x[8] = ' '.join(x[8]).replace('\n','')
#write the result
pd.DataFrame(data).to_csv('proteinblast',sep='\t',header=False,index=False)