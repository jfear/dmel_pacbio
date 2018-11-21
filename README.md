# PacBio analysis for D. melanogaster

(1) The kit for the PacBio library construction
Clonetech SMARTer cDNA Synthesis Kit, SageELF Size-Selection System, and DNA Template Prep Kit V1.0 for SMRTbell template preparation
 
(2) The method to quantify and qualify the library
Qubit used to quantitate the library.
Bioanalyzer used to assess library size and quality.
 
(3) The method to do the PacBio sequencing (e.g., kit, machine)
DNA Sequencing Reagent kit 4.0 v2 (P6-C4 chemistry), 240 minute movie collection, PacBio RS II Sequencer

I can also run the IsoSeq analysis pipeline on the data – this includes:
1) classifying the reads of insert into full length and non-full-length sequences based on library adapter mapping. This step also trims the adapter sequences and filters out chimeric reads
2) clustering the classified reads to reduce the number of redundant reads and then use non-full-length reads to polish/improve clustered seqs using Quiver
3) collapsing similar transcripts to reduce redundancy further using reference alignment (using GMAP)

For each sample library, 3 size fractions were created and each individual library fraction was loaded/run separately to avoid loading bias.

size fractions:
ARL000*_1 = 1-2 kb
ARL000*_2 = 2-3 kb
ARL000*_3 = 3-6 kb

w1118_wfem1:
ARL0001_1
ARL0001_2
ARL0001_3

w1118_wmal1:
ARL0002_1
ARL0002_2
ARL0002_3

w1118_ovary1:
ARL0003_1
ARL0003_2
ARL0003_3

w1118_testi1:
ARL0004_1
ARL0004_2
ARL0004_3

Each library directory in Data_20160630 contains a subreads, roi1, ccs2 directory.

subreads = raw reads from the run; low accuracy reads (average accuracy 0.85, quality value 8) - filtered_subreads.fastq.gz

roi1 = circular consensus reads using current production software; higher accuracy reads; depending on number of passes, the reads can be > 0.999 accurate, > 30 quality value (see roi1_stats.txt file in each directory for statistics for each read) - roi1_stats.txt, reads_of_insert.fastq.gz

ccs2 = circular consensus reads using new development software that will be included in the next software release; improved algorithm; researchers have reported better results using ccs2 reads - ccs2_stats.txt, *.ccs.fastq.gz


For roi1, a description of the commands:
subreads and reads_of_insert (roi1) were generated using smrtpipe tools in PacBio SMRTanalysis software (ver. 2.3) from input bax.h5 files.
https://github.com/PacificBiosciences/cDNA_primer/wiki/Tutorial:-Getting-ReadsOfInsert-from-SMRT-Portal-or-through-the-command-line

filtered subreads = pbfilter (MinReadScore=0.7500,MinSRL=50,MinRL=50) and pls2fasta (tool to convert filtered h5 files to fasta/q)

reads_of_insert = ConsensusTools 
	minFullPasses = 1
	minPredictedAccuracy = 90
	numThreads = 11
 


The ccs2 pipeline isn't part of the current standard production software (v2.3).
It requires converting the bax.h5 files from our instrument to bam files and then running the ccs command. 
A description:
https://github.com/PacificBiosciences/unanimity/blob/master/doc/PBCCS.md

I ran the ccs command with:
maxLength = 40000
minPasses = 1
numThreads = 11

We still have the bax.h5 files for your runs and I can work on setting up the data transfer.

I have been primarily using GMAP for Iso_Seq transcript vs reference genome mapping.

 
(4) The method to generate ccs2, roi1, subreads
 
subreads and reads_of_insert (roi1) were generated using smrtpipe tools in PacBio SMRTanalysis software (ver. 2.3) from input bax.h5 files.
 
Specifically:
 
filtered subreads = pbfilter (MinReadScore=0.7500,MinSRL=50,MinRL=50) and pls2fasta (tool to convert filtered h5 files to fasta/q)
 
reads_of_insert = ConsensusTools (--minFullPasses 1 --minPredictedAccuracy 90)
 
new circular consensus (ccs2) reads generated using tools in PacBio pitchfork software package (ver. 0.0.2) from input bax.h5 files and samtools.
 
Specifically,
 
convert bax.h5 to bam = bax2bam
generate circular consensus = ccs (--maxLength=40000 --minPasses=1)
convert bam to fastq = samtools bam2fq


## Installing SMRT LINK 6.0
Need to change umlit u/n to 8192