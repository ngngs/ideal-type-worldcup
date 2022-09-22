from flask import Flask, render_template, jsonify, request, redirect, url_for
from bson import ObjectId
import requests
import jwt
import json
import datetime # 토큰에 만료시간을 주기 위해.
import hashlib # 해시함수를 통해 항상 256바이트 결과값 만들어줌
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://test:test@43.201.6.176',27017)
db = client.dbjungle_week00 # dbjungle_week00라는 이름의 db


@app.route('/')
def index(): 
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user_info = db.Users.find_one({"id": payload["id"]})
        return render_template('index.html', user_info=user_info)
    except jwt.ExpiredSignatureError :
        return render_template('index.html')
    except jwt.exceptions.DecodeError :
        return render_template('index.html')




# 회원가입
# 토큰 암호화, 복호화를 위한 키
SECRET_KEY = '2022JUNGLE'

@app.route('/signup')
def SignupPage():
   return render_template('SignUp.html')

@app.route('/signup', methods=['POST'])
def SignUp():
    # 1. 클라이언트로부터 데이터를 받기
    nickname_receive = request.form['nickname_give']  # 클라이언트로부터 받는 부분
    id_receive = request.form['id_give'] 
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest() # 해시함수 사용
    User = {'nickname': nickname_receive, 'id': id_receive, 'password': password_hash}

    # 2. mongoDB에 데이터를 넣기
    db.Users.insert_one(User)

    return jsonify({'result': 'success'})

# 회원가입 시 아이디 중복확인
@app.route('/check_dup', methods=['POST'])
def check_dup():
    id_check = request.form['id_give']
    exists = bool(db.Users.find_one({"id": id_check}))
    return jsonify({'result': 'success', 'exists': exists})

