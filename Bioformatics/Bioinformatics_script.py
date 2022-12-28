# Store the DNA sequences in variables
seq1 = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
seq2 = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"

# Initialize a variable to store the Hamming distance
distance = 0

# Iterate through the sequences and compare the bases at each position
for i in range(len(seq1)):
  if seq1[i] != seq2[i]:
    distance += 1

# Print the Hamming distance
print("Hamming distance: ", distance)

# Store the DNA sequence in a variable
dna_sequence = "GATACACTTCCCGAGTAGGTACTG"

# Initialize variables to store the minimum Skewi value and the corresponding position
min_skewi = float("inf")
min_position = 0

# Store the DNA sequence in a variable
dna_sequence = "GATACACTTCCCGAGTAGGTACTG"

# Initialize variables to store the minimum Skewi value and the position where it occurs
min_skewi = float("inf")
min_pos = -1

# Iterate through the DNA sequence and calculate the Skewi value at each position
for i in range(len(dna_sequence)):
  skewi = dna_sequence[:i+1].count("G") - dna_sequence[:i+1].count("C")
  if skewi < min_skewi:
    min_skewi = skewi
    min_pos = i

# Print the position where Skewi attains a minimum value
print("Minimum Skewi at position: ", min_pos)

# Store the DNA sequence in a variable
dna_sequence = "CGTGACAGTGTATGGGCATCTTT"

# Use the count() method to count the number of occurrences of the string "TGT" in the DNA sequence
count1 = dna_sequence.count("TGT")

# Print the result
print("Count1(CGTGACAGTGTATGGGCATCTTT, TGT): ", count1)


# Store the k-mer in a variable
kmer = "CCAGTCAATG"

# Initialize a counter to store the number of 10-mers in the 1-neighborhood
count = 0

# Iterate through the possible 10-mers and count those that are at most Hamming distance 1 from the k-mer
for i in range(1024):
  # Generate the 10-mer by replacing the bases at each position with the corresponding base in the binary representation of i
  neighbor = ""
  for j in range(10):
    if i & (1 << j):
      neighbor += "ACGT"[j % 4]
    else:
      neighbor += kmer[j]
  # Count the 10-mer if it is at most Hamming distance 1 from the k-mer
  if sum(1 for a, b in zip(neighbor, kmer) if a != b) <= 1:
    count += 1

# Print the result
print("Number of 10-mers in the 1-neighborhood of" +kmer+":", count)

