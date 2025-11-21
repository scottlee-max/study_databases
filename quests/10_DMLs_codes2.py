
📌 문제 3 — READ (SELECT) 기본 조회

다음 조건들을 만족하는 SELECT 쿼리를 작성하시오.

students 테이블의 전체 데이터를 조회

SELECT * FROM students;

나이가 22세 이상인 학생만 조회

SELECT * FROM students 
WHERE age >= 22;

name 이 “홍길동”인 학생만 조회

SELECT * FROM students 
WHERE name = '홍길동';