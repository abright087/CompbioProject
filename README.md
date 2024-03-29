# CompbioProject (Track 1): Transcriptome Analysis of Human Cytomegalovirus (HCMV) with Kallisto and Sleuth

## Introduction

- [ ] This project aims to analyze transcriptome data of patients with Human Cytomegalovirus (HCMV) infection.
- [ ] Data for analysis is obtained from the NCBI's SRA database.

## Aim and Objective
- Extract CDS (coding sequences) from a reference genome
- Build a transcriptome index for HCMV with an appropriate reference genome using kallisto
- Quantify TPM (Transcript per million) of each CDS in each transcriptome
- Calculate the minimum, median, mean, and maximum TPM from the results obtained from the transcriptome index
- Perform Sleuth analysis to visualize differential expression of transcripts

## Project Workflow (Approach)

- [x] _**Step 1:**_ Download and extract paired-end fastq files from the SRA database
- [x] _**Step 2:**_ Using biopython's Entrez and other libraries, download a reference genome and extract only coding sequences from it to be used to build a transcriptome index
- [x] _**Step 3:**_ Using Kallisto, build a transcriptome index for the reference CDS sequences extracted
- [x] _**Step 4:**_ Again, with Kallisto, quantify TPM for each CDS in each transcriptome, while finding the mean, midian, minimum and maximum
- [x] _**Step 5:**_ Find differentially expressed genes between two conditions (here, my target is between 2dpi and 6 dpi)
- [x] _**Step 6:**_ Find other virus strains that have genes encoding the most differentially expressed genes using BLAST

## Step One (Retrieving Patients Transcriptome Data)


- [X] The following data was extracted from the SRA database using the links provided below with the 'wget' command in our compbio server.
1. Donor 1 (2dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896360
2. Donor 1 (6dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896363 
3. Donor 3 (2dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896374 
4. Donor 3 (6dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896375
      - [x] *dpi* == **days post infection**
   
### Creating a subdirectory for my transcripts

>> pwd ### Check my current directrory
'/home/basante1' ### This is my current directory

>> mkdir Project ### Creating a folder called 'Project' to hold my data
>> cd ./Project ## Moving into my created folder 

#### Downloading the Sequences to my 'Project' folder
1. >> wget https://www.ncbi.nlm.nih.gov/sra/SRX2896360
2. >> wget https://www.ncbi.nlm.nih.gov/sra/SRX2896363
3. >> wget https://www.ncbi.nlm.nih.gov/sra/SRX2896374
4. >> wget https://www.ncbi.nlm.nih.gov/sra/SRX2896375

#### Extracting to get paired-end fastq files from my downloaded files
1. >> fastq-dump -I --split-files SRX2896360
2. >> fastq-dump -I --split-files SRX2896363
3. >> fastq-dump -I --split-files SRX2896374
4. >> fastq-dump -I --split-files SRX2896375

#### Checking out the files in my 'Project' folder
1. >> ls -lh ./Project
'''The **--split-files** option separates the files into both forward and reverse reads
 
# Code
- [ ] - to be added soon


# References
1. https://github.com/pachterlab/kallisto
2. https://pachterlab.github.io/sleuth_walkthroughs/trapnell/analysis.html
3. https://pachterlab.github.io/sleuth/

