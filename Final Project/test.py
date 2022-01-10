from tempfile import NamedTemporaryFile
import shutil
import csv

filename = 'submission.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False)

fields = ['image', 'ALB', 'BET', 'DOL', 'LAG', 'NoF', 'OTHER', 'SHARK', 'YFT']

with open(filename, 'r') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        # if row['ID'] == str(stud_ID):
        #     print('updating row', row['ID'])
        #     row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
        if row[fields[0]]=='image':
            writer.writerow(row)
            continue
        row = {fields[0]: row[fields[0]].replace("image", "test_stg2/image"),
               fields[1]: row[fields[1]],
               fields[2]: row[fields[2]],
               fields[3]: row[fields[3]],
               fields[4]: row[fields[4]],
               fields[5]: row[fields[5]],
               fields[6]: row[fields[6]],
               fields[7]: row[fields[7]],
               fields[8]: row[fields[8]]}
        writer.writerow(row)

shutil.move(tempfile.name, 'newsubmission.csv')
# import csv

with open('newsubmission.csv') as input, open('newsubmission1.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
