import random
import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd

# import residents list as xlsx file 
residents_df = pd.read_csv('ResidentsList.csv')
# slice the data frame from each column
resident_names = residents_df['Name'].tolist()
resident_seniority = residents_df['Seniority'].tolist()
resident_Hallway = residents_df['Hallway'].tolist()
resident_Kitchen_comp = residents_df['Kitchen comp'].tolist()
resident_Kitchen_bonus = residents_df['Kitchen bonus'].tolist()
resident_bathroom_comp = residents_df['bathroom comp '].tolist()
resident_bathroom_bonus = residents_df['bathroom bonus'].tolist()
resident_common_comp = residents_df['common comp'].tolist()
resident_common_bonus = residents_df['common bonus'].tolist()

# print a few number of residents to verify
for i in range(5):
	print(f"Resident: {resident_names[i]}, Seniority: {resident_seniority[i]}, Hallway: {resident_Hallway[i]}, Kitchen Comp: {resident_Kitchen_comp[i]}, Kitchen Bonus: {resident_Kitchen_bonus[i]}, Bathroom Comp: {resident_bathroom_comp[i]}, Bathroom Bonus: {resident_bathroom_bonus[i]}, Common Comp: {resident_common_comp[i]}, Common Bonus: {resident_common_bonus[i]}")