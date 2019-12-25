import os
import pandas as pd
import time
import io

time0 = time.clock()
training_path = 'dataset/training_set/stemmed/'

k = 0
for csv_file in os.listdir('processed_dataset/no_short'):

    df = pd.read_csv('processed_dataset/no_short/' + csv_file, encoding = 'ISO-8859-1')

    for i in range(len(df['news'])):
        if os.path.exists(training_path + df['type'][i]) == False:
            os.mkdir(training_path + df['type'][i])

        with io.open(training_path + df['type'][i] + '/' + str(k), "w+", encoding='utf-8') as f:
            f.write(df['news'][i])
        print(csv_file + ' ' + str(i))
        k += 1
        
print('time taken = ' + str(time.clock() - time0))
