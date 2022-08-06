import csv
import pandas as pd
df = pd.read_csv('mushrooms.csv')
inputToVector = ['bcxfks',
                 'fgys',
                 'nbcgrpuewy',
                 'tf',
                 'alcyfmnps',
                 'adfn',
                 'cwd',
                 'bn',
                 'knbhg',
                 'ropuewy',
                 'et',
                 'bcuezr?',
                 'fyks',
                 'fyks',
                 'nbcgopewy',
                 'pu',
                 'nowy',
                 'not',
                 'ceflnpsz',
                 'knbhrouwy',
                 'acnsvy',
                 'glmpuwd']
convertString = df.columns;
vectoredInput = []
for i in df.index:
    newVector = []
    for v in range(len(convertString)):
        print(v)
        newVector.append(df[convertString[v]][i]);
    vectoredInput.append(newVector)
print(vectoredInput)

