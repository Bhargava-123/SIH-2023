import csv
import demo

filename = "data.csv"

herbs_name_dict = demo.get_herbs_name_dict()
fields = ["Name","Rasa",'Guna',"Virya","Vipaka","Karma"]

with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for ele in herbs_name_dict.values():
        csvwriter.writerow([ele])