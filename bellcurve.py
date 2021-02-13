import random
import statistics
import plotly.figure_factory as ff

dice_result=[]
list_ofdata=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

#calculating mean and std
mean=sum(dice_result)/len(dice_result)
mode=statistics.mode(dice_result)
std_dev=statistics.stdev(dice_result)


#print(mean)
#print(std_dev)
#fig=ff.create_distplot([dice_result],["result"],show_hist=False)
#fig.show()
first_std_start,first_std_end=mean-std_dev,mean+std_dev
second_std_start,second_std_end=mean-(2*std_dev),mean+(2*std_dev)
list_of_1tsd_data=first_std_end+first_std_start
print("mean and mode of dice roll is {} , {} ".format(mean,mode))
print(" {} % of data lies within 1 std dev".format((list_of_1tsd_data)*100.0/len(dice_result)))

''' example of format function
# The values passed as parameters 
# are replaced in order of their entry 
print ("This is {} {} {} {}"
       .format("one", "two", "three", "four")) '''