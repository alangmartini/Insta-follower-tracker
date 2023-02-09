import glob
import os

first_file = []
files = glob.glob('*.txt')
files.sort(key=lambda x: os.stat(x).st_ctime)


for i, file_name in enumerate(glob.glob('*.txt')):
    with open(file_name, 'r', encoding="utf-8") as f:
        if i == 0:
            for line in f.readlines():
                first_file.append(line)
            continue

        CONTAIN_USER = False

        for username in first_file:
            all_followers = f.readlines()
            for follower in all_followers:
                if follower == username:
                    CONTAIN_USER = True

            if CONTAIN_USER is False:
                if len(all_followers) > len(first_file):
                    print("user " + username + "is now following you")
                    continue

                print("user " + username + "is no longer following you")
