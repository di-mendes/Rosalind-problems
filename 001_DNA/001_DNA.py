'''
Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna/
'''

# Open the file and read the DNA string
with open(r"C:\Users\diogo\OneDrive\Ambiente de Trabalho\rosalind_dna(5).txt", 'r') as f:
    raw_seq = f.readline().rstrip()

# Count and print the occurrences of each nucleotide
print(raw_seq.count("A"), raw_seq.count("C"), raw_seq.count("G"), raw_seq.count("T"))
