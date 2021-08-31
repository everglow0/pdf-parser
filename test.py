import scipdf
article_dict = scipdf.parse_pdf_to_dict('example_data/test.pdf') # return dictionary
#import en_core_web_sm
#nlp = en_core_web_sm.load()
print(article_dict)
print(type(article_dict))
import json
with open("result.json",'w') as f:
    json.dump(article_dict,f)
