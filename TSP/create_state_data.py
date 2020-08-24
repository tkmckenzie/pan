import csv
import geopy.distance
import pandas as pd

f = open('state_centroids.csv', 'r')
f_csv = csv.reader(f)
data = [row for row in f_csv]
f.close()

df = pd.DataFrame(data[1:], columns = data[0])

df = df.loc[-df['name'].isin(['Alaska', 'Hawaii'])]
state_names = df['name']

coord_dict = {row[1]['name']: (float(row[1]['latitude']), float(row[1]['longitude'])) for row in df.iterrows()}
distance_dict = {name_1: {name_2: geopy.distance.distance(coord_dict[name_1], coord_dict[name_2]).miles for name_2 in state_names} for name_1 in state_names}

out_file = open('state_distances.csv', 'w')
out_csv = csv.writer(out_file, lineterminator = '\n')

out_csv.writerow([''] + list(state_names))
for state in state_names:
	row = [state] + [distance_dict[state][other_state] for other_state in state_names]
	out_csv.writerow(row)
out_file.close()
