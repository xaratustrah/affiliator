#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Convert a spread sheet file containing Author-Affiliations to LaTeX header for use with package authblk
It also prints out the EPJ format

2023/2024 xaratustrah
'''

from pyexcel_ods import get_data
import sys,re

AFF_COLUMN_START = 5

def process_tables(data):
    # collect all affiliations in a list

    affs = []
    for row in data['Sheet1'][1:]:
        for entry in row[AFF_COLUMN_START:]:
            affs.append(entry)
        
    # make unique entries
    # keep the order of appearance

    affs_clean = []
    for aff in affs:
        if aff not in affs_clean:
            affs_clean.append(aff)


    final_affiliations_list = []
    final_affiliations_list_epj = []
    
    i = 1
    for aff in affs_clean:
        final_affiliations_list.append(f'\\affil[{i}]{{{aff}}}')
        final_affiliations_list_epj.append(f'{aff}')
        i+= 1

    # now deal with author names

    final_authors_list = []
    final_authors_list_epj = []

    for row in data['Sheet1'][1:]:
        aff_idx = []

        for entry in row[AFF_COLUMN_START:]:
            if entry in affs_clean:
                aff_idx.append(affs_clean.index(entry))    

        # shift indexes
        aff_idx = [i+1 for i in aff_idx]

        # create name
        name = row[1] + ' ' + row[2]
        
        # add tilda for LaTeX
        name = re.sub(r"\s+", '~', name)
        
        final_authors_list.append(f'\\author{aff_idx}{{{name}}}')
               
        final_authors_list_epj.append(f'{name}\\inst{{{", ".join(map(str, aff_idx))}}}')
    
    return final_authors_list, final_affiliations_list, final_authors_list_epj, final_affiliations_list_epj


def main():
    filename = sys.argv[1]
    data = get_data(filename)
    final_authors_list, final_affiliations_list, final_authors_list_epj, final_affiliations_list_epj = process_tables(data)

    print('\n\nauthblk format: \n\n')
    
    print("\n".join(final_authors_list), '\n', "\n".join(final_affiliations_list))
    
    print('\n\nEPJ format: \n\n')
        
    print("\\author{\n", " \\and\n".join(final_authors_list_epj), '\n}')
    
    print("\institute{\n", " \\and\n".join(final_affiliations_list_epj), "\n}\n")
    
    

# ------------------------
if __name__ == '__main__':    
    main()
