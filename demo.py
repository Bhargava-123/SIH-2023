from PyPDF2 import PdfReader
import re
# creating a pdf reader object
def get_herbs_name_dict():
    reader = PdfReader('PDFMINEDEMO.pdf')
    
    # print(len(reader.pages))
    herbs_name_dict = dict()

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        listy = page.extract_text().split("\n")
        num = listy[0].split()
        # print(num)
        try:
            if(num[0][0].isdigit()):
                herb_name = ""
                for ele in num[1:] :  herb_name += ele
                herbs_name_dict[num[0][:-1]] = {"Name" : herb_name}

                # for line in listy:
                #     # if "Rasa" in line or "Guna" in line or"Virya" in line or "Vipaka" in line or "Karma" in line:'
                #     if "Rasa" in line:
                #         print(line)
                #         x = re.split(":",line)
                #         rasa_list = [ele.strip() for ele in x]
                #         herbs_name_dict[num[0][:-1]]["Rasa"] = ele[1]
                        
                # herbs_name_dict[num[0][:-1]] = {"Name" : herb_name,}
        except:
            pass
        for line in listy:
                    # if "Rasa" in line or "Guna" in line or"Virya" in line or "Vipaka" in line or "Karma" in line:'
            if "Rasa" in line:
                print(line)
                x = re.split(":",line)
                rasa_list = [ele.strip() for ele in x]
                herbs_name_dict[num[0][:-1]]["Rasa"] = ele[1]
        # for line in listy:
        #     if "Rasa" in line or "Guna" in line or"Virya" in line or "Vipaka" in line or "Karma" in line:
        #         print(line)

    print(herbs_name_dict)
    return herbs_name_dict
get_herbs_name_dict()