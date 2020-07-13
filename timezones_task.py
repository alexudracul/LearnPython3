from pytz import timezone
from datetime import datetime

timezone_dict = {
    'AU': ('Australia', 'Australia/Melbourne'),
    'BY': ('Belarus', 'Europe/Minsk'),
    'CH': ('Switzerland', 'Europe/Zurich'),
    'CU': ('Cuba', 'America/Havana'),
    'DE': ('Germany', 'Europe/Berlin'),
    'EG': ('Egypt', 'Africa/Cairo'),
    'ES': ('Spain', 'Europe/Madrid'),
    'QA': ('Qatar', 'Asia/Qatar'),
    'RU': ('Russia', 'Europe/Moscow'),
    'UA': ('Ukraine', 'Europe/Kiev')
}


for key in timezone_dict:
    print(key, timezone_dict[key])

print('Please enter a two-letter code of the country to choose the timezone or "q" to quit: ')

while True:
    user_input = input()
    country_code = str(user_input).upper()
    if user_input == 'q':
        break
    if country_code in timezone_dict.keys():
        tz = timezone(timezone_dict[country_code][1])
        print('Local time is', datetime.now(tz=tz))
        print('UTC time is', datetime.utcnow())
    else:
        print('Please try again: ')
        continue
