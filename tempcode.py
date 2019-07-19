from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.common.action_chains import ActionChains
import json   # module to parse JSON to dictionary
import time

caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)

driver = webdriver.Chrome(desired_capabilities=caps, options=options)

driver.get('http://www.youtube.com')
time.sleep(3)

si=driver.find_elements_by_xpath('//*[@aria-label="Sign in"]')
si[0].click()
time.sleep(3)
(driver.find_element_by_xpath('//*[@type="email"]')).send_keys('testsnetwork13@gmail.com')
(driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')).click()
time.sleep(3)

(driver.find_element_by_xpath('//*[@type="password"]')).send_keys('iitbombay13')
(driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')).click()
time.sleep(3)

a=driver.find_element_by_id('search')
a.click()
a.send_keys('minutephysics what is fire\n') #search parameter
time.sleep(3)

c=driver.find_element_by_xpath('//*[@id="overlays"]/ytd-thumbnail-overlay-time-status-renderer/span')
st=(c.text).split(':')
driver.find_element_by_class_name('ytd-video-renderer').click()
time.sleep(int(st[0])*60 + int(st[1]))
#driver.find_element_by_class_name('ytd-video-renderer').click()
#time.sleep(2)   #playback time
#
#tl=((driver.find_element_by_class_name('ytp-time-duration')).text).split(':')
#st=(int(tl[0])*60 + int(tl[1]))
#st
#
#element_to_hover_over = driver.find_element_by_xpath('//*[@id="movie_player"]/div[1]/video')
#ActionChains(driver).move_to_element(element_to_hover_over).perform()

#tl=((driver.find_element_by_class_name('ytp-time-duration')).text).split(':')
#time.sleep(int(tl[0])*60 + int(tl[1]))

driver.get('http://www.youtube.com')
time.sleep(3)

driver.find_element_by_xpath('//*[@id="img"]').click()
time.sleep(2)
driver.find_elements_by_xpath("//*[@class='style-scope ytd-compact-link-renderer' and contains(text(), 'Sign out')]")[0].click()
time.sleep(2)

logs=driver.get_log('performance')
driver.quit()
logreqs = [item for item in logs if 'Network.requestWillBeSent' in str(item)]

file=open(file='get_logs1.txt', mode='w')


for i in logreqs:
    tmp=json.loads(i['message'])
    if (tmp['message']['params']['request']['method']=='GET'):
        file.write('GET ' + tmp['message']['params']['request']['url']+' HTTP/1.1\n' )
        file.write('HOST: '+tmp['message']['params']['documentURL']+'\n')
        file.write('HEADERS: '+str(tmp['message']['params']['request']['headers'])+'\n\n')
        

        
file.close()