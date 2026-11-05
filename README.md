# Python Selenium Automation

Python, Selenium, pytest를 사용한 웹 UI 자동화 학습 프로젝트입니다.

## 테스트 대상
https://automationexercise.com/

## 실행 방법
pip install -r requirements.txt
python -m pytest tests -v -s

## 현재 테스트 상태
- 홈페이지 제목 검증: PASS
- 상품 검색 검증: FAIL 관찰

## 검색 결과 분석
dress 검색 시 상품명에 dress가 없는 상품이 포함됩니다.
수동 검색에서도 동일한 결과를 확인했습니다.

현재 검증은 모든 검색 결과의 상품명에 검색어가 포함되어야
한다는 기준을 사용합니다. 사이트의 검색 대상 범위에 대한
명세 확인이 필요하며, 결함 의심 사례로 기록했습니다.