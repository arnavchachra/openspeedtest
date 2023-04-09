# Import necessary modules
import datetime
import time
import re
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


# Configure Chrome browser and initialize a WebDriver instance
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Navigate to the OpenSpeedTest website
driver.get('https://openspeedtest.com?R')

# Wait for 60 seconds for the speed test to complete
print("Waiting for 60 seconds for the Speed Test to complete...")
time.sleep(60)

# Extract download, upload, and ping speeds from the page
download_speed_str = driver.find_element(By.ID, 'downResultC1').text
download_speed = download_speed_str.replace("\n" , " ")

upload_speed_str = driver.find_element(By.ID, 'upResultC2').text
upload_speed = upload_speed_str.replace("\n" , " ")

ping_str = driver.find_element(By.ID, 'pingResultC3').text
ping_speed = ping_str.replace("\n" , " ")

# Create a directory and log file if they don't already exist
home_dir = os.environ.get('HOME')
log_file= f"{home_dir}/Documents/AA-Sync"
if not os.path.exists(log_file):
    os.makedirs(log_file)

# Write the speed test results to a log file
with open(f'{log_file}/speedtest.log', 'a') as f:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_line = f'{timestamp} OpenSpeedTest Result {download_speed:}  {upload_speed:}  {ping_speed:} \n'
    f.write(log_line)

# Quit the WebDriver instance
driver.quit()