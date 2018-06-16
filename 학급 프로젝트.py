
# coding: utf-8

# In[30]:


import csv
import matplotlib.pyplot as plt

name_station = input("조회를 원하는 역:")
f = open('2014년-일별-역별-시간대별-승하차인원_1_8호선_.csv', encoding = 'utf8')
result = []
result_help = []
check = 0
sp = 0
sp_help = 0
check2 = 0
data = list(csv.reader(f))
for row in data :
    check2 = check2 + 1
    if name_station in row[2]:
        if check == 0:
            for i in range(len(row)-4):
                if sp == 0:                 
                    result.append(int(row[i+4])/730)
                else:
                    result_help.append(int(row[i+4])/730)
            if sp == 0:
                sp_help = check2
            else:
                sp_help = check2 - sp_help
            sp = sp + 1        
            check = check + 1
        else:
            result_help = []
            for i in range(len(row)-4):
                result_help.append(int(row[i+4])/730)
            check = 0;
        if sp !=1 and check !=1:
            for i in range(len(result)):
                result[i] = result[i] + result_help[i]
        if sp == 2 and check == 0:
            break
for k in range(check2 + sp_help , len(data) , sp_help):
            for i in range(20):
                row = data[k]
                result[i] = result[i] + int(row[i+4])/730
            for i in range(20):
                row = data[k+1]
                result[i] = result[i] + int(row[i+4])/730
plt.plot(result)
plt.xticks(range(20),range(5,25))
plt.rc('font',family='Malgun Gothic')
plt.xlabel('시간')
plt.ylabel('혼잡도')
plt.title(name_station)
plt.show()

var1 = (result[0] + result[1] + result[2] + result[3] + result[4]) / 5
var2 = (result[5] + result[6] + result[7] + result[8] + result[9] + result[10]) / 6
var3 = (result[11] + result[12] + result[13] + result[14] + result[15] + result[16]) / 6

h1 = var1/(var1 + var2 + var3)
h2 = var2/(var1 + var2 + var3)
h3 = var3/(var1 + var2 + var3)

if (var1 / (var1 + var2 + var3))+(var3/(var1 + var2 + var3)) >=0.7:
    print("이 지역은 경제중심지 혹은 교통중심지입니다.")
elif (var2 / (var1 + var2 + var3)) >=0.35:
    print("이 지역은 관광지 혹은 관광지의 중간로입니다.")
elif (var1 / (var1 + var2 + var3)) >=0.35:
    print("이 지역은 교통중간로입니다.")
elif (var3 / (var1 + var2 + var3)) >=0.35:
    print("이 지역은 문화중심지입니다.")

             


# In[ ]:



             
                

