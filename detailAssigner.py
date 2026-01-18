import random
import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd

# import residents list as xlsx file 
residents_df = pd.read_csv('ResidentsList.csv')

# sort the residents by seniority (descending order)
residents_df = residents_df.sort_values(by='Seniority', ascending=True).reset_index(drop=True)
print("Residents data loaded and sorted by seniority.")
# print(residents_df.head())

# slice the data based on the first letter of the hallway
resident_girls = residents_df[residents_df['Hallway'].str.startswith('N')].reset_index(drop=True)
resident_boys = residents_df[residents_df['Hallway'].str.startswith('S')].reset_index(drop=True)

# print(resident_boys)

# separate each hallway group into their own dataframes
NW1_residents = resident_girls[resident_girls['Hallway'] == 'NW1'].reset_index(drop=True)
NW2_residents = resident_girls[resident_girls['Hallway'] == 'NW2'].reset_index(drop=True)
NE1_residents = resident_girls[resident_girls['Hallway'] == 'NE1'].reset_index(drop=True)
NE2_residents = resident_girls[resident_girls['Hallway'] == 'NE2'].reset_index(drop=True)
SW1_residents = resident_boys[resident_boys['Hallway'] == 'SW1'].reset_index(drop=True)
SW2_residents = resident_boys[resident_boys['Hallway'] == 'SW2'].reset_index(drop=True)
SE1_residents = resident_boys[resident_boys['Hallway'] == 'SE1'].reset_index(drop=True)
SE2_residents = resident_boys[resident_boys['Hallway'] == 'SE2'].reset_index(drop=True)
# print("Residents dataframes created for each hallway.")
# print(f"Number of residents in NW1: {len(NW1_residents)}")
# print(NW1_residents)

#-------------------------------------------------------------------
# kitchen detail assignment logics
num_kitchen_details = 25
resident_per_kitchen_detail = 3
kitchen_detail_assignments = []
first_round = True
#-------------------------------------------------------------------

# create a array for kitchen comp and bonus
kd_comp = residents_df[['Kitchen comp']].to_numpy()
kd_bonus = residents_df[['Kitchen bonus']].to_numpy()
# count how many new residents there are to assign kitchen details to
num_new_residents = len(residents_df[residents_df['Seniority'] == 0])
total_residents = len(residents_df)
print(f"Total residents: {total_residents}, New residents: {num_new_residents}")

round = 1 # this counter keeps in track of which round it is, so it determines how many details to assign to a specific person
# create an empty dictionary to hold the assignments
current_index = 0
old_resident_index = total_residents - 1 # because old residents are at the end of the sorted list

new_residents_counter = 0 # this keeps track of how many new residents have been assigned in the first round 
# generate an empty list to hold the assignments
kd_assignments = [["" for _ in range(resident_per_kitchen_detail)] for _ in range(num_kitchen_details)]
# print(np.array(kd_assignments).shape)

