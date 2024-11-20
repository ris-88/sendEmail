import smtplib

text = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

website = "https://dvmn.org/referrals/Bi0LsR0LqmTYcz1YYdI4tboUe89XxRjXwwK4vR9x/"
friend_name = "Девман"
my_name = "Илья"
my_email = "devmanorg@yandex.ru"
friends_email = "rozanov.i88@yandex.ru"

text = text.replace("%website%", website)
text = text.replace("%friend_name%", friend_name)
text = text.replace("%my_name%", my_name)

letter = f"""\
From: {my_email}
To: {friends_email}
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";

{text}
"""

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.com', 465)
server.login(my_email)
server.sendmail(my_email, friends_email, letter)
server.quit()
