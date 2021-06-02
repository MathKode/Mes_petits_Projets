from selenium import webdriver
import time

# creer une vr pour déclencher le driver
driver = webdriver.Chrome("/Users/mathis_kremer/Documents/Ecole/Programation/Python/Mes_petits_projets/chromedriver")
driver.get("https://apps.facebook.com/exoty-tarot/")

#Print la page
page_web = str(driver.page_source.encode('utf8'))
#print(page_web)

#Remplir le champ de connection email :
email_entry = driver.find_element_by_class_name("inputtext _55r1 inputtext _1kbt inputtext _1kbt")
email_entry.send_keys('lol')