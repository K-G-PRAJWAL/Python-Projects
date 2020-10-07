from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')
ele = browser.find_element_by_css_selector(
    '.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')

# Click a selected CSS element
ele.click()

# Go forward
browser.forward()

# refresh browser
browser.refresh()

# Quit browser
browser.quit()
