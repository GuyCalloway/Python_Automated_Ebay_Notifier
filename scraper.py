import requests
import re
from bs4 import BeautifulSoup
import smtplib
import time


headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

URL = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR11.TRC1.A0.H0.Xcambridge+audio+a5.TRS0&_nkw=cambridge+audio+a5&_sacat=0"

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

arr = list(range(11))[1:11]

url_array = []

for val in arr:
    item = soup.find(id="srp-river-results-listing"+str(val))
    x = item.a
    url_array.append(x.get('href'))


def send_mail(url, hours_left, feedback):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('g.fr.calloway@gmail.com', 'xqbrawjwklpcbzfh')
    subject = f'This has {hours_left} hours left'
    body = f'check link: {url}!\nfeedback: {feedback}'
    msg = f"{subject}\n\n{body}"

    server.sendmail(
        "g.fr.calloway@gmail.com",
        "g.fr.calloway@gmail.com",
        msg
    )
    print("email sent")
    server.quit()


headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}


def check_URLS(urls, hour_alert, max_price, send_mail):
    for url in urls:
        print(url)
        page1 = requests.get(url, headers=headers)
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        price = soup1.find(id="prcIsum_bidPrice")
        if price:
            price_text = price.get_text()
            time_left = soup1.find(id="vi-cdown_timeLeft").get_text().strip()
            title = soup1.find(id="itemTitle").get_text()
            feedback = soup1.find(id="si-fb").get_text()

        if time_left.find('day') == -1:
            hour_index = time_left.find('h')
            if hour_index < 3:
                hours_left = int(time_left[0:hour_index])
                if hours_left <= hour_alert and int(price_text[-5:-3]) < max_price:
                    send_mail(url, hours_left)


while(True):
    check_URLS(url_array, 4, 50, send_mail)
    time.sleep(3600)
