from PyPDF2 import PdfReader
  
# creating a pdf reader object
reader = PdfReader('PDFMINEDEMO.pdf')
  
# printing number of pages in pdf file
print(len(reader.pages))
herbs_name = dict()
for i in range(len(reader.pages)):
    
    page = reader.pages[i]
    # print(page.extract_text())
    # if "Rasa" in page.extract_text():
    listy = page.extract_text().split("\n")
    num = listy[0].split()
    try:
        if(num[0][0].isdigit()):
            herbs_name[num[0][:-1]] = num[1] + num[2]
    except:
        pass

    # print("heading-->",num)
    # for line in listy:
    #     if "Rasa" in line or "Guna" in line or"Virya" in line or "Vipaka" in line or "Karma" in line:
    #         print(line)
    print()
    print("###################################################")
    print()
print(herbs_name)