import pdfkit
weblink=input("link= ")
pdfkit.from_url(weblink, 'out.pdf')
