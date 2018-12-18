from pyspark import SparkConf, SparkContext
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import string
import sys

conf = SparkConf().setMaster('local').setAppName('HiggsStatistics')
sc = SparkContext(conf=conf)

RDDRaw = sc.textFile("HIGGS.csv")
RDDfiltered = RDDRaw.map(lambda line: [float(x) for x in line.split(',')])
f = open("histogram_values.txt", "w+")
i = 1
while (i < 9):

    RDDneg = RDDRaw.filter(lambda line: float(line.split(',')[i])<  0).map(lambda line: ((line.split(',')[i]),(line.split(',')[0])))
    RDDpos = RDDRaw.filter(lambda line: float(line.split(',')[i])>= 0).map(lambda line: ((line.split(',')[i]),(line.split(',')[0])))

    negAndFound = RDDneg.filter(lambda x: float(x[1]) == 1).count()
    negAndNotFound = RDDneg.filter(lambda x: float(x[1]) != 1).count()
    posAndFound = RDDpos.filter(lambda x: float(x[1]) == 1).count()
    posAndNotFound = RDDpos.filter(lambda x: float(x[1]) != 1).count()
    aux = "Parameter no: "+ str(i)+"\n"
    f.write(aux)
    aux = str("Positive Values:\n")
    f.write(aux)
    aux = str("Bosson Found: "+ str(posAndFound)+ " Bosson Not Found: "+str(posAndNotFound))
    f.write(aux)
    aux = str("\nNegative Values:")    
    f.write(aux)
    aux = str("\nBosson Found: "+ str(negAndFound) + " Bosson Not Found: "+ str(negAndNotFound))
    f.write(aux)
    aux = str("\n\n")
    f.write(aux)
    i = i +1


f.close()
