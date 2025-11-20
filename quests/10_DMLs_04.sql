📌 문제 4 — 키워드 검색 로그 테이블
테이블명: keyword_search_logs
 컬럼:
keyword
result_count
search_time

테이블 생성
CREATE TABLE keyword_search_logs (
    keyword VARCHAR(100),
    result_count INT,
    search_time DATETIME


데이터:
"python", 120, "2025-11-19 10:00:00"
"chatgpt", 300, "2025-11-19 10:05:00"
"docker", 90, "2025-11-19 10:10:00"


👉 요구:
위 3개 데이터를 INSERT

INSERT INTO keyword_search_logs (keyword, result_count, search_time) 
VALUES ('python', 120, '2025-11-19 10:00:00');
INSERT INTO keyword_search_logs (keyword, result_count, search_time) 
VALUES ('chatgpt', 300, '2025-11-19 10:05:00');
INSERT INTO keyword_search_logs (keyword, result_count, search_time) 
VALUES ('docker', 90, '2025-11-19 10:10:00');


result_count가 100 이상인 키워드 조회

SELECT * FROM keyword_search_logs 
WHERE result_count >= 100;


"docker" 검색 결과 수를 150으로 UPDATE

UPDATE keyword_search_logs 
SET result_count = 150 
WHERE keyword = 'docker';


"python" 로그 삭제

DELETE FROM keyword_search_logs 
WHERE keyword = 'python';