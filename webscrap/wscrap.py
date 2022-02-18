# --------------------------
#      Web Scraping
# --------------------------

'''
urllib
BeautifulSoup
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Installing Beautiful Soup
pip install beautifulsoup4
'''

import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# url_aj ="https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
filepath = 'html/aj.html'


class NewsScraper:
    __url = ''
    __data = ''
    __wlog = None
    __soup = None

    def __init__(self, url, wlog):
        self.__url = url
        self.__wlog = wlog

    def retrieve_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print("Retrieved successfully")

    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath, 'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    def read_webpage_from_html_and_parse_to_bs4(self, filepath=filepath):
        try:
            with open(filepath) as fobj:
                self.__data = fobj.read()
                self.__soup = BeautifulSoup(self.__data, "html.parser")
                # print('\n\n __soup Preetify:....... ')
                # print(self.__soup.prettify())

        except Exception as e:
            print(e)
            self.__wlog.report(str(e))


    def parse_soup_data_store_in_dataframe(self):
        seven_day = self.__soup.find(id="seven-day-forecast")

        """ test one data
        forecast_items = seven_day.find_all(class_="tombstone-container")
        tonight = forecast_items[0]
        period = tonight.find(class_="period-name").get_text()
        short_desc = tonight.find(class_="short-desc").get_text()
        temp = tonight.find(class_="temp").get_text()
        img = tonight.find("img")
        desc = img['title']
        # print(desc) print(period) print(short_desc)  print(temp)  """

        period_tags = seven_day.select(".tombstone-container .period-name")
        short_descss_tags = seven_day.select(".tombstone-container .short-desc")
        temps_tag = seven_day.select(".tombstone-container .temp")
        descss_tag = seven_day.select(".tombstone-container img")

        periods = [pt.get_text() for pt in period_tags]
        short_descss = [sd.get_text() for sd in short_descss_tags]
        temps = [t.get_text() for t in temps_tag]
        descss = [d["title"] for d in descss_tag]

       # print(periods)  print(short_descss) print(temps) print(descss)

        weather = pd.DataFrame({
            "period": periods,
            "short_desc": short_descss,
            "temp": temps,
            "desc": descss
        })
        #print(weather)
        # farther work  here is to save the data to database


    def parse_soup_to_simple_html(self):
        ankor_list = self.__soup.find_all(['a'])
        # print(ankor_list)

        htmltext = '''
            <html>
                <head><title>Simple News Link Scrapper</title></head>
                <body>
                    {NEWS_LINKS}
                </body>
            </html>
            '''

        news_links = '<ol>'

        for tag in ankor_list:
            if tag.get('href'):
                # print (self.__url + tag.parent.get('href'), tag.string)
                # link = self.__url + tag.get('href')
                link = tag.get('href')
                title = tag.string
                news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n".format(link, title)

        news_links += '</ol>'
        htmltext = htmltext.format(NEWS_LINKS=news_links)
        self.write_webpage_as_html(filepath="html/simplenews.html", data=htmltext.encode())

    # def print_beautiful_soup(self):
    #     # print (self.__soup.title.string)
    #     news_list = self.__soup.find_all(['h1', 'h2', 'h4'])  # h1
    #
    #     # print (news_list)
    #     for tag in news_list:
    #         if tag.parent.get('href'):
    #             print(self.__url + tag.parent.get('href'), tag.string)


    #----- Used to cange url ----
    # def change_url(self, url):
    #     self.__url = url
