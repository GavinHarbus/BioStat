import pandas as pd
import numpy as np

#differ the same protein in the same scanfold from the inital result
def group(data):
	protein_data = data.groupby('A')
	protein_name = data.A.drop_duplicates()
	group_by_protein = []
	for x in protein_name:
		group_by_protein.append(protein_data.get_group(x))
	group_by_scanfold = []
	for i in range(len(group_by_protein)):
		acceptor = []
		scanfold = group_by_protein[i].B.drop_duplicates()
		temp = group_by_protein[i].groupby('B')
		for y in scanfold:
			acceptor.append(temp.get_group(y))
		group_by_scanfold.append(acceptor)
	group_result = []
	for x in group_by_scanfold:
		for y in x:
			group_result.append(np.array(y).tolist())
	return group_result

#merge two records which has a distance < 100 bp on positive chain
def merge_pos(data):
	result = []
	for x in data:
		if (len(x) == 1):
			result.append(x[0])
		else:
			i = 0
			while(i < len(x) - 1):
				blast = x[i]
				(ps, pe, ns, ne) = blast[6:10]
				score = blast[11]
				for j in range(i+1,len(x)):
					(ps1, pe1, ns1, ne1) = x[j][6:10]
					score1 = x[j][11]
					if (0 < ns - ne1 < 100 ) \
					or (0 < ns1 - ne < 100 ):
						blast[11] = score + score1
						blast[6] = min(ps, ps1)
						blast[7] = max(pe, pe1)
						blast[8] = min(ns, ns1)
						blast[9] = max(ne, ne1)
						i += 1
				i += 1
				result.append(blast)
	return result

#merge two records which has a distance < 100 bp on negative chain
def merge_neg(data):
	result = []
	for x in data:
		if (len(x) == 1):
			result.append(x[0])
		else:
			i = 0
			while(i < len(x) - 1):
				blast = x[i]
				(ps, pe, ne, ns) = blast[6:10]
				score = blast[11]
				for j in range(i+1,len(x)):
					(ps1, pe1, ne1, ns1) = x[j][6:10]
					score1 = x[j][11]
					if (ns - ne1 < 100 and ns - ne1 > 0) \
					or (ns1 - ne < 100 and ns1 - ne > 0):
						blast[11] = score + score1
						blast[6] = min(ps, ps1)
						blast[7] = max(pe, pe1)
						blast[8] = max(ne, ne1)
						blast[9] = min(ns, ns1)
						i += 1
				i += 1
				result.append(blast)
	return result

#group the results by scanfold
def group_by_scanfold(data):
	scanfold = data.B.drop_duplicates()
	group_data = data.groupby('B')
	group_result = []
	for x in scanfold:
		group_result.append(group_data.get_group(x))
	final_result = []
	for x in group_result:
		final_result.append(np.array(x).tolist())
	return final_result

#remove duplicated records on positive chain
def rm_dup_pos(data):
	result = []
	for x in data:
		for i in range(len(x)):
			(ns, ne) = x[i][8:10]
			score = x[i][11]
			size = ne - ns
			for j in range(len(x)):
				if j == i:
					continue
				else:
					(ns1, ne1) = x[j][8:10]
					score1 = x[j][11]
					size1 = ne1 - ns1
					if (ns1 <= ns <= ne <= ne1)\
					or (ns <= ns1 <= ne <= ne1 and (score <= score1 or size <= size1)\
					and (ne - ns1 > 0))\
					or (ns1 <= ns <= ne1 <= ne and (score <= score1 or size <= size1)\
					and (ne1 - ns > 0)):
						break
			if j == len(x) - 1:
				result.append(x[i])
	return result

#remove duplicated records on negative chain
def rm_dup_neg(data):
	result = []
	for x in data:
		for i in range(len(x)):
			(ne, ns) = x[i][8:10]
			score = x[i][11]
			size = ne - ns
			for j in range(len(x)):
				if j == i:
					continue
				else:
					(ne1, ns1) = x[j][8:10]
					score1 = x[j][11]
					size1 = ne1 - ns1
					if (ns1 <= ns <= ne <= ne1)\
					or (ns <= ns1 <= ne <= ne1 and (score <= score1 or size <= size1)\
					and (ne - ns1 > 0))\
					or (ns1 <= ns <= ne1 <= ne and (score <= score1 or size <= size1)\
					and (ne1 - ns > 0)):
						break
			if j == len(x) - 1:
				result.append(x[i])
	return result

#prepare the labels for the inital blast results
columns = ['A','B','C','D','E','F','G','H','I','J','K','L']
#read the inital results
initdata = pd.read_table('res',sep='\t',header=None,names=columns)

#gain the positive records from inital results
positive = initdata[initdata.I - initdata.J < 0]
#gain the negative records from inital results
negative = initdata[initdata.I - initdata.J > 0]
#write the positive records
positive.to_csv('positive',sep='\t',header=False,index=False)
#write the positive records
negative.to_csv('negative',sep='\t',header=False,index=False)

#achieve the classifyed data by scanfold on positive chain
pos_group = group_by_scanfold(positive)
#achieve the classifyed data by scanfold on negative chain
neg_group = group_by_scanfold(negative)

#remove the duplicated records on positive chain
pos_rm_dup = rm_dup_pos(pos_group)
#remove the duplicated records on negative chain
neg_rm_dup = rm_dup_neg(neg_group)

#write the positive records which have removed duplicated results(format : list)
pd.DataFrame(pos_rm_dup).to_csv('positive_rm_dup',sep='\t',header=False,index=False)
#write the positive records which have removed duplicated results(format : list)
pd.DataFrame(neg_rm_dup).to_csv('negative_rm_dup',sep='\t',header=False,index=False)

#gain the positive records which have removed duplicated results(format : DataFrame)
positive_rm_dup = pd.read_table('positive_rm_dup',sep='\t',header=None,names=columns)
#get the records grouped by protein name and scanfold on positive chain
positive_merge_group = group(positive_rm_dup)
#merge the neighbors which have short distance(<100bp) on positive chain
positive_result = merge_pos(positive_merge_group)

#gain the positive records which have removed duplicated results(format : DataFrame)
negative_rm_dup = pd.read_table('negative_rm_dup',sep='\t',header=None,names=columns)
#get the records grouped by protein name and scanfold on negative chain
negative_merge_group = group(negative_rm_dup)
#merge the neighbors which have short distance(<100bp) on negative chain
negative_result = merge_neg(negative_merge_group)

#merge the positive results and negative results as one DataFrame
result = pd.concat([pd.DataFrame(positive_result),pd.DataFrame(negative_result)],axis=0)
result.columns = columns
#sort the result by the scores and output the result
result.sort_values(by='L',ascending=False).to_csv('result',sep='\t',header=False,index=False)
