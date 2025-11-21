📌 문제 6 — PRIMARY KEY 이해 문제

다음과 같은 테이블을 가정하시오:

CREATE TABLE books (
    book_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
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

duplicate key value violates unique constraint "books_pkey"

왜 발생하는가? 

books A, B가 1로 동일, 충돌
이미 존재하는 ID를 재입력함으로 생긴 충돌.

PRIMARY KEY 의 규칙을 쓰시오.

Primary Key(기본키)는 반드시 아래 두 가지 조건을 만족해야 함.
Unique (고유성): 테이블 내에서 중복된 값을 가질 수 없다. (사람의 주민등록번호처럼 식별 가능해야 함)
Not Null (비어있지 않음): 데이터가 반드시 존재해야 함. (NULL 값을 허용하지 않음)

cursor.execute("INSERT INTO books (book_id, title, price) VALUES ('uuid-값-중복', '책 B', 15000);")
except Exception as e:
    print("에러 발생:", e)
    conn.rollback(  ) # 에러 발생 시 롤백 필수.