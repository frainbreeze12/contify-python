import csv
import os

def write_to_csv(content, file):
    with open('resources/{}.csv'.format(file), 'a', newline='') as summaryCSV:
        filewriter = csv.writer(summaryCSV, delimiter=';', quotechar='|', lineterminator=os.linesep)    

        for row in content:
                filewriter.writerow(row)  