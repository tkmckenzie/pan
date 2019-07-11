import csv
import os
import pandas as pd
import subprocess

def query(question_str, expected_responses, expected_type):
	expected_responses_str = [str(e) for e in expected_responses]
	valid_response = False
	while not valid_response:
		response = input(question_str + ' (' + ', '.join(expected_responses_str) + ') ')
		valid_response = response in expected_responses_str
	return expected_type(response)

# Load existing supplemented data, if it exists
if 'supplemented_aac_data.csv' in os.listdir('report_data'):
	supplemented_data_file = open('report_data/supplemented_aac_data.csv', 'r')
	supplemented_data_csv = csv.reader(supplemented_data_file)
	supplemented_data = pd.DataFrame([line for line in supplemented_data_csv])
	supplemented_data.columns = supplemented_data.iloc[0,:]
	supplemented_data = supplemented_data.iloc[1:,:]
	supplemented_data_file.close()
	
	existing_entry_nums = supplemented_data['entry.num'].values
else:
	# Create file with appropriate columns
	supplemented_data_file = open('report_data/supplemented_aac_data.csv', 'w')
	supplemented_data_csv = csv.writer(supplemented_data_file, lineterminator = '\n')
	
	base_cols = ['entry.num', 'year', 'entry.title', 'entry.url', 'entry.text']
	description_cols = ['category', 'MP.url', 'date']
	accident_cols = ['lead.experience', 'belay.experience', 'lead.error', 'belay.error', 'inadequate.equipment', 'equipment.failure', 'fixed.hardware.failure', 'helmet', 'injury.severity']
	
	supplemented_data_csv.writerow(base_cols + description_cols + accident_cols)
	supplemented_data_file.close()
	
	existing_entry_nums = []

# Load raw report data
raw_data_file = open('report_data/raw_aac_data.csv', 'r')
raw_data_csv = csv.reader(raw_data_file)

raw_data = pd.DataFrame([line for line in raw_data_csv])
raw_data.columns = raw_data.iloc[0,:]
raw_data = raw_data.iloc[1:,:]
raw_data_file.close()

raw_data = raw_data.sort_values('entry.num', ascending = False)

# Subset raw data to include only entries not previously supplemented
raw_data = raw_data[[not entry_num in existing_entry_nums for entry_num in raw_data['entry.num']]]

# Open up supplemented data file to write
supplemented_data_file = open('report_data/supplemented_aac_data.csv', 'a')
supplemented_data_csv = csv.writer(supplemented_data_file, lineterminator = '\n')

# Cycle through reports and make queries from user
for index, row in raw_data.iterrows():
	print(row['entry.title'])
	print(row['entry.text'])
	
	print('\n' * 5 + 'Questions:\n')
	summary_response = query('Is this a summary article?', ['y', 'n'], str)
	if summary_response == 'n':
		category_response = query('Was this bouldering, climbing, rappelling, mountaineering, or ice climbing?', ['b', 'c', 'r', 'm', 'i'], str)
		MP_url_response = input('Mountain Project URL: ')
		date_response = input('Date of accident: ')
		lead_experience_response = query('Leader experience level:', [-1, 0, 1], int)
		belay_experience_response = query('Belayer experience level:', [-1, 0, 1], int)
		lead_error_response = query('Was this a leader error?', ['y', 'n'], str)
		belay_error_response = query('Was this a belayer error?', ['y', 'n'], str)
		inadequate_equipment_response = query('Was equipment inadequate?', ['y', 'n'], str)
		equipment_failure_response = query('Did equipment fail?', ['y', 'n'], str)
		fixed_hardware_failure_response = query('Did fixed hardware fail?', ['y', 'n'], str)
		helmet_response = query('Was the leader wearing a helmet?', ['y', 'n', 'u'], str)
		injury_severity_response = query('What was the injury severity (minor, major, death)?', ['m', 'M', 'd', 'u'], str)
		
		category = {'b': 'Bouldering', 'c': 'Climbing', 'r': 'Rappelling', 'm': 'Mountaineering', 'i': 'Ice Climbing'}[category_response]
		MP_url = MP_url_response
		date = date_response
		lead_experience = lead_experience_response
		belay_experience = belay_experience_response
		lead_error = {'y': 1, 'n': 0}[lead_error_response]
		belay_error = {'y': 1, 'n': 0}[belay_error_response]
		inadequate_equipment = {'y': 1, 'n': 0}[inadequate_equipment_response]
		equipment_failure = {'y': 1, 'n': 0}[equipment_failure_response]
		fixed_hardware_failure = {'y': 1, 'n': 0}[fixed_hardware_failure_response]
		helmet = {'y':1, 'n':0, 'u': 'NA'}[helmet_response]
		injury_severity = injury_severity_response
		
		supplemented_data_csv.writerow([row['entry.num'], row['year'], row['entry.title'], row['entry.url'], row['entry.text'],
									 category, MP_url, lead_experience, belay_experience, lead_error, belay_error, inadequate_equipment, equipment_failure, fixed_hardware_failure, helmet, injury_severity])
		
		print('\n' * 5)
		if query('Continue?', ['y', 'n'], str) == 'n':
			break
	else:
		supplemented_data_csv.writerow([row['entry.num']] + [''] * 15)
	
	print('\n' * 100)

supplemented_data_file.close()
