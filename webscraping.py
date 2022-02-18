
# --------------------------
#      Web Scraping
# --------------------------

##  title, link scraping, Weather data scraping and store to database/datarame for farther process

from webscrap import wlog
from webscrap import wscrap

# Define log file location
wlog.set_custom_log_info('html/error.log')
url ="https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"

# news_scrap = wscrap.NewsScraper(wscrap.url_aj, wlog)
news_scrap = wscrap.NewsScraper(url, wlog)

#--------retrive the html from source link. once data is saved into our file then no need to run this script again and again
# news_scrap.retrieve_webpage()

#--- Save retrived data into a file. once data is saved into our file then no need to run this script again and again
news_scrap.write_webpage_as_html()

#-------- Parse  data from htmml to soup data
news_scrap.read_webpage_from_html_and_parse_to_bs4()

#-------From soup data get 7 days data to dataframe and save to database
news_scrap.parse_soup_data_store_in_dataframe()

#-------From soup data get all links and show as a list in simple wab page
news_scrap.parse_soup_to_simple_html()
