'''
Created on 04 Aug 2017

@author: katherine_tansey
'''

import sys
import argparse
     
def vcf_to_fasta(vcf_filename):
    with open("4024.vcf", 'rt') as f:
        geno_call = []
        for line in f:
            if line.startswith('#'):
                continue
            geno_line = line.split('\t')
            if len(geno_line) < 4:
                continue
            if geno_line[4] != '.' :
                geno_call.append(geno_line[4])
            else:
                geno_call.append(geno_line[3])

    with open('4024.fasta','w') as results:
        vcf_filename = "4024.vcf"
        sample_name = vcf_filename.split(".")[0]
        fasta_format = "".join(geno_call)
        results.write(">%s" % str(sample_name) + "\n" )
        results.write("".join(map(str, geno_call)))
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--vcf_file', action='store', dest='input')
    args = parser.parse_args()
    vcf_to_fasta(input)

