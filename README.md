# CompbioProject (Track 1): Transcriptome Analysis of Human Cytomegalovirus (HCMV) with Kallisto and Sleuth

# Introduction

[ x ] This project aims to analyze transcriptome data of patients with Human Cytomegalovirus (HCMV) infection.
[ x ] Data for analysis is obtained from the NCBI's SRA database.

# Step One (Retreiving Patients Transcriptome Data)

[-] The following data was extracted from the SRA database using the links provided below with the 'wget' command in our compbio server.

Donor 1 (2dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896360
Donor 1 (6dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896363 
Donor 3 (2dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896374 
Donor 3 (6dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896375

# Creating a subdirectory for my transcripts
pwd ### Check my current directrory
'/home/basante1' ### This is my current directory
mkdir Project ### Creating a folder called 'Project' to hold my data
cd ./Project ## Moving into my created folder 

# Downloading the Sequences to my 'Project' folder
wget https://www.ncbi.nlm.nih.gov/sra/SRX2896360
wget https://www.ncbi.nlm.nih.gov/sra/SRX2896363
wget https://www.ncbi.nlm.nih.gov/sra/SRX2896374
wget https://www.ncbi.nlm.nih.gov/sra/SRX2896375

## Extracting to get paired-end fastq files from my downloaded files
fastq-dump --splitfiles SRX2896360
fastq-dump --splitfiles SRX2896363
fastq-dump --splitfiles SRX2896374
fastq-dump --splitfiles SRX2896375

# Significance

# Aim and Objective
- Extract CDS (coding sequences) from a reference genome
- Build a transcriptome index for HCMV with an appropriate reference genome using kallisto
- Quantify TPM (Transcript per million) of each CDS in each transcriptome
- Calculate the minimum, median, mean, and maximum TPM from the results obtained from the transcriptome index
- Perform Sleuth analysis to visualize differential expression of transcripts 
 
# Study Workflow (Approach)

# Methods

# Code

# References

