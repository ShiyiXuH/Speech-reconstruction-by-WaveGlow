rm(list = ls())  # delete all variables, clear cache

#install.packages('stringr')
library(stringr)
library(afex)

#set variables for input directory (where the result files are) and output directory (Anova output, etc)
input_dir = "/Users/apple/Library/CloudStorage/OneDrive-UniversityCollegeLondon/MOS_res/exp2_intelligibility"
output_dir = "/Users/apple/Library/CloudStorage/OneDrive-UniversityCollegeLondon/MOS_res/R_output"

#set working directory (to the input directory)
setwd( input_dir )

filenames = dir()[grep(".txt", dir())]        # get filenames of all text files in the working directory
filenames = dir()[grep("^2.*.txt$", dir())]   # create variable with filenames of all text files in the working directory that start with "2" and end with ".txt"

num_files = length( filenames ) # length of filenames is the number of files that we want to iterate through

all_res= NULL # table for all data, empty for now

i=1

for ( i in 1:num_files ) # iterate through all files
{
  this_res = read.table(filenames[i], header=F)                                 
  subject = substr(filenames[i],3,7)                                            
  recognition_rate = this_res[,2]                                               
  a = do.call(rbind, strsplit(as.character(this_res[,1]),split="/") )           # first column contains filenames in format "sounds/vc4_143.wav". Split by "/"
  rev_split = lapply(strsplit(as.character(a[,2]),split='_'), rev)
  b = do.call(rbind, lapply(rev_split, function(x) {
    list(condition = paste(rev(x[-1]), collapse='_'), sound_id = x[1])
  }))
  condition = b[,1] 
  #bands = as.numeric( gsub("[^0-9.-]", "", condition) )                         # The number of bands are represented by the number in the condition
  vocoder_type = str_detect(condition,'f') * 1                                 # 1= bandpassed, o=synthesized or original
  sound_id = b[,2]                                                              # Not used for analysis, the pfart after the _ represents the recording that was used
  this_table = cbind(subject,condition, vocoder_type, recognition_rate, sound_id) # form a table with 6 columns of the variables that we just created
  all_res = rbind(all_res,this_table)                                           # attach this table at bottom of results table all_res
}
all_res = data.frame(all_res)                                                   # transform to data frame type

#-----------------------------------------------
all_res$condition <- as.character(all_res$condition)
mean_recognition = aggregate(as.numeric(all_res$recognition_rate), list(condition=all_res$condition),mean)
sd_recognition = aggregate(as.numeric(all_res$recognition_rate), list(condition=all_res$condition),sd)

trials_per_condition = nrow(all_res) / nrow(sd_recognition)
se = sd_recognition$x / sqrt( trials_per_condition )
ci95 = 1.96 * se
m  = mean_recognition$x
#-----------------ploting---------------------
line_width = 1.5
expansion = 1.2
arrow_width = 0.05



plot( 1:4, m[1:4],  type="p", col="indianred2", pch=16, lty=1, xlab="Condition", ylab="Word recognition rate (%)", ylim=c(-5,108), xlim=c(0.5,6.5),lwd=line_width, cex.axis=expansion, cex.lab = expansion, cex = expansion, xaxt="none" )
axis(side = 1, at = 1:4, labels = c("band1", "band2","band3","band4"))

arrows(1:4, m[1:4]+sd_recognition$x[1:4], 1:4, m[1:4]-sd_recognition$x[1:4], angle=90, code=3,lwd=line_width,length=arrow_width,col="indianred2")

lines(c(1.2,2.2,3.2,4.2), m[5:8],  type="p", col="#00BFC4", pch=17, lty=1,lwd=line_width, cex.axis=expansion, cex.lab = expansion, cex = expansion)

arrows(c(1.2,2.2,3.2,4.2), m[5:8]+sd_recognition$x[5:8], c(1.2,2.2,3.2,4.2), m[5:8]-sd_recognition$x[5:8], angle=90, code=3,lwd=line_width,length=arrow_width, col="#00BFC4")

# 绘制额外的点
points(5, m[9], pch=16, col="indianred2", cex=1.2) # x轴为80的点
axis(side = 1, at = 5, labels = "80")
points(6, m[10], pch=15, col="black", cex=1.2) # x轴为original的点
axis(side = 1, at = 6, labels = "original")

# 绘制箭头
arrows(5, m[9]+sd_recognition$x[9], 5, m[9]-sd_recognition$x[9], angle=90, code=3, lwd=line_width, length=arrow_width, col="indianred2") # x轴为80的箭头
arrows(6, m[10]+sd_recognition$x[10], 6, m[10]-sd_recognition$x[10], angle=90, code=3, lwd=line_width, length=arrow_width, col="black") # x轴为original的箭头

# 添加legend
legend(0.8,108, legend=c("WaveGlow", "Bandpass filter", "Original speech"), col=c("indianred2", "#00BFC4", "black"), pch=c(16, 17, 15), cex=0.9)


#-----------------ANOVA---------------------
ana_data <- all_res
ana_data$condition <- gsub("filtered_bin1_normal", "bin1", ana_data$condition)
ana_data$condition <- gsub("filtered_bin2_normal", "bin2", ana_data$condition)
ana_data$condition <- gsub("filtered_bin3_normal", "bin3", ana_data$condition)
ana_data$condition <- gsub("filtered_bin4_normal", "bin4", ana_data$condition)

data_cleaned <- ana_data[!(ana_data$condition == "normal" | ana_data$condition == "original"), ]

data_cleaned$recognition_rate <- as.numeric(data_cleaned$recognition_rate)

data_cleaned$vocoder_type <- unlist(data_cleaned$vocoder_type)
data_cleaned$vocoder_type <- factor(data_cleaned$vocoder_type, levels=c(0, 1), labels=c("WaveGlow","Bandpass filter")) 

data_cleaned$condition <- factor(data_cleaned$condition, 
                                 levels = c("bin1", "bin2", "bin3", "bin4"),
                                 labels = c("band1", "band2", "band3", "band4"))

data_cleaned$subject <- unlist(data_cleaned$subject)
data_cleaned$subject <- as.factor(data_cleaned$subject)


recog_anova <- aov_car(recognition_rate ~ vocoder_type * condition + Error(subject/(vocoder_type*condition)), data = data_cleaned)

r3 <- aov(recognition_rate ~ vocoder_type * condition + Error(subject/(vocoder_type*condition)), data = data_cleaned)
summary(r3)