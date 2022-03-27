#loading the required libraries
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
fifa=pd.read_csv(r"D:\football analysis\player.csv")
print(fifa.head())
for col in fifa.columns:
    print(col)
fifa.shape
fifa['nationality'].value_counts()
fifa['nationality'].value_counts()[0:10]

fifa['nationality'].value_counts()[0:5].keys()

fifa['nationality'].value_counts()[0:5]
plt.figure(figsize=(5,5))
plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="g")
plt.show()
player_salary=fifa[['short_name','wage_eur']]
player_salary.head()
player_salary=player_salary.sort_values(by=['wage_eur'],ascending=False)
player_salary.head()
plt.figure(figsize=(8,5))
plt.bar(list(player_salary['short_name'])[0:5],list(player_salary['wage_eur'])[0:5],color=["blue","green","red","orange"])
plt.show()
fifa['nationality']=='Germany'

#germany
Germany=fifa[fifa['nationality']=='Germany']
Germany.head(10)


Germany.sort_values(by=['height_cm'],ascending=False).head()
Germany.sort_values(by=['weight_kg'],ascending=False).head()
Germany.sort_values(by=['wage_eur'],ascending=False).head()
Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False).head()
#shooting
player_shooting=fifa[['short_name','shooting']]
player_shooting.sort_values(by=['shooting'],ascending=False).head()
#defending
player_defending=fifa[['short_name','defending','nationality','club']]
player_defending.sort_values(by=['defending'],ascending=False).head()
real_madrid=fifa[fifa['club']=='Real Madrid']
real_madrid.sort_values(by=['wage_eur'],ascending=False).head()
real_madrid.sort_values(by=['shooting'],ascending=False).head()
real_madrid.sort_values(by=['defending'],ascending=False).head()
real_madrid['nationality'].value_counts()


