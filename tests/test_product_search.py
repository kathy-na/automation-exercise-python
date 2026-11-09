import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("keyword",["dress","top","jeans"])
def test_search_products(driver, keyword):

    print("1. 페이지 접속 시작")
    driver.get("https://automationexercise.com/products")
    print("2. 페이지 접속 완료")

    wait = WebDriverWait(driver, 15)

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


def test_search_products_no_results(driver):
    driver.get("https://automationexercise.com/products")

    wait = WebDriverWait(driver,15)

    search_box = wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
    search_box.send_keys("xyz123")

    driver.find_element(By.ID,"submit_search").click()        

    wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "h2.title"),
                "SEARCHED PRODUCTS"
            )
        )

    products = driver.find_elements(By.CSS_SELECTOR,".productinfo p")

    print(f"검색된 상품 수: {len(products)}")

    assert len(products) == 0, (f"검색 결과가 없어야 합니다. 실제 상품 수: {len(products)}")
