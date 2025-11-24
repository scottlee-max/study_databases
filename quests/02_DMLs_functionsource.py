import psycopg2
from psycopg2 import sql

# 📢 데이터베이스 연결 설정 (실제 환경에 맞게 수정 필요)
# 주의: 보안을 위해 실제 서비스에서는 환경 변수 등을 사용하는 것이 좋습니다.
DB_CONFIG = {
    "host": "localhost",
    "database": "your_db_name",  # 실제 데이터베이스 이름으로 변경
    "user": "your_user_name",    # 실제 사용자 이름으로 변경
    "password": "your_password",  # 실제 비밀번호로 변경
    "port": "5432"
}

# 헬퍼 함수: 데이터베이스 연결 및 커서 가져오기
def get_db_connection():
    """데이터베이스 연결 객체를 반환합니다."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"데이터베이스 연결 오류: {e}")
        return None

# ---

## 📌 문제 1 — 테이블 생성 함수 만들기
def create_books_table():
    """요구사항에 맞게 'books' 테이블을 생성합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        
        # UUID 생성을 위한 확장 기능 활성화 (이미 되어 있다면 무시됨)
        cur.execute("CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
        
        # 테이블 생성 쿼리
        create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            title VARCHAR(100) NOT NULL,
            price INT
        );
        """
        cur.execute(create_table_query)
        conn.commit()
        print("books 테이블이 생성되었습니다.")
        
    except psycopg2.Error as e:
        print(f"테이블 생성 오류: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

# 1차, 2차 검증 로직을 포함한 테스트 실행
if __name__ == '__main__':
    print("--- 1. 테이블 생성 테스트 ---")
    create_books_table()

    # 1차, 2차 검증: 테이블이 실제로 생성되었는지 확인
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            # PostgreSQL 시스템 카탈로그에서 'books' 테이블 존재 여부 확인
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE schemaname = 'public' AND tablename  = 'books'
                );
            """)
            exists = cur.fetchone()[0]
            print(f"1차/2차 검증: 'books' 테이블 존재 여부: {'✅ 존재함' if exists else '❌ 존재하지 않음'}")
        except Exception as e:
            print(f"테이블 존재 검증 오류: {e}")
        finally:
            if conn:
                conn.close()

# ---

## 📌 문제 2 — INSERT 함수 만들기
def insert_books():
    """테스트용 데이터를 'books' 테이블에 삽입합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    # id는 제외하고 title과 price만 사용
    test_data = [
        ("파이썬 입문", 19000),
        ("알고리즘 기초", 25000),
        ("네트워크 이해", 30000)
    ]
    
    insert_query = "INSERT INTO books (title, price) VALUES (%s, %s)"
    
    try:
        cur = conn.cursor()
        cur.executemany(insert_query, test_data)
        rows_inserted = cur.rowcount
        conn.commit()
        print(f"{rows_inserted}개 도서가 삽입되었습니다.")
        
    except psycopg2.Error as e:
        print(f"데이터 삽입 오류: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

# 1차, 2차 검증 로직을 포함한 테스트 실행
if __name__ == '__main__':
    print("\n--- 2. 데이터 삽입 테스트 ---")
    insert_books()

    # 1차, 2차 검증: 삽입된 데이터 개수 확인
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM books;")
            count = cur.fetchone()[0]
            print(f"1차/2차 검증: 'books' 테이블 레코드 개수: {count}개 {'✅' if count == 3 else '❌'}")
        except Exception as e:
            print(f"데이터 개수 검증 오류: {e}")
        finally:
            if conn:
                conn.close()

# ---

## 📌 문제 3 — SELECT 함수 만들기

def get_all_books():
    """전체 도서 데이터를 조회합니다."""
    conn = get_db_connection()
    if conn is None:
        return []
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, title, price FROM books ORDER BY price;")
        return cur.fetchall()
    except psycopg2.Error as e:
        print(f"전체 조회 오류: {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_expensive_books():
    """가격이 25000원 이상인 도서를 조회합니다."""
    conn = get_db_connection()
    if conn is None:
        return []
        
    try:
        cur = conn.cursor()
        # SQL Injection 방지를 위해 %s 플레이스홀더 사용
        cur.execute("SELECT id, title, price FROM books WHERE price >= %s ORDER BY price DESC;", (25000,))
        return cur.fetchall()
    except psycopg2.Error as e:
        print(f"가격 필터링 조회 오류: {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_book_by_title(title):
    """제목이 일치하는 도서를 조회합니다."""
    conn = get_db_connection()
    if conn is None:
        return []
        
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, title, price FROM books WHERE title = %s;", (title,))
        return cur.fetchall()
    except psycopg2.Error as e:
        print(f"제목 조회 오류: {e}")
        return []
    finally:
        if conn:
            conn.close()

# 1차, 2차 검증 로직을 포함한 테스트 실행
if __name__ == '__main__':
    print("\n--- 3. 데이터 조회 테스트 ---")
    
    # 1. 전체 조회
    all_books = get_all_books()
    print("✅ 전체 조회 결과:")
    for book in all_books:
        print(f"ID: {book[0]}, Title: {book[1]}, Price: {book[2]}")
    
    # 2. 가격 필터링 조회
    expensive_books = get_expensive_books()
    print("\n✅ 가격 >= 25000 조회 결과:")
    for book in expensive_books:
        print(f"ID: {book[0]}, Title: {book[1]}, Price: {book[2]}")
        
    # 3. 제목으로 조회
    target_title = "파이썬 입문"
    book_by_title = get_book_by_title(target_title)
    print(f"\n✅ 제목이 '{target_title}'인 도서 조회 결과:")
    for book in book_by_title:
        print(f"ID: {book[0]}, Title: {book[1]}, Price: {book[2]}")

    # 1차, 2차 검증: 조회된 데이터의 정확성 확인
    print(f"\n1차/2차 검증: 전체 조회 레코드 수: {len(all_books)}개 {'✅' if len(all_books) == 3 else '❌'}")
    print(f"1차/2차 검증: >= 25000 레코드 수: {len(expensive_books)}개 {'✅' if len(expensive_books) == 2 else '❌'}")

# ---

## 📌 문제 4 — UPDATE 함수 만들기
def update_second_book_price():
    """저장된 순서에서 두 번째 도서의 가격을 27000으로 변경합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    # 옵션: ID를 기준으로 정렬하여 두 번째 도서의 UUID를 가져옵니다.
    select_uuid_query = "SELECT id FROM books ORDER BY id LIMIT 1 OFFSET 1;" # OFFSET 1은 두 번째 레코드를 의미
    update_price_query = "UPDATE books SET price = %s WHERE id = %s;"
    new_price = 27000
    
    try:
        cur = conn.cursor()
        
        # 1단계: 두 번째 도서의 UUID 조회
        cur.execute(select_uuid_query)
        second_book_id = cur.fetchone()
        
        if second_book_id:
            book_uuid = second_book_id[0]
            
            # 2단계: 해당 UUID를 사용하여 가격 업데이트
            cur.execute(update_price_query, (new_price, book_uuid))
            conn.commit()
            print("두 번째 도서 가격이 27000으로 수정되었습니다.")
            
            # 검증을 위해 업데이트된 도서의 ID 반환
            return book_uuid
        else:
            print("두 번째 도서를 찾을 수 없습니다.")
            return None
            
    except psycopg2.Error as e:
        print(f"업데이트 오류: {e}")
        conn.rollback()
        return None
    finally:
        if conn:
            conn.close()

