### This is Sleuth for my transcriptpomics project
### First load the Sleuth package

library(sleuth)

#set my directory to where I have my files
setwd('/home/basante1/PipelineProject_Bright_Asante/')
stab = read.table("./kallistoOut.txt", header=TRUE)

#initialize sleuth object using sleuth_prep function from sleuth library
so = sleuth_prep(stab)

#fit a model comparing the two conditions 
so = sleuth_fit(so, ~condition, 'full')

#fit the reduced model to compare in the likelihood ratio test 
so = sleuth_fit(so, ~1, 'reduced')

#perform the likelihood ratio test for differential expression between conditions 
so = sleuth_lrt(so, 'reduced', 'full')

#load the dplyr package for data.frame filtering
library(dplyr)

#extract the test results from the sleuth object 
sleuth_table = sleuth_results(so, 'reduced:full', 'lrt', show_all = FALSE) 

#filter most significant results (FDR/qval < 0.05) and sort by pval
sleuth_significant = dplyr::filter(sleuth_table, qval <= 0.05) |> dplyr::arrange(pval) 

#print top 10 transcripts
head(sleuth_significant, n=10) ## This is just informative only, in case I want to have a quick look at my results

#write FDR < 0.05 transcripts to file
#Extract just transcript, test_stat, pval, qval (select by column header names) 
sleuth_filter = dplyr::select(sleuth_significant, target_id, test_stat, pval, qval)
head(sleuth_filter)
write.table(sleuth_filter, file = 'PipelineProject.log3', quote = FALSE, row.names = FALSE)