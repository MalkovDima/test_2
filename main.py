import yandex_api



if __name__ == '__main__':
    # добавьте токен от яндекс диска:
    you_token_ya = ''
    uploader = yandex_api.YaUploader(you_token_ya)
  #  print(uploader.new_folder('333333'))
    print(uploader.find_for_name_folder('name_folder'))
  #  print(uploader.amount_folder('/'))






