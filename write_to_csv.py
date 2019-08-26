import csv
import os

def write_to_csv(content):
    with open('resources/summary.csv', 'a', newline='') as summaryCSV:
        filewriter = csv.writer(summaryCSV, delimiter=';', quotechar='|', lineterminator=os.linesep)    

        for row in content:
                filewriter.writerow(row)  