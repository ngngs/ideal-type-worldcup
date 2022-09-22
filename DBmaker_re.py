from pymongo import MongoClient

client = MongoClient('mongodb://test:test@43.201.6.176',27017)
db = client.dbjungle_week00


info = {
    'info' : True,
    'title' : '우리 동네 맛집 월드컵',
    'desc' : '전민동의 맛집을 찾아서!',
    'worldcup_id' : 'food'
}

doc = [
    {
        'id_number' : 0,
        'name' : '국영수떡볶이',
        'url' : 'static/images/food/food1.jfif',
        'worldcup_id' : 'food'
    },

    {
        'id_number' : 1,
        'name' : '화목한우리집',
        'url' : 'static/images/food/food2.jfif',
        'worldcup_id' : 'food'
    },

    {
        'id_number' : 2,
        'name' : '곱이곱다',
        'url' : 'static/images/food/food3.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 3,
        'name' : '고고짬뽕',
        'url' : 'static/images/food/food4.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 4,
        'name' : '플레이버거',
        'url' : 'static/images/food/food5.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 5,
        'name' : '한우곰탕',
        'url' : 'static/images/food/food6.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 6,
        'name' : '어니언키친',
        'url' : 'static/images/food/food7.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 7,
        'name' : '광세족발',
        'url' : 'static/images/food/food8.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 8,
        'name' : '한방삼계탕',
        'url' : 'static/images/food/food9.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 9,
        'name' : '심스스모크하우스',
        'url' : 'static/images/food/food10.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 10,
        'name' : '스시안',
        'url' : 'static/images/food/food11.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 11,
        'name' : '라멘히로시',
        'url' : 'static/images/food/food12.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 12,
        'name' : '제주진고기국수',
        'url' : 'static/images/food/food13.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 13,
        'name' : '우촌면옥',
        'url' : 'static/images/food/food14.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 14,
        'name' : '서민대패',
        'url' : 'static/images/food/food15.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 15,
        'name' : '전민한우',
        'url' : 'static/images/food/food16.jfif',
        'worldcup_id' : 'food'
    }
]

db.worldcup1.insert_one(info)

for i in range(len(doc)):
    db.worldcup1.insert_one(doc[i])

info = {
    'info' : True,
    'title' : '가고싶은 회사 월드컵',
    'desc' : '최고의 회사를 찾아서!',
    'worldcup_id' : 'company'
}

doc = [
    {
        'id_number' : 0,
        'name' : '네이버',
        'url' : 'static/images/company/company1.jpg',
        'worldcup_id' : 'company'
    },

    {
        'id_number' : 1,
        'name' : '라인',
        'url' : 'static/images/company/company2.jpg',
        'worldcup_id' : 'company'
    },

    {
        'id_number' : 2,
        'name' : '펍지',
        'url' : 'static/images/company/company3.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 3,
        'name' : '배민',
        'url' : 'static/images/company/company4.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 4,
        'name' : '스파르타코딩클럽',
        'url' : 'static/images/company/company5.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 5,
        'name' : '당근마켓',
        'url' : 'static/images/company/company6.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 6,
        'name' : '야놀자',
        'url' : 'static/images/company/company7.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 7,
        'name' : '업비트',
        'url' : 'static/images/company/company8.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 8,
        'name' : '직방',
        'url' : 'static/images/company/company9.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 9,
        'name' : '채널톡',
        'url' : 'static/images/company/company10.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 10,
        'name' : '카카오',
        'url' : 'static/images/company/company11.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 11,
        'name' : '코드브릭',
        'url' : 'static/images/company/company12.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 12,
        'name' : '쿠팡',
        'url' : 'static/images/company/company13.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 13,
        'name' : '크래프톤',
        'url' : 'static/images/company/company14.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 14,
        'name' : '토스',
        'url' : 'static/images/company/company15.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 15,
        'name' : '트루밸런스',
        'url' : 'static/images/company/company16.jpg',
        'worldcup_id' : 'company'
    }
]

db.worldcup1.insert_one(info)

for i in range(len(doc)):
    db.worldcup1.insert_one(doc[i])

info = {
    'info' : True,
    'title' : '주류 월드컵',
    'desc' : '최고의 주류를 찾아서!',
    'worldcup_id' : 'alcohol'
}

