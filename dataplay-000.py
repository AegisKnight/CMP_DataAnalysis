import pandas as pd

def makeNewCSV(file,rows,footer,waferid,flag):
    df = pd.read_csv(str(file), index_col = 'TIMESTAMP')
    subfile = open('temp', 'w')
    first = True
    header = ''
    waferids = []
        for line in df:
            if(first):
    df.to_csv('WAFER_ID_'+str(waferid)+'.csv')
    if flag is True:
        print(df)

def timelinearInterpolation(initialtime,finaltime,truetime,initialparam,finalparam):
    slope = (finalparam - initialparam)/(finaltime - initialtime)
    trueparam = initialparam + (truetime - initialtime)*slope
    return trueparam

waferlist = []
    

#data-000
makeNewCSV('CMP-training-000.csv',0,3377,371447024,False)      #286 rows
waferlist.append('WAFER_ID_371447024.csv')
makeNewCSV('CMP-training-000.csv',287,3091,371447028,False)    #286 rows
waferlist.append('WAFER_ID_371447028.csv')
makeNewCSV('CMP-training-000.csv',573,2815,371447036,False)    #276 rows
waferlist.append('WAFER_ID_371447036.csv')
makeNewCSV('CMP-training-000.csv',849,2459,-4113511818,True)  #356 rows
waferlist.append('WAFER_ID_-4113511818.csv')
makeNewCSV('CMP-training-000.csv',1205,2106,-4113511780,False) #353 rows
waferlist.append('WAFER_ID_-4113511780.csv')
makeNewCSV('CMP-training-000.csv',1558,1755,-4224160584,False) #351 rows
waferlist.append('WAFER_ID_-4224160584.csv')
makeNewCSV('CMP-training-000.csv',1909,1404,-4224160580,False) #351 rows
waferlist.append('WAFER_ID_-4224160580.csv')
makeNewCSV('CMP-training-000.csv',2260,1051,-2697400536,False) #353 rows
waferlist.append('WAFER_ID_-2697400536.csv')
makeNewCSV('CMP-training-000.csv',2613,710,-4224160600,False)  #341 rows
waferlist.append('WAFER_ID_-4224160600.csv')
makeNewCSV('CMP-training-000.csv',2954,356,-4113511814,False)  #354 rows
waferlist.append('WAFER_ID_-4113511814.csv')
makeNewCSV('CMP-training-000.csv',3308,0,-873170248,False)     #357 rows
waferlist.append('WAFER_ID_-873170248.csv')

'''
#data-001
makeNewCSV('CMP-training-001.csv',0,4963,-875170052,False) #358 rows
makeNewCSV('CMP-training-001.csv',359,4606,-4113511796,False) #357 rows
makeNewCSV('CMP-training-001.csv',716,4257,-873170272,False) #349 rows
makeNewCSV('CMP-training-001.csv',1065,3904,-4224160694,False) #353 rows
makeNewCSV('CMP-training-001.csv',1418,3551,-4224160690,False) #353 rows
makeNewCSV('CMP-training-001.csv',1771,3192,-2697400532,False) #359 rows
makeNewCSV('CMP-training-001.csv',2130,2830,-4113511792,False) #362 rows
makeNewCSV('CMP-training-001.csv',2492,2468,-4224160600,False) #362 rows
makeNewCSV('CMP-training-001.csv',2854,2113,-4224160592,False) #355 rows
makeNewCSV('CMP-training-001.csv',3209,1746,-873170256,False) #367 rows
makeNewCSV('CMP-training-001.csv',3576,1400,-4113511808,False) #346 rows
makeNewCSV('CMP-training-001.csv',3922,1047,-4113511752,False) #353 rows
makeNewCSV('CMP-training-001.csv',4275,696,-4113511748,False) #351 rows
makeNewCSV('CMP-training-001.csv',4626,349,-4111511820,False) #347 rows
makeNewCSV('CMP-training-001.csv',4973,0,-4113511756,False) #349 rows

#data-002
makeNewCSV('CMP-training-002.csv',0,8979,371447032,False) #267 rows
makeNewCSV('CMP-training-002.csv',268,8713,373446778,False) #266 rows
makeNewCSV('CMP-training-002.csv',534,8423,329446712,False) #290 rows
makeNewCSV('CMP-training-002.csv',824,8151,329446692,False) #272 rows
makeNewCSV('CMP-training-002.csv',1096,7878,329446708,False) #273 rows
makeNewCSV('CMP-training-002.csv',1369,7513,-4224160646,False) #365 rows
makeNewCSV('CMP-training-002.csv',1734,7153,-873170354,False) #360 rows
makeNewCSV('CMP-training-002.csv',2094,6782,-4113511814,False) #371 rows
makeNewCSV('CMP-training-002.csv',2465,6410,-875170112,False) #372 rows
makeNewCSV('CMP-training-002.csv',2837,6044,-873170272,False) #366 rows
makeNewCSV('CMP-training-002.csv',3203,5685,-873170366,False) #359 rows
makeNewCSV('CMP-training-002.csv',3562,5320,-4113511826,False) #365 rows
makeNewCSV('CMP-training-002.csv',3927,4964,-873170346,False) #356 rows
makeNewCSV('CMP-training-002.csv',4283,4618,-4111511824,False) #346 rows
makeNewCSV('CMP-training-002.csv',4629,4252,-4113511818,False) #366 rows
makeNewCSV('CMP-training-002.csv',4995,3888,-873170342,False) #364 rows
makeNewCSV('CMP-training-002.csv',5359,3536,-873170248,False) #352 rows
makeNewCSV('CMP-training-002.csv',5711,3192,-873170318,False) #344 rows
makeNewCSV('CMP-training-002.csv',6055,2847,-4226160424,False) #345 rows
makeNewCSV('CMP-training-002.csv',6400,2484,-4113511792,False) #363 rows
makeNewCSV('CMP-training-002.csv',6763,2119,-4224160690,False) #365 rows
makeNewCSV('CMP-training-002.csv',7128,1776,-4224160650,False) #343 rows
makeNewCSV('CMP-training-002.csv',7471,1426,-4224160694,False) #350 rows
makeNewCSV('CMP-training-002.csv',7821,1046,-873170244,False) #380 rows
makeNewCSV('CMP-training-002.csv',8201,701,-4224160702,False) #345 rows
makeNewCSV('CMP-training-002.csv',8546,345,-4113511808,False) #356 rows
makeNewCSV('CMP-training-002.csv',8902,0,-873170338,False) #345 rows
'''


#for waferdata in list(waferlist):
#    dfw = pd.read_csv(waferdata)
#    print(dfw)
#    for time in dfw['TIMESTAMP']:
#        tminus1 = time
#        print(tminus1)
#        time = dfw[i+1]['TIMESTAMP']
#        print(str(tminus1)+str(time))
        
#check csv
print('Done.')