from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


driver = webdriver.Chrome(options=chrome_options)

url = "https://www.google.com/maps/search/.............."

driver.get(url)

driver.implicitly_wait(10)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
infos = soup.find_all("div", class_="lI9IFe")
for info in infos:
    name = info.find("div", class_="qBF1Pd fontHeadlineSmall").text.strip()
    rate= info.find("span", class_="MW4etd").text.strip()
    print("name: ",name)
    print("rate: ",rate)
    print("-"*50)

driver.quit()
