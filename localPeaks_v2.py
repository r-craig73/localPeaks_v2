import os, csv
from scipy.signal import find_peaks

def peaks(file, yLimit):
    times, peaks, x, y = [], [], [], []

    # open *.asc file
    openFile = open(file, 'r')
    read = csv.reader(openFile, delimiter='\t')

    # change data list to float format
    data = [list(map(float, sublist)) for sublist in read]

    for i in range(0, len(data), 1):
        x.append(data[i][0])
        y.append(data[i][1])

    peakElements, _ = find_peaks(y, height=float(yLimit), prominence=1)
    peaksFound = peakElements.tolist()
    print(f'Peaks detected: {str(len(peaksFound))}')
    
    for i in range(0, len(peaksFound), 1):
        times.append(x[peaksFound[i]])
        peaks.append(y[peaksFound[i]])
    
    f = open(file[0:-4] + '-LocalPeaks.txt', 'w')
    f.write('time\t' + 'value\n')
    for i in range(len(times)):
        f.write(str(times[i]) + '\t' + str(peaks[i]) + '\n')
    f.close

def main():
    filePath = os.sys.argv[1]
    head, tail = os.path.split(filePath)
    limit = os.sys.argv[2]
    if  tail[-3:].lower().endswith(('txt', 'asc')) is True:
        peaks(filePath, limit)
    else:
        print('File is not a txt or asc file type.')

if __name__ == '__main__':
    main()