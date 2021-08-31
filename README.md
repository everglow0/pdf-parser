# pdf解析器
原作者github：https://github.com/titipata/scipdf_parser  

**声明**
* 只做个人学习，并无商用，特别感谢作者的的代码
* 本项目基于：[GROBID](https://github.com/kermitt2/grobid)

## 配置环境

* 首先git clone本项目  
* 使用pip安装 `requirements.txt` 中的包  
* 下载模型文件：`en_core_web_sm-2.2.5.tar.gz` ，并使用pip安装  
* 执行命令： `bash serve_grobid.sh` （默认端口：8070）

## 用法示例

```python
import scipdf
article_dict = scipdf.parse_pdf_to_dict('example_data/futoma2017improved.pdf') # return dictionary
 
# option to parse directly from URL to PDF, if as_list is set to True, output 'text' of parsed section will be in a list of paragraphs instead
article_dict = scipdf.parse_pdf_to_dict('https://www.biorxiv.org/content/biorxiv/early/2018/11/20/463760.full.pdf', as_list=False)

# output example
>> {
    'title': 'Proceedings of Machine Learning for Healthcare',
    'abstract': '...',
    'sections': [
        {'heading': '...', 'text': '...'},
        {'heading': '...', 'text': '...'},
        ...
    ],
    'references': [
        {'title': '...', 'year': '...', 'journal': '...', 'author': '...'},
        ...
    ],
    'figures': [
        {'figure_label': '...', 'figure_type': '...', 'figure_id': '...', 'figure_caption': '...', 'figure_data': '...'},
        ...
    ],
    'doi': '...'
}

xml = scipdf.parse_pdf('example_data/futoma2017improved.pdf', soup=True) # option to parse full XML from GROBID
```

To parse figures from PDF using [pdffigures2](https://github.com/allenai/pdffigures2), you can run

```python
scipdf.parse_figures('example_data', output_folder='figures') # folder should contain only PDF files
```

You can see example output figures in `figures` folder.

