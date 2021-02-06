#!/usr/bin/python
import selenium
import sys
import datetime
import osascript
import os
import pickle
from os import path
from osascript import osascript
from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import options

#Loggar in på nordnet och laddar ner transaktionsrapport
os.chdir("/Users/albinjonfelt/Documents/programmering/aktier/python/")
all_list = list(dict())
folder_path = '/Users/albinjonfelt/Documents/programmering/aktier/bin/'
days_back = int
try:
	with open(folder_path + 'all.pickle', 'rb') as f:
		all_list = pickle.load(f)
	f.close()
except FileNotFoundError:
	print('Pickle file was not found, this will result in creating a new pickle file')
	
if(len(all_list) != 0):
	#Convert all the dates of the current downloaded transactions to a list of datetime
    list_of_dates = [datetime.strptime(all_list[x]['buisday'], '%Y-%m-%d') for x in range(0, len(all_list))]
	#Find the last made transaction
    latest_transactions = max(list_of_dates)
    diff = datetime.now() - latest_transactions
	# Date between the last input in all transactions
    days_back = diff.days
else:
	print('All list was empty, taking 365 days')
	days_back = 365

# Set headless
options = webdriver.ChromeOptions()
options.add_argument('headless')
#This option doesn't seem to work, as it downloads to the python folder instead. 
options.add_argument(
	'download.default_directory=/Users/albinjonfelt/Documents/programmering/aktier/bin')
browser = webdriver.Chrome(options=options)
print("Running chrome headless")

# open the browser
browser.get('https://www.nordnet.se/se')

# login
browser.find_elements_by_class_name('sv-font-button-white')[0].click()
browser.implicitly_wait(7)
open_login_button = browser.find_element_by_xpath(
	"/html/body/div[1]/section/section[2]/section/section/section/div[2]/div/button")
open_login_button.click()
username_field = browser.find_elements_by_id('username')
username_field[0].send_keys('albinjon')
password_field = browser.find_elements_by_id('password')
path = os.path.join(os.path.dirname(
	os.path.dirname(os.getcwd())), 'logins/pass.txt')
password = str()
with open(path) as f:
	password = f.read()
f.close()
password_field[0].send_keys(password)

login_button = browser.find_elements_by_xpath(
	'/html/body/div[1]/section/section[2]/section/section/section/section/section/section/form/section[2]/div[1]/button')
login_button[0].click()
print('Logged in')
browser.implicitly_wait(3)
try:
	my_pages_button = browser.find_element_by_class_name(
		'Typography__Span-sc-10mju41-0 efGqYn Typography__StyledTypography-sc-10mju41-1 gfLMzz MainMenuListItem__AreaButtonText-sc-16pzh42-5 jQmLzz')
	my_pages_button.click()
	transactions_button = browser.find_element_by_class_name(
		'Link__StyledLink-apj04t-0 dOfsdC')
	transactions_button.click()
except selenium.common.exceptions.NoSuchElementException:
	print("Could not find element, moving on with link")
	from_date = date.isoformat(datetime.today() - timedelta(days=days_back))
	to_date = date.isoformat(datetime.today())

	browser.get("https://www.nordnet.se/mediaapi/transaction/csv/filtered?locale=sv-SE&account_id=2&from=" +
				from_date + "&" + "to=" + to_date)
	#Cannot quit the browser if at the download location, therefore go back to another page before quitting
	#Tested browsers are firefox and chrome. 
	browser.implicitly_wait(1)
	browser.get('https://nordnet.se/se')
	try:
		my_pages_button = browser.find_element_by_class_name(
			'Typography__Span-sc-10mju41-0 efGqYn Typography__StyledTypography-sc-10mju41-1 gfLMzz MainMenuListItem__AreaButtonText-sc-16pzh42-5 jQmLzz')
		my_pages_button.click()
	except selenium.common.exceptions.NoSuchElementException:
		print("Download of transaction data complete")

browser.quit()