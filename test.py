
 
import json
import scipdf
import os
from tqdm import tqdm



for root, dirs, files in os.walk("./testpdf-50/"):
    for file in tqdm(files):

        name, ext = file.split('.')
        if ext == 'pdf':

            article_dict = scipdf.parse_pdf_to_dict(os.path.join(root, file)) # return dictionary
            # article_dict = scipdf.parse_pdf_to_dict("/home/guoht/scipdf_parser/testpdf-50/高被引斑岩铜矿论文/Apatite Trace Element Compositions.pdf") # return dictionary

            # print(article_dict)

            with open(os.path.join(root, name) + ".json",'w') as f:
                json.dump(article_dict,f)


'''
article_dict = scipdf.parse_pdf_to_dict("/home/guoht/scipdf_parser/testpdf-50/高被引斑岩铜矿论文/Apatite Trace Element Compositions.pdf") # return dictionary
# print(article_dict)

with open("/home/guoht/scipdf_parser/testpdf-50/高被引斑岩铜矿论文/Apatite Trace Element Compositions" + ".json",'w') as f:
    json.dump(article_dict,f)
'''

