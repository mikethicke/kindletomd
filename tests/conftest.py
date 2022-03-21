"""
Setup and fixtures for pytest
"""

import pytest
import os

@pytest.fixture( scope = 'class' )
def file_paths( request ) :
    """
    Provide file names for various test data files.
    """
    base_test_data_path = os.path.join( os.path.dirname( __file__ ), 'test-data' )
    request.cls.file_paths = {
        'good'       : os.path.join( base_test_data_path, 'book-good.json' ),
        'bad-json'   : os.path.join( base_test_data_path, 'book-bad-json.json~' ),
        'not-kindle' : os.path.join( base_test_data_path, 'book-not-kindle.json' ),
        'not-json'   : os.path.join( base_test_data_path, 'book-not-json.xml' ),
    }

@pytest.fixture( scope = 'class' )
def test_data( request ) :
    """
    Provide test data with various attributes.
    """
    individual_highlights = {
        'just-highlight' : {
            "text"       : "Laborum officia ad magna pariatur id.",
            "isNoteOnly" : False,
            "location"   : {
              "url"   : "kindle://book?action=open&asin=A0A0A0A0A0&location=115",
              "value" : 115
            },
            "note"       : None
        },
        'highlight-and-note' : {
            "text": "Excepteur culpa elit voluptate qui nostrud cupidatat id culpa. Voluptate occaecat mollit velit duis sunt sint non proident voluptate tempor officia ex aute. Velit aliqua quis labore deserunt Lorem consectetur aliqua ipsum velit pariatur incididunt elit enim velit. Nisi aliqua amet ullamco exercitation Lorem excepteur.",
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "Aliquip id anim velit in."
        },
        'just-note' : {
            "text": "",
            "isNoteOnly": True,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=200",
                "value": 200
            },
            "note": "Elit non occaecat sit aliquip ullamco enim culpa est eiusmod ullamco labore."
        },
        'cyrillic' : {
            "text": "Лорем ипсум долор сит амет, видит децоре солеат дуо ин, сцаевола легендос хендрерит ин вим. Меа цасе цорпора делицата ад. Сед те нихил фуиссет, цу порро граецис фацилиси вел, еум путент сапиентем не! Цонгуе нонумы иус ад, меа те поссим.",
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "Cyrillic."
        },
        'japanese' : {
            "text": "育ぴくゅて住一ねりぼ医続ヤ検当関イホヱ流動イモ南更司テチレソ蜻載ルラサヨ交演む練研フを産7割ゅ応盗聞ぐぼレゆ済犬ルシナ送明曽膨ざす。断ずたざス退米だ速86属カチ県9海曲ーちは本者モタチル紹逮ロハスア本設ワス扱冷新ごあびド与芸ち伝傾ょ短和ラひ店食程配株刑ぼかに。音ホナマソ必商込寧リ会技れゅぐづ級育ろまくふ奥倉キラ込主エキ刺一ちば験覧メツ線69偉げレンま店2示りん権車丼さンれ。",
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "Japanese."   
        },
        'arabic' : {
            "text": "بعد ديسمبر الدولارات ثم, بل فكان وصغار اتفاقية حين. لعدم البشريةً ما دون, ذلك كانت أوراقهم انتصارهم أم. جعل وترك الباهضة مع. بعد وبعض مرمى كنقطة عل, كل حاول الطريق ولم.",
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "Arabic (RTL)."
        },
        'french' : {
            "text": "Lôrèm îpsùm dolor sit amet, apêrirï dëtraxît pêténtiûm pri êx, duô an œmnis rëpûdîaré. Sêa îd légendôs inçorrûpte. Nibh étiam èssënt èst no. Ad nâm simùl éfficiantur, séd àliî tâcîmatés éa. Est cû deleçtus êlaborarèt, illùm vêlït glorîatur ïn usû, séd tïbiqùê opôrtere évértitûr ea.",
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "French."
        },
        'punctuation' : {
            "text": "Lorem ipsum dolor sit amet, in duo labore suscipit indoctum, nostro verterem salutatus et vis. Ea sea quot consul, populo primis sententiae mei ne! No mei autem affert tincidunt, te clita phaedrum vix, pri oratio constituam ut! Vix facer mazim similique cu. Mea cibo nobis vocent cu, harum antiopam delicatissimi an usu? An vim harum dictas electram, cum et illum voluptua!",
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "Punctuation."
        },
        'empty' : {
            "text": "",
            "isNoteOnly": None,
            "location": {
                "url": "",
                "value": None
            },
            "note": ""
        },
        'missing-text' : {
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "Missing text highlight."
        },
        'missing-note' : {
            "text": "Lorem ipsum dolor sit amet, in duo labore suscipit indoctum, nostro verterem salutatus et vis. Ea sea quot consul, populo primis sententiae mei ne! No mei autem affert tincidunt, te clita phaedrum vix, pri oratio constituam ut! Vix facer mazim similique cu. Mea cibo nobis vocent cu, harum antiopam delicatissimi an usu? An vim harum dictas electram, cum et illum voluptua!",
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
        },
        'missing-location' : {
            "text": "Lorem ipsum dolor sit amet, in duo labore suscipit indoctum, nostro verterem salutatus et vis. Ea sea quot consul, populo primis sententiae mei ne! No mei autem affert tincidunt, te clita phaedrum vix, pri oratio constituam ut! Vix facer mazim similique cu. Mea cibo nobis vocent cu, harum antiopam delicatissimi an usu? An vim harum dictas electram, cum et illum voluptua!",
            "isNoteOnly": False,
            "note": "Punctuation."
        },
        'incorrect-note-only-true' : {
            "text": "Lorem ipsum dolor sit amet, in duo labore suscipit indoctum, nostro verterem salutatus et vis. Ea sea quot consul, populo primis sententiae mei ne! No mei autem affert tincidunt, te clita phaedrum vix, pri oratio constituam ut! Vix facer mazim similique cu. Mea cibo nobis vocent cu, harum antiopam delicatissimi an usu? An vim harum dictas electram, cum et illum voluptua!",
            "isNoteOnly": True,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "Punctuation."    
        },
        'incorrect-note-only-false' : {
            "text": "",
            "isNoteOnly": False,
            "location": {
                "url": "kindle://book?action=open&asin=A0A0A0A0A0&location=170",
                "value": 170
            },
            "note": "Punctuation."    
        },
        'not-kindle' : {
            "_id": "622353f3106eb7b36c745471",
            "index": 0,
            "guid": "3596b325-da02-461d-b381-ed541460a5e8",
            "email": "saundragregory@isosure.com",
            "phone": "+1 (858) 510-3457",
            "address": "820 Morgan Avenue, Indio, Delaware, 368",
            "about": "Nulla laboris consectetur dolor ad sunt irure incididunt. Voluptate veniam cillum cillum quis anim culpa anim irure commodo exercitation pariatur amet. Duis adipisicing est sit eiusmod aliqua aliquip ea consectetur reprehenderit. Minim consectetur sit Lorem do Lorem ut enim ut esse Lorem reprehenderit laboris. Exercitation deserunt minim tempor incididunt veniam ex exercitation. Cillum ut duis proident duis aute consequat tempor exercitation eu. Mollit et nulla voluptate adipisicing proident velit elit id voluptate sit qui esse.\r\n",
            "registered": "2017-09-29T04:56:27 +04:00",
            "latitude": 72.532592,
            "longitude": -8.773789,
            "tags": [
                "do",
                "nostrud",
                "commodo",
                "voluptate",
                "sit"
            ],
        },
    }
    all_highlights = individual_highlights.values()
    good_highlights = [
        individual_highlights['just-highlight'],
        individual_highlights['just-note'],
        individual_highlights['highlight-and-note'],
        individual_highlights['cyrillic'],
        individual_highlights['japanese'],
        individual_highlights['arabic'],
        individual_highlights['french'],
        individual_highlights['punctuation'],
    ]
    good_book = {
        'asin' : 'A0A0A0A0A0',
        "title": "A Book (With Parentheses)",
        "authors": "An Author, Another Author, and Third Author",
        'highlights' : good_highlights,
    }
    missing_asin = {
        "title": "A Book (With Parentheses)",
        "authors": "An Author, Another Author, and Third Author",
        'highlights' : good_highlights,
    }
    missing_title = {
        'asin' : 'A0A0A0A0A0',
        "authors": "An Author, Another Author, and Third Author",
        'highlights' : good_highlights,
    }
    missing_authors = {
        'asin' : 'A0A0A0A0A0',
        "title": "A Book (With Parentheses)",
        'highlights' : good_highlights,
    }
    missing_highlights = {
        'asin' : 'A0A0A0A0A0',
        "title": "A Book (With Parentheses)",
        "authors": "An Author, Another Author, and Third Author",
    }
    empty_highlights = {
        'asin' : 'A0A0A0A0A0',
        "title": "A Book (With Parentheses)",
        "authors": "An Author, Another Author, and Third Author",
        'highlights' : [],
    }
    bad_highlights = {
        'asin' : 'A0A0A0A0A0',
        "title": "A Book (With Parentheses)",
        "authors": "An Author, Another Author, and Third Author",
        'highlights' : all_highlights,
    }

    test_data = {
        'individual_highlights' : individual_highlights,
        'good_book'             : good_book,
        'missing_asin'          : missing_asin,
        'missing_title'         : missing_title,
        'missing_authors'       : missing_authors,
        'missing_highlights'    : missing_highlights,
        'empty_highlights'      : empty_highlights,
        'bad_highlights'        : bad_highlights
    }

    request.cls.test_data = test_data
