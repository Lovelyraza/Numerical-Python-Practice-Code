import numpy as np
# temp=np.array([30.5, 32.0, 35.1, 33.3, 31.2])
# print(temp)
# degre_tem=temp*1.8+32
# print(degre_tem)
marks = np.array([80, 75, 90, 60, 85])
# print(f"Total Marks in of Student={marks.sum()}")
# print(f"Total Marks in of Student={marks.mean()}")
# print(f"Total Marks in of Student={(390/500)*100}")
# total = np.sum(marks)
# average = np.mean(marks)
# percentage = (total / 500) * 100

# print("Total:", total)
# print("Average:", average)
# print("Percentage:", percentage)
# indexing slicing and conditions 
# sensor = np.array([23, 25, 28, 31, 35, 40, 38, 30, 28, 25])
# print(sensor[sensor>30])
# sensor[sensor>35]=35
# print(sensor)
# print(sensor[::-1])
# data = np.array([
#     [85, 78, 90, 88],   # Student 1
#     [75, 80, 70, 85],   # Student 2
#     [90, 88, 92, 95]    # Student 3
# ])
# student_mark_avg=np.mean(data,axis=1)
# subject_mark_avg=np.mean(data,axis=0)
# print(student_mark_avg)
# print(subject_mark_avg)
# sales=np.random.randint(1000,5000,size=(7,3))
# print(sales)
# shop_total = np.sum(sales, axis=0)
# print("Total sales per shop:", shop_total)
# print('After sorting the shop by sale ')
# sorted_sales = sales[sales[:, 0].argsort()]
# print("Sorted by Shop1 Sales:\n", sorted_sales)

covid_data = np.array([
    [50, 70, 90, 40],
    [55, 60, 100, 35],
    [45, 80, 110, 38],
    [60, 75, 95, 42]
])
# week_avg=np.mean(covid_data,axis=1)
# # print(covid_data)
# # city_total=np.sum(covid_data,axis=0)
# city_total = np.sum(covid_data, axis=0)
# max_cases=np.max(city_total)
# print(max_cases)
# # print(city_total)
city_avg = np.mean(covid_data, axis=0)
print("City-wise Average Cases:", city_avg)

city_total = np.sum(covid_data, axis=0)
max_index = np.argmax(city_total)
print(f"City {max_index+1} has max cases: {city_total[max_index]}")
