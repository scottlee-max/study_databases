📌 문제 2 — CREATE (INSERT) 기초
✔ 요구사항
위 students 테이블에 다음 데이터를 INSERT 하시오.
id
name
age
1
홍길동
23
2
이영희
21
3
박철수
26

● ID가 1, 2, 3--->UUID와 불일치
 (name, age로만 입력)

INSERT INTO students (name, age)
VALUES 
    ('홍길동', 23),
    ('이영희', 21),
    ('박철수', 26);