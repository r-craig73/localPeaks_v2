# localPeaks_v2.py

### by Ron Craig (ron.craig@comcast.net)
### GitHub repository: https://github.com/r-craig73/localPeaks_v2

## Description
###  A Python script that detects and lists local maxima from a two column, tab-delimited ASC or TXT file.

### Peak detection method: SciPy signal package and scipy.signal.find_peaks function.  "The function takes a one-dimensional array and finds all local maxima by simple comparison of neighboring values."  Prominence peak limit is set to 1.

### User can run the script by inputting the following command below...
* Input: (Powershell Terminal)
* ```>py .\pathTo...\localPeaks.py 'C:\pathTo...\filename.asc' thresholdValue```

command | os.sys.argv[0] | os.sys.argv[1] | os.sys.argv[2]
------- | -------------- | -------------- | --------------
```>py``` | ```.\pathTo...\localPeaks.py``` | ```'C:\pathTo...\filename.asc'``` | ```thresholdValue```
* Output #1: (Powershell Terminal) ```Peaks detected: 15```
* Output #2: A txt, tab delimited named "filename-LocalPeaks.txt" located in the "C:\pathTo...\filename.asc" path (or folder where the imported filename is located) with peaks sorted in time and value columns.

### Pros: Script works.
### Cons: Require SciPy package, slow results, possible prominence value issues, and smelly code.

### Technologies Used
* ```Application: Python 3.8.2 64-bit```
* ```Packages: os, csv, and SciPy```

### Things to do..
- [ ] Raise an exception when the Input's thresholdValue is NOT inputted.
- [ ] Raise an exception when the Input's thresholdValue is NOT a float number.

