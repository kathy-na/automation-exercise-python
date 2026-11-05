from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_products():
    driver = webdriver.Chrome()

    try:
        print("1. 페이지 접속 시작")
        driver.get("https://automationexercise.com/products")
        print("2. 페이지 접속 완료")

        wait = WebDriverWait(driver, 15)
        keyword = "dress"

        search_box = wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
        search_box.send_keys(keyword)

        driver.find_element(By.ID,"submit_search").click()

        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "h2.title"),
                "SEARCHED PRODUCTS"
            )
        )

        products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".productinfo p")))

        print(f"검색어: {keyword}")
        print(f"검색된 상품 수: {len(products)}")

        assert len(products) > 0, "검색 결과가 없습니다."

        for product in products:
            product_name = product.text
            print(f"상품명: {product_name}")

            assert keyword in product_name.lower(), (f"검색어와 일치하지 않는 상품입니다.: {product_name}")

    finally:
        driver.quit()
