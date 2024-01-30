from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

#создаем драйвер для хрома
driver = webdriver.Chrome()
#записываем страницу с которой будем работать
url = "https://ptable.com/?lang=ru"
#объявим лист, который будет хранить перечень элементов
elements_list =[]
#создаем класс Сhemical_element
class Сhemical_element ():
    def __init__(self, atomic, name, weight):
        self.atomic = atomic
        self.name = name
        self.weight = weight

try:
    #Запускаем браузер
    driver.get(url=url)
    # Запускаем с режимом тайминга, дабы все атрибуты успели появится
    elent_by = (WebDriverWait(driver, 2).
                until(EC.visibility_of_all_elements_located(((By.CSS_SELECTOR, "ol[id*='Ptable']>li")))))
    # получаем перечень всех дочерних элементов которые хранят в себе имя элемента
    for element in elent_by:
        # преобразуем в html
        element = element.get_attribute('innerHTML')
        soup = BeautifulSoup(element, 'html.parser')
        # теперь можем передать в класс конкретные атрибуты, обращаясь к ним
        сhemical_element = Сhemical_element (atomic = soup.b.string,
                          name = soup.em.string,
                          weight= soup.data.string)
        elements_list.append(сhemical_element)
    pass
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()

#принтуем данные
for element in elements_list:
    print(f"Порядковый номер в таблице: {element.atomic}, Название элемента: {element.name}, атомная масса элемента: {element.weight}")