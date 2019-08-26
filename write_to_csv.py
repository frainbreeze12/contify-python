import csv
import os

def write_to_csv(links, title):
    with open('resources/summary.csv', 'a', newline='') as summaryCSV:
        filewriter = csv.writer(summaryCSV, delimiter=';', quotechar='|', lineterminator=os.linesep)

        filewriter.writerow(links)
        filewriter.writerow(title)