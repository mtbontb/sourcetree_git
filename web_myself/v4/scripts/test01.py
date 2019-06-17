from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()

# loc = (By.CSS_SELECTOR, "#username")

loc = By.CSS_SELECTOR, "#username"

# driver.find_element(loc[0],loc[1])


print(loc[0], loc[1])
print("--" * 50)
print(*loc)
print(type(loc))