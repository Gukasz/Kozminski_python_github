
# homework from class 2

import requests
import io
import numpy as np
import pandas as pd

URL = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Tips/tips.csv'
s=requests.get(URL).content

tips_df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)


# 1. Find out the average `tip` for each `sex`, `smoker`, `time` and `day`.
mean_tip_by_day = tips_df.groupby('day')['tip'].mean()
print(mean_tip_by_day)

mean_tip_by_sex = tips_df.groupby('sex')['tip'].mean()
print(mean_tip_by_sex)

mean_tip_by_smoker = tips_df.groupby('smoker')['tip'].mean()
print(mean_tip_by_smoker)

mean_tip_by_time = tips_df.groupby('time')['tip'].mean()
print(mean_tip_by_time)

# 2. Combine all mentioned columns into a single combination to find out the average `tip` for each combination.
mean_tip_by_all = tips_df.groupby(['day', 'sex', 'smoker', 'time'])['tip'].mean()
print(mean_tip_by_all)

# 3. Display the highest and lowest `tip` for each `day`.
tips_df.groupby('day')['tip'].agg(['max', 'min'])

# 4. Count the number of `smoker` and `non-smoker` for each `day`.
tips_df.groupby(['day', 'smoker']).size()

# 5. Find out the average `total_bill` for each `day` and `time` combination.
tips_df.groupby(['day', 'time'])['total_bill'].agg('mean')

# 6. Use the describe function to get the statistics for `total_bill` for each `day` and `time` combination.
tips_df.groupby(['day', 'time'])['total_bill'].describe()

# homework class 3