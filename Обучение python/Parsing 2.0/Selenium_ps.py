from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle

# driver = webdriver.Chrome()
options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled', False) # убирает флаг в браузере, который говорит о том что скрапит программа
options.set_preference('dom.webnotifications.enabled', False) # убирает всплывающие уведомления
options.set_preference('media.volume_scale', '0.0') # убирает звук
options.set_preference('general.useragent.override', 'example :)') # изменение user агента
# options.headless = True # запуск браузера в фоновом режиме
# options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get('https://nick-name.ru/generate/')
time.sleep(60)
pickle.dump(driver.get_cookies(), open('session', 'wb'))

# while True:
#     button_xpath = '//*[@id="generate"]'
#     driver.find_element(By.XPATH, button_xpath).click()
    
#     link = driver.find_element(By.ID, 'register').get_attribute('href')[36:]
#     print(f'Nickname: {link}')
# button = driver.find_element(By.CLASS_NAME, 'style-scope ytd-rich-grid-renderer')
# all_video = button.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-item-renderer')
# print(all_video)
# # driver.get('https://google.com')
# # driver.save_screenshot('1.png') 
# # driver.refresh()
# driver.quit()
# xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]'
# button = driver.find_element(By.XPATH, xpath).click()