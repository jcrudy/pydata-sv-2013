'''
Created on Mar 13, 2013

@author: jasonrudy
'''
infilename = 'housing.data'
outfilename = 'housing.csv'
header = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
infile = open(infilename, 'r')
outfile = open(outfilename, 'w')
outfile.write(','.join(header))
for line in infile:
    outfile.write('\n')
    outfile.write(','.join(line.split()))
infile.close()
outfile.close()
    
    
