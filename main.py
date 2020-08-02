# -*- coding: utf8 -*-
# "629e71edb6a4aee08321b5be85fc2a19f37324c1f800a7fc8d0e262e1449906728e8f168ad2e68c54c281"
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
"!!!"
about = """
Студенческий педагогический отряд (СПО) «Бриз» - это объединение активных студентов. Основной деятельностью отряда является летняя работа в детских лагерях в качестве вожатых. Так же «Бриз» принимает активное участие в жизни студенческих отрядов Нижегородской области и в жизни университета. В учебный период отряд занимается волонтерской деятельностью, осуществляет социальные проекты городского уровня, участвует в студенческих слётах, фестивалях, школах актива по всей России. 
"""

history = """
Отряд «Бриз» был основан 17 апреля 2004 года. У истоков отряда стоят активисты университета, а именно: Кувшинов Александр и Сутягина Анастасия. Отряд «Бриз» является первым отрядом ФГБОУ ВО «ВГУВТ».
"""

why_breeze = """
Название «Бриз» выбрано не случайно: поскольку каждый из новоиспеченного отряда любил свой вуз, то при выборе названия для отряда, никто не сомневался в связи с морем. Морской бриз всегда остается лучшим воспоминанием с отдыха, потому, на первом же собрании, было единогласно выбрано название для отряда – «Бриз»."""
vk_obj = vk_api.VkApi(token='629e71edb6a4aee08321b5be85fc2a19f37324c1f800a7fc8d0e262e1449906728e8f168ad2e68c54c281')

longpoll = VkLongPoll(vk_obj)
keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Что такое Бриз?', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button('История Отряда', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Почему Бриз?', color=VkKeyboardColor.PRIMARY)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    request = event.text
                    if request == "Начать":
                        user = vk_obj.method("users.get", {"user_ids": event.user_id})
                        vk_obj.method("messages.send", {
                            "peer_id": event.user_id,
                            "message": f'Привет, {user[0]["first_name"]}! Добро пожаловать в группу СПО "Бриз"! Выбери, что тебя интересует.',
                            "random_id": random.randint(0, 2048),
                            "keyboard": keyboard.get_keyboard()})
                    
                    elif request == 'Что такое Бриз?':
                        vk_obj.method("messages.send", {
                            "peer_id": event.user_id,
                            "message": about,
                            "attachment": "photo-71065561_384351105",
                            "random_id": random.randint(0, 2048),
                            "keyboard": keyboard.get_keyboard()})
                    
                    elif request == 'История Отряда':
                        vk_obj.method("messages.send", {
                            "peer_id": event.user_id,
                            "message": history,
                            "attachment": "photo-71065561_328888753",
                            "random_id": random.randint(0, 2048),
                            "keyboard": keyboard.get_keyboard()})
                    
                    elif request == 'Почему Бриз?':
                        vk_obj.method("messages.send", {
                            "peer_id": event.user_id,
                            "message": why_breeze,
                            "attachment": "photo-71065561_343076478",
                            "random_id": random.randint(0, 2048),
                            "keyboard": keyboard.get_keyboard()})

                    else:
                        vk_obj.method("messages.send", {"peer_id": event.user_id, "message": "Извини, я тебя не понял, напиши еще раз!", "random_id": random.randint(0, 2048)})