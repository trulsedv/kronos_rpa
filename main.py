from selenium import webdriver

url = "https://kronos.rainpower.no/wfc/logon"

driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
input("\n\nTrykk enter når du har logget inn og valg korrekt lønnsperiode.")
iframe = driver.find_element_by_xpath("//iframe[@name='widgetFrame723']")
driver.switch_to.frame(iframe)
table = driver.find_elements_by_xpath('//*[@id="contentjqxGrid0"]')

print(table[0].text)
driver.close()
