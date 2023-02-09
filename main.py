import instaloader
import time

o = instaloader.instaloader.Instaloader()

username = 'your_username_here'
password = 'your_password_here'

o.login(user=username, passwd=password)

profile = instaloader.Profile.from_username(o.context, username=username)

followers = profile.get_followers()
current_day_arr = time.ctime().split(' ')
current_day_name = '-'.join(current_day_arr) + '.txt'

file = open(current_day_name, 'w')

for fol in followers:
  file.write(fol.username + '\n')
