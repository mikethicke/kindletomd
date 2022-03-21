"""
Unit tests for kindle_to_md.py | parse_single_entry()
"""

import pytest

from kindle_to_md import single_entry_to_md
from kindle_to_md import MisformattedKindleData

@pytest.mark.usefixtures( 'test_data' )
class TestSingleEntryToMd :
    def test_just_highlight( self ) :
        markdown = single_entry_to_md( self.test_data['individual_highlights']['just-highlight'] )
        assert( markdown == '- Laborum officia ad magna pariatur id. ([115](kindle://book?action=open&asin=A0A0A0A0A0&location=115))\n')

    def test_highlight_and_note( self ) :
        markdown = single_entry_to_md( self.test_data['individual_highlights']['highlight-and-note'] )
        assert( markdown == '- Excepteur culpa elit voluptate qui nostrud cupidatat id culpa. Voluptate occaecat mollit velit duis sunt sint non proident voluptate tempor officia ex aute. Velit aliqua quis labore deserunt Lorem consectetur aliqua ipsum velit pariatur incididunt elit enim velit. Nisi aliqua amet ullamco exercitation Lorem excepteur. ([170](kindle://book?action=open&asin=A0A0A0A0A0&location=170))\n    - Note: Aliquip id anim velit in.\n')

    def test_just_note( self ) :
        markdown = single_entry_to_md( self.test_data['individual_highlights']['just-note'] )
        assert( markdown == '- Note: Elit non occaecat sit aliquip ullamco enim culpa est eiusmod ullamco labore. ([200](kindle://book?action=open&asin=A0A0A0A0A0&location=200))\n')

    def test_cyrillic( self ) :
        markdown = single_entry_to_md( self.test_data['individual_highlights']['cyrillic'] )
        assert( markdown == '- Лорем ипсум долор сит амет, видит децоре солеат дуо ин, сцаевола легендос хендрерит ин вим. Меа цасе цорпора делицата ад. Сед те нихил фуиссет, цу порро граецис фацилиси вел, еум путент сапиентем не! Цонгуе нонумы иус ад, меа те поссим. ([170](kindle://book?action=open&asin=A0A0A0A0A0&location=170))\n    - Note: Cyrillic.\n')
    
    def test_japanese( self ) :
        markdown = single_entry_to_md( self.test_data['individual_highlights']['japanese'] )
        assert( markdown == '- 育ぴくゅて住一ねりぼ医続ヤ検当関イホヱ流動イモ南更司テチレソ蜻載ルラサヨ交演む練研フを産7割ゅ応盗聞ぐぼレゆ済犬ルシナ送明曽膨ざす。断ずたざス退米だ速86属カチ県9海曲ーちは本者モタチル紹逮ロハスア本設ワス扱冷新ごあびド与芸ち伝傾ょ短和ラひ店食程配株刑ぼかに。音ホナマソ必商込寧リ会技れゅぐづ級育ろまくふ奥倉キラ込主エキ刺一ちば験覧メツ線69偉げレンま店2示りん権車丼さンれ。 ([170](kindle://book?action=open&asin=A0A0A0A0A0&location=170))\n    - Note: Japanese.\n')
    
    def test_arabic( self ) :
        markdown = single_entry_to_md( self.test_data['individual_highlights']['arabic'] )
        assert( markdown == '- بعد ديسمبر الدولارات ثم, بل فكان وصغار اتفاقية حين. لعدم البشريةً ما دون, ذلك كانت أوراقهم انتصارهم أم. جعل وترك الباهضة مع. بعد وبعض مرمى كنقطة عل, كل حاول الطريق ولم. ([170](kindle://book?action=open&asin=A0A0A0A0A0&location=170))\n    - Note: Arabic (RTL).\n')
    
    def test_french( self ) :
        markdown = single_entry_to_md( self.test_data['individual_highlights']['french'] )
        assert( markdown == '- Lôrèm îpsùm dolor sit amet, apêrirï dëtraxît pêténtiûm pri êx, duô an œmnis rëpûdîaré. Sêa îd légendôs inçorrûpte. Nibh étiam èssënt èst no. Ad nâm simùl éfficiantur, séd àliî tâcîmatés éa. Est cû deleçtus êlaborarèt, illùm vêlït glorîatur ïn usû, séd tïbiqùê opôrtere évértitûr ea. ([170](kindle://book?action=open&asin=A0A0A0A0A0&location=170))\n    - Note: French.\n')
    
    def test_punctuation( self ) :
        markdown = single_entry_to_md( self.test_data['individual_highlights']['punctuation'] )
        assert( markdown == '- Lorem ipsum dolor sit amet, in duo labore suscipit indoctum, nostro verterem salutatus et vis. Ea sea quot consul, populo primis sententiae mei ne! No mei autem affert tincidunt, te clita phaedrum vix, pri oratio constituam ut! Vix facer mazim similique cu. Mea cibo nobis vocent cu, harum antiopam delicatissimi an usu? An vim harum dictas electram, cum et illum voluptua! ([170](kindle://book?action=open&asin=A0A0A0A0A0&location=170))\n    - Note: Punctuation.\n')

    def test_empty( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = single_entry_to_md( self.test_data['individual_highlights']['empty'] )
    
    def test_missing_text( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = single_entry_to_md( self.test_data['individual_highlights']['missing-text'] )
    
    def test_missing_note( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = single_entry_to_md( self.test_data['individual_highlights']['missing-note'] )
    
    def test_missing_location( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = single_entry_to_md( self.test_data['individual_highlights']['missing-location'] )
    
    def test_incorrect_note_only_true( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = single_entry_to_md( self.test_data['individual_highlights']['incorrect-note-only-true'] )

    def test_not_kindle( self ) :
        with pytest.raises( MisformattedKindleData ) :
            markdown = single_entry_to_md( self.test_data['individual_highlights']['not-kindle'] )
