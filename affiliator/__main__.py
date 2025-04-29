#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Convert a spread sheet file containing Author-Affiliations to LaTeX header for use with package authblk
It also prints out the EPJ and arXiv formats

2023/2024 xaratustrah
"""

from pyexcel_ods import get_data
import sys, re

AFF_COLUMN_START = 5


def process_tables(data):
    # collect all affiliations in a list

    affs = []
    for row in data["Sheet1"][1:]:
        for entry in row[AFF_COLUMN_START:]:
            affs.append(entry)

    # make unique entries
    # keep the order of appearance

    affs_clean = []
    for aff in affs:
        if aff not in affs_clean:
            affs_clean.append(aff)

    final_affiliations_list_authblk = []
    final_affiliations_list_epj = []
    final_affiliations_list_arxiv = []

    i = 1
    for aff in affs_clean:
        final_affiliations_list_authblk.append(f"\\affil[{i}]{{{aff}}}")
        final_affiliations_list_epj.append(f"{aff}")
        final_affiliations_list_arxiv.append(f"({i}) {aff}")
        i += 1

    # now deal with author names

    final_authors_list_authblk = []
    final_authors_list_epj = []
    final_authors_list_arxiv = []

    for row in data["Sheet1"][1:]:
        aff_idx = []

        for entry in row[AFF_COLUMN_START:]:
            if entry in affs_clean:
                aff_idx.append(affs_clean.index(entry))

        # shift indexes
        aff_idx = [i + 1 for i in aff_idx]

        # create name
        name = row[1] + " " + row[2]

        # add tilda for LaTeX
        name = re.sub(r"\s+", "~", name)

        final_authors_list_authblk.append(f"\\author{aff_idx}{{{name}}}")

        final_authors_list_epj.append(f"{name}\\inst{{{', '.join(map(str, aff_idx))}}}")

        final_authors_list_arxiv.append(f"{name} ({' and '.join(map(str, aff_idx))})")

    return (
        final_authors_list_authblk,
        final_affiliations_list_authblk,
        final_authors_list_epj,
        final_affiliations_list_epj,
        final_authors_list_arxiv,
        final_affiliations_list_arxiv,
    )


def main():
    filename = sys.argv[1]
    data = get_data(filename)
    (
        final_authors_list_authblk,
        final_affiliations_list_authblk,
        final_authors_list_epj,
        final_affiliations_list_epj,
        final_authors_list_arxiv,
        final_affiliations_list_arxiv,
    ) = process_tables(data)

    print("\n\nauthblk format: \n\n")

    print(
        "\n".join(final_authors_list_authblk),
        "\n",
        "\n".join(final_affiliations_list_authblk),
    )

    print("\n\nEPJ format: \n\n")

    print("\\author{\n", " \\and\n".join(final_authors_list_epj), "\n}")

    print("\institute{\n", " \\and\n".join(final_affiliations_list_epj), "\n}\n")

    print("\n\n arXiv format:\n\n")

    print(", ".join(final_authors_list_arxiv))

    print("(", ", ".join(final_affiliations_list_arxiv), ")")


# ------------------------
if __name__ == "__main__":
    main()