doc = [
    {
        'id_number' : 0,
        'name' : '기린이치방',
        'url' : 'static/images/Alcohol/Alcohol1.jpg',
        'worldcup_id' : 'alcohol'
    },

    {
        'id_number' : 1,
        'name' : '대선',
        'url' : 'static/images/Alcohol/Alcohol2.jfif',
        'worldcup_id' : 'alcohol'
        
    },

    {
        'id_number' : 2,
        'name' : '발렌타인',
        'url' : 'static/images/Alcohol/Alcohol3.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 3,
        'name' : '버드와이져',
        'url' : 'static/images/Alcohol/Alcohol4.jfif',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 4,
        'name' : '아사히',
        'url' : 'static/images/Alcohol/Alcohol5.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 5,
        'name' : '연태고량주',
        'url' : 'static/images/Alcohol/Alcohol6.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 6,
        'name' : '조니워커',
        'url' : 'static/images/Alcohol/Alcohol7.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 7,
        'name' : '좋은데이',
        'url' : 'static/images/Alcohol/Alcohol8.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 8,
        'name' : '진로',
        'url' : 'static/images/Alcohol/Alcohol9.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 9,
        'name' : '참이슬',
        'url' : 'static/images/Alcohol/Alcohol10.png',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 10,
        'name' : '처음처럼',
        'url' : 'static/images/Alcohol/Alcohol11.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 11,
        'name' : '청하',
        'url' : 'static/images/Alcohol/Alcohol12.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 12,
        'name' : '칭다오',
        'url' : 'static/images/Alcohol/Alcohol13.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 13,
        'name' : '카스',
        'url' : 'static/images/Alcohol/Alcohol14.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 14,
        'name' : '테라',
        'url' : 'static/images/Alcohol/Alcohol15.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 15,
        'name' : '화요',
        'url' : 'static/images/Alcohol/Alcohol16.jpg',
        'worldcup_id' : 'alcohol'
    }
]

db.worldcup1.insert_one(info)

for i in range(len(doc)):
    db.worldcup1.insert_one(doc[i])

info = {
    'info' : True,
    'title' : '우리 동네 커피집 월드컵',
    'desc' : '최고의 커피를 찾아서!',
    'worldcup_id' : 'coffe'
}

doc = [
    {
        'id_number' : 0,
        'name' : '랩플레이스',
        'url' : 'static/images/coffecup/coffecup1.jfif',
        'worldcup_id' : 'coffe'
    },

    {
        'id_number' : 1,
        'name' : '리본커피',
        'url' : 'static/images/coffecup/coffecup2.jfif',
        'worldcup_id' : 'coffe'
    },

    {
        'id_number' : 2,
        'name' : '메가커피',
        'url' : 'static/images/coffecup/coffecup3.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 3,
        'name' : '스타벅스',
        'url' : 'static/images/coffecup/coffecup4.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 4,
        'name' : '연하커피',
        'url' : 'static/images/coffecup/coffecup5.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 5,
        'name' : '온유',
        'url' : 'static/images/coffecup/coffecup6.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 6,
        'name' : '이디야',
        'url' : 'static/images/coffecup/coffecup7.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 7,
        'name' : '커피가',
        'url' : 'static/images/coffecup/coffecup8.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 8,
        'name' : '커피디자인',
        'url' : 'static/images/coffecup/coffecup9.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 9,
        'name' : '커피라운지',
        'url' : 'static/images/coffecup/coffecup10.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 10,
        'name' : '커피커피',
        'url' : 'static/images/coffecup/coffecup11.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 11,
        'name' : '커피포터',
        'url' : 'static/images/coffecup/coffecup12.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 12,
        'name' : '크리미스윗',
        'url' : 'static/images/coffecup/coffecup13.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 13,
        'name' : '14_할리스',
        'url' : 'static/images/coffecup/coffecup14.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 14,
        'name' : '모리스커피',
        'url' : 'static/images/coffecup/coffecup15.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 15,
        'name' : '더리터',
        'url' : 'static/images/coffecup/coffecup16.jfif',
        'worldcup_id' : 'coffe'
    }
]

db.worldcup1.insert_one(info)

for i in range(len(doc)):
    db.worldcup1.insert_one(doc[i])



