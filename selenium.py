from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManger

driver = webdriver.Chrome(executable_path=ChromeDriverManger().install())