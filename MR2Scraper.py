from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://collectorcarfeed.com/forum/viewtopic.php?f=2&t=64')


pricelist = []
table = browser.find_elements_by_xpath("//table[@id=\'ebayTable\']/tbody/tr/td[contains(text(), '$')]")

for elem in table:
    pricelist.append(elem.text)

print(pricelist)