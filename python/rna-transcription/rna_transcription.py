def to_rna(dna_strand):

    dna_list = list(dna_strand)

    rna_string = ""

    for character in dna_list:
        if character == "G":
            rna_string += "C"
        elif character == "C":
            rna_string += "G"
        elif character == "T":
            rna_string += "A"
        elif character == "A":
            rna_string += "U"

    return rna_string





