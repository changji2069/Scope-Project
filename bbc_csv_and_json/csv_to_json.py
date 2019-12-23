import json
import csv
import pandas as pd



def csv_to_json_trial(csv_path,json_path):
	data = {}
	with open(csv_path) as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for rows in csv_reader:
			label = rows['label']
			data[label] = rows

	with open(json_path, 'w') as json_file:
		json_file.write(json.dumps(data,indent = 4))

	return data

def csv_to_json(csv_path,json_path):
	data_df = pd.read_csv(csv_path, usecols = ['label', 'data'], encoding = 'ISO-8859-1')
	#use orient = 'records' to get each data point and its label paired
	export = data_df.to_json(json_path, orient = 'records')

	return data_df



if __name__ == '__main__':
	csv_path = 'bbc_dataset.csv'
	json_path = 'bbc_dataset.json'
	#data = csv_to_json(csv_path,json_path)
	#print(data)
	data_df = csv_to_json(csv_path,json_path)
	#print(data_df)
