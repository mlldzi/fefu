def bin_seq(N):
    if N == 0:
        return ['']
    else:
        sequences = []
        for seq in bin_seq(N - 1):
            sequences.append(seq + '0')
            sequences.append(seq + '1')
        return sequences


def main():
    with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
        N = int(fin.read())
        sequences = bin_seq(N)
        for seq in sequences:
            fout.write(seq + '\n')


if __name__ == "__main__":
    main()
