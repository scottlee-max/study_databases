
### 📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
아래 요구사항에 맞는 CREATE TABLE 문을 작성하시오.

✔ 요구사항

테이블명: students
컬럼:

id (INT, PRIMARY KEY) #PRIMARY KEY는 해당 테이블에서 각 행(Row)을 식별하는 고유한 키이므로 중복될 수 없다.

name (VARCHAR(50))
age (INT)

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);


### 📌 문제 2 — CREATE (INSERT) 기초

✔ 요구사항

위 students 테이블에 다음 데이터를 INSERT 하시오.

id, name, age
1
홍길동
23
2
이영희
21
3
박철수
26

INSERT INTO students (id, name, age) VALUES (1, '홍길동', 23);
INSERT INTO students (id, name, age) VALUES (2, '이영희', 21);
INSERT INTO students (id, name, age) VALUES (3, '박철수', 26);

or
INSERT INTO students (id, name, age) VALUES 
(1, '홍길동', 23), (2, '이영희', 21), (3, '박철수', 26);

### 📌 문제 3 — READ (SELECT) 기본 조회

다음 조건들을 만족하는 SELECT 쿼리를 작성하시오.

students 테이블의 전체 데이터를 조회.

SELECT * FROM students;

나이가 22세 이상인 학생만 조회

SELECT * FROM students WHERE age >= 22;

name 이 “홍길동”인 학생만 조회

SELECT * FROM students WHERE name = '홍길동';


### 📌 문제 4 — UPDATE 연습

✔ 요구사항

id = 2 인 학생의 나이를 25로 수정하시오.

UPDATE students 
SET age = 25 
WHERE id = 2;


### 📌 문제 5 — DELETE 연습

✔ 요구사항
id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.

DELETE FROM students 
WHERE id = 3;


### 📌 문제 6 — PRIMARY KEY 이해 문제
다음과 같은 테이블을 가정하시오:
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);

아래 데이터 INSERT 시 발생할 문제를 설명하시오.
INSERT INTO books (book_id, title, price)
VALUES (1, '책 A', 10000);

INSERT INTO books (book_id, title, price)
VALUES (1, '책 B', 15000);

📌 질문:
어떤 에러가 발생하는가?
PRIMARY KEY는 주민등록번호인데. 현실에서 주민번호가 같은 사람이 두 명일 수 없다. 쌍둥이라도, 테이블에 PRIMAEY KEY가 같은 행은 두 개일 수 없다.

왜 발생하는가?

PRIMARY KEY의 중복 실행.

PRIMARY KEY 의 규칙을 쓰시오.

-- 테이블 생성
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT, 
    title VARCHAR(100),
    price INT
);

INSERT INTO books (title, price) VALUES ('책 A', 10000); 
INSERT INTO books (title, price) VALUES ('책 B', 15000); 

SOLUTION

INSERT INTO books (book_id, title, price)
VALUES (2, '책 B', 15000);