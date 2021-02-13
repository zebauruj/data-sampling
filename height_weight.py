import random
import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv

df=pd.read_csv("C:/Users/zeba/Desktop/python/normaldistribution/data.csv")
height_list=df["Height(Inches)"].tolist()
weight_list=df["Weight(Pounds)"].tolist()

#mean 
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
#median
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)
#mode
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)
#std deviation
height_std=statistics.stdev(height_list)
weight_std=statistics.stdev(weight_list)

#printing mean,median,mode
print("Mean,median and mode of height is{}, {} and {}".format(height_mean,height_median,height_mode))
print("Mean,median and mode of weight is{}, {} and {}".format(weight_mean,weight_median,weight_mode))

#1,2, and 3 std of height
height_1std_strt,height_1std_end=height_mean-height_std,height_mean+height_std
height_2std_strt,height_2std_end=height_mean-(2*height_std),height_mean+(2*height_std)
height_3std_strt,height_3std_end=height_mean-(3*height_std),height_mean+(3*height_std)

#1,2, and 3 std of weight
weight_1std_strt,weight_1std_end=weight_mean-weight_std,weight_mean+weight_std
weight_2std_strt,weight_2std_end=weight_mean-(2*weight_std),weight_mean+(2*weight_std)
weight_3std_strt,weight_3std_end=weight_mean-(3*weight_std),weight_mean+(3*weight_std)

#percentage of data within 1 ,2 and 3 std of height
height_list_1std=[result for result in height_list if result>height_1std_strt and result<height_1std_end]
height_list_2std=[result for result in height_list if result>height_2std_strt and result<height_2std_end]
height_list_3std=[result for result in height_list if result>height_3std_strt and result<height_3std_end]

#percentage of data within 1 ,2 and 3 std of weight
weight_list_1std=[result for result in weight_list if result>weight_1std_strt and result<weight_1std_end]
weight_list_2std=[result for result in weight_list if result>weight_2std_strt and result<weight_2std_end]
weight_list_3std=[result for result in weight_list if result>weight_3std_strt and result<weight_3std_end]

#print the percentage
print("{} of data for height lies within 1 std deviation ".format(len(height_list_1std)*100.0/len(height_list)))
print("{} of data for height lies within 2 std deviation ".format(len(height_list_2std)*100.0/len(height_list)))
print("{} of data for height lies within 3 std deviation ".format(len(height_list_3std)*100.0/len(height_list)))
print("{} of data for weight lies within 1 std deviation ".format(len(weight_list_1std)*100.0/len(weight_list)))
print("{} of data for weight lies within 1 std deviation ".format(len(weight_list_2std)*100.0/len(weight_list)))
print("{} of data for weight lies within 1 std deviation ".format(len(weight_list_3std)*100.0/len(weight_list)))