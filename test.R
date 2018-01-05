#去除标题列的干扰【前两列】 
data2<-data[,3:67] 

#随机抽取至少 5 列数据
n=5
#得到列名称【标题行】 
col.name=colnames(data2) 
#按列随机抽样
sam.col.name = sample(col.name,n,replace=F) #查看抽样结果
sam.col.name 

#按行随机抽样
row.name=rownames(data2)
sam.row.name = sample(row.name,n,replace=F)

#提取子数据集
sub.data <- data2[, sam.col.name]