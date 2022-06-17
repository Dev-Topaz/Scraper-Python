from os import write
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv

baseURL = "https://www.carepark.com.au/find-a-care-park/"
opts = Options()
opts.add_argument('headless')
opts.add_argument('log-level=2')
driver = webdriver.Chrome(options=opts)
driver.get(baseURL)
driver.implicitly_wait(30)

park_list = driver.find_elements(by=By.CLASS_NAME, value="find_care_park_listing_item-title")
park_urls = []
for park_item in park_list:
    item_title = park_item.get_attribute('innerHTML')
    title_string_list = item_title.replace(',', '').split(' ')
    new_title = '-'.join(title_string_list)
    new_url = baseURL + new_title
    new_url.lower()
    if new_url == 'https://www.carepark.com.au/find-a-care-park/149-Brebner-Drive-West-Lakes':
        new_url = 'https://www.carepark.com.au/find-a-care-park/the-balconies'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/SkyCity-Casino-Adelaide---The-Terrace':
        new_url = 'https://www.carepark.com.au/find-a-care-park/the-terrace'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Corporate-Centre-1-Car-Park':
        new_url = 'https://www.carepark.com.au/find-a-care-park/corporate-centre-1'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Piazza-on-the-Boulevard':
        new_url = 'https://www.carepark.com.au/find-a-care-park/5-view-avenue-surfers-paradise'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Acuity-Business-Park':
        new_url = 'https://www.carepark.com.au/find-a-care-park/acuitybusinesspark'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Queen-Victoria-Market---Munro-Street':
        new_url = 'https://www.carepark.com.au/find-a-care-park/queen-victoria-market-munro'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Siddeley-Street-Car-Park':
        new_url = 'https://www.carepark.com.au/find-a-care-park/671-701-flinders-st-docklands/'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Heidelberg-Repatriation-Hospital-(Austin-Health)':
        new_url = 'https://www.carepark.com.au/find-a-care-park/heidelberg-repatriation-hospital'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Spring-Street/Flinders-Street-Melbourne':
        new_url = 'https://www.carepark.com.au/find-a-care-park/spring-street-flinders-street-melbourne'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Melbourne-Sports-and-Aquatic-Centre-(MSAC)':
        new_url = 'https://www.carepark.com.au/find-a-care-park/melbourne-sports-aquatic-centre-msac'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Royal-Talbot-Rehabilitation-Centre-(Austin-Health)':
        new_url = 'https://www.carepark.com.au/find-a-care-park/royal-talbot-rehabilitation-centre'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Coles-Kew':
        new_url = 'https://www.carepark.com.au/find-a-care-park/coles_kew'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Toorak-Place-Toorak':
        new_url = 'https://www.carepark.com.au/find-a-care-park/toorak-place-jackson-street'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/793-Burke-Road-Camberwell':
        new_url = 'https://www.carepark.com.au/find-a-care-park/13-14-burke-avenue-hawthorn-east'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/1010-Whitehorse-Road-Box-Hill':
        new_url = 'https://www.carepark.com.au/find-a-care-park/1010-whitehorse-road'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Holmesglen-Institute---Moorabbin':
        new_url = 'https://www.carepark.com.au/find-a-care-park/488-south-road-moorabbin'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Holmesglen-Institute-Glen-Waverley':
        new_url = 'https://www.carepark.com.au/find-a-care-park/595-waverley-road-glen-waverley'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/1-Station-Street-Wickham':
        new_url = 'https://www.carepark.com.au/find-a-care-park/1_station_street_wickham'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Hub-Arcade-Dandenong':
        new_url = 'https://www.carepark.com.au/find-a-care-park/15-23-langhorne-street-dandenong'
    if new_url == 'https://www.carepark.com.au/find-a-care-park/Woolworths-Wonthaggi':
        new_url = 'https://www.carepark.com.au/find-a-care-park/wonthaggi'
    
    park_urls.append(new_url)

output_data = []
for index, park_url in enumerate(park_urls):
    driver.get(park_url)
    
    try:
        times_open = driver.find_element(by=By.CLASS_NAME, value='carepark_opening_times-times').find_element(by=By.TAG_NAME, value='span').get_attribute('innerHTML')
        if times_open == '24 Hours':
            output_data.append([index + 1, '24 Hours', '24 Hours', 1])
            output_data.append([index + 1, '24 Hours', '24 Hours', 2])
            output_data.append([index + 1, '24 Hours', '24 Hours', 3])
            output_data.append([index + 1, '24 Hours', '24 Hours', 4])
            output_data.append([index + 1, '24 Hours', '24 Hours', 5])
            output_data.append([index + 1, '24 Hours', '24 Hours', 6])
            output_data.append([index + 1, '24 Hours', '24 Hours', 7])
        else:
            times_array = driver.find_elements(by=By.CLASS_NAME, value='carepark_opening_times-times')
            for idx, time_item in enumerate(times_array):
                time = time_item.find_element(by=By.TAG_NAME, value='span').get_attribute('innerHTML')
                output_data.append([index + 1, time, time, idx + 1])
    except EC.NoSuchElementException:
        print(park_url)
        output_data.append([index + 1, '', '', 1])
        output_data.append([index + 1, '', '', 2])
        output_data.append([index + 1, '', '', 3])
        output_data.append([index + 1, '', '', 4])
        output_data.append([index + 1, '', '', 5])
        output_data.append([index + 1, '', '', 6])
        output_data.append([index + 1, '', '', 7])

with open('output.csv', 'w') as data_file:
    writer = csv.writer(data_file)
    writer.writerows(output_data)

driver.quit()