# 로그인
@app.route('/login')
def LoginPage():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def Login():
    loginid_receive = request.form['loginid_give']
    loginpw_receive = request.form['loginpw_give']
    loginpw_hash = hashlib.sha256(loginpw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된 pw를 통해 데이터조회
    result = db.Users.find_one({'id' : loginid_receive, 'password': loginpw_hash })

    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': loginid_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3000) # 3000초 후 자동 로그아웃
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token' : token})
        
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail'})

# 최초 화면 로딩
@app.route('/loadCard')
def loadCard():
    result = []
    worldcups = list(db.worldcup1.find({'info':True},{'_id':False}))
    for worldcup in worldcups:
        worldcup_id = worldcup['worldcup_id']
        info1 = list(db.worldcup1.find({'worldcup_id':worldcup_id, 'id_number':0},{'_id':False}))
        info2 = list(db.worldcup1.find({'worldcup_id':worldcup_id, 'id_number':1},{'_id':False}))
        result_dict = {
            'worldcup_id' : worldcup_id,
            'img_left' : info1[0]['url'],
            'name_left' : info1[0]['name'],
            'img_right' : info2[0]['url'],
            'name_right' : info2[0]['name'],
            'worldcup_title' : worldcup['title'],
            'worldcup_desc' : worldcup['desc']
        }
        result.append(result_dict)
    
    return jsonify({'result': 'success', 'worldcups': result})

# 월드컵 페이지
@app.route('/worldcup')
def worldcup():
    token_receive = request.cookies.get('mytoken')
    
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user_info = db.Users.find_one({"id": payload["id"]})
        return render_template('worldcup_page.html', user_info=user_info)
    except jwt.ExpiredSignatureError :
        return render_template('worldcup_page.html')
    except jwt.exceptions.DecodeError :
        return render_template('worldcup_page.html')

# 선택한 월드컵 가져오기
@app.route('/whichWorldcup', methods=['POST'])
def findWorldcup():
    worldcup_id = request.form['worldcup_id']
    data = list(db.worldcup1.find({'info':True, 'worldcup_id':worldcup_id},{'_id':False}))
    return jsonify({'result' : 'success', 'data' : data})

# 해당 월드컵 DB에서 일치하는 데이터 가져오기
@app.route('/worldcuppage', methods=['POST'])
def findDB():
    worldcup_id = request.form['worldcup_id']
    id_number = request.form['id_number']
    id_number = int(id_number)
    data = list(db.worldcup1.find({'worldcup_id':worldcup_id, 'id_number':id_number},{'_id':False}))
    return jsonify({'result' : 'success', 'data' : data})


# 월드컵 결과창으로 이동 시, 토큰 유지
@app.route('/result')
def result():
    token_receive = request.cookies.get('mytoken')
    
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user_info = db.Users.find_one({"id": payload["id"]},{'_id':False})
        user_info1 = json.dumps(user_info)
        return render_template('Result.html', user_info=user_info, user_info1=user_info1)
    except jwt.ExpiredSignatureError :
        return render_template('Result.html')
    except jwt.exceptions.DecodeError :
        return render_template('Result.html')




@app.route('/result/memo', methods=['POST'])
def comment_post():
    token_receive = request.cookies.get('mytoken')
    try:
        comment_receive = request.form['comment_give']
        worldcupid_receive = request.form['worldcupid_give']
        winner_receive = request.form['winner_give']
        cupresult1 = db.worldcup1.find_one({"worldcup_id" :  worldcupid_receive, "id_number" : int(winner_receive) })
        cupresult2 = db.worldcup1.find_one({"worldcup_id" :  worldcupid_receive})
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms='HS256')
        user_info = db.Users.find_one({"id": payload["id"]})
        comment_list = list(db.dbmemos.find({}, {'_id':False}))
        count = len(comment_list) + 1


        doc = {
            'num':count,
            'winner' : cupresult1['name'],
            'title' : cupresult2['title'],
            'comment': comment_receive,
            'done':0,
            'userNickname' : user_info['nickname'],
            'userId' : user_info['id']
        }



        db.dbmemos.insert_one(doc)

        return jsonify({'msg': '저장완료'})
    
    except:
        usernickname = "(익명)"
        comment_list = list(db.dbmemos.find({}, {'_id':False}))
        count = len(comment_list) + 1
        doc = {
            'num':count,
            'winner' : cupresult1['name'],
            'title' : cupresult2['title'],
            'comment': comment_receive,
            'done':0,
            'userNickname' : usernickname,
            'userId' : ''
        }
        db.dbmemos.insert_one(doc)

        return jsonify({'msg': '저장완료'})

# testing !!!!!!!
@app.route('/result/memotest', methods=['POST'])
def getting():
    client_id = request.form['id_info']
    comment_list = list(db.dbmemos.find({}))

    for comment in comment_list:
        comment['_id'] = str(comment['_id'])

        if client_id == comment['userId']:
            comment['myComment'] = True
        else:
            comment['myComment'] = False

    return jsonify({'dbmemos':comment_list})



@app.route('/result/memo', methods=['GET'])
def comment_get():
    comment_list = list(db.dbmemos.find({}, {'_id':False}))
    return jsonify({'dbmemos':comment_list})

@app.route('/result/memo/update', methods=['POST'])
def update_comment():
    upcomment_receive = request.form['num_givee']
    db.dbmemos.update_one({'num':int(upcomment_receive)},{'$set':{'done':1}})

    return jsonify({'result': 'success', 'msg': '수정되었습니다!'})

@app.route('/result/memo/edit', methods=['POST'])
def edit_comment():
    edit_comment_receive = request.form['edit_comment_give']
    id_receive = request.form['id_give']

    db.dbmemos.update_one({'_id':ObjectId(id_receive)},{'$set':{'comment':edit_comment_receive}})

    return jsonify({'result': 'success', 'msg': '수정되었습니다!'})

@app.route('/result/memo/delete', methods=['POST'])
def delete_comment():
    id_receive = request.form['id_give']
    db.dbmemos.delete_one({'_id':ObjectId(id_receive)})


    return jsonify({'result': 'success', 'msg': '삭제되었습니다!'})


if __name__ == '__main__':  
   app.run('0.0.0.0', port=5000, debug=True)