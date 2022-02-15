# initial test of the browser and setups in funt.py


from selenium import webdriver

browswer = webdriver.Firefox()
browswer.get('http://localhost:8000')

assert browswer.page_source.find('Pharmacy')