#0.import
import mysql.connector
from mysql.connector import Error


host="localhost"
user="phonebook"
password="phonebook"
database="phonebook_db"


#저장함수
def add_person():
        
    try:
        with mysql.connector.connect(
            host = host, 
            user = user, 
            password = password, 
            database = database
        ) as conn:

            #2.커서생성
            with conn.cursor() as cursor:

                #3.SQL문준비/바인딩/실행
                #--SQL문
                query = """
                    insert into person             
                    values(null, %s, %s, %s)
                """

                #--바인딩(튜플)
                data = ("유재석", "010-1111-1111", "02-1111-1111")

                #--실행
                cursor.execute(query, data)     #임시반영
                conn.commit()                   #최종반영    


                #4.결과처리
                print(f"{cursor.rowcount}건 등록되었습니다.")
        
    
    except Error as e:
        print(f"데이터베이스 오류: {e}")



##########################################################################

#전체가져오기 함수
def get_person_list():
    try:
    
        #1.연결/컨넥션 얻기
        conn = mysql.connector.connect(
            host = host, 
            user = user,
            password = password,
            database = database
        )

        #2.커서생성
        cursor = conn.cursor()

        #3.SQL문준비  / 바인딩 / 실행
        #--SQL문
        query = """
            select 	person_id,
                    name,
                    hp,
                    company
            from person
        """
        
        #--바인딩(튜플)
        
        #--실행
        cursor.execute(query)
        resultset = cursor.fetchall()
        
        #4.결과처리   리스트[(튜플),(튜플),(튜플)] --> 리스트[{딕션어리},{딕션어리},{딕션어리}]
        print(resultset)
        person_list = []
        for row in resultset:
            person_vo = {
                "person_id": row[0],    #person_id
                "name": row[1],         #name
                "hp": row[2],           #hp
                "company": row[3]       #company
            }
            person_list.append(person_vo)
        
        print(person_list)
        print(person_list[0]["name"])
    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        #5.자원정리
        if conn is not None:
            conn.close()

        if cursor is not None:
            cursor.close()

##########################################################################

# 실행
if __name__ == "__main__":
    get_person_list()

if __name__ == "__main__":
    add_person()

##########################################################################