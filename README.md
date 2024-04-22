This script renames .txt files created using mzxml2txt.py according to a .csv file of the corresponding MALDI plate map. 

The script requires a "clean" plate map in .csv format. And with "clean" I mean that the plate map should only contain the individual placement of spots and their corresponding names. Not the "coordinate" rows (fx 1-24) or columns (A-P).

Samples spotted in triplicate (or more) will be named [samplename_1.txt] for the first spot, [samplename_2.txt] for the second spot and [samplename_3.txt] for the third and so on.
