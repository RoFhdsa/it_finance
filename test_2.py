from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup



import time
#создаем драйвер для хрома
driver = webdriver.Chrome()
#имитируем, что мы попали на страницу
url = "https://ptable.com/?lang=ru"
#url = "https://www.google.ru/?hl=ru"
class Сhemical_element ():
    def __init__(self, atomic, name, weight):
        self.atomic = atomic
        self.name = name
        self.weight = weight

try:
    #Запускаем браузер
    driver.get(url=url)
    # Запускаем с режимо тайминга, дабы все отрибуты успели появится
    elent_by = (WebDriverWait(driver, 2).
                until(EC.visibility_of_all_elements_located(((By.CSS_SELECTOR, "ol[id*='Ptable']>li")))))
    # получаем перечень всех дочерних элементов которые хранят в себе имя элемента
    for element in elent_by:
        # преобразуем в html
        element = element.get_attribute('innerHTML')
        soup = BeautifulSoup(element, 'html.parser')
        # теперь можем передать в класс конкретные атрибуты, обращаясь к ним
        Сhemical_element (atomic = soup.b.string,
                          name = soup.em.string,
                          weight= soup.data.string)
        break
    pass
except Exception as e:
    print('ERROR')
    print(e)
finally:
    driver.close()
    driver.quit()
