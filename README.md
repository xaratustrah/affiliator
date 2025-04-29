# affiliator

This script converts a spread sheet file containing Author-Affiliations to LaTeX header for use with package `authblk`. This might be needed for submission to some journals. Two additional Journal formats are also supported, the EPJ format.

authblock format renders the list to this output:

```
\author[1]{Author One}
\author[1,2]{Author Two}
\author[2]{Author Three}
\affil[1]{Affiliation1}
\affil[2]{Affiliation2}
```

The EPJ format:

```
\author{
Author One\inst{1} \and
Author Two\inst{1, 2} \and
Author Three\inst{2}
}
\institute{
Affiliation1 \and
Affiliation2
}
```

The arXiv format:

```
Author One (1), Author Two (1 and 2), Author Three (2)
((1) Affiliation1, (2) Affiliation2)
```

## Motivation

Some journals need a specific Author Affiliation format, which is based on LaTeX package `authblk`. But sometimes it is easier to manage the affiliations of a large collaboration using a spreadsheet file, like in [LibreOffice](https://www.libreoffice.org/). After you set the order of the appearance of the authors, then you can feed the ODS file to the script. It will automatically generate the LaTeX header. 

## Installation

You can directly use the app:

```
python3 -m affiliator coauthor_list.ods
```

or first install it by:

```
pip install -r requirements.txt
pip install .
```

Uninstalling is similarly using `pip`.


## Example:

For example an ODS file containing this information:


| First      | First Abb. | Last     | Email                       | ORCID               | 1st Affiliation | 2nd Affiliation | 3rd Affiliation    | 4th Affiliation                      |
|------------|------------|----------|-----------------------------|---------------------|-----------------|-----------------|--------------------|--------------------------------------|
| Eva Lilith | E. L.      | Cielo    | elcielo@example.edu         | 0000-0123-4567-8910 | City University | College of Arts | Another University | University of Antarctica             |
| Eva Maria  | E. M.      | Cemballo | elcielo@example.another.edu | 0000-0123-4567-8910 | City University | Penn State      | Another University | Japan University of Natural Sciences |


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

Here is a link to the [exampmle file](https://github.com/xaratustrah/affiliator/blob/main/rsrc/test.ods).
