from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_home_page_title():
    driver = webdriver.Chrome()

    try:
        driver.get("https://automationexercise.com/")

        WebDriverWait(driver, 15).until(lambda browser: "Automation Exercise" in browser.title)

        print("현재 페이지 제목:", driver.title)
        assert "Automation Exercise" in driver.title, (f"페이지 제목이 예상과 다릅니다. 실제 제목: {driver.title}")
        

    finally:
        driver.quit()