import numpy as np
import pandas as pd
from statsmodels.stats.libqsturng import psturng, qsturng
def SEDifference(n1, n2, MSE):
    return (1/np.sqrt(2))*np.sqrt(MSE*(1/n1+1/n2))#standard error difference formula
datastat=pd.read_clipboard()
SSE=0 #SUM OF SQUARES ERROR
for i in range(len(datastat["SD"].values)):
    SSE1=(datastat["SD"].values[i])**2
    SSE2=(datastat["N"].values[i]-1)*SSE1 ##group df*group variance
    SSE=SSE+SSE2##sum
MSE=SSE/(sum(datastat["N"].values)-len(datastat["SD"].values)) #SSE/df MEAN SQUARED ERROR
output001=pd.DataFrame()
output1=pd.DataFrame()

for b in range(len(datastat["SD"].values)-1):
    c=b+1
    for d in range(c,len(datastat["SD"].values)):
        q=np.absolute(datastat["mean"].values[b]-datastat["mean"].values[d])/SEDifference(datastat["N"].values[b],datastat["N"].values[d],MSE) #mean difference/standard error difference
        output001['name1']=[datastat["name"].values[b]] # for some reason square brackets are absolutely neccessary
        output001['name2']=datastat["name"].values[d]
        output001['q']=q
        output001['p']=psturng(q, len(datastat["N"].values), (sum(datastat["N"].values)-len(datastat["N"].values))) #convert to p values
        output1=pd.concat([output1, output001])
output1
