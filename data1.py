import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import csv
import statistics

df = pd.read_csv("data.csv")
fig = px.bar(df, x='parental level of education', y='math score')
fig.show()
height_list = df["math score"].to_list()
weight_list = df["reading score"].to_list()

#calculating mean of height and weight
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

#calculating median of height and weight
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

#calculating mode of height and weight
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

#printing mean median and mode
#format will fill in the 3 empty curly brackets respectively  
print("mean median and mode of height is {},{},{}".format(height_mean,height_median,height_mode))
print("mean median and mode of weight is {},{},{}".format(weight_mean,weight_median,weight_mode))

#std deviation for height and weight
#stdev is std deviation
height_sd = statistics.stdev(height_list)
weight_sd = statistics.stdev(weight_list)

#calculating 1 2 and 3 std deviations for height
height_firstsd_start,height_firstsd_end = height_mean-height_sd,height_mean+height_sd
height_secondsd_start,height_secondsd_end = height_mean-(2*height_sd),height_mean+(2*height_sd)
height_thirdsd_start,height_thirdsd_end = height_mean-(3*height_sd),height_mean+(3*height_sd)

#calculating 1 2 and 3 std deviations for weight
weight_firstsd_start,weight_firstsd_end = weight_mean-weight_sd,weight_mean+weight_sd
weight_secondsd_start,weight_secondsd_end = weight_mean-(2*weight_sd),weight_mean+(2*weight_sd)
weight_thirdsd_start,weight_thirdsd_end = weight_mean-(3*weight_sd),weight_mean+(3*weight_sd)

#list of data that lies between 1 2 and 3 std
height_list_of_data_within_1_std_deviation = [result for result in height_list if result>height_firstsd_start and result<height_firstsd_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result>height_secondsd_start and result<height_secondsd_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result>height_thirdsd_start and result<height_thirdsd_end]

#list of data that lies between 1 2 and 3 std
weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result>weight_firstsd_start and result<weight_firstsd_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result>weight_secondsd_start and result<weight_secondsd_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result>weight_thirdsd_start and result<weight_thirdsd_end]

#printing % of data in 1 2 and 3 std
#len will calculate the length of the list 
#number of elements in first std *100 and then divided by total number of elements in height_list
print("{} % of data for height lies within the first std deviation".format(len(height_list_of_data_within_1_std_deviation)*100/len(height_list)))
print("{} % of data for height lies within the second std deviation".format(len(height_list_of_data_within_2_std_deviation)*100/len(height_list)))
print("{} % of data for height lies within the third std deviation".format(len(height_list_of_data_within_3_std_deviation)*100/len(height_list)))

#printing % of data in 1 2 and 3 std
#len will calculate the length of the list 
#number of elements in first std *100 and then divided by total number of elements in weight_list
print("{} % of data for weight lies within the first std deviation".format(len(weight_list_of_data_within_1_std_deviation)*100/len(weight_list)))
print("{} % of data for weight lies within the second std deviation".format(len(weight_list_of_data_within_2_std_deviation)*100/len(weight_list)))
print("{} % of data for weight lies within the third std deviation".format(len(weight_list_of_data_within_3_std_deviation)*100/len(weight_list)))

