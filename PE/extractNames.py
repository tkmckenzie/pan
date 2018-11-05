import csv

f = open('names.txt', 'r')
s = f.read().strip()
f.close()

s = s.replace('"', '')
names = s.split(',')

out = open('names.csv', 'w')
out_CSV = csv.writer(out, lineterminator = '\n')

for name in names:
    out_CSV.writerow([name])

out.close()
