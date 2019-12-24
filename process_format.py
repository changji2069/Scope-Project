import os
import pandas as pd

training_path = 'dataset/training_set/'

for csv_file in os.listdir('processed_dataset/train'):

    df = pd.read_csv('processed_dataset/train/' + csv_file, encoding = 'ISO-8859-1')

    for i in range(len(df['news'])):
        if os.path.exists(training_path + df['type'][i]) == False:
            os.mkdir(training_path + df['type'][i])
        k = 0
        while os.path.exists(training_path + df['type'][i] + '/' + str(k)) == True:
            k += 1
        # Saving the text file
        f = open(training_path + df['type'][i] + '/' + str(k), "w+")
        f.write(df['news'][i])
        f.close()