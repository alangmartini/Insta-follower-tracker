import time
import instaloader

o = instaloader.instaloader.Instaloader()

USERNAME = 'your_username_here'
PASSWORD = 'your_password_here'

o.login(user=USERNAME, passwd=PASSWORD)

profile = instaloader.Profile.from_username(o.context, username=USERNAME)

followers = profile.get_followers()
current_day_arr = time.ctime().split(' ')
CURRENT_DAY_NAME = '-'.join(current_day_arr) + '.txt'

with open(CURRENT_DAY_NAME, 'w', encoding='utf-8') as file:
    for fol in followers:
        file.write(fol.username + '\n')
