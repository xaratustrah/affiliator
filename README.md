# affiliator

This script converts a spread sheet file containing Author-Affiliations to LaTeX header for use with package `authblk`. This might be needed for submission to some journals.

## Motivation

Some journals need a specific Author Affiliation format, which is based on LaTeX package `authblk`. But sometimes it is easier to manage the affiliations of a large collaboration using a spreadsheet file, like in [LibreOffice](https://www.libreoffice.org/). After you set the order of the appearance of the authors, then you can feed the ODS file to the script. It will automatically generate the LaTeX header. 

## Usage example:
Type:

```
python3 affiliator.py coauthor_list.ods
```

For example an ODS file containing this information:

| First      | First Abb. | Last     | Email                        | ORCID               | 1. Afiiliation  | 2. Affiliation  | 3. Affiliation     | 4. Affiliation                       |
|------------|------------|----------|------------------------------|---------------------|-----------------|-----------------|--------------------|--------------------------------------|
| Eva Lilith | E. L.      | Cielo    | elcielo@example.edu          | 0000-0123-4567-8910 | City University | College of Arts | Another University | University of Antarctica             |
| Eva Maria  | E. M.      | Cemballo | elcielo@example.edumcemballo | 0000-0123-4567-8910 | City University | Penn State      | Another University | Japan University of Natural Sciences |


will render to:

```
\author[1, 2, 3, 4]{E.~L.~Cielo}
\author[1, 5, 3, 6]{E.~M.~Cemballo} 
\affil[1]{City University}
\affil[2]{College of Arts}
\affil[3]{Another University}
\affil[4]{University of Antarctica}
\affil[5]{Penn State}
\affil[6]{Japan University of Natural Sciences}
```

As long as the script knows on which column the affiliations start, all affiliations are considered. This can be set in the code.
