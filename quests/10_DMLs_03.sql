📌 문제 3 — HTML 스크래핑 결과 테이블
테이블명: scraping_html_results
 컬럼:
page_title
page_url
html_length
status_code

테이블 생성
CREATE TABLE scraping_html_results (
    page_title VARCHAR(100),
    page_url VARCHAR(255),
    html_length INT,
    status_code INT

데이터:
"홈페이지", "https://site.com", 15700, 200
"블로그", "https://blog.com", 9800, 200
"404 페이지", "https://site.com/notfound", 0, 404

👉 요구:
데이터 3개 추가

INSERT INTO scraping_html_results (page_title, page_url, html_length, status_code)
VALUES ('홈페이지', '[https://site.com](https://site.com)', 15700, 200);
INSERT INTO scraping_html_results (page_title, page_url, html_length, status_code)
VALUES ('블로그', '[https://blog.com](https://blog.com)', 9800, 200);
INSERT INTO scraping_html_results (page_title, page_url, html_length, status_code)
VALUES ('404 페이지', '[https://site.com/notfound](https://site.com/notfound)', 0, 404);



status_code가 200인 페이지만 조회

SELECT * FROM scraping_html_results 
WHERE status_code = 200;

"블로그"의 html_length를 12000으로 수정

UPDATE scraping_html_results 
SET html_length = 12000 
WHERE page_title = '블로그';


status_code가 404인 데이터 삭제

DELETE FROM scraping_html_results 
WHERE status_code = 404;