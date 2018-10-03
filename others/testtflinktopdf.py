#import pdfkit
#weblink=input("link= ")
#pdfkit.from_url(weblink, 'out.pdf')

import pdfkit
path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
pdfkit.from_url("http://chemcal.chemistry.unimelb.edu.au/en/subjects/chem10003/online-prelabs/experiment-6-analysis-of-a-polyiodide-salt/#preface", "out.pdf", configuration=config)
