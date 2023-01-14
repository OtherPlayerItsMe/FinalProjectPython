import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")# абсолютный путь
connection = sqlite3.connect(db_path)

#connection = sqlite3.connect("profession.sqlite")

def relevanseQwery():
    keyProf = "(\"team lead\", \"тимлид\", \"тим лид\"" \
              ", \"teamlead\", \"lead\", \"руководит\"" \
              ", \"директор\", \"leader\", \"director\"" \
              ", \"начальник\", \"лидер\",\"управляющий проект\"" \
              ", \"керівник\", \"chief\", \"начальник it\")"
    query = "SELECT salary_from, salary_to, published_at " \
            + "FROM informationAboutProfession " \
            + "WHERE salary_currency = \"RUR\" " \
            + "AND name IN " + keyProf + ";"
    print(connection.execute(query))
    connection.close()

     #база с данными готова для использования, настраивалась в SQL Studio тк как ограничений не было
     #но выдает ошибку при запросе, выдает ошибку с тем что не находит таблицу в бд, я так и не разобрался
     #в чем заключается ошибка

if connection:
    print("соеденение с бд есть")
    relevanseQwery()
else:
    print("соеденение с бд нет")