# 1차, 2차 검증 로직을 포함한 테스트 실행
if __name__ == '__main__':
    print("\n--- 4. 데이터 업데이트 테스트 ---")
    updated_id = update_second_book_price()

    # 1차, 2차 검증: 업데이트된 레코드의 가격 확인
    if updated_id:
        conn = get_db_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT price FROM books WHERE id = %s;", (updated_id,))
                updated_price = cur.fetchone()[0]
                print(f"1차/2차 검증: 업데이트된 도서 (ID: {updated_id})의 가격: {updated_price} {'✅' if updated_price == 27000 else '❌'}")
            except Exception as e:
                print(f"업데이트 검증 오류: {e}")
            finally:
                if conn:
                    conn.close()

# ---

## 📌 문제 5 — DELETE 함수 만들기
def delete_third_book():
    """저장된 순서에서 세 번째 도서 데이터를 삭제합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    # 옵션: ID를 기준으로 정렬하여 세 번째 도서의 UUID를 가져옵니다.
    select_uuid_query = "SELECT id FROM books ORDER BY id LIMIT 1 OFFSET 2;" # OFFSET 2는 세 번째 레코드를 의미
    delete_query = "DELETE FROM books WHERE id = %s;"
    
    try:
        cur = conn.cursor()
        
        # 1단계: 세 번째 도서의 UUID 조회
        cur.execute(select_uuid_query)
        third_book_id = cur.fetchone()
        
        if third_book_id:
            book_uuid = third_book_id[0]
            
            # 2단계: 해당 UUID를 사용하여 데이터 삭제
            cur.execute(delete_query, (book_uuid,))
            rows_deleted = cur.rowcount
            conn.commit()
            
            if rows_deleted > 0:
                print("세 번째 도서가 삭제되었습니다.")
                return book_uuid
            else:
                print("세 번째 도서를 삭제하지 못했습니다.")
                return None
        else:
            print("세 번째 도서를 찾을 수 없습니다.")
            return None
            
    except psycopg2.Error as e:
        print(f"삭제 오류: {e}")
        conn.rollback()
        return None
    finally:
        if conn:
            conn.close()

# 1차, 2차 검증 로직을 포함한 테스트 실행
if __name__ == '__main__':
    print("\n--- 5. 데이터 삭제 테스트 ---")
    deleted_id = delete_third_book()

    # 1차, 2차 검증: 삭제된 레코드가 존재하지 않는지 확인
    if deleted_id:
        conn = get_db_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute("SELECT COUNT(*) FROM books WHERE id = %s;", (deleted_id,))
                count = cur.fetchone()[0]
                print(f"1차/2차 검증: 삭제된 도서 (ID: {deleted_id}) 존재 여부: {'❌ 존재함' if count > 0 else '✅ 존재하지 않음'}")
            except Exception as e:
                print(f"삭제 검증 오류: {e}")
            finally:
                if conn:
                    conn.close()
    
    # 최종적으로 남은 데이터 확인
    print("\n--- 최종 데이터 상태 ---")
    final_books = get_all_books()
    if final_books:
        for book in final_books:
            print(f"ID: {book[0]}, Title: {book[1]}, Price: {book[2]}")
    else:
        print("테이블에 남은 데이터가 없습니다.")

# ---