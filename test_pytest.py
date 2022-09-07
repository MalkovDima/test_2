import pytest
from yandex_api import YaUploader
#добавьте токен от яндекс диска:
you_token_ya = ""
uploader = YaUploader(you_token_ya)

test_name = 'name_folder'
#количество папок на яндекс диске
how_foldef = 5

def test_new_folder():
    assert uploader.new_folder(test_name) == 201

def test_find_for_name_folder():
    assert uploader.find_for_name_folder(test_name) == 200

def test_amount_folder():
    assert uploader.amount_folder('/') == how_foldef
