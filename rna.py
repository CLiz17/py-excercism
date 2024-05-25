def to_rna(dna_strand):
    result = []
    for char in dna_strand:
        if char == "G":
            result.append("C")
        elif char == "C":
            result.append("G")
        elif char == "T":
            result.append("A")
        elif char == "A":
            result.append("U")
    return "".join(result)