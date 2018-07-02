## Genomic
* [相关数据库](#1)
* [绪论](#2)
* [遗传图与物理图绘制](#3)
* [基因组测序](#4)
* [基因组序列组装](#5)
* [新基因发现与基因结构建模](#6)
* [基因组进化研究内容](#7)
* [RNA序列分析](#8)
* [题目](#9)

### <a id="1"></a>相关数据库
```
基因组图谱数据库：
Genbank-Genome-Map viewer
UCSC-Genome browserEnsembl-Genome browser

从头计算预测：
GENSCAN: http://genes.mit.edu/GENSCAN.html
tRNAscan-SE: http://selab.janelia.org/tRNAscan-SE/

基因结构建模：
NCBI Splign
UCSC BLAT	
EMBL-EBI GeneWise

原核生物从头预测基因：
GLIMMER
GeneMark  GeneMarkS  GeneMarkS+

真核生物从头预测基因：
GENSCAN
Geneid
Augustus
GeneMark-ES  GeneMark-ET
GlimmerHMM
mSplicer
CONTRAST
mGen
FGENESH

密码子偏好：
JAVA Codon Adaptation Tool (JCat): http://www.jcat.de/
Codon Optimization Tool: http://sg.idtdna.com/CodonOpt
检验gff3格式：
http://genometools.org/cgi-bin/gff3validator.cgi https://github.com/modENCODE-DCC/validator 
galaxy：https://usegalaxy.org/ 
Variant Effect Predictor：http://asia.ensembl.org/Tools/VEP （输入突变信息）

启动子数据库：
http://molbiol-tools.ca/Promoters.htm
https://bip.weizmann.ac.il/toolbox/seq_analysis/promoters.html
EPD:https://epd.vital-it.ch/index.php
https://cb.utdallas.edu/cgi-bin/TRED/tred.cgi?process=home
transfac:不能用
ENCODE: https://www.encodeproject.org
果蝇启动子：http://www.fruitfly.org/seq_tools/promoter.html
promoter2.0：http://www.cbs.dtu.dk/services/Promoter/
http://linux1.softberry.com/berry.phtml?topic=fprom&%20group=programs&subgroup=promoter
cister：https://zlab.bu.edu/~mfrith/cister.shtml
tfsearch:http://diyhpl.us/~bryan/irc/protocol-online/protocol-cache/TFSEARCH.html
Tssw：http://linux1.softberry.com/berry.phtml?topic=tssw&group=programs&subgroup=promoter
FPROM:
http://linux1.softberry.com/berry.phtml?topic=fprom&group=programs&subgroup=promoter
Tssg：http://linux1.softberry.com/berry.phtml?topic=tssg&group=programs&subgroup=promoter

比较基因组学数据库:
dcode：https://ecrbrowser.dcode.org/
rvista2.0 ：https://rvista.dcode.org
CoGe: https://genomevolution.org/CoGe/ 
homologene: https://www.ncbi.nlm.nih.gov/homologene/?term=
ENSEMBLE: http://asia.ensembl.org/
clustal: https://www.ebi.ac.uk/Tools/msa/clustalo/

RNA数据库:
http://biobases.ibch.poznan.pl/ncRNA/
http://rfam.xfam.org/
https://www.science.co.il/biomedical/databases/RNA-databases.php

RNA修饰：
http://mods.rna.albany.edu
miRNA：http://www.mirbase.org
siRNA:http://sirna.sbc.su.se
http://www.ncrna.org/ 
long-noncodingrna：http://lncrnadb.com/ 

RNA结构预测：
https://bibiserv.cebitec.uni-bielefeld.de/rna
http://rna.urmc.rochester.edu/RNAstructureWeb/ 
http://mfold.rit.albany.edu/?q=mfold
http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi
tRNA: http://lowelab.ucsc.edu/tRNAscan-SE/ 
microRNA：https://cm.jefferson.edu/rna22v2/ 
sirna：http://www.imtech.res.in/raghava/desirm/ 

密码子偏好性优化：http://www.jcat.de/CAICalculation.jsp

```
###<a id="2"></a>绪论
```
*	基因组》单倍体基因组
1.核/染色体基因组
2.线粒体基因组
3.叶绿体基因组
4.病毒基因组
*	基因组学：应用重组DNA、DNA测序方法和生物信息学来对基因组的功能和结构进行排序、组装和分析。
*	人类基因组：核基因组：3*10^9bp（每个染色体55-250Mb）
           线粒体基因组：16569bp（每个细胞800个线粒体，每个线粒体10个基因组拷贝）
*	可变的DNA结构：A-DNA, B-DNA, Z-DNA [DNA结构取决于其环境]
  ①A-DNA结构在脱水样品中占主导地位，类似于双链RNA和DNA/RNA杂交。
  ②水环境,包括大多数的DNA在细胞,BDNA是最常见的结构。
  ③Z-DNA是一种少见的结构中发现DNA绑定到特定的蛋白质。
*	DNA超螺旋：
    30亿对碱基；拉直2m长；6微米宽
*	人类基因组计划：
    30亿个碱基对，30亿美元，1990-2005【1999.9中国正式加入，承担人类第3号染色
    体的短臂区域3000万个碱基对（1%）】
    [1998国家人类基因组南方研究中心、华大基因成立；1999国家人类基因组北方研究
     中心、诺赛基因成立]
    英日法德中印
    =》国际人类基因组组织HUGO
*	基因组进化复杂性【宏观问题】》C值悖论
*	基因组的序列组成【微观一级结构】
*	重复序列k-mers：
高度重复序列（卫星DNA/小卫星DNA/微卫星DNA/VNTR）；
中度重复序列（逆转录转座子、DNA转座子、长末端重复(LTRs)、非长末端重复 (non-LTRs)、长间隔重复(LINEs)、短间隔重复(SINEs)）
*	非重复序列：单一序列（80%基因）
*	其他DNA元件：CpG岛、G-quadruplex、启动子、TFBs、转录起始位点TSS、终止子
   PS:卫星DNA:由大段重复的非编码组成的，卫星DNA是功能性中心粒主要组分，形成异染色质的主要结构;
      小卫星DNA:一类可变串联重复（ variable number tandem repeat， VNTR）， 有一系列 10~60bp重复序列组成的 DNA片段;
      微卫星DNA:简单序列重复(SSRs)或短串联重复序列，是重复序列的2-6碱基对DNA。它是一种变数串联重复(VNTR);
      VNTR是基因组中的一个位置，短核苷酸序列被组织成串联重复序列。这些可以在许多染色体上发现，并且经常显示个体之间的长度变化。

*	non-codingRNA基因：rRNA、tRNA、scRNA、snRNA、snoRNA、miRNA
*	coding蛋白基因：mRNA
*	生物基因中有哪些异常结构基因: 重叠基因【基因内基因、反义基因】
*	假基因： 
    指来源于功能基因但已使其活性的DNA序列，有沉默的假设基因，也有可转录的假基因
*	全基因组测序=》序列组装=》基因组注释
           =》信息查询、基因搜寻、启动子分析、其他DNA元件
           =》比较基因组学、RNA序列分析、其他核酸分析软件使用


```
### <a id="3"></a>遗传图与物理图绘制
```
1.	遗传图【连锁图】：基因/DAN标志在染色体上的相对位置与遗传距离，显示基因以及其他序列特征在基因组上位置的图。
遗传距离通常以基因或 DNA 片段在染 色体交换过程中的分离频率厘摩 （ cM ）来表示：
①	cM 值越大，两者之间距离越远；
②	一般可由遗传重组检测结果推算
2.	遗传作图方法：孟德尔遗传学、遗传重组-连锁分析
3.	人类基因组计划绘制人类基因组的四张图：遗传图、物理图、序列图、转录图
4.	匹配小片段序列在基因组（染色体）上的正确位置=》两种测序策略
4.1.作图法测序：
高密度分子标记遗传图和大分子DNA克隆重叠群contig，
将单个大分子DNA克隆逐个测序（小段），
序列组装
4.2.鸟枪法测序
全基因组鸟枪法随机测序（小片段），
搭建重叠群，并到大分子克隆内，
以分子标记为基点将其锚定到染色体上
5.	遗传作图的标记物：
5.1.基因标记：等位基因allele
5.2.DNA标记：限制性片段长度多态性RFLP
              简单序列长度多态性SSLP[小卫星序列、微卫星序列]
              单核苷酸多态性SNP     
6.	遗传作图的不足：
6.1.遗传图的分辨率有限（基因组规模子代数量）
6.2.遗传图的覆盖较低(随机交换)
6.3.遗传图分子标记有时会出现差错（随机取样）
7.	物理图：指标明一些界标（如：限制酶切位点 、基因等）在 DNA 上的位置，图距以物理长度为单位，例如染色体带区、核苷酸对数目等。
8.	物理作图方法：
  8.1.限制性酶切作图:
          限制性核酸内切酶；
          限制性位点长度问题（6bp的随机概率=1/（4^6））
  8.2.基于克隆的基因组作图
  8.3.染色体细胞图
  8.4.STS作图【大规模基因组物理图的主流技术】
          STS是一已知的单一序列，根据选定的STS序列设计专一性引物，可对大量的单个克隆进行PCR检测，能扩增出的均含有序列重叠的插入子。距离模型:最大似然法
人类基因组计划（ HGP ）的研究目标是，构建人的每条染色体的 STS 图，标记之间相距约 100kb 。获得一组组 DNA 片段的克隆，组内两两片段之间有共同的重叠序列；或是获得标记按正确次序排列、相互毗邻的片段，其连续长度超过 2000kb ，以便把染色体分段进行研究。
  8.5.辐射杂交作图X-ray breakage
```
![](pattern/1.png)
### <a id="4"></a>基因组测序
```
1.	第一代DNA测序【sanger测序技术】：
1.1.	原理：以待测DNA为模板，使用带有标记的碱基类似物体外合成新链，可在任意一个碱基位置终止 =》凝胶电泳时形成彼此只差一个碱基的梯形条带 =》得到序列。
1.2.	原理：链终止法（完成了人类基因组计划）、化学降解法。
1.3.	凝胶电泳对于信号捕捉是存在缺陷的，且不高效 =》毛细管电泳、高效毛细管电泳
2.	第二代DNA测序:【高通量测序平台】
2.1.	焦磷酸测序【光点测序】
2.2.	DNA芯片测序
2.3.	将二代测序技术按测序原理分类：
2.3.1.	边合成边测序SBS：454、illumina、HiSeq/MiSeq/NextSeq、Ion torrent/proton
2.3.2.	边连接边测序SBL：solid【缺点：读长短】
3.	第三代测序技术：【高通量测序平台】
3.1.	原理：单分子测序SMS
3.2.	特点：
3.2.1.	测序读长：平均测序读长达到 10 ~ 18 kb ，最长可超过 60 kb ；
3.2.2.	准确度高：测序深度达到 30× 时，准确度达到 99.999% （ Q50 ）；
3.2.3.	敏感性强：可以检测频率在 0.1% 的 Minor Variants ；
3.2.4.	无 PCR 扩增偏好性：样本不需要进行 PCR 扩增，避免了覆盖度不均一以及 PCR Artifacts 的产生；
3.2.5.	最小的 GC 偏好性（ GC bias ）：在极端高 GC 和极端低 GC 区域，可以轻松测 定，从而保证序列的均匀覆盖度；
3.2.6.	可直接检测碱基修饰：利用测序过程聚合酶反应的动力学变化，首次实现在 测序的同时对碱基修饰进行直接检测
3.3.	技术路线：
单分子实时测序技术SMRT：读长超过10kb，插入缺失错误率1%【Sparc】
纳米孔单分子技术【Sparc】：纳米孔单分子DNA电流阻遏、纳米孔单分子DNA碱基序列的电子阅读
4.	全基因组测序注意事项：
4.1.	基因组测序的覆盖面P0 = e-m【P0 ：丢失概率、m：为覆盖面（单倍体基因组数）】
m= 1，P0 = 37% ，覆盖率63% 
m=5， P0 = 0.67% ，覆盖率99.33% 
m=10， P0 = 0.0045% ，覆盖率99.9955%
4.2.	物理间隙（Physical gap） 和 序列间隙（Sequence gap）
4.2.1.	物理间隙：构建基因组文库时被丢失的DNA序列
4.2.2.	序列间隙：测序时遗漏的序列，这个序列仍保留在尚未挑选到的克隆中
4.3.	插入片段的两端测序：
   同一个载体的两段有两个引物，每个克隆读序只有400bp，每个克隆内部不能进行连续的测序，因为缺少引物，所以>800bp的片段中间就存在gap
5.	序列读取模拟软件：ART、pIRS、PBSIM、Wessim、IgSimulato
6.	ART_454:
6.1.	单末端测序SINGLE-END SIMULATION art_454 
6.2.	双末端测序PAIRED-END SIMULATION art_454 
6.3.	扩增子测序AMPLICON SEQUENCING SIMULATION art_454 
PS:SAM 是一种序列比对格式标准， 由 sanger 制定，是以TAB为分割符的文本格式。 
主要应用于测序序列mapping到基因组上的结果表示、表示任意的多重比对结果 
SAM分为两部分：注释信息部分（header section）、比对结果部分（alignment section）
7.	GenomeABC: http://crdd.osdd.net/raghava/genomeabc/
```
### <a id="5"></a>基因组序列组装
```
1.	序列组装的基本理论
1.1.	流程：
多个基因组测序的副本 -》碎片化（fragments） -》长度过小的过滤 –》BAC/YAC双末端测序序列（带有BAC末端的序列，reads） -》通过overlap寻找重叠群区域（contigs） -》锚定在染色体上的重叠群（scaffold） -》草图序列（可覆盖测序克隆片段3-4倍的DAN序列，含间隙/没有间隙，排列方向和位置未定） -》完成序列（错误碱基数<0.01%的DNA序列，排列方向确定，内部不含间隙，测序覆盖率在8-10个单倍体基因组）
Ps：根据确定BAC的排序方向以及重叠群（contigs）在支架scaffold中的排列方向; 酵母人工染色体（YAC）、细菌人工染色体（BAC）
1.2.	问题：
测序错误
重复序列
多态性变异-》contigs
倒位inversion
覆盖率
1.3.	组装类型：
	从头组装（De novo） vs基于参考的组装（ reference-based(mapping)）：
1.3.1.	de novo组装：
即使可以获得参考基因组，也应该进行从头组装，因为它可以从基因组组装中丢失的基因组片段中恢复转录的转录本。
1.3.2.	mapping组装：
对现有的主干序列进行读取，构建一个类似的序列，但不一定与主干序列相同。
转录组数据主要通过对参考基因组的mapping进行分析
1.3.3.	de novo:
即使可以获得参考基因组，也应该进行从头组装，因为它可以从基因组组装中丢失的基因组片段中恢复转录的转录本。
1.3.4.	mapping缺点：
无法解释mRNA转录本结构改变的原因,如可变剪接。由于基因组包含可能存在于转录本的所有内含子和外显子，因此在基因组中不连续排列的剪接变体可能被折现为实际的蛋白质亚型。
	基因组组装vs转录组组装：
1.3.5.	基因组：基因组序列覆盖水平可以根据non-codingDNA内含子区域的重复序列随便改变；
        这些重复序列也会造成基因组组装重叠群contigs组成的错误;        
1.3.6.	转录组：转录组的覆盖水平可以表示为基因表达水平；
               转录组装中的重叠群contigs区域可能是剪接的异常或者基因家族成员之间的差异
1.3.7.	基因组组装软件不能被用于转录组组装
     一个基因组的基因组测序深度通常相同，但转录的深度不同；
     两条链在基因组测序都是按顺序排列的，但RNA-seq可以是特异的；
    来自相同基因的转录变异体（transcript variants）可以共享外显子，难以处理
2.	序列组装的软件：
TIGR组装
Minimus组装：
Minimus2组装：
Minimo
Newbler
BioPerl -》 Module:Bio::Assembly::IO
AllPathsLG –》 DISCOVAE de novo
Velvet https://www.ebi.ac.uk/~zerbino/velvet/
SOAPdenovo http://soap.genomics.org.cn/soapdenovo.html
SOAPdenovo ：SOAPdenovo2（基因组）、SOAPdenovo-Trans（转录组）
Trinity（转录组）
CAP3
应用于转录组的序列组装：
SeqMan NGen
SOAPdenovo-Trans
Velvet（基因组很小的reads）-》Oases（应用于转录组）
Trans-ABySS
Trinity
3.	CAP3小规模序列组装 http://doua.prabi.fr/software/cap3
使用genebank的unigene数据库中搜索的某个基因的EST序列进行组装
4.	获得某个基因的EST序列：
NCBI-UniGene –》 某基因 -》下面有mRNA序列和EST序列（fasta）
5.	序列组装算法：
5.1.从头组装（De novo）
     贪婪图算法：OLC、DBG
给定一组 reads ，从中挑选一个 read 作为“种子”【规则】，用与它两端中 的一段有足够数量的碱基序列相同的 read来扩展；迭代进行，直到不可继续 扩展。再选择其他未参与拼接的 reads 序列拼 接，重复上述过程，直到所有 read被 拼接完成。
计算多有fragments的成对对齐程度
-》选择最大重叠的两个fragments
-》合并选择的fragments
【不断迭代，中间的重叠区就是contig】
          5.1.1.OLC方法【Sanger-data组装】Hamilton path：
1.把每个 DNA片段 (reads) 看成一个节点 ;
2.如果两个 DNA片段之间存在重叠，就在相应的节点之间建立 一条边 ;
3.所有 DNA 片段通过这种重叠关联，构造出一个有向图 ;
4.通过寻找图中经过每个节点一次且仅一次的一条路径 （ Hamilton 路径） ;
5.即可获得目标 DNA 序列。
1.对参与拼接的 reads进行比对，分析它们之间的重叠信息 （ overlap ） ; 
2.把存在重叠的 reads进行组合，形成拼接结果 contigs （ layout ） ;
3.对 contigs形成的图上的 reads 进行排列，通过在图中寻找 Hamilton 路径来确定最终序列（ consensus ）。
应用的软件Celera Assembler, Arachne, CAP，PCAP，TIGR， PHRAP……
          5.1.2.DBG方法Eularian path：
                1. 对给定的 reads ，按照长度 k 进行连续划分（步长 =1 ），得到若干等长度段序列（ k-mer）。一个长度为 l 的 read ，将被分成 lk+1 个 k-mer
2. 对于任意两个 k-mers ： k1 和 k2 ，如果 k1 的后 k-1 个碱基序列与 k2 的前 k-1 个碱基序列相同，则建立一条从 k1 指向 k2 的有向边。
通过以上两步即可构建出一个 de Bruijn 图，拼接结果序列可以通 过在图中寻找 Eulerian path 获得。
3. 第一个 k-mer 的序列全部读出，后面的每个 k-mer 只读取 最后一个碱基
          5.1.3.DBG方法的问题：
                Q1.测序错误：tip结构和bubble结构
                         错误的reads-》错误的k-mer节点-》deBruijin图大且复杂
-》降低组装效率
                Q2.测序gap：
                         基因组覆盖不全-》k-mer信息不全-》deBruijin图连通性降低
                        -》产生dead-end路径-》k-mer越长问题越严重
                Q3.分支问题：
                         数据错误/重复序列-》deBruijin图出现分支-》无法处理
             =》Solution：设定过滤标准（k-mer出现次数）-》过滤掉可能出错的reads；
                          直接删除dead-end路径-》可能导致gap问题；
          5.1.4.对比 Hamilton path 和 Eularian path：
               当短的reads数量很多时，Hamilton图基于reads，巨大复杂-》时间复杂度高-》空间复杂度低；Eularian图基于k-mer，不受影响-》时间复杂低-》空间复杂度高
5.2.基于参考的mapping组装
6.	大规模序列组装软件：
6.1.AllPaths-LG:短reads
    给定一个参考基因组，pipeline能在基因组组装的不同阶段对组装过程 和结果进行评估
BASIC:基础评估，不需要参考基因组；
frag_size:小片段文库插入片段长度的均值； 
frag_stddev:小片段文库的插入片段长度估算的标准偏差； 
insert_size:大片段文库插入片段长度的均值； 
insert_stddev:大片段文库插入片段长度估算的标准偏差； read_orientation:reads的方向，小片段文库为inward，大片段文库为outward； genomic_start:reads从该位置开始，读入数据，如果不为0，之前的碱基都被剪掉； genomic_end:reads从该位置开始，停止读入数据，如果不为0，之后的碱基都被剪掉。
   6.2.Velvet + SOAPdenovo
7.	CAP3序列组装结果分析：
    UCSC –》 Blat –》提交cap3生成的contig结果 –》browser
```
![](pattern/2.png)

```
8.	序列比对基本原则：
相似性、同源性
8.1.相似性：是指序列比对过程中， 用来描述检测序列和目标序列之间，相同DNA碱基或氨基酸 残基顺序所占比例的高低。  《= 统计
8.2.同源性：是指从某一共同祖 先经趋异进化而形成的不同序列。   《=进化
8.3.当相似程度高于50%时，比较容易推测检测序列和目标 序列可能是同源序列；
     当相似性程度低于20%时，就难以确定或者根本无法 确定其是否具有同源性；
     无论相似程度有多高或多低，都不能100%确保两个序列 之间一定同源，它只能作为推测的依据之一
```
![](pattern/3.png)

```
 在蛋白质家族或超家族中经常存在，不同的蛋白质序列之间只有局部区域存在高度相似性（保守性Motif），而这些局部区域在整个序列中所占的比例有时很低！
     序列比对过程中需要在检测序列或目标序列中引入空位， 以表示插入(Insertions)或删除(Deletions) [Indel]
     序列比对的数学模型大体可以分为两类： 一类从全长序列出发，考虑序列的整体相似性，即整体比对/全局比对； 第二类考虑序列部分区域的相似性，即局部比对。
     局部相似性比对的生物学基础，是蛋白质功能位点 往往是由较短的序 列片段组成的，这些部位的序列具有相当大的保守性，尽管在序列的 其它部位可能有插入、删除或突变。此时，局部相似性比对往往比整 体比对具有更高的灵敏度，其结果更具 生物学意义
8.6.序列比对时的打分模型：
突变数据矩阵MD、模块替换矩阵BLOSUM
8.6.1.MD:
       建立在已知的同源蛋白质/蛋白质家庭 的多序列比对的基础之上的;
       统计某位点出现各种氨基酸的比例(%) [Pj, j=1 To 20，对应20种Aa，伪随机概率;
       该位点一个氨基酸发生改变，改变成另一个Aa 的概率 P1,2 = Pj1/Pj2;
       可接受点突变(Point Accepted Mutation,PAM) 1个PAM的进化距离表示100个残基中发生一个残基突变的概率;
       PAM是在蛋白质高度相似的基础上选择的。蛋白质对齐要求显示至少是85% 
8.6.2.BLOSUM:
       以序列片段为基础;基于蛋白质模块数据库BLOCKS;从蛋白质模块数据库BLOCKS中找出一组替换矩阵，用于解决序列的远距离相关。
8.6.3.PAM和BLOSUM换算：
PAM后的数字——越大 越适用于序列相似性低的序列之间的比对
PAM后的数字——越小 越适用于序列相似性高的序列之间的比对
Blosum正好相反
```
![](pattern/4.png)
![](pattern/5.png)
![](pattern/6.png)

```
空位开放罚分
空位延伸罚分
v(g) = - d - (g-1)e 
【g代表连续空位数 d代表空位开放罚分 e代表空位延伸罚分】
8.7.序列比对原则：动态规划算法(最长共同子序列)、启发式搜索算法（最优方案、完整性、准确度精密度、执行时间）
启发式算法应用：神经网络、自学习。
启发式算法应用在序列比对 ：等长的高分片段对-》通过延伸或连接优化结果-》运用动态规划算法引入空位
8.8.回溯：从最高的 分数开始 ，进行 traceback 直到碰到0 为止。
8.9.序列比对软件：EBI ClustalW2【动态规划算法 >> 全局联配工具】
```
![](pattern/7.png)

```
8.10.BLAST和指定的物种进行序列比对：【启发式搜索算法（局部打分策略）：】
```
![](pattern/8.png)
![](pattern/9.png)

```
 EBI >> FASTA【启发式搜索算法（局部打分策略）：】

https://www.ebi.ac.uk/Tools/sss/fasta/

```
![](pattern/10.png)

```
8.12.二代测序NGS比对（4）
      BWA、Bowtie、Bowtie2(=》illumina,solid)、samtools、
```
### <a id="6"></a>新基因发现与基因结构建模
```
1.	新基因范畴：
1.1.	该物种没有报道 =》 同源基因搜索
1.2.	所有物种都没有报道 =》EST/cDNA序列文库、RNA-seq、从头计算鉴别新基因
2.	AP为例 blast：s
```
![](pattern/11.png)
![](pattern/12.png)

```
在结果中选择高相似区域，扩展上下游，各延伸1kb
3.	基于EST/cDNA序列文库的新基因发现：
```
![](pattern/13.png)

```
4.	基于 RNA-seq 数据的新基因发现：
```
![](pattern/14.png)

```
5.	从头计算鉴别新基因
```
![](pattern/15.png)
![](pattern/16.png)

```
6.	基因结构建模：
NCBI Splign
UCSC BLAT	
EMBL-EBI GeneWise
```
![](pattern/17.png)
![](pattern/18.png)
![](pattern/19.png)

```
7.	对比各个基因结构建模软件：
```
![](pattern/20.png)

```
8.	原核生物从头预测基因：
8.1.原核生物的启动子区域信号：
Pribnow box
转录因子结合位点
   8.2.ORF区
有成百上千的碱基对长
终止密码子
9.	真核生物从头预测基因
9.1.真核生物的启动子区域信号：
CpG岛
poly(A)尾巴的结合位点
   9.2.外显子和内含子的剪接机制：
         剪接位点
         外显子
10.	密码子偏好：
RNA二级结构、转录/基因表达、翻译延伸速度、蛋白质折叠
JAVA Codon Adaptation Tool (JCat) http://www.jcat.de/
Codon Optimization Tool http://sg.idtdna.com/CodonOpt

11.	原核生物从头预测基因：
GLIMMER
GeneMark  GeneMarkS  GeneMarkS+
12.	真核生物从头预测基因：
GENSCAN
Geneid 【HMM】
Augustus 【HMM】
GeneMark-ES  GeneMark-ET
GlimmerHMM 【HMM】
mSplicer
CONTRAST
mGen
FGENESH 【HMM】


13.	 基因组注释数据库的查询和应用
Genebank-Genome、UCSC-genome browser、Ensembl
1).genome：https://www.ncbi.nlm.nih.gov/genome/?term=
可以FTP模式下载物种基因组数据，下载格式有：
asn:标记语言（抽象语法标记：在任何需要以数字方式发送信息的地方，ASN都可以发送各种形式的信息（声频、视频、数据等等）。ASN编码规则推进了结构化数据的传输，尤其是网络中应用程序之间的结构化数据传输，它以一种独立于计算机架构和语言的方式来描述数据结构。）
fa:FASTA （每条序列开始>）
gbk:genbank  （下一条序列以//开始）
gbs：genbank (没有序列信息，是contig和gap描述信息)
mfa：多重fasta（几乎与fasta格式相同，在序列描述方面包含了更多信息，如简单重复序列）
且可以下载gff格式的基因组注释文件，可以提交基因组数据
首页包括包含人类基因组，微生物基因组资源，亚细胞器基因组资源，原核基因组注释，真核基因组注释，病毒基因组成对比较，基因组装配数据库资源，基因组计划数据库资源，生物样本数据库资源，人类基因组blast搜索快速链接，微生物基因组blast搜索快速链接
```
![](pattern/21.png)

```
GENEBANK-GENOME
>Custom resources:
人类基因组、微生物基因组资源、亚细胞器基因组资源、病毒基因组资源
>Other resources：
基因组装配数据库资源（assembly）、基因组计划数据库资源（bioproject）、生物样本数据库资源（biosample）、大量的基因组绘图和测序数据-老版(map viewer)、大量的基因组绘图和测序数据-新版（genome data viewer）
>Genome annotation and analysis
原核基因组注释、真核基因组注释、病毒基因组成对比较（PASC-pairwise sequence comparison）
>External resources：
GOLD提供全世界范围内各种基因组测序项目的访问通道、Sanger研究所的细菌基因组数据下载的访问链接、Ensembl基因组可视化浏览数据库
一、	基因组注释信息的数据存放格式
包括gff1,gff2,gff3,gtf1/2
gff文件,以tab分割，
gff1：
```
![](pattern/22.png)

```
GFF2:
“group”注释分类，包含class和ID，也会存目标序列的相似性位点，例如：Transcript "R119.7"，添加note，添加别名，识别参考序列，序列比对情况.
Gff2格式支持GMOD，gtf格式不支持GMOD
GFF3:
```
![](pattern/23.png)
![](pattern/24.png)

```
除gff1以外均由9列数据組成，前8列在gff的3個版本中信息都是相同的，只是名稱不同：例如第一列在gff1、gff2和gff3中分別叫做”seqname"，“reference  sequence”和“seqID”，type在gff1、gff2中也被稱作feature，phase在gff1、gff2中也被稱作frame。
第9列attributes的內容存在很大的版本特異性。這9列信息（以gff3為例）分別是：
seqid source type start end score strand strandattributes
•	seqid ：參考序列的id。
•	source：註釋的來源。如果未知，則用點（.）代替。一般指明產生此gff3文件的軟件或方法。
•	type： 類型，此處的名詞是相對自由的，建議使用符合SO慣例的名稱（sequenceontology），如gene，repeat_region，exon，CDS等。
•	start：開始位點，從1開始計數（區別於bed文件從0開始計數）。
•	end：結束位點。
•	score：得分，對於一些可以量化的屬性，可以在此設置一個數值以表示程度的不同。如果為空，用點（.）代替。
•	strand：“＋”表示正鏈，“－”表示負鏈，“.”表示不需要指定正負鏈。
•	phase ：步進。對於編碼蛋白質的CDS來說，本列指定下一個密碼子開始的位置。可以是0、1或2，表示到達下一個密碼子需要跳過的鹼基個數。
•	attributes：屬性。一個包含眾多屬性的列表，格式為“標籤＝值”（tag=value），不同屬性之間以分號相隔。

gtf同gff3很相似，也是9列內容
•  seqname: 序列的名字。通常格式染色體ID或是contig ID。 
•  source：註釋的來源。通常是預測軟件名或是公共數據庫。
•  start：開始位點，從1開始計數。
•  end：結束位點。
•  feature ：基因結構。CDS，start_codon，stop_codon是一定要含有的類型。
•  score ：這一列的值表示對該類型存在性和其座標的可信度，不是必須的，可以用點“.”代替。
•  strand：鏈的正向與負向，分別用加號+和減號-表示。
•  frame：密碼子偏移，可以是0、1或2。
•  attributes：必須要有以下兩個值：
gene_id value; 表示轉錄本在基因組上的基因座的唯一的ID。gene_id與value值用空格分開，如果值為空，則表示沒有對應的基因。
transcript_id value; 預測的轉錄本的唯一ID。transcript_id與value值用空格分開，空表示沒有轉錄本。
```
![](pattern/25.png)

```
GENGBANK基因组注释相关的其他数据库：
1>.Genes：EST,Gene,GEO DATASEYS,GEO PROFILES,homologene,PopSet,unigene
2>.Health:ClinVar,dbGap,GTR,MedGen,OMIM,pubmed health
3>.Genomes:assemble,biocollections,bioproject,biosample,cDNAclones,dbvar,genome,gss,nucleotide,primers,snp,sra,taxonomy
```
GENEBANK数据库及分析工具的本地化
![](pattern/26.png)

```
第三方工具：bioperl、R包：genbankr、R包：rentrez、R包：seqinR、R包：ape。
2).UCSC Gennome Browser
genomebrower：https://genome.ucsc.edu/
打开ENCODE查看转录因子结合位点

3).Ensemble
ensemble: http://asia.ensembl.org/有blat/blast（输入蛋白序列与其他物种进行比对）
可看genetree，orthologues（直系同源）可用biomart处理数据
```
![](pattern/27.png)

```
限制查询：region、gene、phenotype、gene ontology、multi species comparisons、protein domain andfamilies、variant
设定输出返回字段：features、variant(Germline)、structures、variant(Somatic)、Homologues、sequences
>bimart在线使用方法 http://asia.ensembl.org/biomart
[1].	选择ensemblgenes92
[2].	选择humangenes（38.p12）
[3].	点击filter，设定数据库筛选条件
[4].	点击attributes，设定筛选返回结果字段
[5].	点击result即可
>VEP查看变异影响预测
>查看ensembl数据库中可用的物种数据集R包
useEnsembl(biomart="ensembl")
listDatasets(ensembl)
1 oanatinus_gene_ensembl Ornithorhynchus anatinus genes (OANA5) OANA5 
2 cporcellus_gene_ensembl Cavia porcellus genes (cavPor3) cavPor3 
3 gaculeatus_gene_ensembl Gasterosteus aculeatus genes (BROADS1) BROADS1 
4 lafricana_gene_ensembl Loxodonta africana genes (loxAfr3) loxAfr3 
5 itridecemlineatus_gene_ensembl Ictidomys tridecemlineatus genes (spetri2) spetri2
 查看人类的ensembl数据库
ensembl = useEnsembl(biomart="ensembl", dataset="hsapiens_gene_ensembl")
listMarts(host="uswest.ensembl.org")
1 ENSEMBL_MART_ENSEMBL Ensembl Genes 79 
2 ENSEMBL_MART_SNP Ensembl Variation 79 
3 ENSEMBL_MART_FUNCGEN Ensembl Regulation 79 
4 ENSEMBL_MART_VEGA Vega 59 
5 pride PRIDE (EBI UK)
 查看ensembl中人类数据集的可用过滤器
listFilters(ensembl)
1 chromosome_name Chromosome name 
2 start Gene Start (bp) 
3 end Gene End (bp) 
4 band_start Band Start
5 band_end Band End
6 marker_start Marker Start
 查看ensembl中人类数据集的可用属性
listAttributes(ensembl)
1 ensembl_gene_id Ensembl Gene ID
2 ensembl_transcript_id Ensembl Transcript ID
3 ensembl_peptide_id Ensembl Protein ID
4 ensembl_exon_id Ensembl Exon ID
5 description Description
6 chromosome_name Chromosome Name
>biomart中获取数据的函数
Functions：getBM、getBMlist、getGene、getLDS、getSequence、getXML

》MGI老鼠基因组信息：
基因功能注释”Mutations,alleles,and phenotypes”(突变，等位基因和表型)，all mutations/alleles：gene trapped；targeted
Ps：gene trapped使用高通量方式显示插入突变 
Gene targeted利用同源重组来改变内源性基因的技术。该方法可以用于删除一个基因，删除外显子，添加一个基因，引入点突变。
》ZFIN斑马鱼基因组信息
》其他可本地化的基因组可视化平台：
>”genome viewer”
Integrative Genomics Viewer（IGV）：http://software.broadinstitute.org/software/igv/
NCBI Genome Data Viewer （GDV）：https://www.ncbi.nlm.nih.gov/genome/gdv/
UCSC Genome Browser：https://www.genome.ucsc.edu/
Genome View：http://genomeview.org/
Artemis: http://www.sanger.ac.uk/science/tools/artemis
Apollo: http://genomearchitect.org/
NCBI Genome Workbench: https://www.ncbi.nlm.nih.gov/tools/gbench/
JGI Genome Viewer: https://genome.jgi.doe.gov/help/browser_viewer.jsf
BioViz Genome Viewer:
http://www.svgopen.org/2002/papers/lewis_et_al__bioviz_genome_viewer/
>”genome viewer javascript”
Jbrowse Genome Browser: http://jbrowse.org/
GenomeD3Plot: https://github.com/brinkmanlab/GenomeD3Plot/
pileup.js: http://www.hammerlab.org/2015/06/19/introducing-pileup-js-a-browser-basedgenome-viewer/
NCBI's Sequence Viewer: https://www.ncbi.nlm.nih.gov/projects/sviewer/

14.	隐马尔可夫模型
是一种最简单的动态贝叶斯模型
包含隐藏状态，可观察输出，转移概率，输出概率
概念延伸:在生物序列分析中，给你一组同源基因序列或同一家族的蛋白质序列，构建出一个HMM;然后再利用该模型去识别一个新序列是否属于该类同源基因或该蛋白质家族。
```
![](pattern/28.png)

```
states = (\'Rainy\', \'Sunny\')
observations = (\'walk\', \'shop\', \'clean\')
start_probability = {\'Rainy\': 0.6, \'Sunny\': 0.4}
transition_probability = {
\'Rainy\' : {\'Rainy\': 0.7, \'Sunny\': 0.3},
\'Sunny\' : {\'Rainy\': 0.4, \'Sunny\': 0.6},
}
emission_probability = {
\'Rainy\' : {\'walk\': 0.1, \'shop\': 0.4, \'clean\': 0.5},
\'Sunny\' : {\'walk\': 0.6, \'shop\': 0.3, \'clean\': 0.1},
}
```
![](pattern/29.png)
![](pattern/30.png)

```
Node:时间序列中的某一天
States：每天有2种基本的天气状态——Sunny/Rainy
Transition（arrow）：前一天天气对后一天天气的影响情况
Transition Probability的统计方法：某个时间序列中相邻两天天气的分布情况
应用于基因组：
Node:DNA序列中的某个位点
States：每个位点有4种可能的碱基状态——A/T/C/G
Transition（arrow）：前一位点碱基对后一位点碱基的影响情况
Transition Probability的统计方法：某个DNA序列中相邻两个碱基的分布情况
应用于CpG岛分析：
Step1-统计序列集中每条序列内部两个相邻碱基转移情况
Step2-统计每个序列集中两个相邻碱基的总体转移情况
Step3-转移概率标准化【CpG+/-合二为一】S(x) = log ( P(x|CpG+) / P(x|CpG-) )
Step4-最佳的状态序列应该使用上述公式计算出来的概率值，在所有可能的状态路径中达到最大
当序列长度增加时，最终的计算概率会呈指数形式减小，在实际运算中会造成向下溢出错误，解决方法：计算其log值
```
![](pattern/31.png)
![](pattern/32.png)
![](pattern/33.png)

```
15.	启动子类型
1.	核心启动子：引发转录的必要部份及转录起始点，位置约为- 35;且是RNA聚合酶的结合位点及一般转录因子结合位点。
2.	近端启动子：基因的近端序列上游，包括一些基本的调控元件，位置约为-250，且是特定转录因子结合位点。
3.	远处启动子：基因的远处序列上游，包括一些额外的调控元件，影响力较近端启动子弱。
16.	原核生物启动子：
```
![](pattern/34.png)

```
17.	真核生物启动子
真核生物启动子是极端的分化及很难表现其特征。它们一般处于基因的上游及有着远离转录起始点的调控元件。转录复合物可以引起脱氧核糖核酸(DNA)向自己屈曲，以容许放置调控序列。很多真核生物启动子，但不是全部，都包含一个TATA盒(序列TATAAA)会与 TATA结合蛋白结合，以协助形成RNA聚合酶转录复合物。TATA盒一般会处于非常接近转录起始点(通常于50个碱基对以内)
RNA聚合酶Ⅰ  核仁 合成rRNA前体
RNA聚合酶Ⅱ  核质 合成mRNA前体、大多数snRNA
RNA聚合酶Ⅲ  核质 合成5S rRNA前体、tRNA前提、其他核和胞质小RNA前体
1). I类启动子
RNA聚合酶Ⅰ识别Ⅰ类启动子，只控制rRNA前体基因的转录，转录产物经切割和加工后生成各种成熟rRNA.
》I类启动子的序列组成：核心启动子（位于转录起点附近-45~+20）;
上游控制元件（UCE,位于-180~-107）
    》RNA聚合酶Ⅰ对其转录需要2种因子参与：UBF1(结合在上述两部分的富含GC区，一个TBP(TATA结合蛋白));SL1（一个四聚体蛋白，含有3个不同的转录辅助因子TAFⅠ，在SL1因子介导下RNA聚合酶Ⅰ结合在转录起点上并开始转录）
2).II类启动子：
     RNA聚合酶Ⅱ识别Ⅱ类启动子，催化mRNA和大多数核内小RNA合成。
》组成：
*基本启动子：序列为中心在-25至-30左右的7 bp保守区，TATAAAA/T， 称 为TATA框或Goldberg-Hogness框。与RNA聚合酶的定位有关，DNA双链在此解开并决定转录的起点位置。失去TATA框， 转录将在许多位点上开始。 
*起始子：转录起点位置处的一保守序列，共有序列为: PyPyANT(A)PyPyPy为嘧啶碱(C或T)，N为任意碱基，A为转录的起点。 DNA在此解开并起始转录。 
*上游元件：普遍存在的上游元件有CAAT框、GC框和八聚体(octamer) 框等。CAAT框的共有序列是GCCAATCT，GC框的共有序列 为GGGCGG和CCGCCC，八聚体框含有8bp，共有序列为 ATGCAAAT。 
*应答元件：诱导调节产生的转录激活因子与靶基因上的应答元件结合。 如热休克效应元件 HSE 的共有序列是 CNNGAANNTCCNNG， 可被热休克因子HSF识别和作用;血清效应元件SRE的共有序 列CCATATTAGG，可被血清效应因子SRF识别和作用。 
》参与RNA聚合酶Ⅱ转录起始地各类因子：
*通用因子：作用于基本启动子上的辅助因子称为通用（转录）因子（GTF），为任何细胞类别 Ⅱ启动子起始转录所必需，以TFⅡⅩ来表示，其中Ⅹ按发现先 后次序用英文字母定名，如TFⅡA、TFⅡD、TFⅡH。
*上游因子：转录辅助因子是指识别上 游元件的转录因子
*可诱导因子：生长发育不同阶段相关的基因表达调控【自我调控】
Ps: 对外界刺激信号的响应【各种应答反应？？？】 =》主要通过转录激活物（transcription activator）的可诱导 调节 =》诱导的转录激活因子与靶基因上应答元件相结合
3).III类启动子：
》类别III启动子为RNA聚合酶III所识别，涉及一些小分子RNA的转录。 
*类型1基因内启动子：
如5S rRNA基因的启动子，位于转录起点下游，即在基因内部， 是 下游启动子，有两个框架序列，被3种辅助因子所识别。 5SrRNA基因的启动子包括框架A(box A)、中间元件 (intermediate element)和框架C(box C)3个元件组成。 TFIIIA结合在框架A上，然后促使TFIIIC结合，后者结合导致 TFIIIB结合到转录起点附近，并引导RNA聚合酶III结合在起点 上。TFIIIB使RNA聚合酶III正确定位，起“定位因子” (positioning factor)作用。 
*类型2基因内启动子：
如tRNA基因的启动子，有两个控制元件，分别为框架A和框架 B。 TFIIIC结合框架B，其结合区域包括框架A和框架B，然后 导致TFIIIB结合到转录起点附近，并引导RNA聚合酶III结合在 起点上。 
*上游启动子
如snRNA基因的启动子，位于转录起点上游。 有3个上游元件:OCT(八 聚体基序 octamer motif)、PSE (邻近序列元件 proximal sequence element)、TATA元件。 在RNA聚合酶III的上游启动子中，只有靠近起点存在TATA元 件，就能起始转录。 然而PSE和OCT元件的存在将会增加转录效率。 
18.	启动子区域预测：
*利用UCSCgalaxy，genebank，TRED等数据库，获取某个基因的可能的启动子序列信息
*可以使用NNPP、promoter2.0、FPROM、TSSW、TSSG、CISTER等，计算分析某个基因上游的启动子
*可以使用ENCODE、TRANSFAC等数据库，查找某个基因启动子区域的转录因子信息
*可以TRED、TFSEARCH等，计算分析某个基因启动子区域可能的转录因子结合位点
19.	可能转录因子的靶基因研究：
可以利用PubMed数据库，查找某个基因已有研究报道的启动子信息
=》CpG DNA library、Genomic DNA
=》免疫沉淀
=》克隆测序、高通量二代测序chip-seq
=》通过序列分析找出靶基因
```
![](pattern/35.png)
![](pattern/36.png)
![](pattern/37.png)

```
20.	对外界刺激信号的响应
1.	主要通过转录激活物
2.	诱导的转录激活因子与靶基因上应答元素相结合
21.	研究某一基因的启动子和转录因子
1. 查文献报道（要查基因别名）
2. 找其他实验数据（USCS ENCODE整合的chip-seq数据）
3. 使用启动子和转录因子分析工具进行分析和预测
4. 克隆引物设计
```
### <a id="7"></a>基因组进化研究内容
```
1.	传统的生物进化论：达尔文
2.	寒武纪生命大爆发=》奥陶纪辐射=》志留纪=》泥盆纪=》二叠纪-三叠纪=》侏罗纪=》白垩纪=》古近纪
3.	基因组进化与比较基因组学的生物信息学基础：
高通量测序技术（二代测序NGS）
=》海量的基因组数据
=》基因比较方法的进化基因组学
4.	基因进化：结构（序列）和大小（size）
5.	基因组进化包含多个领域
structural analysis of the genome 
the study of genomic parasites 
gene and ancient genome duplications 
polyploidy 
comparative genomics 
6.	新基因产生的机制：
exon shuffling 	
gene fission/fusion
retrotransposition	
duplication-divergence
lateral gene transfer
7.	基因复制：recombination、retrotransposition
8.	全基因组复制：polyploidy
9.	转座因子：机制类似”cut-and-paste””copy-and=paste”
10.	突变：一个或多个核苷酸碱基的增加或删除=》可导致一个frameshift失去功能；在启动子区域、增强子区域或转录因子编码区域发生的突变可能会导致基因转录功能的损失或是上调下调
11.	突变、假基因：基因功能紊乱
12.	exon shuffling 	-> transposon mediated shuffling
                     sexual recombination
                     illegitimate recombination
13.	基因组减少和基因丢失：a parasitic life style
14.	突变产生的生物学效应：基因组规模的增大、新基因的产生
```
![](pattern/38.png)

```
15.	基因的从头预测：
新基因可以从non-coding RNA中产生（Junk DNA）

1.NCBI >> BLAST (Microbial Nucleotide BLAST, megablast, psi-blast)
2.UCSC Genome Browser (Comparative genomics)
3.ECR browser, rVista, VISTA
4.CoGe, MEGA, PAUP, MacClade
```
![](pattern/39.png)

```
微生物核苷酸blast【NCBI-> Genome-> Genome Tools-> Microbial Nucleotide BLAST】
https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastSearch&BLAST_SPEC=MicrobialGenomes
检索NC_002655 【在Nucleotide库中有具体的】
在GenBank中，每一个物种或阶元都有一个taxid，他是taxa的ID。而且taxa之间存在父子关系。我们的研究对象是蜘蛛目（Aranaea），其taxaid为6893，其父级阶元是蛛形纲（Arachnida），taxaid为6854。按照递归查询的原则，只要有自6893以下所有taxa的父子关系对照表，就能查询到目前在GenBank中记录的所有蜘蛛的名录。
```
![](pattern/40.png)

```
但是设置参数BLAST后
```
![](pattern/41.png)
![](pattern/42.png)

```
Accession不一致
但是ident很高，score很高，cover也很高
=》进化。。。

系统发育树phylogenetic tree
1.ensembl
2.clustal omega
https://www.ebi.ac.uk/Tools/msa/clustalo/

进化树绘制算法：
1.distance：
   neighbor-joining 、UPGMA 
2.evolution：
   Maximum parsimony 、Maximum likelihood 

Genebank- Genome数据库中下载多种真菌或细菌的基因组序列
-》使用blastn进行两两比较，根据相似性打分绘制进化树；
   使用Mauve进行获得进化树
=》相互比较
```
### <a id="8"></a>RNA序列分析
```
Coding RNA------mRNA
Non-coding RNA （ncRNA):
    rRNA
    tRNA
    micro RNA
    siRNA 
    long ncRNA
RNA相关数据库：
http://research.imb.uq.edu.au/rnadb/index.htm
http://biobases.ibch.poznan.pl/ncRNA/
http://www.science.co.il/Biomedical/RNA-Databases.asp
http://mybio.wikia.com/wiki/RNA_database
http://rfam.xfam.org
http://mods.rna.albany.edu/
http://www.mirbase.org
http://sirna.sbc.su.se/
http://www.ncrna.org/
http://lncrnadb.com/

1.sequence secondary structure prediction
2.Single sequence tertiary structure prediction
3.Comparative methods
4.Inter molecular interactions: RNA-RNA, MicroRNA:any RNA, MicroRNA:UTR
5.ncRNA gene prediction software
6.Family specific gene prediction software RNA homology search software Benchmarks Alignment viewers/editors Inverse Folding/RNA design Secondary structure viewers/editors

1.rna结构预测：
RNAfold WebServer
结果两张图：一种是最小自由能预测，一种是热力学整体预测
http://www.ebi.ac.uk/Tools/msa/clustalw2/
2.计算RNA序列自身内部的碱基配对折叠
3.密码子偏好性和优化：
密码子使用偏差是指编码DNA中同义密码子出现频率的差异。
会影响RNA二级结构
影响转录/基因的表达
影响翻译伸长速度
影响蛋白质折叠
http://genomes.urv.cat/OPTIMIZER
http://bioinfo.hr/research/inca/
http://www.jcat.de/CAICalculation.jsp
http://www.jcat.de/

课堂练习三、 密码子优化改造 
（1）目标基因：人的任意一个编码 蛋白的基因 
（2）目标物种：一是酵母 （yeast），二是细菌（E.coli）
课堂练习三、 密码子优化改造
•	目标基因：人的任意一个编码蛋白的基因 
APOE基因
=》NM_000041.4 进入mRNA区
=》cds
=》截取coding区
```
![](pattern/43.png)

```
Atgaaggttctgtgggctgcgttgctggtcacattcctggcaggatgccaggccaaggtggagcaagcggtggagacagagccggagcccgagctgcgccagcagaccgagtggcagagcggccagcgctgggaactggcactgggtcgcttttgggattacctgcgctgggtgcagacactgtctgagcaggtgcaggaggagctgctcagctcccaggtcacccaggaactgagggcgctgatggacgagaccatgaaggagttgaaggcctacaaatcggaactggaggaacaactgaccccggtggcggaggagacgcgggcacggctgtccaaggagctgcaggcggcgcaggcccggctgggcgcggacatggaggacgtgtgcggccgcctggtgcagtaccgcggcgaggtgcaggccatgctcggccagagcaccgaggagctgcgggtgcgcctcgcctcccacctgcgcaagctgcgtaagcggctcctccgcgatgccgatgacctgcagaagcgcctggcagtgtaccaggccggggcccgcgagggcgccgagcgcggcctcagcgccatccgcgagcgcctggggcccctggtggaacagggccgcgtgcgggccgccactgtgggctccctggccggccagccgctacaggagcgggcccaggcctggggcgagcggctgcgcgcgcggatggaggagatgggcagccggacccgcgaccgcctggacgaggtgaaggagcaggtggcggaggtgcgcgccaagctggaggagcaggcccagcagatacgcctgcaggccgaggccttccaggcccgcctcaagagctggttcgagcccctggtggaagacatgcagcgccagtgggccgggctggtggagaaggtgcaggctgccgtgggcaccagcgccgcccctgtgcccagcga
```

```
•	目标物种：一是酵母 （yeast）
=》导入”Coden Adaptation Tool”http://www.jcat.de/Result.jsp
=》选择“Saccharomyces cerevisae”物种 

图表 1.密码子优化结果
=》将优化前后的序列导入”RNAfold WebServer”进行比较 http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi
```
### <a id="9"></a>题目
```
（        ）1、	下列哪个基因位于人类基因组2号染色体的1到100,000区间内？
A. APOB			B. ALK				C. MSH2			D.** FAM110C**

（        ）2、	在GFF1格式的基因组注释文件中，描述序列特征（feature）信息是哪一列？
A. 1					B. **3**					C. 5					D. 7

（        ）3、	编号为rs1045435的SNP与哪一个基因相关？
A. CDK1			B.** CDK2**			C. CDK3			D. CDK6

（        ）4、	人类（human）的ID为1636、名称为ACE的基因，在小鼠（mouse）中的同源基因ID是哪一个？
A. **11421**			B. 419953			C. 565980			D. 100144634

（        ）5、	利用UCSC genome browser整合的各种注释信息，在人类（human）的GRCh37/hg19版本基因组中检索MYC基因，哪些转录因子在其上游启动子区域1kb以内有强结合位点？
A. **TBP**		B. **E2F1**				C.** E2F4**			D. **POU2F2**

（        ）6、	对下图描述中哪些是正确的？
 
A. X是可观察输出			B.** y是可观察输出**	
C. **a是转移概率**				D. b隐藏状态

（        ）7、	给定一个转录因子结合位点的碱基分布的Matrix，下面哪个序列片段最有可能是该Matrix所代表的转录因子结合位点？
PO	A	C	G	T
01	31	14	4	1	
02	0	0	50	0	
03	48	2	0	0	
04	43	1	5	1	
05	23	1	14	12	

A. AGAAC			B. CGAAA
C. CGAAG			D.** AGAAA**
（        ）8、	给定一个TATA-box的HMM模型，哪个位点保守性最高？
Position	1	2	3	4	5	6	7	8	9	10	11	12
% A	21.4	15.9	3.7	91.1	0.0	94.5	67.3	97.3	52.1	40.7	16.5	23.6
% C	22.7	39.3	9.8	0.0	0.0	0.0	0.0	0.0	0.0	9.1	34.8	37.1
% G	28.2	35.2	2.9	0.0	0.0	0.0	0.0	2.7	12.0	40.2	38.0	30.4
% T	27.7	9.6	83.6	8.9	100.0	5.5	32.7	0.0	35.9	10.0	10.7	8.9

A. 4				B.** 5**				C. 6				D. 7	
（        ）9、	启动子按照位置（相对于基因转录起始位点）来分，一般可分为哪几类？
A. **核心启动子** 			B. **近端启动子** 				C. **远处启动子** 
（        ）10、	在真核生物启动子数据库（EPD）中，人类TP53基因的启动子有几个？
A. 1		B. **2**		C. 3		D. 4
（        ）11、	根据ENCODE的ChIP-seq数据，下列哪些转录因子在人类DDIT3基因的启动子区域（上游1-1000bp以内）存在结合位点？
A.PHF8		B.**PML**		C.**KDM5B**		D. NRF1
（        ）12、	下面是一条人类某基因上游1kb的序列，使用TSSW分析时，启动子位置在哪里？
GGAGACCACCCCCGTTTTTTTGTTTGTTTGTTTTGTTTTTTGTTTTTGGTGAAACGTAGT
CTCGCTCTGTCACCCAGGCTGGAGTGCAGTGGCGCGATCTCGGTCACTGCAACATCCGCC
TCCAGGGTTCAAGCGATTCTTCTGCCTCTGCCTCCAGAGTAGCTGGGATTACAGGCGCGC
ATCACCACACCCGGCTAATTTTTGTATTTTTAGTAGAGACGGGGTTTCACCATGTTGGTC
AGGCTGATCTCGAACTCCTGACCTCAAGTGATCCGCTCTCCTCAGCCTCCCAAAGTGCTG
GGATTACAGGCGTAAGCCACTGAGCCCGGCCAGGAGACCTCTTTAAGAAGACTCGAGATG
TCGACAATCCCAGTGGATGGATACCAACTTTAAAAAGAAAAGTTCAAAAGGCCTATGTGC
CCATTAGCTGGGAGGGGCCAAGAAATATGGGAGTCCCTTATAGTGGGGGTAAAACGGCGG
GTAAAGCTAGGTGGGCGGAACAGCAGCTTCTGGGGGAGACAAGCGGCAAAGAGGCTCACG
ACCGACTAGGGGCGACCAAGGCTGATAGCCGTTGGGGCCGTTGGGCGCCGGGAGCTGGCG
CCCCGCCCTCTCTCCTCTCCCCCACCCTCCGCACCTCCCACCACCCTCGGTGTCCCCTGC
GCGTGCGCGTGCAGACACCGGTTGCCAAACATTGCATCATCCCCGCCCCCCTTTCCTCCC
CTCCCCCCCCGCTACACTCCCCTCCGCGCGCGCGCATGACTCACCCACCTCCTCCGTGAA
GCCTCGTGACCCAAAGCCACTTCCGGGTCCGACACTACGTCGACCCCCTAGCGAGAGGGA
GCGACGGGGGCGGTGCCGCGGGGCTCCTGAGTGGCGGATGCGAGGGACGGGGCGGGGCCA
ATGCCGGCGTGCCACTTTCTGATTGGTAGGTTTTGGGGTCCCGCCCCTGAGAGGAGGGCA
AGGCCATGGTAAAAGATTACAGCCAGGCGCTCCCGAGGTC
A. 600		B. **638**		C. 909		D.** 952**

（        ）1、	下面哪些是属于基因组进化的研究内容？
A.** structural analysis of the genome**
B. **the study of genomic parasites **
C. **gene and ancient genome duplications**
D. **polyploidy**
E. **comparative genomics**

（        ）2、	新基因产生的机制有哪些？
A.** exon shuffling **				B.** gene fission/fusion**
C. **retrotransposition	**			D. **duplication-divergence**
E. **lateral gene transfer**

（        ）3、	下面三条序列所代表的物种之间，哪两个亲缘关系更近？
[CLUSTAL]
>1
MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE
>2
MGDVEKGKKIFVQKCAQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGFSYTDANKNKGITWGEETLMEYLENPKKYIPGTKMIFAGIKKKGEREDLIAYLKKATNE
>3
MGDVEKGKKVFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAEGFSYTDANKNKGIVWDEDTLMVYLENPKKYIPGTKMIFAGIKKKGERQDLIAYLKQSTSS

A.** 1 and 2** 	B. 1 and 3 	C. 2 and 3

（        ）4、	下列RNA中哪些属于广义non-coding RNA范畴？
A. mRNA		B. **tRNA**		C. **rRNA**		D. **miRNA**

（        ）5、	下列中哪一中RNA的二级结构是三叶草型的？
A. mRNA		B.** tRNA**		C. rRNA		D. miRNA

（        ）6、	下列系统发育树（进化树）构建算法中哪些是基于距离的？
A. **neighbor-joining** 			B. **UPGMA** 	
C. Maximum parsimony 		D. Maximum likelihood 

（        ）7、	CLIP是针对下列哪种研究领域的全基因高通量检测技术？
A. DNA-protein	B. **RNA-protein**	C. protein-protein	D. RNA-RNA

（        ）8、	Long non-coding RNA的研究思路，通常参照哪种RNA？
A. mRNA		B. tRNA		C. rRNA		D. **miRNA**


（        ）9、	下列关于密码子偏好性的描述正确的有哪些？
A. **不同物种之间的密码子偏好性通常存在差异**
B. **基因组的编码区和基因间区域的密码子偏好性通常存在差异**
C. **密码子偏好性会影响RNA二级结构**
D. **密码子偏好性会影响mRNA的翻译效率**


（        ）10、	不同基因组区间的序列在进化上的保守性从高到低排列正确的是哪一个?
A. Intergenic region > Intron > Exon > CDS
B. Exon > Intron > Intergenic region > CDS
C. **CDS > Exon > Intron > Intergenic region**
D. CDS > Intron > Exon > Intergenic region

```