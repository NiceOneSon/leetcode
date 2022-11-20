def solution(id_pw, db):
    for row in db:
        if row == id_pw:
            return "login"
        elif row[0] == id_pw[0]:
            return "wrong pw"
        
    return "fail"
    