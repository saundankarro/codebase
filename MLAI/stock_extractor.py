from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import shutil
import os
import time

l= list()
obj={}

def expand_shadow_element(driver, element):
    return driver.execute_script('return arguments[0].shadowRoot', element)

download_path = "C:/Users/saund/Downloads"
dest = "C:/Users/saund/Rohit/Code/codebase/MLAI/nasdaq/data"

def get_stock_data(stock):

    nasdaq_url = 'https://www.nasdaq.com/market-activity/stocks/'
    target_url = nasdaq_url + stock + '/historical'

    wb_final = pd.ExcelWriter("price_data.xlsx",engine='xlsxwriter')


    print(f"Opening Chrome")
    # Connecting to the Web Page
    driver = wd.Chrome()
    print(f"Opening Nasdaq page - {target_url}")
    driver.get(target_url)
    driver.maximize_window()
    

    time.sleep(2)
    resp = driver.page_source.encode('utf-8').strip()
    soup = bs(resp,'html5lib')

    wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='onetrust-button-group']//button[@id='onetrust-accept-btn-handler']")))   
    cookies_button = driver.find_element(By.XPATH, "//div[@id='onetrust-button-group']//button[@id='onetrust-accept-btn-handler']")
    cookies_button.click()

    head_host = driver.find_element(By.TAG_NAME,"nsdq-quote-header")
    head_root = expand_shadow_element(driver, head_host)
    print(f"Shadow Root:- {head_root}")

    # Getting the Stock name from the webpage
    Stock =head_root.find_element(By.CSS_SELECTOR,'[class=nsdq-quote-header__asset-information-name]').text
    print(f"Stock Name- {Stock}")

    Stock_Abb = stock
    print(f"Stock Abbreviation - {Stock_Abb}")

    Price = head_root.find_element(By.CSS_SELECTOR,'[class=nsdq-quote-header__pricing-information-saleprice]').text
    print(f"Stock Price = {Price}")

    print(f"Switching to Max Tab")

    driver.find_element(By.CSS_SELECTOR, '[data-tab-id=y10]').click()

    print(f"Clicked on Max Tab")

    print(f"Finding the Download button")
    
    time.sleep(10)

    ########## Click "Download Data" button ##########  
    driver.find_element(By.CSS_SELECTOR, '[class=historical-download]').click()
    print(f"Clicked on download button")

    print(f"Waiting for file to download")

    time.sleep(20)
    
    driver.close()



    print(f"Moving files from {download_path} to {dest}")
    for file in os.listdir(download_path):
        if file.startswith("HistoricalData"):
            file_path = f"{download_path}/{file}"
            dest_path = f"{dest}/{stock}/{file}"
            print(f"File Path - {file_path}\nDest Path - {dest_path}")
            shutil.move(file_path, dest_path)
            print(f"Moved {file} to {dest}")



# writer = pd.ExcelWriter('default.xlsx') # Arbitrary output name
# for csvfilename in sys.argv[1:]:
#     df = pd.read_csv(csvfilename)
#     df.to_excel(writer,sheet_name=os.path.splitext(csvfilename)[0])
# writer.save()


def consolidate_data(stock):
    
    writer = pd.ExcelWriter("price_data.xlsx")

    file_path = f"{dest}/{stock}"

    print(f"Reading files inside {file_path} for consolidation")

    for file in os.listdir(file_path):
        print(f"Found file - {file}")
        if file.split('_')[0] == "HistoricalData":
            print(f"Reading file {file}")
            df = pd.read_csv(f"{file_path}/{file}", index_col = 'Date')
            print(f"Saving file information to excel")
            df.to_excel(writer, sheet_name=stock)
        else:
            continue
    writer.close()



    print(f"Finished consolidating the price data for {stock}")

if __name__ == "__main__":
    stock = input().upper()

    print(f"Starting to get the historical data for {stock}")
    get_stock_data(stock)
    print(f"Downloaded and moved historical data")
    print("-----------------------------------------------------------------------------------------------")
    print(f"Starting to consolidate all data for {stock} into one file")
    consolidate_data(stock)
    print(f"Consolidated all data for {stock}")