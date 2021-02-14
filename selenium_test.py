from selenium import webdriver

# change driver location to match your system
chrome_driver_exe = r"drivers\chromedriver.exe"
url = r'https://www.google.com'
textbox_full_xpath = "/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input"
button_full_xpath = "/html/body/div[1]/div[3]/form/div[2]/div[1]/div[3]/center/input[1]"
search_phrase = "i just googled using selenium, invoked by jenkins pipeline"

chromedriver = webdriver.Chrome(executable_path=chrome_driver_exe)
chromedriver.get(url)
element = chromedriver.find_element_by_xpath(textbox_full_xpath)
element.send_keys(search_phrase)
chromedriver.find_element_by_xpath(button_full_xpath).click()

# adding some comment to change file content