
📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
아래 요구사항에 맞는 CREATE TABLE 문을 작성하시오.
✔ 요구사항
테이블명: students

컬럼:

id (UUID PRIMARY KEY DEFAULT uuid_generate_v4())
name (VARCHAR(50))
age (INT)

UUID 확장 기능 활성화
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

테이블 생성
CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50),
    age INT
);