## PROMPT
```
## 💡 문제 해결 프롬프트 JSON 출력

요청하신 [5가지 문제 해결 과제]에 대한 [가이드]를 준수한 **문제 풀이 프롬프트**를 JSON 형식으로 출력합니다. 
이 프롬프트는 PostgreSQL 데이터베이스 연동을 가정하며, `psycopg2` 라이브러리를 사용합니다.
편의를 위해 데이터베이스 연결 설정은 예시 코드 내에서 변수로 처리합니다.

```json
{
  "user_persona": "나는 Python, JavaScript, C++ 외 모든 코딩언어 마스터야",
  "problem_solving_guide": {
    "1": "반드시 요구사항에 기반하여 함수 제작.",
    "2": "각각의 문제마다 < if '__name__' == '__main__' : >을 사용해서 테스트를 진행하고 예시까지 생성.",
    "3": "이후 1차, 2차 검증 실행."
  },
  "prompt_for_solution": [
    {
      "problem_number": 1,
      "title": "테이블 생성 함수 만들기",
      "function_name": "create_books_table()",
      "language": "Python",
      "description": "PostgreSQL 데이터베이스에 'books' 테이블을 생성하는 Python 함수를 작성하시오.",
      "requirements": {
        "table_name": "books",
        "columns": [
          {"name": "id", "data_type": "UUID PRIMARY KEY DEFAULT uuid_generate_v4()"},
          {"name": "title", "data_type": "VARCHAR(100)"},
          {"name": "price", "data_type": "INT"}
        ]
      },
      "expected_output_example": "books 테이블이 생성되었습니다.",
      "solution_prompt": "PostgreSQL 연결 및 'books' 테이블을 요구사항에 맞게 생성하는 Python 함수 `create_books_table()`을 작성하고, `if '__name__' == '__main__':` 블록 내에서 함수를 호출하여 테이블 생성 후 성공 메시지를 출력하세요. 검증 과정은 데이터베이스에서 테이블 존재 여부를 확인하는 쿼리를 포함합니다.",
      "tool_suggestion": "psycopg2"
    },
    {
      "problem_number": 2,
      "title": "INSERT 함수 만들기",
      "function_name": "insert_books()",
      "language": "Python",
      "description": "제공된 테스트용 데이터를 'books' 테이블에 삽입하는 Python 함수를 작성하시오. id 컬럼은 자동 생성(UUID)되므로 INSERT 시 제외해야 합니다.",
      "test_data": [
        {"id": 1, "title": "파이썬 입문", "price": 19000},
        {"id": 2, "title": "알고리즘 기초", "price": 25000},
        {"id": 3, "title": "네트워크 이해", "price": 30000}
      ],
      "expected_output_example": "3개 도서가 삽입되었습니다.",
      "solution_prompt": "데이터 리스트를 반복하여 'books' 테이블에 데이터를 삽입하는 Python 함수 `insert_books()`를 작성하세요. 삽입 후 영향을 받은 행의 수를 확인하고, `if '__name__' == '__main__':` 블록 내에서 함수 호출 및 출력 예시를 재현하세요. 검증 과정은 삽입된 레코드의 수를 확인하는 SELECT COUNT(*) 쿼리를 포함합니다.",
      "tool_suggestion": "psycopg2"
    },
    {
      "problem_number": 3,
      "title": "SELECT 함수 만들기",
      "language": "Python",
      "description": "아래 조건을 만족하는 조회용 Python 함수들을 작성하시오.",
      "required_functions": [
        {"function_name": "get_all_books()", "condition": "전체 조회"},
        {"function_name": "get_expensive_books()", "condition": "가격이 25000원 이상인 데이터 조회"},
        {"function_name": "get_book_by_title(title)", "condition": "title 이 매개변수와 일치하는 데이터 조회"}
      ],
      "solution_prompt": "PostgreSQL에서 데이터를 조회하는 세 가지 Python 함수(`get_all_books`, `get_expensive_books`, `get_book_by_title`)를 작성하세요. 각 함수는 조회된 결과를 반환해야 하며, `if '__name__' == '__main__':` 블록 내에서 세 함수를 모두 호출하여 조회된 데이터를 출력하고 예시를 생성하세요. 검증 과정은 각 쿼리의 정확성과 반환된 데이터의 유효성을 확인합니다.",
      "tool_suggestion": "psycopg2"
    },
    {
      "problem_number": 4,
      "title": "UPDATE 함수 만들기",
      "function_name": "update_second_book_price()",
      "language": "Python",
      "description": "저장된 순서에서 두 번째 도서의 가격을 27000으로 변경하는 Python 함수를 작성하시오.",
      "option": "두 번째 도서의 UUID를 SELECT로 먼저 가져온 후 UPDATE를 수행한다.",
      "new_price": 27000,
      "expected_output_example": "두 번째 도서 가격이 27000으로 수정되었습니다.",
      "solution_prompt": "첫 번째 레코드를 기준으로 두 번째 레코드(예: ID 순 또는 입력 순)의 UUID를 먼저 조회한 후, 해당 UUID를 사용하여 가격을 27000으로 업데이트하는 Python 함수 `update_second_book_price()`를 작성하세요. `if '__name__' == '__main__':` 블록 내에서 함수를 호출하고 성공 메시지를 출력하세요. 검증 과정은 업데이트된 레코드의 가격을 다시 SELECT하여 27000이 되었는지 확인합니다.",
      "tool_suggestion": "psycopg2"
    },
    {
      "problem_number": 5,
      "title": "DELETE 함수 만들기",
      "function_name": "delete_third_book()",
      "language": "Python",
      "description": "저장된 순서에서 세 번째 도서 데이터를 삭제하는 Python 함수를 작성하시오.",
      "option": "SELECT로 UUID 조회 후 DELETE 수행",
      "expected_output_example": "세 번째 도서가 삭제되었습니다.",
      "solution_prompt": "첫 번째 레코드를 기준으로 세 번째 레코드(예: ID 순 또는 입력 순)의 UUID를 먼저 조회한 후, 해당 UUID를 사용하여 레코드를 삭제하는 Python 함수 `delete_third_book()`를 작성하세요. `if '__name__' == '__main__':` 블록 내에서 함수를 호출하고 성공 메시지를 출력하세요. 검증 과정은 삭제 후 'books' 테이블에 해당 UUID를 가진 레코드가 존재하지 않는지 확인하는 SELECT 쿼리를 포함합니다.",
      "tool_suggestion": "psycopg2"
    }
  ]
}
```
