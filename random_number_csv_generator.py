import pandas as pd
import random

# to generate specific amounts of random values at specific ranges
values = []
for i in range(0,30):
  values.append(random.uniform(0.7, 1))
for i in range(30,60):
  values.append(random.uniform(0.4, 0.7))
for i in range(60,100):
  values.append(random.uniform(0, 0.4))
for i in values:
  print(f"{i:.4f}")

# to create a comma-separated-values file with those numbers
data = {
  'Index': list(range(len(values))),
  'Value': values
}
#print(data)
df = pd.DataFrame(data)
csv_file_path = 'data.csv'
df.to_csv(csv_file_path, index=False)