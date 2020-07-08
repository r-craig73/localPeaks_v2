# localPeaks_v2.py

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/localPeaks_v2

## Description
###  A Python script that detects and lists local maxima from an imported two column ASC file.

### Peak detection method: SciPy signal package and scipy.signal.find_peaks function.  "The function takes a one-dimensional array and finds all local maxima by simple comparison of neighboring values."  Prominence peak limit is set to 1.

### User can run the script by running...
* Input: (powershell)>py .\pathTo...\localPeaks_v2.py "C:\pathTo...\file.asc" thresholdValue
* Output: TXT file "file-LocalPeaks.txt" located in the "C:\pathTo...\file.asc" path with peaks sorted in time and value columns, tab delimited.
### Pros: Script works.
### Cons: Require SiPy package, slow results, possible prominence value issues, and smelly code.

## Technologies Used
```
Application: Python 3.8.2 64-bit
Packages: os, csv, and SciPy
Testing: None
```

### Things to do: Add error filtering to verify thresholdValue is a float number.