for ii in range(num_kitchen_details):
	if first_round:
		if new_residents_counter < num_new_residents:
			# assign one old residents with other new residents to the kitchen detail 
			while True: 
				# find the next old resident to assign
				if kd_comp[old_resident_index] == 100:
					# skip this resident as they have 100 compensation
					old_resident_index -= 1
				elif kd_bonus[old_resident_index] != 0:
					# skip this resident as they have a bonus for this time
					# decrement their bonus count 
					kd_bonus[old_resident_index] -= 1
					old_resident_index -= 1
				else:
					# assign this old resident to the kitchen detail
					kd_assignments[ii][0] = residents_df.iloc[old_resident_index]['Name']
					old_resident_index -= 1
					break

			for jj in range(1, resident_per_kitchen_detail):
				# check if the new residents has bonus or comp
				while True:
					# find the next new resident to assign
					if kd_comp[current_index] == 100:
						# skip this resident as they have 100 compensation
						current_index += 1
					elif kd_bonus[current_index] != 0:
						# skip this resident as they have a bonus for this time
						# decrement their bonus count 
						kd_bonus[current_index] -= 1
						current_index += 1
						
					else:
						# assign this new resident to the kitchen detail
						kd_assignments[ii][jj] = residents_df.iloc[current_index]['Name']
						current_index += 1
						new_residents_counter += 1
						break
		else: 
			# all new residents have been assigned, switching to normal assignment
			for jj in range(resident_per_kitchen_detail):
				# check if the resident has bonus or comp
				while True:
					# check if all residents have been assigned, if so, reset the index
					if current_index > old_resident_index:
						first_round = False
						round += 1
						if round == 5:
							round = round - 4
						current_index = 0
					# find the next resident to assign
					if kd_comp[current_index] == 100 or (kd_bonus[current_index] == 75 and round == 2):
						# skip this resident as they have 100 compensation
						current_index += 1
					elif kd_bonus[current_index] != 0:
						# skip this resident as they have a bonus for this time
						# decrement their bonus count 
						kd_bonus[current_index] -= 1
						current_index += 1
					else:
						# assign this resident to the kitchen detail
						kd_assignments[ii][jj] = residents_df.iloc[current_index]['Name']
						current_index += 1
						break
	else:
		# normal assignment after first round
		for jj in range(resident_per_kitchen_detail):
			# check if the resident has bonus or comp
			while True:
				# wrap around the current_index
				if current_index == total_residents:
					current_index = 0
					round += 1
					if round == 5:
						round = round - 4
				# find the next resident to assign
				if kd_comp[current_index] == 100 :
					# skip this resident as they have respective compensation
					current_index += 1
				elif round ==2 and kd_comp[current_index] == 75:
					# skip this resident as they have respective compensation
					current_index += 1
				elif round ==3 and (kd_comp[current_index] == 50 or kd_comp[current_index] == 75):
					# skip this resident as they have respective compensation
					current_index += 1
				elif round ==4 and (kd_comp[current_index] == 25 or kd_comp[current_index] == 50 or kd_comp[current_index] == 75):
					# skip this resident as they have respective compensation
					current_index += 1
				elif kd_bonus[current_index] != 0:
					# skip this resident as they have a bonus for this time
					# decrement their bonus count 
					kd_bonus[current_index] -= 1
					current_index += 1
				else:
					# assign this resident to the kitchen detail
					kd_assignments[ii][jj] = residents_df.iloc[current_index]['Name']
					current_index += 1
					break

# print the kitchen detail assignments
for i in range(num_kitchen_details):
	print(f"Kitchen Detail {i+1}: {', '.join(kd_assignments[i])}")




# # slice the data frame from each column
# resident_names = residents_df['Name'].tolist()
# resident_seniority = residents_df['Seniority'].tolist()
# resident_Hallway = residents_df['Hallway'].tolist()
# resident_Kitchen_comp = residents_df['Kitchen comp'].tolist()
# resident_Kitchen_bonus = residents_df['Kitchen bonus'].tolist()
# resident_bathroom_comp = residents_df['bathroom comp '].tolist()
# resident_bathroom_bonus = residents_df['bathroom bonus'].tolist()
# resident_common_comp = residents_df['common comp'].tolist()
# resident_common_bonus = residents_df['common bonus'].tolist()
# 
# # print a few number of residents to verify
# for i in range(5):
# 	print(f"Resident: {resident_names[i]}, Seniority: {resident_seniority[i]}, Hallway: {resident_Hallway[i]}, Kitchen Comp: {resident_Kitchen_comp[i]}, Kitchen Bonus: {resident_Kitchen_bonus[i]}, Bathroom Comp: {resident_bathroom_comp[i]}, Bathroom Bonus: {resident_bathroom_bonus[i]}, Common Comp: {resident_common_comp[i]}, Common Bonus: {resident_common_bonus[i]}")