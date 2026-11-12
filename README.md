# Python Selenium Automation

Python, Selenium, pytest를 사용한 웹 UI 자동화 학습 프로젝트입니다.

## 테스트 대상
https://automationexercise.com/

## 실행 방법
프로젝트 루트 폴더에서 시작합니다.
pip install -r requirements.txt
python -m pytest tests -v -s

## 프로젝트 구성

- tests/conftest.py: 브라우저 생성·종료를 관리하는 공통 fixture
- tests/test_home.py: 홈페이지 제목 검증
- tests/test_product_search.py: 공통 검색 함수 및 상품 검색 테스트

## 현재 테스트 상태
- 홈페이지 제목 검증: PASS
- 상품 검색 결과 화면 및 상품 표시 검증: PASS(dress,top,jeans)
- 검색 결과 없음 검증: PASS (xyz123, 상품 수 0개)

## 검증 내용

### 홈페이지
- 페이지 제목에 "Autoamtion Exercise"가 포함되는지 확인

### 상품 검색
- "dress"입력 후 검색 실행
- "SEARCHED PRODUCTS" 제목 표시 확인
- 검색 결과 상품이 1개 이상 표시되는지 확인
- 검색된 상품명을 콘솔에 출력
- 검색 결과가 없는 검색어 검증: PASS

## 검색 결과 분석 및 검증 조건 조정
초기에는 모든 검색 결과의 상품명에 검색어가 포함되어야 한다는
조건으로 검증했습니다.

"dress" 검색 결과에 상품명에 해당 단어가 없는 상품이 표시되었으며,
수동 확인 과정에서 해당 상품이 DRESS 카테고리에 포함된 것을
확인했습니다.

검색 대상이 상품명으로만 제한된다는 명세는 확인되지 않았으므로,
상품명에 검색어가 없다는 이유만으로 결함으로 판단하지 않았습니다.

현재는 검색 결과 화면 표시와 상품 조회 여부를 검증합니다.
검색 결과의 정확성 검증은 검색 대상 범위와 기대 결과를 확인한 뒤
보완할 예정입니다.

### 검색 결과 없음

- 상품과 일치하지 않는 검색어로 검색 실행
- "SEARCHED PRODUCTS" 제목 표시 확인
- 검색 결과 상품 수가 0개인지 검증

## 테스트 실행 구조
pytest fixture를 사용하여 각 테스트 실행 전에 브라우저를 생성하고, 테스트 종료 후 브라우저를 종료합니다.

## 코드 개선

- 반복되는 페이지 접속, 검색어 입력, 검색 버튼 클릭,
  검색 결과 제목 대기를 `search_products(driver, keyword)` 함수로 분리
- 검색 결과가 있는 테스트와 없는 테스트에서 공통 함수 재사용
- 상품 수 검증은 각 테스트에 유지
- 리팩터링 후 검색 테스트 4개 PASS 확인