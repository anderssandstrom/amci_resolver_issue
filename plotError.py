#!/usr/bin/python
# coding: utf-8
import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from caPVArrayLib import caPVArray
from caMonitorArrayParserLib import caMonitorArrayParser 
 
def printOutHelp():
  print ("python plotError.py")


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
  
  pvNames.append("ForwardY")
  pvNames.append("ForwardX")
  pvNames.append("BackwardY")
  pvNames.append("BackwardX")

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
  index=0
  for pvname in pvNames:
    avg=np.mean(yData[index])
    mini=np.min(yData[index])
    maxi=np.max(yData[index])
    yDataAvg.append(avg)
    yDataMax.append(maxi)
    yDataMin.append(mini)
    print(pvname + ': '+ str(mini) + '..'+ str(maxi) + ' ' + str(avg))
    index=index+1

  plt.rcParams.update({'font.size': 20})

  legstr=[]
  legstr.append("Forward direction")
  legstr.append("Backward direction")

  fig1=plt.figure(1)
  ax1=fig1.add_subplot(1, 1, 1)
  ax1.plot(yData[1],yData[0], 'b')
  ax1.plot(yData[3],yData[2], 'g')
  #ax1.set_ylabel("Error [deg]")
  ax1.legend(legstr)
  ax1.grid()
  plt.title('Resolver error vs position (as recorded)')

  plt.xlabel("Angle [deg]", fontsize=20)
  plt.ylabel("Error [deg]", fontsize=20)

  # Best case
  offset=(yDataMin[0]+yDataMax[2])/2
  fig2=plt.figure(2)
  ax1=fig2.add_subplot(1, 1, 1)
  ax1.plot(yData[1],yData[0] - offset, 'b')
  ax1.plot(yData[3],yData[2] - offset, 'g')
  #ax1.set_ylabel("Error [deg]")
  ax1.legend(legstr)
  ax1.grid()
  plt.title('Resolver error vs position (best case)')

  plt.xlabel("Angle [deg]", fontsize=20)
  plt.ylabel("Error [deg]", fontsize=20)

  # Worst case
  offset=yDataMin[0]
  fig3=plt.figure(3)
  ax1=fig3.add_subplot(1, 1, 1)
  ax1.plot(yData[1],yData[0] - offset, 'b')
  ax1.plot(yData[3],yData[2] - offset, 'g')
  #ax1.set_ylabel("Error [deg]")
  ax1.legend(legstr)
  ax1.grid()
  plt.title('Resolver error vs position (worst case)')

  plt.xlabel("Angle [deg]", fontsize=20)
  plt.ylabel("Error [deg]", fontsize=20)
  plt.show()

if __name__ == "__main__":
  main()
