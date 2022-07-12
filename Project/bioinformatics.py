# To find K-mers
def  Frequent_Kmer(p,length):
    import collections
    int(length)

    l_all_words_counter=collections.Counter(p[i:i + length] for i in range(0, len(p) - length + 1))
    l_max_value=max(l_all_words_counter.values())
    l = [k for k,v in l_all_words_counter.items() if v == l_max_value]
    print(' '.join(l))

#Pattern Matching
def Pattern_Matching(p,t):
    Pattern = str(p)
    Genome = str(t)
    Position = []
    for i in range(len(Genome) - len(Pattern)+1):
        if Genome[i:i + len(Pattern)] == Pattern:
            Position.append(i)
    print("Position: ",*Position)
# clump Finding problem
def Find_Clumps(text, k, l, t):
    kmer = []
    for i in range(0, len(text)-l):
        window = text[i:i+l]
        lst = []
        for n in range(0, k):
            for i in range(n, len(window) - 1, k):  # Freqency
                lst.append(window[i:i+k])
        for i in lst:
            if lst.count(i) == t:
                kmer += [i]
            return(set(kmer))

# Sknew analysis
def Skew(text): # Estimating Skew

    skew = 0

    skew_list= []

    skew_list.append(0)

    for i in range(len(text)):

        if text[i] == 'C' :

            skew = skew - 1

        elif text[i] == 'G':

            skew += 1

        else :

            skew = skew

        skew_list.append(skew)

    return skew_list
def Min_Skew(text): # Min Skewness


    skew_list = Skew(text)

    minimum = min(skew_list)

    min_skew_list = list()

    for i in range(len(text)):

        if skew_list[i] == minimum:

            min_skew_list.append(i)

    min_skew_list = str(min_skew_list)

    min_skew_list = min_skew_list.replace(',','')

    print(min_skew_list)
def Max_Skew(text):  # Max Skewness 

    skew_list = Skew(text)

    maximum = max(skew_list)

    max_skew_list = list()

    for i in range(len(text)):

        if skew_list[i] == maximum:

            max_skew_list.append(i+1)

    max_skew_list = str(max_skew_list)

    max_skew_list = max_skew_list.replace(',','')

    print(max_skew_list)
def Hamming_Distance(string1, string2): # Hamming Distance between two Sequence
    dist_counter = 0
    for n in range(len(string1)):
        if string1[n] != string2[n]:
            dist_counter += 1
            print(dist_counter)


def Data_input(t,p,n):
    Skew(t)
    Min_Skew(t)
    Max_Skew(t)
    Hamming_Distance(t)
    if p == str() and n != int(0):  # P = string and N not equal to 0 execute.
        Frequent_Kmer(p,n)
    # Find_Clumps(t) # No idea what to do with this Defination.
    if p == str():
        Pattern_Matching(p,t)

