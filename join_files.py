import csv
import pandas
import argparse

parser = argparse.ArgumentParser(description='This script joins files.')
parser.add_argument('--output', default='rides.csv', help="Output file.")
parser.add_argument('--input', default='uber.com_sitejabber.csv,lyft.com_sitejabber.csv', help="Input files.")
args = parser.parse_args()

values = []
output = args.output
if ',' in args.input:
	files = args.input.split(',')
else:
	files = [args.input]
for file in files:
	reader = csv.DictReader(open(file, 'r'))
	for row in reader:
		value = {}
		content = row['content'].replace('\n',' ')
		content = content.replace('  ',' ')
		value['content'] = content
		value['rating'] = row['rating']
		if 'source' in row:
			value['source'] = row['source']
		else:
			value['source'] = file.split('_')[0]
		values.append(value)
df = pandas.DataFrame(values)
df.to_csv(output)