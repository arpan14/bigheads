bigheads :scissors:
============
An efficient command line python library to scrape webpages and download the relevant pages as PDFs. It is optimised to be fast and is beneficial for people who do not have access to high-speed internet and require webpages for offline reading.

Download
--------

### pip install (recommended):
```sh
$ pip install bigheads
``` 
#### **Dependencies**
Note that ``bigheads`` depends on ``bs4``, ``httplib2``, ``wkhtmltopdf`` and ``pdfkit``. 

#### **Known Issues**
```sh
IOError: No wkhtmltopdf executable found: 
If this file exists please check that this process can read it. Otherwise please install wkhtmltopdf - https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
```
Visit the [URL](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf) to see the steps for your respective OS.

Usage
-----
```sh
$ bigheads URL [OPTIONS]
```

Options
-------
```sh
-t, --tags          	[TAG1, TAG2 ....]	Space delimited list of tags for which web articles will be scraped.
-d, --directoryPath 	DIR_PATH 			Path of the directory where PDF files are to be saved.
-l, --limit             LIMIT       		Limit on the number of articles to be scraped.
```

Examples
--------

Recursively scrape all URLs from the provided seed URL and save the PDFs to a default folder. 
```sh
$ bigheads  https://www.geeksforgeeks.org/tag/queue
```

Recursively scrape URLs from the provided seed URL ensuring that the articles match the provided tags.
```sh
$ bigheads https://www.geeksforgeeks.org/tag/queue --tags amazon microsoft
```

Recursively scrape URLs from the provided seed URL ensuring that the articles match the provided tags and store it on the provided path.
```sh
$ bigheads https://www.geeksforgeeks.org/tag/queue --tags amazon microsoft -d queue
```

Recursively scrape URLs from the provided seed URL ensuring that the articles match the provided tags and a provided limit is not breached.
The limit is for the number of articles whose PDFs is downloaded to the device.
```sh
$ bigheads https://www.geeksforgeeks.org/tag/queue --tags amazon microsoft -d queue -l 100
```

#### NOTE:
- By default, a new folder called "pdfs_<url>" will be created in the working directory, containing all the downloaded PDFs.
- We have a limit of 300 articles that can be scraped in one run. This limit can be increased by parallelising the scraping tasks.
- If some tags are provided, articles that match all the provided tags will be considered and scraped to form the downloaded PDFs.

Issues
------
- Lot of noise files may be downloaded because the mechanism to compute relevance by matching tags is a naive approach and not very consistent.
- For large number of recursive URLs, the current routine to convert into PDFs takes more time. There is scope to parallelise these tasks into different batches.

Contribute
----------
If you want to add features, improve them, or report issues, feel free to send a pull request or leave a comment.

### Contributors

- [arpan14](https://github.com/arpan14) ([Arpan Mishra](http://arpanmishra.com/))


Disclaimer
----------

bigheads is a tool to ease an user's convenience to go through webpages in the absence of internet. It should not be misused or used for purposes other than education/research. The user agrees to USE IT AT THEIR OWN RISK.


License
-------
![GPL V3](https://raw.githubusercontent.com/arpan14/bigheads/master/images/gpl.png)

FAQs
-------
### Why was it named 'bigheads'?

**Answer** - Well, I wrote this program in 2015. Distributed the initial version to PyPi in 2016. In 2020, when I was revisiting this code
I had no clue why I had named this package 'bigheads' because the name had no correlation with the work the code was doing. It took me about 30 minutes to recall that the name is based on the famous character 'Bighead' from the TV Series Silicon Valley.

![GPL V3](https://raw.githubusercontent.com/arpan14/bigheads/master/images/bighead_character.png)

I never thought I would reference a TV Series character in my work. But at that time I felt the influence of the TV Series was pretty high to inculcate a sense of love for Computer Science, Entrepreneurship and Comedy.

