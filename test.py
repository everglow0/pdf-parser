
 
import json
import scipdf
import os
from tqdm import tqdm
import re

'''
for root, dirs, files in os.walk("/home/guoht/scipdf_parser/pdf-new/Mathematical Geosciences"):
    for file in tqdm(files):
        date = re.findall(r"\d{4}",root)
        if date:
            name, ext = os.path.splitext(file)
            if ext == '.pdf':
                if re.findall(r"\d{4}",name):
                    continue
                else:
                    # os.path.join(root, file)
                    os.rename(os.path.join(root, file), os.path.join(root, name + '_' + date[-1] + ext))
                    # print(os.path.join(root,file))
'''    
# article_dict = scipdf.parse_pdf_to_dict("/home/guoht/scipdf_parser/pdf-new/Mathematical Geosciences/Volume1/March 1969/Autoassociation, a new geological tool_1969.pdf") # return dictionary

# print(article_dict)
              
for root, dirs, files in os.walk("/home/guoht/scipdf_parser/OGR"):
    for file in tqdm(files):
        name, ext = os.path.splitext(file)
        if ext == '.pdf':
            if os.path.isdir(os.path.join(root, name) + ".json"):
                continue
            if os.path.join(root, file) is None:
                continue
            try:
                article_dict = scipdf.parse_pdf_to_dict(os.path.join(root, file)) # return dictionary
                # article_dict = scipdf.parse_pdf_to_dict("/home/guoht/scipdf_parser/pdf-new/Mathematical Geosciences/Volume1/March 1969/Autoassociation, a new geological tool_1969.pdf") # return dictionary

                # print(article_dict)

                with open(os.path.join("/home/guoht/scipdf_parser/OGR_res", name) + ".json",'w') as f:
                    json.dump(article_dict,f)
            except Exception as e:
                print(e)



'''
article_dict = scipdf.parse_pdf_to_dict("/home/guoht/scipdf_parser/testpdf-50/高被引斑岩铜矿论文/Apatite Trace Element Compositions.pdf") # return dictionary
# print(article_dict)

with open("/home/guoht/scipdf_parser/testpdf-50/高被引斑岩铜矿论文/Apatite Trace Element Compositions" + ".json",'w') as f:
    json.dump(article_dict,f)
'''

