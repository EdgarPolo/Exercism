def distance(strand_a, strand_b, distancia=0):

    if len(strand_a) != len(strand_b):
        raise ValueError("ValueError")
    else:
        for x in range(len(strand_a)):
            if strand_a[x] != strand_b[x]:
                distancia += 1

    return distancia
