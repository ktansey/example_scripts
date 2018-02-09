'''
Created on 04 Aug 2017

@author: katherine_tansey
'''

import sys
import argparse


def filter_genotypes(genotype_file, filter):
    filename = genotype_file.split(".")
    with open(genotype_file, 'rt') as f:
        sig = []
        datalines = (line.rstrip('\r\n') for line in f)
        for line in datalines:
            if line.startswith('#'):
                continue
            if line.startswith('alternate_ids'):
                row = line.split(' ')
                sig.append(line)
            else:
                row = line.split(' ')
                if row[41] != "NA" and float(row[41]) <= filter:
                    sig.append(line)

    with open(filename + "_filters.txt", 'w') as results:
        for row in sig:
            results.write( '%s\n' % str(row) )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--genotype_file', action='store', dest='input1')
    parser.add_argument('--filter', action='store', dest='input2')
    args = parser.parse_args()
    filter_genotypes(input1, input2)
