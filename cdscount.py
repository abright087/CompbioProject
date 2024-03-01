#!/usr/bin/env python3

from Bio import Entrez, SeqIO
from Bio.SeqRecord import SeqRecord

## First, I wanted to count the number of CDS features directly from the genebank file and write the count number to my output file,
## so I first defined a function to count unique CDS features with the NCBI accession number given

## This is my python function to count CDS from the genebank file
def count_cds_sequences_from_accession(genome_accession):
    Entrez.email = "abright087@gmail.com" 
    handle = Entrez.efetch(db="nucleotide", id=genome_accession, rettype="gb", retmode="text")
    genbank_record = SeqIO.read(handle, "genbank")
    handle.close()
    
    ### To count the total CDS, I use the sum() funtion in this for loop, together with Entrez's '.feature' function
    cds_count = sum(1 for feature in genbank_record.features if feature.type == "CDS")
    return cds_count
  
## Now I will have to write the total number of CDS from our fasta file to my logfile
def write_count_to_file(count, logfile):
    with open(logfile, "w") as file:
      
      ## I want my logfile to print the count number with this string
      text = "The HCMV genome (NC_006273.2) has "+ str(count) + " CDS"
      file.write(text)

### Moving on to extract CDS sequenecs from Genebank and make a fasta file out of it
def download_genome_cds(genome_accession, cds_file):
    Entrez.email = "abright087@gmail.com"
    handle = Entrez.efetch(db="nucleotide", id=genome_accession, rettype="gb", retmode="text")
    genome_record = SeqIO.read(handle, "genbank")
    handle.close()

    cds_records = [] ## I initiate the cds_records to an empty list so that any other cds records can be added 
    for feature in genome_record.features:
        if feature.type == "CDS": ##Identify CDS with the '.feature.type()' function
            cds_seq = feature.extract(genome_record.seq)
            cds_record = SeqRecord(cds_seq, id=feature.qualifiers["protein_id"][0], description="")
            cds_records.append(cds_record) ## for any cds, which is identified with a unique protein id, add to my cds_records list

    SeqIO.write(cds_records, cds_file, "fasta")
    print("Your CDS sequences saved to:", cds_file)
        
if __name__ == "__main__":
    download_genome_cds(genome_accession, cds_file)
    genome_accession = 'NC_006273.2' ## My NCBI genome accession number
    cds_count = count_cds_sequences_from_accession(genome_accession)
    cds_file = "cds_sequences.fasta"  ## My output file name
    logfile = "PipelineProject.log" ##My logfile
    write_count_to_file(cds_count, logfile)
    print("Number of CDS sequences from"+ genome_accession + " written to:", logfile)
