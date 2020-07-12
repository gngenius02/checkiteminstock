
# coded by gnenius02
# https://github.com/gngenius02/checkiteminstock/master

import requests, yagmail
from bs4 import BeautifulSoup

# Pulls in the credentials from the creds.txt
creds = [line.rstrip('\n') for line in open('creds.txt')]

# pulls in the urls to be be checked.
urls = [line.rstrip('\n') for line in open('urls.txt')]

#function to send emails whenever necessary.
def sendemail(message):
    receiver = "%s" % (creds[0])
    body = "%s" % (message)

    yag = yagmail.SMTP(creds[0], creds[1])
    yag.send(
        to=receiver,
        subject="HEY, an item you requested is back in stock!!!!",
        contents="HEY, an item you requested is back in stock!!!!\n\nCheck out the item at the link below:\n\n\t%s" % (body),
    )

#main routine.
for url in urls:
    action = 'checking url %s' % (url)
    print(action)
    data = requests.get(url, headers = {'User-agent': 'Mozilla Firefox 5.0'})
    soup = BeautifulSoup(data.text,'html.parser')
    for form in soup.find_all('form', {'class':'variations_form cart'}):
        for attrib in form.get_attribute_list('data-product_variations'):
            insidesoup = BeautifulSoup(attrib, 'html.parser')
            for p in insidesoup.find_all('p'):
                if p.text.startswith("In"):
                    print('in stock sending email')
                    sendemail(url)
                else:
                    print('not in stock moving on')
