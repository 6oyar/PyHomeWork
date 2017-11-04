# -*- coding: utf-8 -*-
import vk

from time import sleep
from re import sub, findall
from getpass import getpass
from csv import writer, QUOTE_ALL


class User(object):

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.id = ''

    # аторизирует юзера
    def auth(self):
        session = vk.AuthSession(app_id='28867730', user_login=self.login, user_password=self.password)
        api = vk.API(session)
        return api

    # возвращает массив объектов друзей
    def friends(self, api):
        # возвращает в том порядке, в котором расположены в разделе Мои
        user_friends = api.friends.get(user_id=self.id, order='hints')
        return user_friends

    # возвращает количество друзей
    def friends_count(self, api):
        user_friends = User.friends(self, api)
        friends_count = len(user_friends)
        return friends_count

    # возвращает массив данных о юзере
    def info(self, api):
        user = api.users.get(user_id=self.id)
        return user[0]


def norm_mob(str):
    if len(str) != '':
        norm_mob = sub(r'(\s+)?[+]?[-]?', '', str)
        right_mob = findall(r'[\d]', norm_mob)
        if (len(right_mob) == len(norm_mob)) and (len(norm_mob) >= 10):
            return norm_mob
    else:
        return False


def find_correct_phone_numbers(api, friends, friends_count):
    users_phones = []
    for i in range(0, friends_count):
        cur_user_id = int(friends[i])
        cur_user = api.users.get(user_id=cur_user_id, fields='contacts')
        try:
            cur_mob = cur_user[0]['mobile_phone']
        except KeyError:
            sleep(0.3)
            continue
        mob = norm_mob(cur_mob)
        if mob:
            users_phones.append({
                'user_name': '{} {}'.format(cur_user[0]['first_name'], cur_user[0]['last_name']),
                'user_phone': '{}'.format(mob)
            })
        sleep(0.4)
    return users_phones


def saveCSV(data, path):
    with open(path, 'w') as csvfile:
        my_writer = writer(csvfile, delimiter='	', quotechar='"', quoting=QUOTE_ALL)
        my_writer.writerow(('Имя пользователя', 'Номер моб. телефона'))
        for item in data:
            try:
                my_writer.writerow((item['user_name'], item['user_phone']))
            except Exception:
                my_writer.writerow(('(Ошибка в кодировке)', item['user_phone']))


def main():
    while True:
        login = input('E-mail: ')
        password = getpass('Password: ')
        try:
            vk_user = User(login, password)
            api = vk_user.auth()
            print('Авторизация выполнена успешно!')
            break
        except Exception:
            print('Вы ввели неверные данные, пожалуйста, повторите попытку.')
    friends = vk_user.friends(api)
    friends_count = vk_user.friends_count(api)
    print('Найдено {} друзей.'.format(friends_count))
    print('Идет выборка мобильных номеров...')

    users_phones = find_correct_phone_numbers(api, friends, friends_count)
    print('Выборка окончена. Сохранение...')
    saveCSV(users_phones, 'vk_mob.csv')
    print('Данные успешно сохранены.')


if __name__ == '__main__':
    main()
