from PyPDF2 import PdfReader
import re
# creating a pdf reader object
def get_herbs_name_dict():
    reader = PdfReader('PDFMINEDEMO.pdf')
    
    # print(len(reader.pages))
    herbs_name_dict = dict()
    count  = 1

    for i in range(len(reader.pages)):
        # print(count)
        count += 1

        page = reader.pages[i]
        listy = page.extract_text().split("\n")
        num = listy[0].split()
        Rasa = ""
        Guna = ""
        Vipaka = ""
        Virya = ""
        temp_num = ""

        print(listy[0])
        
        
        # print(listy[0])
        # if(num[0][0].isdigit()):
        #     herb_name = ""
        #     for ele in num[1:] :  herb_name += ele
        #     herbs_name_dict[num[0][:-1]] = {"Name" : herb_name}
        # for line in listy:
        #     if "Rasa" in line:
        #         x = re.split(':',line)
        #         rasa_list = [ele.strip() for ele in x]
        #         for ele in rasa_list:
        #             Rasa += ele + ","
        #         # print("Rasa->",Rasa)
        #     if "Guna" in line:
        #         x = re.split(':',line)
        #         guna_list = [ele.strip() for ele in x]
        #         for ele in guna_list:
        #             Guna += ele + ","
        #         # print("Guna->",Guna)
        #     if "Virya" in line:
        #         x = re.split(':',line)
        #         virya_list = [ele.strip() for ele in x]
        #         for ele in virya_list:
        #             Virya += ele + ","
        #         # print("Virya->",Virya)
        #     if "Vipaka" in line:
        #         x = re.split(':',line)
        #         vipaka_list = [ele.strip() for ele in x]
        #         for ele in vipaka_list:
        #             Vipaka += ele + ","
        #         # print("Vipaka->",Vipaka)

    print(herbs_name_dict)
    return herbs_name_dict
get_herbs_name_dict()