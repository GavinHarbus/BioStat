##统计案例
## 目录
* [国民幸福指数的代理性测量指标统计结果](#1)
* [基因表达谱 GDS4794](#2)
* [等位基因 + 不同基因型（ 高血压组 vs. 对照组 ）](#3)
* [基因表达谱 GDS6100](#4)
* [Health Breakfast 健康早餐](#5)
* [探索经纬度与温度变化的关系](#6)
* [学生成绩](#7)
* [非参数统计](#8)
* [其他](#9)

## <a id="1"></a>1 国民幸福指数的代理性测量指标统计结果
```
（1. 数据文档读取；2.分类数据提取；3. 均值和标准差计算；4. 最关心指标的筛选（order）；5.并集／交集运算；6.绘制维恩图）

1. 数据文档读取:

#设定 R 的工作路径
setwd("/Users/apple1/Documents/R workspace")
#数据文件
infile = "1-国民幸福指数-代理性测量指标统计.csv"
#读入数据
mydata = read.table(infile,header=TRUE,sep="\t")
#转换格式-有些情况下有必要
mydata <- as.data.frame(mydata)
#查看前 10 行
head(mydata,10)
#查看列名
colnames(mydata)

2.分类数据提取：

#男女总人数
total <- subset(mydata,Class.ID=="0") 
#查看内容
total
#第一类是事业方面的人数
x1 <- subset(mydata,Class.ID=="1") 
#其他方面人数
x2 <- subset(mydata,Class.ID=="2") 
x3 <- subset(mydata,Class.ID=="3") 
x4 <- subset(mydata,Class.ID=="4") 
x5 <- subset(mydata,Class.ID=="5") 

#示例查看x1内容
x1

3. 均值和标准差计算

#分别计算男女在事业方面的关注比例【均值】 
fp1 <- mean(x1[,4]) /total[,4]
mp1 <- mean(x1[,5]) /total[,5]

fp2 <- mean(x2[,4]) /total[,4]
mp2 <- mean(x2[,5]) /total[,5]

fp3 <- mean(x3[,4]) /total[,4]
mp3 <- mean(x3[,5]) /total[,5]

fp4 <- mean(x4[,4]) /total[,4]
mp4 <- mean(x4[,5]) /total[,5]

fp5 <- mean(x5[,4]) /total[,4]
mp5 <- mean(x5[,5]) /total[,5]


#分别计算男女在事业方面的关注比例【标准差】 
fsd1 <- sd(x1[,4]) /total[,4]
msd1 <- sd(x1[,5]) /total[,5]

fsd2 <- sd(x2[,4]) /total[,4]
msd2 <- sd(x2[,5]) /total[,5]

fsd3 <- sd(x3[,4]) /total[,4]
msd3 <- sd(x3[,5]) /total[,5]

fsd4 <- sd(x4[,4]) /total[,4]
msd4 <- sd(x4[,5]) /total[,5]

fsd5 <- sd(x5[,4]) /total[,4]
msd5 <- sd(x5[,5]) /total[,5]

#或 fsd1 <- sd(x1[,4] /total[,4])

4. 最关心指标的筛选:
4.1 所有人共同最关心的前10个指标

#计算每个栏目的人数之和 
mydata[,6] <- mydata[,4] + mydata[,5] 
#命名该列为 Sum
names(mydata)[6] = 'Sum'
#查看前 10 行
head(mydata,10)

#按照 Sum 列进行排序
mix_order <- mydata[order(-mydata$Sum),] 
#查看前 10 行
head(mix_order,10)
#提取前 10 个所有人最关心子栏目名称
mix_set = mix_order[2:11,3]
#查看
mix_set


4.2 女性共同最关心的前10个指标

#根据女性数据行(Female.count)进行排序 
female_order <- mydata[order(-mydata$Female.count),] 
#查看前 10 行
head(female_order,10)
#提取前 10 个女性最关心子栏目名称
female_set = female_order[2:11,3]
#查看
female_set

4.3 男性共同最关心的前10个指标

#根据男性数据行(Female.count)进行排序 
male_order <- mydata[order(-mydata$Male.count),] #查看前 10 行
head(male_order,10).
#提取前 10 个男性最关心子栏目名称
male_set = male_order[2:11,3]
#查看
male_set



5. 男性和女性关注点的异同之处: 

5.1 并集计算:
set_u2 <- union(female_set,male_set) 
set_u2

5.2 交集计算:
set_i2 <- intersect(female_set,male_set) 
set_i2


5.3 交集维恩图的绘制

5.3.1 绘制简单维恩图 
#载入 gplots 包
library(gplots)
#绘制简单维恩图 
venn(list(female_set,male_set)) 

#这里应该保存一个结果图片 1



5.3.2 绘制维恩图

#安装 VennDiagram 包 
install.packages("VennDiagram")
#载入 VennDiagram 包 
library(VennDiagram)

#两个集合的交集维恩图定义 
venn.diagram(list(female=female_set,male=male_set),
	filename="VennDiagram_2 _sets.tiff",lwd=1,lty=2,
	col=c('red','green'),fill=c('red','green'),cat.col=c('red','green') )


#集合大小
lenA<-length(female_set) 
lenB<-length(male_set) 
lenAB<-length(intersect(female_set,male_set))
#绘制维恩图 
draw.pairwise.venn(area1=lenA,area2=lenB,cross.area=lenAB,
	category=c('A','B') ,lwd=rep(1,1),lty=rep(2,2),col=c('red','green'),
	fill=c('red','green'),cat.col=c('red','green'))

#这里应该保存一个结果图片 2
```
## <a id="2"></a>2 基因表达谱 GDS4794
```
1.数据读取；2.查看数据相关信息；3.提取数据表；4.随机抽取数据；
5.中心极限定理的验证（绘制概率密度分布图，绘制数据频率分布直方图（频数分布直方图（freq=T），频率分布直方图（freq=F）），频率分布直方图 + 概率密度分布曲线）；
6.集中趋势测度（F频率分布直方图 + 概率密度分布曲线 + 代表各种统计指标的线的添加，对数转换）；
7.离散测度（箱型图，对数转换）；
8.绘制条形图（堆积／不堆积，对数转换）；
9.概率分布曲线的绘制和分析（对数转换）；
10.卡方检验（频数统计，卡方独立性检验/卡方等比例检验，卡方拟合优先度检验）；
11.t检验（提取数据表（分肿瘤和对照组），数据格式转换，等方差和异方差 t 检验的比较，统计绘图（a，b两组数据概率密度分布曲线 + 代表各种统计指标的线的添加））
12.Person相关分析（不同基因表达水平 Pearson 相关系数计算（基因表达谱遍历 + 记录 p.value 和相关系数值(cor)并赋名 ），高相关性基因筛选（ 设定阈值进行筛选 + 计算交集 + 输出结果文件 ））
13.线性回归分析
14.单因素方差分析 ———— 不同基因表达水平之间的单因素方差分析（接13）
15.单因素方差分析 —— 2水平 —— 某个基因在正常和肺癌中的表达水平对比
16.多元线性回归分析
17.Logistic 回归分析 ———— 基于基因表达水平(自变量 xi)的样本类型的 Logistic 回归分析（随机取样分析，差异表达基因分析）
18.聚类分析 ———— 基于肿瘤组和对照组基因表达谱的聚类分析

）


1.数据读取：

（1）网上下载：

#安装 GEOquery
source("http://bioconductor.org/biocLite.R") 
biocLite("GEOquery")
#加载 GEOquery
library(GEOquery)
#从 Genbank 的 GEO Datasets 数据库中下载制定 ID 的表达谱数据
gds4794 <- getGEO("GDS4794")

（2）加载本地的数据：

#安装 GEOquery
source("http://bioconductor.org/biocLite.R") 
biocLite("GEOquery")
#加载 GEOquery
library(GEOquery)

gds4794 <- getGEO(filename='GDS4794')


2.查看数据相关信息：

#查看数据类型
mode(gds4794)
#查看注释信息
Meta(gds4794)$channel_count
Meta(gds4794)$feature_count
Meta(gds4794)$platform
Meta(gds4794)$sample_count
Meta(gds4794)$sample_organism
Meta(gds4794)$sample_type
Meta(gds4794)$title
Meta(gds4794)$type

#查看数据表的列名
colnames(Table(gds4794))

#查看部分数据标内容，前 10 行，前 6 列; （从第三列开始是数据列）
Table(gds4794)[1:10,1:6]




3.提取数据表：

（1）不分肿瘤和对照组：

#从数据类中提取所需数据表 
data<-Table(gds4794) 

#第一列设定为行标题
rownames(data)<-data[,1] 

##查看数据表的行、列数【实验结果中需要记录】 
ncol(data)
#[1] 67
nrow(data)
#[1] 54675 

##去除标题列的干扰【前两列】 
data2<-data[,3:67] 

（2）分肿瘤和对照组：

#从数据类中提取所需数据表 
data<-Table(gds4794)

head(data)
#屏幕回显结果(部分)=》第 1、2 列是标题列

##查看数据表的行、列数【实验结果中需要记录】 
ncol(data)
#[1] 67
nrow(data)
#[1] 54675 

#肿瘤数据
tumor<-data[,3:25]
#正常组织数据
normal<-data[,26:67]

#data 第 1 列设定为 tumor 和 normal 行标题 
rownames(tumor)<-data[,1] 
rownames(normal)<-data[,1]


4.随机抽取数据：


（1）抽取列数据：

#随机抽取至少 5 列数据
n=5
#得到列名称【标题行】 
col.name=colnames(data2)
#按列随机抽样
sam.col.name = sample(col.name,n,replace=F) 
#查看抽样结果【实验结果中需要记录】 
sam.col.name 

##提取子数据集
sub.data <- data2[, sam.col.name]

#或，对于出现 numeric 相关错误警告信息的
sub.data <- as.numeric(unlist(data2[, sam.col.name]))


（2）抽取行数据：

#随机抽取至少 5 行数据
n=5
row.name=rownames(data2)
sam.row.name = sample(row.name,n,replace=F) 

##提取子数据集
sub.data <- data2[, sam.row.name]

#或，对于出现 numeric 相关错误警告信息的
sub.data <- as.numeric(unlist(data2[, sam.col.name]))




5.中心极限定理的验证：

（1）加载本地的数据；
（2）查看数据相关信息；
（3）提取数据表；

（4）抽取列数据：

#随机抽取至少 5 列数据
n=5
#得到列名称【标题行】 
col.name=colnames(data2)
#按列随机抽样
sam.col.name = sample(col.name,n,replace=F) 
#查看抽样结果【实验结果中需要记录】 
sam.col.name 
##提取子数据集
sub.data <- data2[, sam.col.name]


（5）绘制概率密度分布图，查看基因表达谱的数据分布规律：

#计算数据子集的最大、最小值，用作限制横坐标范围 
x1 <- min(sub.data, na.rm=TRUE)
x2 <- max(sub.data, na.rm=TRUE)
#定义纵坐标最大值，根据绘图结果自行调整，最小值固定为 0 
y_max = 7e-4
#绘制概率分布图，不同曲线使用不同颜色 
dnorm_png<-png("dnorm.png")
curve(dnorm(x,mean(sub.data[,i], na.rm=TRUE), sd(sub.data[,i], na.rm=TRUE)),xlim=c(x1,x2), ylim=c(0,y_max), col=rev(rainbow(i)), lwd=3)

for (i in 2:ncol(sub.data))
{
curve(dnorm(x,mean(sub.data[,i], na.rm=TRUE), sd(sub.data[,i], na.rm=TRUE)), add=TRUE , xlim=c(x1,x2), ylim=c(0,y_max), col=rev(rainbow(i)), lwd=3)
}
#保存图片
dev.off()



（6）数据频率分布直方图的绘制，直接看看数据自身大小分布规律：

a<- sub.data[,1] 
#频率频率直方图, 分 100 个 bins 

##count 图
png(file = "gds4794-hist1.png") 
hist(a, freq = T, breaks = 100) 
dev.off()

#Frequency 图
png(file = "gds4794-hist2.png") 
hist(a, freq = F, breaks = 100) 
dev.off()


（7）抽样评估验证中心极限定理
 
#随机抽样 1 次
png(file = "gds4794-hist-sample1.png") 
hist(a[sample(a, 100)], freq = F, breaks = 100) 
dev.off()

#重复抽样 100 次
png(file = "gds4794-hist-sample100.png")
x <- replicate(100, sample(a, size=100, replace = FALSE)) 
hist(x, freq = F, breaks = 100)
dev.off()

#重复抽样 100 次, 绘制均值分布图
png(file = "gds4794-hist-sample100-mean.png") 
x<-replicate(100, mean(a[sample(a, 100)])) 
hist(x, freq = F, breaks = 100)
dev.off()


（8）数据转换的重要性：

采用对数（log）转换后再次进行Frequency图的绘制，并加入概率密度分布曲线

#对数转换(log) 
b<-log(a) 
x1<-min(b,na.rm=TRUE) 
x2<-max(b,na.rm=TRUE) 

#Frequency 图
hist(b, freq = F, breaks = 100)
#概率密度分布图 
curve(dnorm(x,mean(b,na.rm=TRUE),sd(b,na.rm=TRUE)),xlim=c(x1,x2),col="red",l wd=3, add=TRUE)


6.集中趋势测度：
（F频率分布直方图 + 概率密度分布曲线 + 代表各种统计指标的线的添加，对数转换）


（1）加载本地的数据；
（2）查看数据相关信息；
（3）提取数据表；

（4）抽取列数据：

#随机抽取 1 列数据
n=1
#得到列名称【标题行】 
col.name=colnames(data2)
#按列随机抽样
sam.col.name = sample(col.name,n,replace=F) #查看抽样结果【实验结果中需要记录】 
sam.col.name
#提取子数据集
sub.data <- data2[, sam.col.name]
a <-sub.data[sub.data<500] # 只取表达水平低于 500 的数据



（5）计算各种统计指标并绘制统计图：

x1<-min(a,na.rm=TRUE) # 计算最小值 

x2<-max(a,na.rm=TRUE) # 计算最大值 

ave<-mean(a,na.rm=TRUE) # 计算均值 

med<-median(a,na.rm=TRUE) # 计算中位数

ds=density(a,na.rm=TRUE)
mode <- ds$x[which.max(ds$y)]# 连续分布的众数定义为其分布的密度函数峰值对应的取值 

quan<-quantile(a,na.rm=TRUE) # 计算四分位数 (0%,25%,50%,75%,100%) 


dnorm_png<-png("d1-means-medium-mode.png") # 定义图片文档

hist(a, freq = F, breaks = 100) # 绘制频率分布直方图 

curve(dnorm(x,mean(a,na.rm=TRUE), sd(a,na.rm=TRUE)), xlim=c(x1,x2), col="blue", lwd=3, add=TRUE) # 绘制概率分布曲线 

abline(v=ave,lty=3,lwd=3,col="red") # 增加均值线 
abline(v=med,lty=3,lwd=3,col="purple") # 增加中位数线 
abline(v=mode,lty=3,lwd=3,col="green") # 增加众数线 
abline(v=quan,lty=3,lwd=3,col="blue") # 增加四分位数线

dev.off() # 保存图片文档


（6）数据转换后再次绘制以上统计图：

b<- log(a)

x1<-min(b,na.rm=TRUE) # 计算最小值 

x2<-max(b,na.rm=TRUE) # 计算最大值 

ave<-mean(b,na.rm=TRUE) # 计算均值 

med<-median(b,na.rm=TRUE) # 计算中位数

ds=density(b,na.rm=TRUE)
mode <- ds$x[which.max(ds$y)]# 连续分布的众数定义为其分布的密度函数峰值对应的取值 

quan<-quantile(b,na.rm=TRUE) # 计算四分位数 (0%,25%,50%,75%,100%) 


dnorm_png<-png("d2-means-medium-mode.png") # 定义图片文档

hist(b, freq = F, breaks = 100) # 绘制频率分布直方图 

curve(dnorm(x,mean(b,na.rm=TRUE), sd(b,na.rm=TRUE)), xlim=c(x1,x2), col="blue", lwd=3, add=TRUE) # 绘制概率分布曲线 

abline(v=ave,lty=3,lwd=3,col="red") # 增加均值线 
abline(v=med,lty=3,lwd=3,col="purple") # 增加中位数线 
abline(v=mode,lty=3,lwd=3,col="green") # 增加众数线 
abline(v=quan,lty=3,lwd=3,col="blue") # 增加四分位数线

dev.off() # 保存图片文档



7.离散测度：
（箱型图，对数转换）


（1）加载本地的数据；

（2）绘制箱型图：

#对上述 gds4794 的整个数据表，在进行对数(log)转换前后分别绘制一个箱形图，然后对两者之间的异同之处加以分析讨论。

png(file = "boxplot-all.png") 
boxplot(data[,3:67]) 
dev.off()

png(file = "boxplot-all-log2.png") 
boxplot(log(data[,3:67])) 
dev.off()



8.绘制条形图

（1）加载本地的数据；
（2）查看数据相关信息；
（3）提取数据表；

（4）抽取列数据：

#随机抽取至少 5 列数据
n=5
#得到列名称【标题行】 
col.name=colnames(data2)
#按列随机抽样
sam.col.name = sample(col.name,n,replace=F) 
#查看抽样结果【实验结果中需要记录】 
sam.col.name 
a <- data2[, sam.col.name]


（5）两种条形图的绘制：

# 把 a 从大到小分成 10 个区间进行频数统计
# 初始化频数矩阵 
freq = matrix(rep(0,50),10,5) 

for(i in 1:5){
	x <-table(as.numeric(cut(a[,i],10))) 
	y <- as.data.frame(x)
	freq[,i] <- y[,2]
}
colnames(freq)<-colnames(a) # 列名

#不堆积
#besides=T 时,单列数据中的每个值没有堆积起来,相邻排列,众坐标显示的每个数值。
png(file = "barplot.png") 
barplot(t(freq),beside=T,col=rainbow(5))
dev.off()

# 堆积
png(file = "barplot2.png")
barplot(freq,col=rainbow(10))
dev.off()

（6）数据转换后重复绘制两种条形图:

b<-log()

# 把 b 从大到小分成 10 个区间进行频数统计
# 初始化频数矩阵 
freq2 = matrix(rep(0,50),10,5)

for(i in 1:5){
	x <-table(as.numeric(cut(b[,i],10)))
	y <- as.data.frame(x)
	freq2[,i] <- y[,2]
}
colnames(freq2)<-colnames(b) # 列名

#不堆积
#besides=T 时,单列数据中的每个值没有堆积起来,相邻排列,众坐标显示的每个数值。
png(file = "barplot-log.png")
barplot(t(freq2),beside=T,col=rainbow(5))
dev.off()

# 堆积
png(file = "barplot2-log.png")
barplot(freq2,col=rainbow(10))
dev.off()


9.概率分布曲线的绘制和分析：

（1）加载本地的数据；
（2）提取数据表：

data<-Table(gds4794)

##去除标题列的干扰【前两列】 
data2<-data[,3:67] 

（3）对整个数据表进行对数转换：

data3 <- log(data2)

（4）绘制概率分布曲线

x1<-min(data3,na.rm=TRUE) 
x2<-max(data3,na.rm=TRUE) 

y_max<-0.25 
dnorm_png<-png("all-curve.png")

curve(dnorm(x,mean(data2[,1],na.rm=TRUE), sd(data2[,1],na.rm=TRUE)), xlim=c(x1,x2), ylim=c(0,y_max), col=1, lwd=3)

for (i in 2:ncol(data2))
{
curve(dnorm(x,mean(data2[,i], na.rm=TRUE), sd(data2[,i], na.rm=TRUE)), add=TRUE , xlim=c(x1,x2), ylim=c(0,y_max), col=i, lwd=3)
}

dev.off()



10.卡方检验：

（频数统计，卡方独立性检验/卡方等比例检验，卡方拟合优先度检验）


（1）加载本地的数据；

（2）提取数据表；

（3）抽取列数据：

#随机抽取至少 2 列数据
n=2
#得到列名称【标题行】 
col.name=colnames(data2)
#按列随机抽样
sam.col.name = sample(col.name,n,replace=F) 
#查看抽样结果【实验结果中需要记录】 
sam.col.name 
##提取子数据集
sub.data <- data2[, sam.col.name]
#或，对于出现 numeric 相关错误警告信息的
sub.data <- as.numeric(unlist(data2[, sam.col.name]))


（4）频数统计

# 把 sub.data 从大到小分成 10 个区间进行频数统计 
# 初始化频数矩阵
freq = matrix(rep(0,20),10,2) 

for(i in 1:2){
	x <-table(as.numeric(cut(sub.data[,i],10))) 
	y <- as.data.frame(x)
	freq[,i] <- y[,2]
}

colnames(freq)<-colnames(sub.data) # 列名


（5）卡方独立性检验/等比例检验: 

chisq.test(freq,correct=F)

（6）卡方拟合优先度检验 

x<- freq[,1]
p<-freq[,2]/sum(freq[,2])

chisq.test(x, p = p, rescale.p = TRUE) 



11.t检验：

（1）加载本地的数据；
（2）查看数据相关信息：

#查看样本数量 
Meta(gds4794)$sample_count 
#查看列注释信息
Columns(gds4794)
# 用来确定哪些列是肿瘤，哪些列是正常对照
#=》1:23是 small cell lung cancer样本，24:65是normal组织样本



（3）提取数据表（分肿瘤和对照组）；

（4）抽取数据（按行抽取）：

#随机抽取 1 行数据
n=1
#按行随机抽样
row.name = rownames(tumor)
sam.row.name = sample(row.name,n,replace=F)
sam.row.name #查看抽中的数据行【某个基因在不同样本中的表达水平】

#提取子数据集
tumor_expression_level <- tumor[sam.row.name,] 
normal_expression_level <- normal[sam.row.name,]



（5）数据格式转换：

#数据格式转换

#a<-tumor_expression_level 
#b<-normal_expression_level 

a<-unlist(tumor_expression_level) 
b<-unlist(normal_expression_level) 

#a<-as.numeric(unlist(tumor_expression_level)) 
#b<-as.numeric(unlist(normal_expression_level))


（6）计算均值和方差：

a_average<-mean(a,na.rm=TRUE) 
a_sd<-sd(a,na.rm=TRUE) 

b_average<-mean(b,na.rm=TRUE) 
b_sd<-sd(b,na.rm=TRUE) 

a_average
a_sd

b_average
b_sd


（7）等方差和异方差 t 检验的比较


t.test(a,b,var.equal=TRUE) 

t.test(a,b) 

#此例中a,b两组数据方差不同，故等方差和异方差 t 检验所得数值结果不同



（8）统计绘图（a，b两组数据概率密度分布曲线 + 代表各种统计指标的线的添加）

x1=min(a,b)
x2=max(a,b)
y1=0
y2=0.1

png(file = "t_test_1DEG.png")

curve(dnorm(x,mean(a,na.rm=TRUE), sd(a,na.rm=TRUE)), xlim=c(x1,x2), ylim=c(y1,y2), col="blue", lwd=3)

abline(v=a_average,lty=3, lwd=3, col="blue") 
abline(v=a_average+a_sd, lty=3, lwd=3, col="blue") 
abline(v=a_average-a_sd, lty=3, lwd=3, col="blue") 

curve(dnorm(x,mean(b,na.rm=TRUE), sd(b,na.rm=TRUE)), add=TRUE, xlim=c(0,100), ylim=c(0,0.04), col="red", lwd=3)

abline(v=b_average, lty=3, lwd=3, col="red") 
abline(v=b_average+b_sd, lty=3, lwd=3, col="red") 
abline(v=b_average-b_sd, lty=3, lwd=3, col="red")

dev.off()




12.Person相关分析


（1）加载本地的数据；
（2）查看数据相关信息；
（3）提取数据表：

library(GEOquery) 
gds4794 <- getGEO(filename='GDS4794') 

data<-Table(gds4794)
head(data) 
ncol(data)
nrow(data)
rownames(data)<-data[,1]


（4）抽取数据（按行抽取）（两行）：

#随机抽取 1 行数据
n=1
#按行随机抽样
set.seed(1)
row.name = rownames(data)


#随机抽取第一个数据行
sam.row.name = sample(row.name,n,replace=F) 
sam.row.name 

#获取随机抽取的行数据
a <- unlist(data[sam.row.name,3:67]) 

#获取行对应的基因名称
gene_name_a <- as.character(data[sam.row.name,2]) 
gene_name_a



#随机抽取第二个数据行
sam.row.name2 = sample(row.name,n,replace=F) 
sam.row.name2 

#获取随机抽取的行数据
b <- unlist(data[sam.row.name2,3:67])



（5）pearson 相关系数计算及显著性检验

cor.test(a,b, method="pearson")

x <- cor.test(a,b, method="pearson")

x[] 
#查看pearson相关系数检验函数计算结果的数据结构





（6）不同基因表达水平 Pearson 相关系数计算（基因表达谱遍历 + 记录 p.value 和相关系数值(cor)并赋名 ）

#本次实验重点关注 x$p.value 和 x$estimate 两项数值

#变量初始化，用来存放计算结果中的 p.value 和相关系数 cor 值 
p=NULL
r=NULL


#基因表达谱遍历
for(i in 1:nrow(data)) {
       if(rownames(data)[i] != sam.row.name)
       {
			b <- unlist(data[i,3:67])
			
			#pearson 相关系数计算及显著性检验
			x <- cor.test(a,b, method="pearson") 
			p <- c(p,x$p.value)
			r <- c(r,x$estimate)
       } 
}


#每个统计量对应的基因名称 
gene_names<-data[,2]
#删除一开始所选基因名称
gene_names2 <- gene_names[-match(gene_name_a,gene_names)] 
names(p)<- gene_names2
names(r)<- gene_names2

#对于多探针基因，上述修正方法还需改进： 换成探针 ID 来分析，然后再转成基因名称

#l<-which(rownames(data)==sam.row.name)
#datanew<-data[-l,]
#names(p)<-datanew[,2] 
#names(r)<-datanew[,2]



（7）高相关性基因筛选（ 设定阈值进行筛选 + 计算交集 + 输出结果文件 ）

#设定阈值进行筛选 
p_value = 0.01 
r_cutoff = 0.6 

#筛选
p2 <- p[p<p_value] 
r2 <- r[r>r_cutoff] 

#查看筛选结果 
length(p2)
length(r2)

#计算 p2 和 r2 相关基因名称的交集 =》与数据行 a 对应基因表达水平具有较高相关性的基因 
genes <- intersect(names(p2),names(r2))
length(genes)
tail(genes)
#[1] "ZSCAN16-AS1" "AI224894"
#[6] NA
#=》最后两个不是
#=》实际应该是 787 个基因 #=》加上所选择的基因，共有 788 个 

#合并有效基因名称
genes2 <-c(gene_name_a,genes[1:787]) 
#输出基因名称
out = "pearson-related-genes"
write.table(genes2,out)




13.线性回归分析


（1）加载本地的数据；
（2）查看数据相关信息；
（3）提取数据表：

library(GEOquery) 
gds4794 <- getGEO(filename='GDS4794') 

data<-Table(gds4794)
head(data) 
ncol(data)
nrow(data)
rownames(data)<-data[,1] 


（4）抽取数据（按行抽取）：

#随机抽取 1 行数据
n=1
set.seed(1)
row.name = rownames(data)
sam.row.name = sample(row.name,n,replace=F) 
sam.row.name 

#获取随机抽取的行数据
a <- unlist(data[sam.row.name,3:67]) 

#获取行对应的基因名称
gene_name_a <- as.character(data[sam.row.name,2]) 
gene_name_a



（5）不同基因表达水平线性回归分析（基因表达谱遍历 + 记录斜率、截距、R2 以及 F 检验的 p.value + 为所有 p.value 和 R2 赋名 ）

p=NULL
r=NULL
xl=NULL
jj=NULL

#基因表达谱遍历
for(i in 1:nrow(data)) {
       if(rownames(data)[i] != sam.row.name)
	       {
				b <- unlist(data[i,3:67])

				#线性回归分析及显著性检验
			    lm.sol <- lm(b~1+a) 

				p <- c(p,pf(as.numeric(summary(lm.sol)$fstatistic[1]), as.numeric(summary(lm.sol)$fstatistic[2]), as.numeric(summary(lm.sol)$fstatistic[3]), lower.tail = FALSE))
				r <- c(r,summary(lm.sol)$r.squared)
				xl<- c(xl,summary(lm.sol)$coefficient[1,1])
				jj<- c(jj,summary(lm.sol)$coefficient[2,1])
			} 
}



#每个统计量对应的基因名称 
gene_names<-data[,2]
#删除一开始所选基因名称
gene_names2 <- gene_names[-match(gene_name_a,gene_names)] 
names(p)<- gene_names2
names(r)<- gene_names2

#对于多探针基因，上述修正方法还需改进： 换成探针 ID 来分析，然后再转成基因名称



（6）高相关性基因筛选（ 设定阈值进行筛选 + 计算交集 + 输出结果文件 ）

#每个统计量对应的基因名称 
datanames <- data[data$ID_REF != sam.row.name,2]
dataids <- data[data$ID_REF != sam.row.name,1]
names(p)<-datanames
names(r)<-datanames
names(jj)<-datanames
names(xl)<-datanames

target <- cbind.data.frame(dataids,datanames,xl,jj,r,p)


#设定阈值进行筛选
p_value = 0.01
r_cutoff = 0.25

#筛选
p2 <- p[p<p_value]
r2 <- r[r>r_cutoff]

#查看筛选结果 
length(p2)
length(r2)


#计算 p2 和 r2 相关基因名称的交集 =》与数据行 a 对应基因表达水平具有较高相关性的基因 

result <- target[target$p<p_value & target$r>r_cutoff,1:6]

colnames(result)<-c("gene ID","gene_name","斜率","截距","R2","p.value")

#输出含有所筛选基因相关信息的数据表
out = "genes.csv"
write.csv(result,out)



14.单因素方差分析————不同基因表达水平之间的单因素方差分析（接13）

（1）数据准备：

#所选基因的数据
x <- unlist(data[sam.row.name,3:67]) 

#查看生成的数据表后发现与所选基因表达水平相关性最高的那个基因为"212457_at"
highest<-"212457_at"
y <- unlist(data[highest,3:67]) 

（2）两个基因的表达水平进行线性回归分析
lm.sol <- lm(y~1+x)
summary(lm.sol)


（3）绘制表达水平的散点图和回归方程

png(file = "liner-regression.png") 

#画散点图 
plot(x,y,lwd=2,main="")


weight_mean=mean(y)
abline(h=y_mean,col="blue")
height_mean=mean(x)
abline(v=x_mean,col="purple") 

#将回归直线方程画在散点图上 
abline(lm.sol,col="red") 

dev.off()


（4）绘制评价回归分析结果中的四张图片
png(file = "liner-regression-2.png") 
par(mfrow=c(2,2))
plot(lm.sol)
dev.off()

（5）单因素方差分析
aov<-aov(y~x)
summary(aov)



15.单因素方差分析 ———— 2水平

 某个基因在正常和肺癌中的表达水平对比

library(GEOquery)
gds4794 <- getGEO(filename='GDS4794')

#查看列注释信息=》用来确定哪些列是肿瘤，哪些列是正常对照
Columns(gds4794)
#=》1:23是 small cell lung cancer样本，24:65是 normal组织样本

#提取所需数据表 
data<-Table(gds4794)

#查看数据表的行、列数 
ncol(data)
#还可以用head(data)来查看 
head(data)

#data第一列设为rownames
rownames(data)<-data[,1]



(1)抽取一个异方差，F检验没有显著差异的数据行

#随机抽取1行数据 
n=1
#按行随机抽样
row.name = rownames(data)
sam.row.name = sample(row.name,n,replace=F) 
sam.row.name #查看抽中的数据行(某个基因在不同样本中的表达水平)


#样本的疾病类型设定为因子 
ge<-data.frame(x<-t(data[sam.row.name,3:67]), A<- factor(Columns(gds4794)$disease.state))
ge

#在进行方差分析之前先对几条假设进行检验，由于随机抽取 ，假设总体满足独立、正态，考察方差齐次性(用bartlett检验)
bartlett.test(x~A,data=ge)
#若p小于等于0.05则方差不齐
#结果异方差，故数据范围重叠。

#强制进行单因素方差分析 
ge.aov<-aov(x~A,data=ge)
summary(ge.aov)

#t检验结果
t.test(ge[1:23,1],ge[24:65,1])


#Ps:对方差的检验用F检验，对均值的检验用t检验
#Ps:对数据进行log转换之后，异方差消失变为方差齐性
#Ps: 如果单因素方差分析时只有两个水平(一个试验组、一个对 照组)，此时与t检验等价。
     H0:两组均值相同 H1:两组均值不同(双尾检验)，或只在一个方向上不同 (单尾


（2）抽取一个齐方差，F检验有显著差异的数据行

#随机抽取1行数据 
n=1
sam.row.name = sample(row.name,n,replace=F) 
sam.row.name 
#查看抽中的数据行(某个基因在不同样本中的表达水平)

#样本的疾病类型设定为因子 
ge2<-data.frame(x<-t(data[sam.row.name,3:67]), A<- factor(Columns(gds4794)$disease.state))
ge2

bartlett.test(x~A,data=ge2)

#绘制箱型图
plot(x~A,data=ge2)

#进行单因素方差分析
ge2.aov<-aov(x~A,data=ge2)
summary(ge2.aov)

#t检验结果
t.test(ge2[1:23,1],ge2[24:65,1])





16.多元线性回归分析

（1）加载本地的数据；
（2）查看数据相关信息；
（3）提取数据表：

#加载本地的数据
library(GEOquery)
gds4794 <- getGEO(filename='GDS4794')

#查看数据类型
mode(gds4794)
#查看注释信息
Meta(gds4794) 
##查看列注释信息=》用来确定哪些列是肿瘤，哪些列是正常对照 
Columns(gds4794)
#1:23 是肺癌，24:65 是正常组织

#提取数据
data<-Table(gds4794)
#查看数据表的列名
colnames(data)
#查看数据表行列数
ncol(data)
#[1] 67
nrow(data)
#[1] 54675
#前面两列是标题列，分别为探针 id 和基因名称
#3:25列是 lung cancer，26:67列是 normal
#第一列探针 IDs 定义为 data 的行标题 
rownnames(data)<-data[,1]


(4)逐个计算数据表中的所有基因在肺癌组和正常组中的差异表达倍数 fold.chage

#变量初始化，用来存放计算结果中的p.value和fold change值 p=NULL
fold.change=NULL
#R 用 Sys.time()可以查看当前系统时间
#程序开始时记录: 
timestart<-Sys.time() 

#基因表达谱遍历
for(i in 1:nrow(data)) {
       a <- unlist(data[i,3:25])
       b <- unlist(data[i,26:67])
       fold.change<-c(fold.change,mean(a,na.rm=TRUE)/mean(b,na.rm=TRUE))
       x<-t.test(a,b)
       p<-c(p,x$p.value)
}
#程序临结束时记录: 
timeend<-Sys.time() 
#程序运行时间:
timeend-timestart
#Time difference of 51.29762 secs


#data 第一列探针名 IDs 作为 p 和 fold.change 的名称 
names(p)<-data[,1]
names(fold.change)<-data[,1]


（5）设定阈值进行筛选 
p_value = 0.01
up = 50 #lung cancer 上调2倍 
down = 0.02 #lung cancer 下调2倍

#筛选
#p值筛选
p2 <- p[p<p_value] 
#查看p值筛选结果
length(p2)
#[1] 17664

#上调基因筛选
fc.up <- fold.change[fold.change>up] 

#下调基因筛选
fc.down <- fold.change[fold.change<down] 


#查看上调基因和下调基因筛选后的数量
length(fc.up);length(fc.down) 
#[1] 3
#[1] 143

#符合统计学显著性的上调基因
probes.up<-intersect(names(p2),names(fc.up))  
length(probes.up)
#[1] 3


#符合统计学显著性的下调基因
probes.down<-intersect(names(p2),names(fc.down))  
length(probes.down)
#[1] 13

#合并统计学显著性的上调和下调基因
probes<-union(probes.up,probes.down)  

#上述过程合并进行：probes <- intersect(names(p2),union(names(fc.up),names(fc.down))) 

length(probes)
#[1] 16


#从原始基因表达谱数据表中提取筛选出来的基因数据
sub.data<-data[probes,3:67]  

#设定探针IDs为行标题
rownames(sub.data)<-probes 

nrow(sub.data)
#[1] 16
#加上样本病理类型数据共 17 列

#初始化数据表
data2<-data.frame(matrix(NA,65, 17)) 

#增加样本病理类型分类数据，肺癌=1，其他正常=2 
data2[,1]<-c(rep(1,23),rep(2,42)) 

#后面16列存放筛选出来的基因数据，注意矩阵行列转换 
data2[,2:17]<-t(sub.data) 

#设定列标题
colnames(data2)<-c("y",paste("x",1:16,sep="")) 
#如果筛选的基因数量过多，接下来则无法进行下去

#将所有数据列两两组合绘制散点图和拟合曲线，看看不同数据列之间的关联 
png("lec10_gds4794_pairs.png")
pairs(data2,panel=panel.smooth)
dev.off()

#以样本类型为因变量 y，其他所有基因表达式水平为自变量 x1..1234，进行总体回归分析 
lm0<-lm(y~.,data=data2)
summary(lm0)

#向后逐步回归法
lm.step<-step(lm0,direction="backward")
summary(lm.step)

#通过查找 rownames(sub.data) 找出模型中的对应探针 IDs
#在通过探针 IDs 在 data 中找到原始数据行，其中还有基因名称 
#然后随机提起某个样本中和回归模型中的对应基因的表达水平，预测 y 值(predict)， 看看结果如何?

#查看回归结果的统计图谱:
png(file = "lec10_gds4794_lm_data.png") 
#同一个图形文件中绘制2*2=4个图像 
par(mfrow=c(2,2)) 
plot(lm.step)
dev.off()

#多重共线性分析: 
library(car) 
vif(lm.step)

#检查离群点、高杠杆点、强影响点，保存屏幕反馈结果(如果有的话)和统计图:
#car 包里 influencePlot()函数能一次性同时检查离群点、高杠杆点、强影响点。 
png("lec10_gds4794_influencePlot.png")
influencePlot(lm.step,id.method = "identity", main="Influence Plot", sub="Circle size is proportional to Cook's distance")
dev.off()


17.Logistic 回归分析 ———— 基于基因表达水平(自变量 xi)的样本类型的 Logistic 回归分析

尝试把不同样本作为因变量(y)，几万个基因表达水平作为自 变量(x1，2，...)，进行探讨。


2.1、数据读取:

 

（1）加载本地的数据；
（2）查看数据相关信息；
（3）提取数据表：

#加载本地的数据
library(GEOquery)
gds4794 <- getGEO(filename='GDS4794')

#查看数据类型
mode(gds4794)
#查看注释信息
Meta(gds4794) 
##查看列注释信息=》用来确定哪些列是肿瘤，哪些列是正常对照 
Columns(gds4794)
#1:23 是肺癌，24:65 是正常组织

#提取数据
data<-Table(gds4794)
#查看数据表的列名
colnames(data)
#查看数据表行列数
ncol(data)
#[1] 67
nrow(data)
#[1] 54675
#前面两列是标题列，分别为探针 id 和基因名称
#3:25列是 lung cancer，26:67列是 normal
#第一列探针 IDs 定义为 data 的行标题 
rownnames(data)<-data[,1]

（4）随机取样分析：

至少有 3 个基因的表达水平回归分析结果达到 0.05 的显著水平。

#随机抽取至少 10 行数据
n=10 
#按行随机抽样
row.names<-rownames(data)
sam.row.name <- sample(row.names,n,replace=F)
#查看抽中的数据行探针id
sam.row.name 

#提取抽样数据
subdata<-data[sam.row.name,3:67] 

#加上样本病理类型数据共 n+1 列 。
#初始化数据表
data2<-data.frame(matrix(NA,65, n+1))
#增加样本病理类型分类数据，肺癌=1，其他正常=0
data2[,1]<-c(rep(1,23),rep(0,42))

#后面n列存放筛选出来的基因数据，注意矩阵行列转换
data2[,2:(n+1)]<-t(log(subdata)) 

#设定列标题y,x1,x2,...,x10
colnames(data2)<-c("y",paste("x",1:n,sep="")) 


#以样本类型为因变量 y，其他所有基因表达式水平为自变量 x1,x2,...x10，进行总体回归分析
glm0<-glm(y~.,family=binomial(link='logit'),data=data2)
summary(glm0)

#向后逐步回归法 
glm.step<-step(glm0,direction="backward") 
summary(glm.step)

#绘制回归评估的 4 张图 
png(file = "glm4.png") 
par(mfrow=c(2,2)) 
plot(glm.step) 
dev.off()

#car 包里的 influencePlot()函数能一次性同时检查离群点、高杠杆点、强影响点 
library(car)
png("influencePlot.png")
influencePlot(glm.step,id.method = "identity", main="Influence Plot", sub="Circle size is proportional to Cook's distance")
dev.off()

#绘制 subdata 的热图 
colnames(subdata)<-Columns(gds4794)$disease.state 
png(file = "heatmap1.png") 
heatmap(as.matrix(log(subdata)), Rowv = NA, Colv = NA) 
dev.off()



（5）差异表达基因分析 + 混合上调和下调基因进行 Logistic 回归分析:

#变量初始化，用来存放计算结果中的p.value和fold change值 
p=NULL
fold.change=NULL

#R 用 Sys.time()可以查看当前系统时间
#程序开始时记录: 
timestart<-Sys.time() 

#基因表达谱遍历
for(i in 1:nrow(data)) {
       a <- unlist(data[i,3:25])
       b <- unlist(data[i,26:67])
       fold.change<-c(fold.change,mean(a,na.rm=TRUE)/mean(b,na.rm=TRUE))
       x<-t.test(a,b)
       p<-c(p,x$p.value)
}

#程序临结束时记录:
timeend<-Sys.time() 
#程序运行时间:
timeend-timestart
#Time difference of 51.29762 secs

#data 第一列探针名 IDs 作为 p 和 fold.change 的名称 
names(p)<-data[,1]
names(fold.change)<-data[,1]

#设定阈值进行筛选
p_value = 0.01
#lung cancer 上调2倍
up = 50 
#lung cancer 下调2倍 
down = 0.02 

#筛选
#p值筛选
p2 <- p[p<p_value]
#上调基因 
fc.up <- fold.change[fold.change>up] 
#下调基因 
fc.down <- fold.change[fold.change<down] 

#查看筛选结果
length(p2); length(fc.up); length(fc.down) 

#交集计算
#符合统计学显著性的上调基因 
probes.up<-intersect(names(p2),names(fc.up)) 
length(probes.up)
#符合统计学显著性的下调基因
probes.down<-intersect(names(p2),names(fc.down)) 
length(probes.down)



#合并统计学显著性的上调和下调基因
probes<-union(probes.up,probes.down)

#上述过程合并进行：probes <- intersect(names(p2),union(names(fc.up),names(fc.down))) 

length(probes)

#从原始基因表达谱数据表中提取筛选出来的基因数据
subdata2<-data[probes,3:67] 

#设定探针IDs为行标题
rownames(subdata2)<-probes 

nrow(subdata2)
#如果筛选的基因数量过多，接下来则无法进行下去

#加上样本病理类型数据共 17 列
#初始化数据表
data3<-data.frame(matrix(NA,65, 17))
#增加样本病理类型分类数据，肺癌=1，其他正常=0 
data3[,1]<-c(rep(1,23),rep(0,42)) 
#后面16列存放筛选出来的基因数据，注意矩阵行列转换
data3[,2:17]<-t(log(subdata2)) 
#设定列标题
colnames(data3)<-c("y",paste("x",1:16,sep="")) 


#以样本类型为因变量 y，其他所有基因表达式水平为自变量 x1,x2,...，进行总体回归分析
glm0<-glm(y~.,family=binomial(link='logit'),data=data3)
summary(glm0)

glm.step<-step(glm0,direction="backward")
summary(glm.step)

png(file = "lec11_ICU_glm.png") par(mfrow=c(2,2))
plot(glm.step)
dev.off()

#car 包里的 influencePlot()函数能一次性同时检查离群点、高杠杆点、强影响点。 
library(car)
png("influencePlot.png")
influencePlot(glm.step,id.method = "identity", main="Influence Plot", sub="Circle size is proportional to Cook's distance")
dev.off()

#绘制 subdata2 的热图 
colnames(subdata2)<-Columns(gds4794)$disease.state 
png(file = "heatmap.png") 
heatmap(as.matrix(log(subdata2)), Rowv = NA, Colv = NA) 
dev.off()


18.聚类分析 ———— 基于肿瘤组和对照组基因表达谱的聚类分析


（1）加载本地的数据；
（2）查看数据相关信息；
（3）提取数据表：

#加载本地的数据
library(GEOquery)
gds4794 <- getGEO(filename='GDS4794')

#查看数据类型
mode(gds4794)
#查看注释信息
Meta(gds4794) 
##查看列注释信息=》用来确定哪些列是肿瘤，哪些列是正常对照 
Columns(gds4794)
#1:23 是肺癌，24:65 是正常组织

#提取数据
data<-Table(gds4794)
#查看数据表的列名
colnames(data)
#查看数据表行列数
ncol(data)
#[1] 67
nrow(data)
#[1] 54675
#前面两列是标题列，分别为探针 id 和基因名称
#3:25列是 lung cancer，26:67列是 normal
#第一列探针 IDs 定义为 data 的行标题 
rownnames(data)<-data[,1]


（4）差异表达基因筛选:
按照基因(探针)表达水平采用 t 检验进行统计分析，计算差异显著性 p 值， 以及差异表达倍数(肺癌/正常);
设定好筛选的 p 值和上、下调倍数；
按照设定阈值，筛选出区别这两组样本的主要基因(探针); 
提取这些差异表达基因的表达水平数据。


#变量初始化，用来存放计算结果中的p.value和fold change值 
p=NULL
fold.change=NULL

#R 用 Sys.time()可以查看当前系统时间
#程序开始时记录: 
timestart<-Sys.time() 

#基因表达谱遍历
for(i in 1:nrow(data)) {
       a <- unlist(data[i,3:25])
       b <- unlist(data[i,26:67])
       fold.change<-c(fold.change,mean(a,na.rm=TRUE)/mean(b,na.rm=TRUE))
       x<-t.test(a,b)
       p<-c(p,x$p.value)
}

#程序临结束时记录:
timeend<-Sys.time() 
#程序运行时间:
timeend-timestart
#Time difference of 51.29762 secs

#data 第一列探针名 IDs 作为 p 和 fold.change 的名称 
names(p)<-data[,1]
names(fold.change)<-data[,1]

#设定阈值进行筛选
p_value = 0.05
up = 35 
down = 1/35

#筛选
#p值筛选
p2 <- p[p<p_value]
#上调基因 
fc.up <- fold.change[fold.change>up] 
#下调基因 
fc.down <- fold.change[fold.change<down] 
#查看筛选结果
length(p2); length(fc.up); length(fc.down) 

#交集计算
#符合统计学显著性的上调基因 
probes.up<-intersect(names(p2),names(fc.up)) 
length(probes.up)
#符合统计学显著性的下调基因
probes.down<-intersect(names(p2),names(fc.down)) 
length(probes.down)


#合并统计学显著性的上调和下调基因
probes<-union(probes.up,probes.down)

#上述过程合并进行：probes <- intersect(names(p2),union(names(fc.up),names(fc.down))) 

length(probes)


#从原始基因表达谱数据表中提取筛选出来的基因数据
subdata2<-data[probes,3:67] 

#设定探针IDs为行标题
rownames(subdata2)<-probes 

nrow(subdata2)

（5）数据标准化前后的对比:
   注意表达水平数据矩阵的行列转换，原数据矩阵列为样本，行为基因(探针)，
   后续分析需要进行行列转置。

#数据标准化，除以方差
subdata2<-scale(t(subdata), center=T, scale=T)

#使用数据编号代替样本名称
rownames(subdata2)<-rep(1:65) 

subdata2

png("lec12_gds4794_clustering_boxplot1.png",width=600*3,height=300*3,res=72*3) 
par(mfrow=c(1,2),las=2)
#数据标准化前
boxplot(t(subdata))
#数据标准化后
boxplot(subdata2)
dev.off()


（6）层次聚类：

根据标准化的基因表达水平计算不同样本之间的距离，然后按照“最短距离”策略急性层次聚类分析。

d<-dist(subdata2, method = "euclidean")
#r语言中使用hclust(d, method = "complete", members=NULL) 来进行层次聚类。 
hc<-hclust(d,"single") 
png("lec12_gds4794_clustering_tree_plot.png",width=600,height=300) 
plot(hc)
dev.off()


（7）确定分类：

根据层次聚类的绘图结果，自己选择合适的分类参数 k 来确定分类结果，并对分类结果加以探讨。

#使用rect.hclust(tree, k = NULL, which = NULL, x = NULL, h = NULL,border = 2, cluster = NULL)来确定类的个数。 
#tree 就是求出来的对象。k 为分类的个数，h 为 类间距离的阈值。
#border 是画出来的颜色，用来分类的 。

png("lec12_gds4794_clustering_tree_plot2.png", width=600,height=300)
plot(hc)
rect.hclust(hc,k=2)
dev.off()

#该函数可以用来提取每个样本的所属类别
result=cutree(hc,k=3) 
result
```
## <a id="3"></a>3 等位基因 + 不同基因型（ 高血压组 vs. 对照组 ）
```
1.Kappa一致性测量，
2.卡方独立性检验／卡方等比例检验，
3.卡方拟合优先度检验
4.计算风险比(RR)、几率比(OR)、使用概率计算的几率比(OR’)
5.样本量的计算：



1.Kappa一致性测量：

install.packages("vcd")
library(vcd)

#等位基因
x<-cbind(c(115,103),c(121,180)) #第一列为高血压组，第二列为对照组 
Kappa(x)


#不同基因型
y<-cbind(c(17,197,4),c(48,146,107))
Kappa(y)


2.卡方独立性检验／卡方等比例检验：

#等位基因
x<-cbind(c(115,103),c(121,180))
chisq.test(x,correct=T)

#不同基因型
y<-cbind(c(17, 197, 4), c(48, 146, 107))
chisq.test(y,correct=T)


3.卡方拟合优先度检验：

#等位基因
x<-c(121,180) #对照组人数
p<-c(52.9,47.1) #高血压组等位基因频率
chisq.test(x, p = p, rescale.p = TRUE) 


#不同基因型
y<-c(48,146,107) #对照组人数
p<-c(7.8,90.4,1.8) #高血压组基因型频率
chisq.test(x, p = p, rescale.p = TRUE)


4.如果原始列联表数据不是 2*2 类型，则根据数据分布特征转成 2*2 类型;
假定疾病风险因素为暴露因素(E+)，而后计算风险比(RR)、几率比(OR)、使用概率计算的几率比(OR’)。


（1）根据暴露因素，将数据转换成 2*2 列联表：

		高血压组 (D+) 对照组 (D-)  合计
IV(E+)      197      146        343
II+VV(E-)    21      155        176
合计         218      301        519


（2）计算：

RR = (197/343)/(21/176) = 4.81355
OR = (197*155)/(21*146) = 9.95923
p1=p(D+|E+)=50/550 = 0.091 =》odds1 = p1(1-p1) = 0.083 
p2=p(D+|E-)=20/1020 = 0.020 =》odds2 = p2(1-p2) = 0.020 
OR‘ = odds1/odds2 = 4.15


5.样本量的计算：

Ps：π为表中对应的等位基因／基因型频率，即括号中的数字

调查高血压组中IV基因型的比例(± 5%区间)，α=0.05，π=0.9
n = (1.96/0.05)2 × (0.9×0.1) = 138.2976 ≈ 139 

调查高血压组中IV基因型的比例(± 2.5%区间)，α=0.05，π=0.9 
n = (1.96/0.025)2 × (0.9×0.1) = 553.1904 ≈ 554 
=》要求比例越接近真实情况，样本量需求越大 

调查对照组中IV基因型的比例(± 2.5%区间)，α=0.05，π=0.5
n = (1.96/0.025)2 × (0.5×0.5) = 1536.64 ≈ 1537
=》不同基因型比例分布越均匀，样本量需求越大
```
## <a id="4"></a>4 基因表达谱 GDS6100
```
（1.双因素方差分析；2.基因表达谱数据中的协方差分析）

1.双因素方差分析：

数据表中一共涉及两种不同的因素，分别是 protocol 和 time。

（1）加载本地的数据：

library(GEOquery)
#从Genbank的GEO Datasets数据库中下载制定ID的表达谱数据
gds6100 <- getGEO("GDS6100")
#加载本地的数据：gds6100 <- getGEO(filename='GDS6100')

（2）查看数据相关信息：

#查看数据类型
mode(gds6100)

#查看注释信息
Meta(gds6100) 

#查看列注释信息=》用来确定哪些列是肿瘤，哪些列是正常对照 
Columns(gds6100)

（3）提取数据表：

data<-Table(gds6100)

#查看数据表的列名
colnames(data)

#查看数据表行列数
ncol(data)
#[1] 14
nrow(data)
#[1] 48107
#前面两列是标题列，分别为探针 id 和基因名称
#3:8列是 miRNA135b transfected，9:14列是 scambled transfected 
rownames(data)<-data[,1]


（4）抽取数据（按行抽取）（三种要求）

#随机抽取至少 1 行数据
n=1 

#使用以下代码进行循环测试:
#齐方差、F检验，双因素方差分析中的所有 p>0.1;
#齐方差、F 检验，双因素方差分析中的所有 p<0.1，但交互作用 p>0.1(即无明显交互作用)；
#齐方差、F 检验，双因素方差分析中的所有 p 无要求，但交互作用 p<0.1(即有明显交互作用)。


#按行随机抽样
row.names<-rownames(data)
sam.row.name <- sample(row.names,n,replace=F)
sam.row.name #查看抽中的数据行探针id 

（5）为该行数据设定两个因子，因素 A 为 protocol、因素 B 为 time

ge<-data.frame(x<-t(data[sam.row.name,3:14]), 
	A<- factor(substring(Columns(gds6100)$protocol,1,9)), 
	B<- factor(substring(Columns(gds6100)$time,6)))
ge


（6）对数据 x 进行正态性检验
#正态性检验
shapiro.test(x)


（7）分别对数据 x 和因素 A、B 之间进行方差齐性检验
#方差齐性检验
bartlett.test(x~A,data=ge) 
bartlett.test(x~B,data=ge)


（8）绘制直方图(plot 函数) 和 交互作用图(interaction.plot)，查看数据分布规律;

par(mfrow=c(2,2),las=2, cex.axis=1.2, cex.lab=1.2) 

#绘制直方图
plot(x~A+B,data=ge)

#attach(ge)

#绘制交互作用图
interaction.plot(A,B,x,legend=F) 
interaction.plot(B,A,x,legend=F) 



（9）双因素方差分析(aov 函数)，并查看统计分析结果摘要(summary 函数)：

#不考虑交互作用 
ge.aov<-aov(x~A+B,data=ge) 
summary(ge.aov)

#考虑交互作用
ge.aov2<-aov(x~A*B,data=ge)
summary(ge.aov2)




#Ps：抽样所用代码（便于抽样）
row.names<-rownames(data)
sam.row.name <- sample(row.names,n,replace=F)
sam.row.name 
ge<-data.frame(x<-t(data[sam.row.name,3:14]), 
	A<- factor(substring(Columns(gds6100)$protocol,1,9)), 
	B<- factor(substring(Columns(gds6100)$time,6)))
ge
bartlett.test(x~A,data=ge) 
bartlett.test(x~B,data=ge)
ge.aov<-aov(x~A+B,data=ge) 
summary(ge.aov)
ge.aov2<-aov(x~A*B,data=ge)
summary(ge.aov2)



2.基因表达谱数据中的协方差分析：

将上述 protocol 和 time 中的 time 设定为协变量，然后进行协方差分析;
基本步骤 同上，只是在协方差分析之后，查看 4 张统计评估图。


（1）加载本地的数据：

library(GEOquery)
#从Genbank的GEO Datasets数据库中下载制定ID的表达谱数据
gds6100 <- getGEO("GDS6100")
#加载本地的数据：gds6100 <- getGEO(filename='GDS6100')

（2）查看数据相关信息：

#查看数据类型
mode(gds6100)

#查看注释信息
Meta(gds6100) 

#查看列注释信息=》用来确定哪些列是肿瘤，哪些列是正常对照 
Columns(gds6100)

（3）提取数据表：

data<-Table(gds6100)

#查看数据表的列名
colnames(data)

#查看数据表行列数
ncol(data)
#[1] 14
nrow(data)
#[1] 48107
#前面两列是标题列，分别为探针 id 和基因名称
#3:8列是 miRNA135b transfected，9:14列是 scambled transfected rownames(data)<-data[,1]

（4）抽取数据（按行抽取）（三种要求）

#随机抽取至少 1 行数据
n=1 

#使用以下代码进行循环测试:
#齐方差、F检验，双因素方差分析中的所有 p>0.1;
#齐方差、F 检验，双因素方差分析中的所有 p<0.1，但交互作用 p>0.1(即无明显交互作用)；
#齐方差、F 检验，双因素方差分析中的所有 p 无要求，但交互作用 p<0.1(即有明显交互作用)。


#按行随机抽样
row.names<-rownames(data)
sam.row.name <- sample(row.names,n,replace=F)
sam.row.name #查看抽中的数据行探针id 


（5）为该行数据设定两个因子，因素 A 为 protocol、协变量 x 为 time

ge<-data.frame(y<-t(data[sam.row.name,3:14]), A<-factor(substring(Columns(gds6100)$protocol,1,9)), 
				x<-as.numeric(substring(Columns(gds6100)$time,6)))
ge

（6）对数据 y 进行正态性检验
#正态性检验
shapiro.test(y)

（7）分别对数据 y 和因素 A、协变量 x 之间进行方差齐性检验
#方差齐性检验
bartlett.test(y~A,data=ge)
bartlett.test(y~x,data=ge)


（8）绘制直方图(plot 函数) 和 交互作用图(interaction.plot)，查看数据分布规律;：

par(mfrow=c(2,2),las=2, cex.axis=1.2, cex.lab=1.2)

#绘制直方图
plot(y~x+A,data=ge)

#attach(ge)

#绘制交互作用图
interaction.plot(x,A,y,legend=F)
interaction.plot(A,x,y,legend=F)

（9）双因素方差分析(aov 函数)，并查看统计分析结果摘要(summary 函数)：


#不考虑交互作用
ge.aov<-aov(y~x+A,data=ge)
summary(ge.aov) 
#查看协方差分析后的统计评估图 —— 4 张 
par(mfrow=c(2,2), cex.axis=1.2, cex.lab=1.2) 
plot(ge.aov)

 
#考虑交互作用
ge.aov2<-aov(y~x:A,data=ge)
summary(ge.aov2) 
#查看协方差分析后的统计评估图 —— 4 张 
par(mfrow=c(2,2), cex.axis=1.2, cex.lab=1.2) 
plot(ge.aov2)
```
## <a id="5"></a>5 Health Breakfast 健康早餐
```
1.多元回归分析(不考虑哑变量)；2.多元回归分析(考虑哑变量)）


1.多元回归分析(不考虑哑变量)
（1）读取数据表：
file="Data_Healthy_Breakfast.txt" 
data<-read.table(file,head=TRUE,sep="\t") 

（2）查看数据信息：
head(data)
ncol(data)
#[1] 16
nrow(data)
#[1] 77


（3）两两组合绘制散点图和拟合曲线，从总体上看看不同变量之间的关联
png("lec10_Healthy_Breakfast_pairs.png")
pairs(data[,4:16],panel=panel.smooth)
dev.off()

（4）以“rating”数据列为因变量(y),对其他所有数据列进行多元回归分析，并查看分析结果:
data2=data[,4:16]
lm0<-lm(rating~.,data=data2)
summary(lm0)

（5）以【向后】逐步回归法计算最终多元回归模型(记录逐步回归的结果)，并查看 分析结果(summary),并根据分析结果，写出相应的多元线性方程：
lm.step<-step(lm0,direction="backward")
summary(lm.step)

（6）查看回归结果的统计图谱，通过这四张统计图来讨论回归结果的可靠性：
png(file = "lec10_Healthy_Breakfast_lm_data.png") 
par(mfrow=c(2,2)) 
plot(lm.step)
dev.off()

（7）多重共线性分析: 
理想中的线性模型各个自变量应该是线性无关的，若自变量间存在共线性， 则会降低回归系数的准确性。
一般用方差膨胀因子VIF(Variance Inflation Factor)来衡量共线性。
《统计学习》中认为 VIF 超过 5 或 10 就存在共线性，
《R 语言实战》中认为 VIF 大于 4 则存在共线性。理想中的线性模型 VIF=1，表 完全不存在共线性。

library(car)
vif(lm.step)

（8）检查离群点、高杠杆点、强影响点，保存屏幕反馈结果(如果有的话)和统计图: 
纵坐标超过+2 或小于-2 的点可被认为是离群点，水平轴超过 0.2 或 0.3 的就是高杠杆值(通常为预测值的组合)。
圆圈大小与影响成比例，圆圈很大的点可能是对模型参数的估计造成的不成比例影响的强影响点。

#car 包里 influencePlot()函数能一次性同时检查离群点、高杠杆点、强影响点 
png("lec10_Healthy_Breakfast_influencePlot.png") 
influencePlot(lm.step,id.method = "identity", main="Influence Plot", sub="Circle size is proportional to Cook's distance")
dev.off()

Ps：【可选内容】：（9）针对该数据表，一次性计算所有数据列的相关性，然后选择相关性最高的作为起始自变量，与“rating”进行线性回归分析，
而后采用【向前】逐步回归法进行多元线性回归分析，主要步骤同上。

install.packages("psych")
library(psych)
corr.test(data[,4:16]) #一次性计算第4:16列数据两两之间的相关系数






2.多元回归分析(考虑哑变量)

（1）将该数据表的第 2(mfr)和 3(type)两列数据，转换为哑变量(Proxy and dummy variables)，与4:16列重新组合成一个新的数据表：

#查看第2列数据种类
table(data[,2])
#结果：共 7 种不同分类，设置 6 个哑变量

#查看第3列数据种类
table(data[,3]) 
#结果：共 1 种不同分类，设置 1 个哑变量即可

#故新的数据矩阵共有 16-3+6+1=20列
data2<-data.frame(matrix(NA,77,20))

#哑变量转换
for(i in 1:nrow(data)) {

	#第二列 mfr 分类
	if(data[i,2]=="A")
	{data2[i,1:6]<-c(0,0,0,0,0,0)} 
	if(data[i,2]=="G")
	{data2[i,1:6]<-c(1,0,0,0,0,0)} 
	if(data[i,2]=="K")
	{data2[i,1:6]<-c(0,1,0,0,0,0)} 
	if(data[i,2]=="N")
	{data2[i,1:6]<-c(0,0,1,0,0,0)} 
	if(data[i,2]=="P")
	{data2[i,1:6]<-c(0,0,0,1,0,0)} 
	if(data[i,2]=="Q")
	{data2[i,1:6]<-c(0,0,0,0,1,0)} 
	if(data[i,2]=="R")
	{data2[i,1:6]<-c(0,0,0,0,0,1)} 

	#第三列 type 分类
	if(data[i,3]=="C")
	{data2[i,7]<-0} 
	if(data[i,3]=="H")
	{data2[i,7]<-1}
}

#还要加上原第 4:16 列数据
data2[,8:20]<-data[,4:16]



（2）将原数据表的第一列数据作为新数据表的行标题，列标题作为新数据表相应列的列标题:

rownames(data2)<-data[,1]
colnames(data2)<- c(paste("mfr_",c("G","K","N","P","Q","R"),sep=""),"type_CH",colnames(data)[4:16])
data2 #查看 data2 相关信息是否符合预期格式


（3）将所有数据列两两组合绘制散点图和拟合曲线，看看不同数据列之间的关联：
png("lec10_Healthy_Breakfast_pairs2.png")
pairs(data2,panel=panel.smooth)
dev.off()

（4）以“rating”数据列为因变量(y),对其他所有数据列进行多元回归分析，并查看分析结果：
lm0<-lm(rating~.,data=data2)
summary(lm0)


（5）以【向后】逐步回归法计算最终多元回归模型(记录逐步回归的结果)，并查看 分析结果(summary),并根据分析结果，写出相应的多元线性方程：
lm.step<-step(lm0,direction="backward")
summary(lm.step)

（6）查看回归结果的统计图谱，通过这四张统计图来讨论回归结果的可靠性：
png(file = "lec10_Healthy_Breakfast_lm_data2.png") 
par(mfrow=c(2,2)) 
plot(lm.step)
dev.off()

（7）多重共线性分析: 
理想中的线性模型各个自变量应该是线性无关的，若自变量间存在共线性， 则会降低回归系数的准确性。
一般用方差膨胀因子VIF(Variance Inflation Factor)来衡量共线性。
《统计学习》中认为 VIF 超过 5 或 10 就存在共线性，
《R 语言实战》中认为 VIF 大于 4 则存在共线性。理想中的线性模型 VIF=1，表 完全不存在共线性。

library(car)
vif(lm.step)

（8）检查离群点、高杠杆点、强影响点，保存屏幕反馈结果(如果有的话)和统计图: 
纵坐标超过+2 或小于-2 的点可被认为是离群点，水平轴超过 0.2 或 0.3 的就是高杠杆值(通常为预测值的组合)。
圆圈大小与影响成比例，圆圈很大的点可能是对模型参数的估计造成的不成比例影响的强影响点。

#car 包里 influencePlot()函数能一次性同时检查离群点、高杠杆点、强影响点 
png("lec10_Healthy_Breakfast_influencePlot2.png") 
influencePlot(lm.step,id.method = "identity", main="Influence Plot", sub="Circle size is proportional to Cook's distance")
dev.off()

Ps：【可选内容】：（9）针对该数据表，一次性计算所有数据列的相关性，然后选择相关性最高的作为起始自变量，与“rating”进行线性回归分析，
而后采用【向前】逐步回归法进行多元线性回归分析，主要步骤同上。

install.packages("psych")
library(psych)
corr.test(data[,4:16]) #一次性计算第4:16列数据两两之间的相关系数
```
## <a id="6"></a>6 探索经纬度与温度变化的关系
```
1.多项式回归分析：

（1）数据读取与可视化:
 
file="US_Temperatures_Data_win.txt" 
data<-read.table(file,head=T,sep="\t")
colnames(data)
 
（2）数据可视化
#设定颜色梯度区间
a<-max(data$JanTemp) - min(data$JanTemp) + 1  
png(file = "plot_y_x_t_scatter.png")
cPal <- colorRampPalette(c('green','red'))
Cols <- cPal(a)[as.numeric(cut(data$JanTemp,breaks = a))]

#绘制散点图 
plot(data$Long,data$Lat,pch = 20,col = Cols,cex=2)
dev.off()

（3）局部多项式回归拟合探索: 
在R语言中进行局部多项式回归拟合是利用loess函数。
LOESS的优势是并不需要确定具体的函数形式，而是让数据自己来说话，其缺点在于需要大量的数据和运算能力。
LOESS作为一种平滑技术，其目的是为了探寻响应变量和预测变量之间的关系，所以LOESS更被看作一种数据探索方法，而不是作为最终的结论。 
用loess来建立模型时重要的两个参数是span和degree：
span表示数据子集的获取范围，取值越大则数据子集越多，曲线越为平滑。
degree表示局部回归中的阶 数，1表示线性回归，2表示二次回归(默认)，也可以取0，此时曲线退化为简 单移动平均线。
这里我们设span取0.4和0.8，从下图可见取值0.8的蓝色线条较为平滑。



#JanTemp~Lat拟合
model1=loess(JanTemp~Lat,data=data,span=0.4)
summary(model1)

png(file = "plot_T_Lat_loess.png")
plot(data$JanTemp~data$Lat,pch = 20,col = Cols,cex=2)
lines(data$Lat,model1$fit,col='red',lty=2,lwd=2)
dev.off()




#JanTemp~Long拟合 
model2=loess(JanTemp~Long,data=data,span=0.8) 
summary(model2)

png(file = "plot_T_Long_loess.png")
plot(data$JanTemp~data$Long,pch = 20,col = Cols,cex=2)
lines(data$Long,model2$fit,col='red',lty=2,lwd=2)
dev.off()





#Ps：JanTemp~Lat+Long的二元三次曲面拟合【可选内容】
（三维散点+拟合二元二次曲面）
library(rgl)
#预测脚本 
predictgrid<-function(model,xvar,yvar,zvar,res=16,type=NULL){
  xrange<-range(model$model[[xvar]])
  yrange<-range(model$model[[yvar]])
  newdata<-expand.grid(x=seq(xrange[1],xrange[2],length.out=res),
					   y=seq(yrange[1],yrange[2],length.out=res))
  names(newdata)<-c(xvar,yvar)
  newdata[[zvar]]<-predict(model,newdata=newdata,type=type)
  newdata
}

#x,y,z 转为列表 
df2mat<-function(p,xvar=NULL,yvar=NULL,zvar=NULL){
  if(is.null(xvar)) xvar<-names(p)[1]
  if(is.null(yvar)) yvar<-names(p)[2]
  if(is.null(zvar)) zvar<-names(p)[3]
  x<-unique(p[[xvar]])
  y<-unique(p[[yvar]])
  z<-matrix(p[[zvar]],nrow=length(y),ncol=length(x))
  m<-list(x,y,z)
  names(m)<-c(xvar,yvar,zvar)
  m 
}

#交错出现两个向量元素
interleave<-function(v1,v2) as.vector(rbind(v1,v2))

#拟合二元一次平面 
#mod<-lm(y~x1+x2+x1:x2,data=data)

#拟合二元三次曲面
mod<-lm(JanTemp~Lat+Long+I(Long^2)+I(Long^3),data=data)  

pred_JanTemp<-predict(mod) 
mpgrid_df<-predictgrid(mod,'Lat','Long','JanTemp') 
mpgrid_list<-df2mat(mpgrid_df)

plot3d(data$Lat,data$Long,data$JanTemp,xlab='',ylab='',zlab='',axes=FALSE,size=
.5,type='s',lit=FALSE)

spheres3d(data$Lat,data$Long,pred_JanTemp,alpha=0.4,type='s',size=0.5,lit=FALSE
)

segments3d(interleave(data$Lat,data$Long),
          interleave(data$Long, data$Lat),
          interleave(pred_JanTemp, pred_JanTemp),
          alpha=0.4,col='red'
          )
#预测曲面 
surface3d(mpgrid_list$Lat,mpgrid_list$Long,mpgrid_list$JanTemp,alpha=.4,front=' lines',back='lines')

#其他设置 
rgl.bbox(color='grey50',emission='grey50',xlen=0,ylen=0,zlen=0)
rgl.material(color='black') 
axes3d(edges=c('x--','y+-','z--'), cex=.75) 
mtext3d('Lat',edge='x—',line=2) 
mtext3d('Long',edge='y+-',line=3) 
mtext3d('JanTemp',edge='z—',line=3)


（4）二元线性回归分析:

#二元线性回归的探索 
lm.line<-lm(JanTemp~Lat+Long,data=data) 
summary(lm.line)

#绘图预测
png(file = "plot_y_x_t_lm.png")
par(mfrow=c(2,2))
plot(lm.line)
dev.off()



（5）多项式回归分析：
#Lat为线性，Long为三次项
model <- lm(JanTemp ~ Lat + poly(Long,3),data=data)
summary(model)
 
#模型参数的置信区间 
confint(model, level=0.95)

#拟合VS残差图,如果这是一个拟合效果比较不错的模型，应该看不到任何一种模型的特征
png(file = "plot_T_Lat_Long_model_residuals.png")
par(mfrow=c(2,2))
plot(model)
plot(fitted(model),residuals(model))
dev.off()
```
## <a id="7"></a>7 学生成绩
```
1.主成分分析: 
学生成绩的主成分分析: 
利用教师提供的学生多门课程成绩表，开展主成分分析实践，
看看能够有效地提取反应不同课程成绩分布特征信息的主成分，以及这些主成分能够有效地区分不同学生的学习成绩特点。

（1）读取学生成绩数据：

file="grades"
scores<-read.table(file,head=T,sep="\t") 
colnames(scores)
ncol(scores)
#[1] 25 =》24门课程
nrow(scores)
#[1] 30

#创建数据框 
data<-data.frame(scores[,2:25]) 
colnames(data)<-paste("x",1:24, sep="") 
rownames(data)<-scores[,1]
#查看数据
data 

（2）分析各门课程成绩之间的相关性：
library(psych)
corr.test(data) 



#Ps：（3）绘制 3D 条形图，查看不同学生不同课程成绩分布规律:【可选内容】
#epade 包里面的 bar3d.ade 函数画 3D 条形图，它接受一个矩阵来描述数据。
install.packages("epade")
library(epade)
png("lec12_scores_3d_barplot1.png")
par(las=2,cex=0.8)
bar3d.ade(as.matrix(t(data)),xw=0.8,alpha=0.8)
dev.off()


（4）数据的标准化处理前后的对比：
#原数据: 
png("boxplot1.png") 
boxplot(data,las=2) 
dev.off()

#数据中心化，使其均值变为零【原点】 
data2<-scale(data, center=T,scale=F) 
data2
png("lboxplot2.png") 
boxplot(data2,las=2)
dev.off()
#数据围绕 0 附近波动，但是方差变异很大


#数据标准化，除以方差 
data3<-scale(data, center=T, scale=T) 
data3
png("boxplot3.png") 
boxplot(data3,las=2)
dev.off()

#Ps：（5）标准化数据的正态性检验:【可选内容】 
#看看哪些成绩符合，哪些不符合正态性分布?
apply(data3,2,shapiro.test) 

（6）标准化数据协方差矩阵的计算:
对比 corr.test 结果，看看什么规律?

mc<-cov(data3)
mc


（7）主成分分析(PCA)：
#cor:逻辑变量，若为cor=T表示用 样本的相关矩阵R 作主成分分析；cor=F, 表示用 样本的协方差矩阵 s  作为主成分分析

pca<-princomp(data,cor=T)
pca2<-princomp(data2,cor=T)
pca3<-princomp(data3,cor=T)
#以上几个结果相同，princomp 自动进行上述中心化和标准化处理 

pca



（8）观察主成分分析的摘要信息:

保留变异累计达到 90%(四舍五入)的几个主成分信息。

summary(pca) 

pca[]#查看详细信息
pca$sdev #Standard deviation 
pca$loadings #loading系数矩阵
pca$center #每一门课程均值=》数据中心化 
pca$scale #每一门课程方差=》数据标准化 
pca$scores #每个样本每个组分的得分
pca$loadings #查看loadins信息
pca$loadings[] #查看loadings全部数值 

#计算得到各个样本主成分的数据=》等价于 pca$scores 

pca_data <- predict(pca)


（9）绘图查看主成分的变异贡献度:
#针对 princomp()对象的 plot 方法
#该方法可以绘制展示每个主成分与其自身方差贡献度相关性的悬崖碎石图。 

png("lec12_bar-stone_plot1.png",width=600*3,height=3*300,res=72*3) 

par(mfrow=c(1,2),las=2)

#条形图
plot(pca)
abline(h=1,type="2",col="red")

#主成分的碎石图
screeplot(pca, type="lines")
abline(h=1,type="2",col="red")

dev.off()



（10）绘制得分(scores)图:

了解新变量(主成分)数值对 30 个同学的区分程度到底如何。

#=》主成分分布更为离散=》把 30 个样本区分的更好
#得分图(Score plot) 
png("lec12_15scores_scores_plot6.png",width=600*3,height=3*400,res=72*3) 
par(mfrow=c(2,3))

#主成分分析之后的前四个主成分得分绘图
plot(pca$scores[,1], pca$scores[,2],type="n") 
text(pca$scores[,1],pca$scores[,2],labels=rownames(pca$scores),cex=0.8) 
plot(pca$scores[,1], pca$scores[,3],type="n") 
text(pca$scores[,1],pca$scores[,3],labels=rownames(pca$scores),cex=0.8) 
plot(pca$scores[,1], pca$scores[,4],type="n") 
text(pca$scores[,1],pca$scores[,4],labels=rownames(pca$scores),cex=0.8) 
plot(pca$scores[,2], pca$scores[,3],type="n") 
text(pca$scores[,2],pca$scores[,3],labels=rownames(pca$scores),cex=0.8) 
plot(pca$scores[,2], pca$scores[,4],type="n") 
text(pca$scores[,2],pca$scores[,4],labels=rownames(pca$scores),cex=0.8) 
plot(pca$scores[,3], pca$scores[,4],type="n") 
text(pca$scores[,3],pca$scores[,4],labels=rownames(pca$scores),cex=0.8) 

dev.off()




（11）绘制载荷(loadings)图: 

了解新变量(主成分)与原变量(不同课程)之间的关系。

png("lec12_15scores_loadings_plot6.png",width=600*3,height=3*400,res=72*3) 
par(mfrow=c(2,3))

#主成分分析之后的前四个主成分得分绘图
plot(pca$loadings[,1], pca$loadings[,2],type="n")
text(pca$loadings[,1],pca$loadings[,2],labels=rownames(pca$loadings),cex=0.8)
plot(pca$loadings[,1], pca$loadings[,3],type="n")
text(pca$loadings[,1],pca$loadings[,3],labels=rownames(pca$loadings),cex=0.8)
plot(pca$loadings[,1], pca$loadings[,4],type="n")
text(pca$loadings[,1],pca$loadings[,4],labels=rownames(pca$loadings),cex=0.8)
plot(pca$loadings[,2], pca$loadings[,3],type="n")
text(pca$loadings[,2],pca$loadings[,3],labels=rownames(pca$loadings),cex=0.8)
plot(pca$loadings[,2], pca$loadings[,4],type="n")
text(pca$loadings[,2],pca$loadings[,4],labels=rownames(pca$loadings),cex=0.8)
plot(pca$loadings[,3], pca$loadings[,4],type="n")
text(pca$loadings[,3],pca$loadings[,4],labels=rownames(pca$loadings),cex=0.8)

dev.off()




#Ps：（12）绘制双标图:【可选内容】：

   了解新变量(主成分)与原变量(不同课程)之间关系的同时，查看新变量对
   不同学生的区分程度，以及这些区分主要是有哪些原变量(不同课程)贡献出
   来的。

#choices是选择的主成分，缺省值是第1，第2主成分。
#pc.biplot是逻辑变量，缺省值为 F,当 pc.biplot=T，用 Gabriel 提出的方法绘图 

png("lec12_15scores_biplot6-2.png",width=600*3,height=3*400,res=72*3) 
par(mfrow=c(2,3))
biplot(pca,choices=1:2,pc.biplot=T)
biplot(pca,choices=c(1,3),pc.biplot=T)
biplot(pca,choices=c(1,4),pc.biplot=T)
biplot(pca,choices=2:3,pc.biplot=T)
biplot(pca,choices=c(2,4),pc.biplot=T)
biplot(pca,choices=3:4,pc.biplot=T)
dev.off()
```
## <a id="8"></a>8 非参数统计
```
一）、Wilcoxon 符号秩和检验
1.配对设计资料的符号秩和检验；2.完全随机设计两个独立样本的秩和检验【计量资料】；3.完全随机设计两个独立样本的秩和检验【等级资料】

（二）、Kruskal-Wallis H检验
1.完全随机设计多个独立样本的秩和检验【计量资料】；2.完全随机设计多个独立样本的秩和检验【等级资料】；3.随机区组设计资料(多组)的秩和检验-Friedman 检验

（三）.随机区组设计资料(多组)的秩和检验-Friedman 检验

）



（一）、Wilcoxon 符号秩和检验

1.配对设计资料的符号秩和检验

数据描述（同一组样本用药前后）:
某研究人员使用中药舒心散治疗 21 例冠心病患者，分别于治疗前和治疗后 1 个月检测优球蛋白(ELT)。

试比较用药前后冠心病患者的 ELT 水平有无差别?


（1）数据读取:
     
file="e12-data-1-1-win.txt"
data<-read.table(file,head=T,sep="\t")
data
x<-data[,2];y<-data[,3]


（2）数据可视化观察:

#绘制散点图
png("e12_data-1-1_boxplot.png")
boxplot(data[,2:3])
dev.off()


（3）正态性检验:

shapiro.test(x)
shapiro.test(y)

# p>0.05为服从正态分布


（4）方差齐性检验:

data2<-data.frame(X<-c(data[,2],data[,3]),A<-factor(rep(1:2,c(21,21)))) 


#Bartlett检验 - 如果我们的数据服从正态分布，那么这种方法将是最为适用的。
#对于 正态分布 的数据，这种检验极为灵敏;而当数据为非正态分布时，使用该方法则很容易导致假阳性误判。

bartlett.test(data[,2:3])
#或 bartlett.test(X~A,data=data2)

#Levene 检验 – 相较于 Bartlett 检验，这一方法更为稳健，这一方法被封装于 car 程序包中。

library(car)
leveneTest(X~A,data=data2)

#Fligner-Killeen检验 – 这是一个非参数的检验方法，完全不依赖于对分布的假设
fligner.test(X~A,data=data2)




（5）Wilcoxon 配对符号秩和检验(双侧):

#H0:Md=0，H1:Md≠0
wilcox.test(x, y, paired = TRUE, alternative = "two.sided")



（6）配对 t 检验(等方差双侧检验): 

#H0:μ1=μ2, H1: μ1≠μ2
t.test(x,y, paired = TRUE, var.equal=TRUE, alternative = "two.sided")
 


（7）配对t检验(异方差双侧检验-Welch t检验):

#H0:μ1=μ2, H1: μ1≠μ2
t.test(x,y, paired = TRUE, alternative = "two.sided")






2.完全随机设计两个独立样本的秩和检验【计量资料】

数据描述（用药组和不用药组）: 
某药厂为观察某新药治疗胃溃疡的效果，对已有溃疡的大鼠随机分组后，一组用新药治疗，另一组不用药，
一段时间后分别测定两组大鼠的胃黏膜溃疡面积(cm2)

分析该药是否有效?



（1）数据读取:
     
file="e12-data-1-2-win.txt"
data<-read.table(file,head=T,sep="\t")
data
x<-data[,1];y<-data[,2]


（2）数据可视化观察:

#绘制散点图
png("e12_data-1-2_boxplot.png")
boxplot(data)
dev.off()


（3）正态性检验:

shapiro.test(x)
shapiro.test(y)

# p>0.05为服从正态分布


（4）方差齐性检验:

data2<-data.frame(X<-c(data[,1],data[,2]),A<-factor(rep(1:2,c(9,9))))


#Bartlett检验 - 如果我们的数据服从正态分布，那么这种方法将是最为适用的。
#对于 正态分布 的数据，这种检验极为灵敏;而当数据为非正态分布时，使用该方法则很容易导致假阳性误判。

bartlett.test(data)
#或 bartlett.test(X~A,data=data2)

#Levene 检验 – 相较于 Bartlett 检验，这一方法更为稳健，这一方法被封装于 car 程序包中。

library(car)
leveneTest(X~A,data=data2)

#Fligner-Killeen检验 – 这是一个非参数的检验方法，完全不依赖于对分布的假设

fligner.test(X~A,data=data2)



（5）Wilcoxon 符号秩和检验(单侧):

#H0:M1=M2, H1:M1<M2【单侧】
wilcox.test(x, y, alternative = "less")


（6）t 检验(等方差双侧检验): 

#H0:μ1=μ2, H1:μ1<μ2【单侧】
t.test(x, y, var.equal=TRUE, alternative = "less")


（7）t检验(异方差双侧检验-Welch t检验):

#H0:μ1=μ2, H1:μ1<μ2【单侧】
t.test(x,y, alternative = "less")




3.完全随机设计两个独立样本的秩和检验【等级资料】

数据描述:
用中草药治疗不同类型的小儿肺炎，其疗效分为 4 个等级（控制，显效，有效，无效）

比较该药物对不同类型的小儿肺炎疗效有无差别?



（1）数据读取:
     
file="e12-data-1-3-win.txt"
data<-read.table(file,head=T,sep="\t")
data
x<-data[,2];y<-data[,3]


（2）数据可视化观察:

#绘制散点图
png("e12_data-1-3_boxplot.png")
boxplot(data)
dev.off()

（3）卡方检验：
chisq.test(cbind(x,y))


（4）计量资料转换成秩和检验数据:
x2<-rep(1:4,data[,2])
y2<-rep(1:4,data[,3])

（5）正态性检验:

shapiro.test(x2)
shapiro.test(y2)

# p>0.05为服从正态分布


（6）方差齐性检验:

data2<-data.frame(X<-c(x2,y2),A<-factor(rep(1:2,c(length(x2),length(y2)))))


#Bartlett检验 - 如果我们的数据服从正态分布，那么这种方法将是最为适用的。
#对于 正态分布 的数据，这种检验极为灵敏;而当数据为非正态分布时，使用该方法则很容易导致假阳性误判。

bartlett.test(data2)
#或 bartlett.test(X~A,data=data)

#Levene 检验 – 相较于 Bartlett 检验，这一方法更为稳健，这一方法被封装于 car 程序包中。

library(car)
leveneTest(X~A,data=data2)

#Fligner-Killeen检验 – 这是一个非参数的检验方法，完全不依赖于对分布的假设
fligner.test(X~A,data=data2)


（7）Wilcoxon 符号秩和检验(双侧):

#H0:M1=M2, H1:M1≠M2【双侧】
wilcox.test(x2, y2, alternative = "two.sided")

（8）t 检验(等方差双侧检验): 

#H0:μ1=μ2, H1:μ1≠μ2【双侧】
t.test(x2, y2, var.equal=TRUE, alternative = "two.sided")

（9）t检验(异方差双侧检验-Welch t检验):

#H0:μ1=μ2, H1:μ1≠2【双侧】
t.test(x2,y2, alternative = "two.sided")






（二）、Kruskal-Wallis H检验

1.完全随机设计多个独立样本的秩和检验【计量资料】

数据描述:
某研究组欲研究 A、B 两个菌种对小鼠巨噬细胞功能的激活作用，将 57 只小鼠随机分为三组，
其中一组为生理盐水对照组，用常规巨噬细胞吞噬功能的检测方法，获得三组的吞噬指数如下表:

A、B 两个菌种是否对小鼠巨噬细胞功能产生明显地影响?


（1）数据读取:

file="e12-data-2-1-win.txt"
data<-read.table(file,head=T,sep="\t")
data

（2）数据可视化观察:

png("e12_data-2-1_boxplot.png")
boxplot(data)
dev.off()

（3）正态性检验:

shapiro.test(data[,1])
shapiro.test(data[,2])
shapiro.test(data[,3])

（4）方差齐性检验:
data2<-data.frame(X<-c(data[,1],data[,2],data[,3]),A<- factor(rep(1:3,c(24,24,24))))


#Bartlett检验 - 如果我们的数据服从正态分布，那么这种方法将是最为适用的。对于 正态分布的数据，这种检验极为灵敏;而当数据为非正态分布时，使用该方法则很容 易导致假阳性误判。
bartlett.test(data)
#或 bartlett.test(X~A,data=data2)
#Levene 检验 – 相较于 Bartlett 检验，这一方法更为稳健，这一方法被封装于 car 程序包中。
library(car)
leveneTest(X~A,data=data2)
#Fligner-Killeen检验 – 这是一个非参数的检验方法，完全不依赖于对分布的假设
fligner.test(X~A,data=data2)


（5）Kruskal-Wallis 检验:

install.packages("agricolae") 
library(agricolae)
#H0:M1=M2=M3, H1:三者不等 
kruskal.test(X~A,data=data2)


（6）单因素方差分析:

m<-aov(X~A,data=data2)
summary(m)

（7）多重比较:

mm<-TukeyHSD(m)
mm
png("e12_data-2-1_TurkeyHSD_plot.png")
plot(mm)
dev.off()




2.完全随机设计多个独立样本的秩和检验【等级资料】

数据描述:
使用 3 种不同药物治疗随机分配的三组样本(双盲试验)，治疗 2 周和 4 周后的疗效

任选一个治疗时间，比较不同药物的疗效有无差异?


（1）数据读取:

file="e12-data-2-2-win.txt"
data<-read.table(file,head=T,sep="\t")
data
subdata<-data[1:4,]


（2）数据可视化观察:

png("e12_data-2-2_boxplot.png")
boxplot(subdata[,3:5])
dev.off()

（3）正态性检验:

shapiro.test(x)
shapiro.test(y)
shapiro.test(z)

（4）方差齐性检验:

data2<-data.frame(X<-c(x,y,z),A<- factor(rep(1:3,c(length(x),length(y),length(z)))))


#Bartlett检验 - 如果我们的数据服从正态分布，那么这种方法将是最为适用的。对于 正态分布的数据，这种检验极为灵敏;而当数据为非正态分布时，使用该方法则很容 易导致假阳性误判。
bartlett.test(X~A,data=data2)
#Levene 检验 – 相较于 Bartlett 检验，这一方法更为稳健，这一方法被封装于 car 程序包中。
library(car)
leveneTest(X~A,data=data2)
#Fligner-Killeen检验 – 这是一个非参数的检验方法，完全不依赖于对分布的假设
fligner.test(X~A,data=data2)

（5）卡方检验：
chisq.test(cbind(subdata[,3],data[,4],data[,5]))

（6）计量资料转换成秩和检验数据：
x<-rep(1:4,subdata[,3])
y<-rep(1:4,subdata[,4])
z<-rep(1:4,subdata[,5])


（7）Kruskal-Wallis 检验:

install.packages("agricolae") 
library(agricolae)

#H0:M1=M2=M3, H1:三者不等
#支持list变量
kruskal.test(list(x,y,z))





（三）.随机区组设计资料(多组)的秩和检验-Friedman 检验

数据描述:
在某项实验中，9 名受试对象对四种不同频率声音刺激的反应率(%)结果如下：。。。

比较受试者对不同频率声音刺激的反应率之间有无明显差异?

（1）数据读取:

file="e12-data-3-1-win.txt"
data<-read.table(file,head=T,sep="\t")
data

（2）数据可视化观察:


png("e12_data-3-1_boxplot.png")
boxplot(data[,2:5])
dev.off()

（3）正态性检验:

apply(data[,2:5],2,shapiro.test)

（4）方差齐性检验:

data2<-data.frame(X<-c(data[,2],data[,3],data[,4],data[,5]), A<- factor(rep(1:4,rep(9,4))))

#Bartlett检验 - 如果我们的数据服从正态分布，那么这种方法将是最为适用的。对于 正态分布的数据，这种检验极为灵敏;而当数据为非正态分布时，使用该方法则很容 易导致假阳性误判。
bartlett.test(data[,2:5]) 
#或 bartlett.test(X~A,data=data2)

#Levene 检验 – 相较于 Bartlett 检验，这一方法更为稳健，这一方法被封装于 car 程序包中。
library(car)
leveneTest(X~A,data=data2)

#Fligner-Killeen检验 – 这是一个非参数的检验方法，完全不依赖于对分布的假设
fligner.test(X~A,data=data2)


（5）Friedman 检验:

dm<-as.matrix(data[,2:5])
dimnames(dm) <- list(1:9, c("A", "B", "C", "D"))
friedman.test(dm)

（6）单因素方差分析:

m<-aov(X~A,data=data2)
summary(m)

（7）多重比较:

mm<-TukeyHSD(m)
mm
png("e12_data-3-1_TurkeyHSD_plot.png")
plot(mm)
dev.off()
```
## <a id="9"></a>9 其他
```
（1.等方差和异方差 t 检验的比较；2.单因素方差分析 ———— 5水平；3.多次项曲线的模拟；4.医学和流行病学统计 ———— 可视化统计数据（此处为折线图））



1.等方差和异方差 t 检验的比较


（1）随机生成两组、每组 100 个 0~100 之间的数值，然后分别进行等方差和异方差 t 检 验;


set.seed(1)
a<-seq(0,100,length.out=100)

set.seed(2)
b<-seq(0,100,length.out=100)

t.test(a,b,var.equal=TRUE) 

t.test(a,b) 



#统计绘图（a，b两组数据概率密度分布曲线 + 代表各种统计指标的线的添加）

png(file = "t_test1.png") 

curve(dnorm(x,mean(a,na.rm=TRUE),sd(a,na.rm=TRUE)),xlim=c(0,100),ylim=c(0,0.04) ,col="blue",lwd=3)

abline(v=mean(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 
abline(v=mean(a,na.rm=TRUE)+sd(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 
abline(v=mean(a,na.rm=TRUE)-sd(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 

curve(dnorm(x,mean(b,na.rm=TRUE),sd(b,na.rm=TRUE)),add=TRUE,xlim=c(0,100),ylim= c(0,0.04),col="red",lwd=3)

abline(v=mean(b,na.rm=TRUE),lty=3,lwd=3,col="red") 
abline(v=mean(b,na.rm=TRUE)+sd(b,na.rm=TRUE),lty=3,lwd=3,col="red")
abline(v=mean(b,na.rm=TRUE)-sd(b,na.rm=TRUE),lty=3,lwd=3,col="red")

dev.off()




（2）随机生成两组 0~100 之间的数值(seq 函数)，第一组 100 个数值，第二组 50 个 数值，然后分别进行等方差和异方差 t 检验:

set.seed(1)
a<-seq(0,100,length.out=100)

set.seed(2)
b<-seq(0,100,length.out=50)

t.test(a,b,var.equal=TRUE) 

t.test(a,b) 




#统计绘图（a，b两组数据概率密度分布曲线 + 代表各种统计指标的线的添加）

png(file = "t_test2.png") 

curve(dnorm(x,mean(a,na.rm=TRUE),sd(a,na.rm=TRUE)),xlim=c(0,100),ylim=c(0,0.04) ,col="blue",lwd=3)

abline(v=mean(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 
abline(v=mean(a,na.rm=TRUE)+sd(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 
abline(v=mean(a,na.rm=TRUE)-sd(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 

curve(dnorm(x,mean(b,na.rm=TRUE),sd(b,na.rm=TRUE)),add=TRUE,xlim=c(0,100),ylim= c(0,0.04),col="red",lwd=3)

abline(v=mean(b,na.rm=TRUE),lty=3,lwd=3,col="red") 
abline(v=mean(b,na.rm=TRUE)+sd(b,na.rm=TRUE),lty=3,lwd=3,col="red")
abline(v=mean(b,na.rm=TRUE)-sd(b,na.rm=TRUE),lty=3,lwd=3,col="red")

dev.off()





（3）随机生成两组、每组 100 个的数值，第一组 60~90 之间，第二组 70~80 之间，然后 分别进行等方差和异方差 t 检验:

set.seed(1)
a<-seq(60,90,length.out=100)
set.seed(2)

b<-seq(70,80,length.out=100)

t.test(a,b,var.equal=TRUE) 

t.test(a,b) 




#统计绘图（a，b两组数据概率密度分布曲线 + 代表各种统计指标的线的添加）

png(file = "t_test3.png") 
curve(dnorm(x,mean(a,na.rm=TRUE),sd(a,na.rm=TRUE)),xlim=c(0,100),ylim=c(0,0.15) ,col="blue",lwd=3)

abline(v=mean(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 
abline(v=mean(a,na.rm=TRUE)+sd(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 
abline(v=mean(a,na.rm=TRUE)-sd(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 

curve(dnorm(x,mean(b,na.rm=TRUE),sd(b,na.rm=TRUE)),add=TRUE,xlim=c(0,100),ylim= c(0,0.15),col="red",lwd=3)

abline(v=mean(b,na.rm=TRUE),lty=3,lwd=3,col="red") 
abline(v=mean(b,na.rm=TRUE)+sd(b,na.rm=TRUE),lty=3,lwd=3,col="red")
abline(v=mean(b,na.rm=TRUE)-sd(b,na.rm=TRUE),lty=3,lwd=3,col="red")

dev.off()





（4）随机生成两组、每组 100 个的数值，第一组 50~80 之间，第二组 70~100 之间，然 后分别进行等方差和异方差 t 检验:

set.seed(1)
a<-seq(50,80,length.out=100)

set.seed(2)
b<-seq(70,100,length.out=100)

t.test(a,b,var.equal=TRUE) 

t.test(a,b) 



#统计绘图（a，b两组数据概率密度分布曲线 + 代表各种统计指标的线的添加）

png(file = "t_test4.png")

curve(dnorm(x,mean(a,na.rm=TRUE),sd(a,na.rm=TRUE)),xlim=c(0,150),ylim=c(0,0.05) ,col="blue",lwd=3)

abline(v=mean(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 
abline(v=mean(a,na.rm=TRUE)+sd(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 
abline(v=mean(a,na.rm=TRUE)-sd(a,na.rm=TRUE),lty=3,lwd=3,col="blue") 

curve(dnorm(x,mean(b,na.rm=TRUE),sd(b,na.rm=TRUE)),add=TRUE,xlim=c(0,150),ylim= c(0,0.05),col="red",lwd=3)

abline(v=mean(b,na.rm=TRUE),lty=3,lwd=3,col="red") 
abline(v=mean(b,na.rm=TRUE)+sd(b,na.rm=TRUE),lty=3,lwd=3,col="red")
abline(v=mean(b,na.rm=TRUE)-sd(b,na.rm=TRUE),lty=3,lwd=3,col="red")

dev.off()





2.单因素方差分析 ———— 5水平

试验的目的是要考察这些抗生素与血浆蛋白质结合的百分比的均值有无显著的差异。

单因素方差分析的任务就是检验 s 个总体的均 值 μj 是否相等。

ab<-read.table("lec9_antibiotic",head=TRUE,sep="\t") 
ab2<-data.frame( x<-c(ab[,1], ab[,2],ab[,3], ab[,4], ab[,5]), A<-factor(rep(colnames(ab),each=4)))
ab2 

bartlett.test(x~A,data=ab2)

#绘制箱型图
png(file = "lec9_anova_1_ways_boxplot_ab2_x~A.png") 
plot(x~A,data=ab2)
dev.off()

#进行单因素方差分析
ab2.aov<-aov(x~A,data=ab2)
summary(ab2.aov)





3.多次项曲线的模拟：
（1）一元多次项模拟:

#针对ggplot2的多图排版
library(ggplot2)
library(gridExtra) 

#几次项?=》更改这个参数即可 
k=2 

#一共生成7组数据，每组100个数值 
group=7; n=100

#自变量最大区间
x_min=-3; x_max=3

#系数区间
b_min=-8; b_max=8

#则因变量理论区间
y_min=y_max=0

for(j in 0:k)
{
	y_min += b_min*(x_max^j)
	y_max += b_max*(x_max^j)
} 

#自变量波动区间
c_min=-1;c_max=1


#创建存储数据的data.frame，共3列，第一列group序号，第二列自变量x，第三列因变量y
data<-data.frame(matrix(NA,group*n,3)) 
colnames(data)<-c("group","x","y") 
#存放方程式
formula<-data.frame(matrix(NA,group,1)) 

#根据设定参数进行数据模拟 
for(i in 1:group)
{
	set.seed(i+runif(1,0,100))
	x<-runif(n,min=x_min,max=x_max)
	b<-round(runif(k+1,min=b_min,max=b_max))
	c<-runif(n,min=c_min,max=c_max)
	x<-x+c
	y<-data.frame(matrix(0,n,1))
	for(m in 0:k){ 
		y <- y + b[m+1] *(x^m) 
	} 
	from = (i-1)*n+1; to = n*i data[from:to,1]=rep(i,n)
	data[from:to,2]=x
	data[from:to,3]=y
}

#绘制一元多次项模拟散点图+拟合曲线
g1=ggplot(data, aes(x=x, y=y, colour=group)) + geom_point()#以颜色梯度区分 
data$group <- as.factor(data$group) #group列定义为因子
g2=ggplot(data, aes(x=x, y=y, colour=group)) + geom_point() #以不同颜色区分 
g3= ggplot(data, aes(x=x, y=y, colour=group)) + geom_point() + stat_smooth(method='lm', formula=y~poly(x,k)) #增加拟合曲线
g4= ggplot(data, aes(x=x, y=y, colour=group)) + geom_point() + stat_smooth(method='lm', formula=y~poly(x,k)) + theme(axis.title =element_text(face="bold",size=12), axis.text = element_text(face="bold", color="blue", size=10)) #增加图片修饰

#注意 4 张图的区别，输出到一张图片上 
png(file = "plot_y_x-k_ggplot.png") 
grid.arrange(g1, g2, g3, g4, ncol=2) 
dev.off()




（2）二元二次项模拟:【可选内容】

#绘制3D图
library(scatterplot3d) 

#模拟方程:y=b5*x1^2 + b4*x1 + b3*x2^2 + b2*x2 + b1*x1x2 + b0 

##设定模拟参数
#一共生成1组数据，每组100个数值
group=1; n=100
#自变量x1最大区间 
x1_min=-3; x1_max=3 
#自变量x2最大区间 
x2_min=-5; x2_max=5 
#系数区间 
b_min=-10; b_max=10 
##自变量波动区间
c_min=-1;c_max=1


 #创建存储数据的data.frame，共4列，第1列group序号，第2-3列自变量x1,2，第4列因变 量y
data<-data.frame(matrix(NA,group*n,4)) 
colnames(data)<-c("group","x1","x2","y")

#存放方程式
formula<-data.frame(matrix(NA,group,1))  

#根据设定参数进行数据模拟
for(i in 1:group)
{
	set.seed(i+runif(1,0,100))
	x1<-runif(n,min=x1_min,max=x1_max)
	x2<-runif(n,min=x2_min,max=x2_max)
	b<-round(runif(6,min=b_min,max=b_max))
	c1<-runif(n,min=c_min,max=c_max)
	c2<-runif(n,min=c_min,max=c_max)
	x1<-x1+c1
	x2<-x2+c2
	y<-b[6]*x1^2 + b[5]*x1 + b[4]*x2^2 + b[3]*x2 + b[2]*x1*x2 + b[1]
	from = (i-1)*n+1; to =  n*i
	data[from:to,]=c(rep(i,n),x1,x2,y)
 }

#group列定义为因子
data$group <- as.factor(data$group) 

#三维散点图
plot3d <- with(data, scatterplot3d(x1, x2, y, col.axis="blue",col.grid="light- blue", 
	main="scatterplot3d - 1", color = as.numeric(group), pch = 20, angle = 45,type="h"))

#三维散点+二元二次曲面拟合
library(rgl)
#预测脚本 
predictgrid<-function(model,xvar,yvar,zvar,res=16,type=NULL){
  xrange<-range(model$model[[xvar]])
  yrange<-range(model$model[[yvar]])
  newdata<-expand.grid(x=seq(xrange[1],xrange[2],length.out=res),
                       y=seq(yrange[1],yrange[2],length.out=res))
  names(newdata)<-c(xvar,yvar)
  newdata[[zvar]]<-predict(model,newdata=newdata,type=type)
  newdata 
}

#x,y,z 转为列表 
df2mat<-function(p,xvar=NULL,yvar=NULL,zvar=NULL){
  if(is.null(xvar)) xvar<-names(p)[1]
  if(is.null(yvar)) yvar<-names(p)[2]
  if(is.null(zvar)) zvar<-names(p)[3]
  x<-unique(p[[xvar]])
  y<-unique(p[[yvar]])
  z<-matrix(p[[zvar]],nrow=length(y),ncol=length(x))
  m<-list(x,y,z)
  names(m)<-c(xvar,yvar,zvar)
  m 
}

#交错出现两个向量元素
interleave<-function(v1,v2) as.vector(rbind(v1,v2))

#拟合二元一次平面 
#mod<-lm(y~x1+x2+x1:x2,data=data) 

#拟合二元二次曲面
mod<-lm(y~x1+I(x1^2)+x2+I(x2^2),data=data) 
pred_y<-predict(mod) 
mpgrid_df<-predictgrid(mod,'x1','x2','y') 
mpgrid_list<-df2mat(mpgrid_df)

plot3d(data$x1,data$x2,data$y,xlab='',ylab='',zlab='',axes=FALSE,size=.5,type='s',lit=FALSE)

spheres3d(data$x1,data$x2,pred_y,alpha=0.4,type='s',size=0.5,lit=FALSE)

segments3d(interleave(data$x1, data$x1),
          interleave(data$x2, data$x2),
          interleave(pred_y, pred_y),
          alpha=0.4,col='red'
          )
#预测曲面 
surface3d(mpgrid_list$x1,mpgrid_list$x2,mpgrid_list$y,alpha=.4,front='lines',ba ck='lines')
 
#其他设置 
rgl.bbox(color='grey50',emission='grey50',xlen=0,ylen=0,zlen=0) 
rgl.material(color='black')
axes3d(edges=c('x--','y+-','z--'), cex=.75) 
mtext3d('x1',edge='x—',line=2)
mtext3d('x2',edge='y+-',line=3)
mtext3d('y',edge='z—',line=3)






4.医学和流行病学统计 ———— 可视化统计数据（此处为折线图）

（1）不同年份和/或不同地区的医疗资源比较：

data1<-read.table("1-1.txt",header=T,sep=" ")
png(file = "1-1plot.png") 
plot(data1,type="o",ylim=c(0,10000000))
dev.off()

（2）不同年份和/或不同地区的人口出生率、死亡率比较：

data2<-read.table("1-2.txt",header=T,sep=" ")
year <- data2[,1]
birth <- data2[,2]
death <- data2[,3]
growth <- data2[,4]
png(file = "1-2plot.png") 
plot(x=year,y=birth,col='red',type="o",pch=1,ylim=c(-10,40),ylab='')
lines(x=year,y=death,col='blue',type="o",pch=2)
lines(x=year,y=growth,col='green',type="o",pch=3)
legend('topright',c("Birth","Death","Natural_Growth_Rate"),col=c('red','blue','green'),pch=c(1,2,3))
dev.off()



（3）不同年份和/或不同地区的总体患病率比较：


data3<-read.table("1-3.txt",header=T,sep=" ")
year <- data3[,1]
city <- data3[,2]
rural <- data3[,3]
total <- data3[,4]
png(file = "1-3plot.png") 
plot(x=year,y=city,col='red',type="o",pch=1,ylim=c(125,250),ylab='')
lines(x=year,y=rural,col='blue',type="o",pch=2)
lines(x=year,y=total,col='green',type="o",pch=3)
legend('topright',c("City","Rural_area","Total"),col=c('red','blue','green'),pch=c(1,2,3))
dev.off()


（4）不同年份和/或不同地区的某种疾病患病率比较：

data4<-read.table("1-4.txt",header=T,sep=" ")
year <- data4[,1]
city <- data4[,2]
rural <- data4[,3]
total <- data4[,4]
png(file = "1-4plot.png") 
plot(x=year,y=city,col='red',type="o",pch=1,ylim=c(100,300),ylab='')
lines(x=year,y=rural,col='blue',type="o",pch=2)
lines(x=year,y=total,col='green',type="o",pch=3)
legend('topright',c("City","Rural_area","Total"),col=c('red','blue','green'),pch=c(1,2,3))
dev.off()
```