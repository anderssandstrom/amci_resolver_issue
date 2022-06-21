#!/usr/bin/python
# coding: utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
import math as math
from datetime import datetime
from caPVArrayLib import caPVArray
from caMonitorArrayParserLib import caMonitorArrayParser 
 
def printOutHelp():
  print ("python slask.py")
  print ("Custom plot for target rotor displacement sensors: cat *.log | slask.py")

def main():
  # Check args
  if len(sys.argv)>1:    
    pos1=sys.argv[1].find('-h')
    if(pos1>=0):
      printOutHelp()
      sys.exit()

  scale=1.0  # default

  if len(sys.argv)==2:      
     scale=float(sys.argv[1])

  
  pvNames=[]
  
  startPvName="Axis"
  pvNames.append("Axis")
  pvNames.append("Enc")

  dataFile=sys.stdin

  parser = caMonitorArrayParser()
  pvY=[]  
  for pvname in pvNames:
   pvY.append(caPVArray(pvname))
  
  for line in dataFile:
    
    if not parser.lineValid(line):      
      continue
    
    lineValid = False
    for pvname in pvNames:
      if line.find(pvname)!=-1:
        lineValid=True;

    if not lineValid:
      continue  
    
    # just store every other value

    pvName, timeVal, data = parser.getValues(line)
    

    index=0
    for pvname in pvNames:      
      if pvName.find(pvname)>=0:
        pvY[index].setValues(timeVal,data)
      index=index+1

  yTime=[]
  yData=[]
  index=0

  for pvname in pvNames:
    yTimeTemp,yDataTemp = pvY[index].getData()
    print(pvname +"[" + str(len(yDataTemp)) + "]")
    yTime.append(yTimeTemp)
    yData.append(yDataTemp)
    index=index+1
  
  yDataAvg=[]
  yDataMax=[]
  yDataMin=[]
  yDataLen=[]
  yDataAvg=[]
  index=0
  for pvname in pvNames:
    yAvgTemp=np.mean(yData[index])
    yDataAvg.append(yAvgTemp)
    yMaxTemp=np.max(yData[index])
    yDataMax.append(yMaxTemp)
    yMinTemp=np.min(yData[index])
    yDataMin.append(yMinTemp)
    yLenTemp=len(yData[index])
    yDataLen.append(yLenTemp)
    print(pvname + "[" + str(yLenTemp) + "] " + str(yMinTemp) + ".." + str(yMaxTemp) + "avg: " + str(yAvgTemp)  )
    index=index+1


  
  fig2=plt.figure(2)
  
  # find fist zero crossing

  

  #delin resolver
  vals=1000
  z, res, g, g, g = np.polyfit(yData[0][0:vals], yData[1][0:vals], 1, full=True)

  deLin=yData[1][0:vals]-np.polyval(z,yData[0][0:vals])
  print (deLin)
#
  yold=deLin[0]
  counter=0
  for y in deLin:
    if y>0 and yold<0:
      break
    yold=y
    counter=counter+1


  
  ax1=fig2.add_subplot(1, 1, 1)
  
  ax1.plot((yData[0][counter:vals]-np.floor(yData[0][counter:vals]))*360,deLin[counter:vals], 'b')
  #ax1.plot((yData[0][counter:vals]),deLin[counter:vals], 'b')
  #ax1.plot((yData[0][counter:vals]),deLin[counter:vals], 'b')
  #ax1.plot(yData[0][counter:vals],deLin[counter:vals], 'b')
  ax1.set_ylabel("Error [mm]")
  
  ax1.grid()

  
  
  plt.xlabel("Position [deg]")
  plt.show()


if __name__ == "__main__":
  main()
