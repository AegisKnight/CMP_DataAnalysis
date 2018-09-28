import pandas as pd

def makeCSV(fileAddress):
    sourcefile = open(fileAddress, 'r')
    subfile = open("temp",'w')
    first = True;
    header=""
    waferids = []
    for line in sourcefile:
        if(first):
            first=False
            header=line.split(',')
            header[0],header[1],header[2] = header[2],header[0],header[1]
            del header[3]
            continue
        splitline = line.split(',')
        splitline[0],splitline[1],splitline[2] = splitline[2],splitline[0],splitline[1]
        waferid = splitline[3]
        del splitline[3]
        
        if waferid not in waferids:
            waferids.append(waferid)
            subfile.close()
            subfile = open('WAFER_ID_'+str(waferid)+'.csv','w')
            subfile.write(','.join(map(str, header)))
        else:
            subfile.write(','.join(map(str, splitline)))
            
    return waferids

def timelinearInterpolation(initialtime,finaltime,truetime,initialparam,finalparam):
    slope = (finalparam - initialparam)/(finaltime - initialtime)
    trueparam = initialparam + (truetime - initialtime)*slope
    return trueparam

m0 = makeCSV('CMP-training-000.csv')
           
    