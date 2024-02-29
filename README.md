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

- [ ] Step 1: Download and extract paired-end fastq files from the SRA database
- [ ] Step 2: Using biopython's Entrez and other libraries, download a reference genome and extract only coding sequences from it to be used to build a transcriptome index
- [ ] Step 3: Using Kallisto, build a transcriptome index for the reference CDS sequences extracted
- [ ] Step 4: Again, with Kallisto, quantify TPM for each CDS in each transcriptome, while finding the mean, midian, minimum and maximum
- [ ] Step 5: Find differentially expressed genes between two conditions (here, my target is between 2dpi and 6 dpi)
- [ ] Find other virus strains that have genes encoding the most differentially expressed genes using BLAST

## Step One (Retrieving Patients Transcriptome Data)


[*] The following data was extracted from the SRA database using the links provided below with the 'wget' command in our compbio server.
Donor 1 (2dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896360
Donor 1 (6dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896363 
Donor 3 (2dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896374 
Donor 3 (6dpi): https://www.ncbi.nlm.nih.gov/sra/SRX2896375

### Creating a subdirectory for my transcripts

> pwd ### Check my current directrory
'/home/basante1' ### This is my current directory

> mkdir Project ### Creating a folder called 'Project' to hold my data
> cd ./Project ## Moving into my created folder 

#### Downloading the Sequences to my 'Project' folder
> wget https://www.ncbi.nlm.nih.gov/sra/SRX2896360
> wget https://www.ncbi.nlm.nih.gov/sra/SRX2896363
> wget https://www.ncbi.nlm.nih.gov/sra/SRX2896374
> wget https://www.ncbi.nlm.nih.gov/sra/SRX2896375

#### Extracting to get paired-end fastq files from my downloaded files
fastq-dump -I --split-files SRX2896360
fastq-dump -I --split-files SRX2896363
fastq-dump -I --split-files SRX2896374
fastq-dump -I --split-files SRX2896375

#### Checking out the files in my 'Project' folder
> ls -lh ./Project
'''The **--split-files** option separates the files into both forward and reverse reads
 


# Methods

# Code

# References

