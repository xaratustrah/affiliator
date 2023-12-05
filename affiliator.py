#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Convert a spread sheet file containing Author-Affiliations to LaTeX header for use with package authblk

2023 xaratustrah
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
    i = 1
    for aff in affs_clean:
        final_affiliations_list.append(f'\\affil[{i}]{{{aff}}}')
        i+= 1

    # now deal with author names

    final_authors_list = []

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
    
    return final_authors_list, final_affiliations_list


def main():
    filename = sys.argv[1]
    data = get_data(filename)
    final_authors_list, final_affiliations_list = process_tables(data)
    print("\n".join(final_authors_list), '\n', "\n".join(final_affiliations_list))

# ------------------------
if __name__ == '__main__':    
    main()
