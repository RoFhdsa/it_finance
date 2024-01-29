from selenium import webdriver
from urllib.parse import urlparse
#создаем драйвер для хрома
driver = webdriver.Chrome ()
#имитируем, что мы попали на страницу
url = "https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE"

def return_query_curl(url_txt):
    """
    :param url_txt: урл текстом
    :return: слорваь расспарченный query
    """
    # создаем словарь, в которой помещаем распарсенное значнеие квери параметра
    query_url_dict = {}
    # из урла получаем квери параметр
    query_url = urlparse(url_now).query
    # проходимс в цикле
    for param in query_url.split('&'):
        # получаем ключ и значения
        key, value = param.split('=')
        # записываем
        query_url_dict[key] = value
    # выводим значение
    return query_url_dict


try:
    #Запускаем браузер
    driver.get(url=url)
    # получаем текущий урл в браузере
    url_now = driver.current_url
    query_url_dict = return_query_curl (url_now)
    clickid = query_url_dict['clickid']
    print(clickid)
    pass
except:
    pass
finally:
    driver.close()
    driver.quit()

