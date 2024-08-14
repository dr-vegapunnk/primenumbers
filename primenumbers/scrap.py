from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
 # Headless mode

driver = webdriver.Chrome(options=chrome_options)

url = 'https://hprera.nic.in/PublicDashboard'
driver.get(url)
driver.implicitly_wait(300)  
all_matches = driver.find_elements(By.XPATH,'//a[@title = "View Application"]')
print(len(all_matches))
list_projects = []
for i in range(0,6,1):
    if i <=len(all_matches):
        button = all_matches[i]
        button.click()
        content = []
        tr = driver.find_elements(By.XPATH,'//div[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr')
        for td in tr:
            content.append(f"{td.find_element(By.XPATH,'./td[1]').text} : {td.find_element(By.XPATH,'./td[2]').text} ")

        list_projects.append(content)
        close_button = driver.find_element(By.XPATH,'//button[@class="close"]')
        close_button.click()


print(list_projects)

driver.quit()
