#authet:Zhao Feiyang
#judge the days
getDays <- function(X){
	len<-length(which(X>=28))
	len
}
operate <- function(X){
	#open the pdf
	pdf("1.pdf")
	#load the weather data
	Weather <- read.table(file=X,sep="\t",header=TRUE)
	#first tansfer the weather data to list
	Weather <- as.list(Weather[2:13])
	#get the mean of the weather
	aim <- sapply(Weather,mean,na.rm=TRUE)
	#count the days and make the barplot
	barplot(sapply(Weather,mean,na.rm=TRUE),col=ifelse(sapply(Weather,getDays)>7,"red",0))
	#close the stream
	dev.off()
}
operate("tem_HK.txt")