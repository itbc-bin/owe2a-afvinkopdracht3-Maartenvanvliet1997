import pickle, os

AA_dict = pickle.load(open('aa_dict.dat', 'rb'))

def main():
    file_name = show_FASTA()
    file = open_FILE(file_name)
    seq = read_SEQ(file)
    p_seq = create_PROTEIN(seq)

    print('Protein sequence: ', p_seq)

    try:
        b = input('Would you like to show the original sequence? (Y/N)\n').upper()
    except:
        print('Incorrect option.')

    if b == 'Y':
        print('The original sequence:\n', seq)


def show_FASTA():
    fa = []
    
    for name in os.listdir('.'):
        if name.endswith('.fasta'):
            fa.append(name)

    if fa != []:
        for i in range(len(fa)):
            print('[' + str(i + 1) + '] - ', fa[i])
        
        try:
            b = (int(input('Enter the number of the file you would like to use: ')) - 1)
        except ValueError:
            print('Incorrect option, please try again.')
            a = input('- Press Enter to continue -')
            os.system('CLS')

            show_FASTA()

        file_name = fa[b]

        return file_name

    print('No usable files have been found, please add one to the working directory',
          '\n' + str(pos))
    a = input('- Press Enter to continue -')
    os.system('CLS')

    show_FASTA()
    
def open_FILE(file_name):
    file = open(file_name, 'r').readlines()
    file = file[1:]

    return file

def read_SEQ(file):
    seq = []
    codon = ''
    start = False

    for line in file[:30]:
        line = line.rstrip().replace('N','')
        for char in line.lower():
            if len(codon) < 3:
                codon += char
            elif len(codon) >= 3:
                if codon == 'ATG' and start == False:
                    start = True
                else:
                    seq.append(codon)
                codon = ''

    return seq

def create_PROTEIN(seq):
    p_seq = ''
    
    for codon in seq:
        if codon in AA_dict:
            p_seq += AA_dict[codon]

    return p_seq

main()
                    
                






    
