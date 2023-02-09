import glob

first_file = []
for i, file_name in enumerate(glob.glob('*.txt')):
    with open(file_name, 'r') as f:
        if i == 0:
            for line in f.readlines():
                first_file.append(line)

        if i != 0:
            contain_user = False

            for username in first_file:
                all_followers = f.readlines()
                for follower in all_followers:
                    if follower == username:
                        contain_user = True

                if contain_user == False:
                    if len(all_followers) > len(first_file):
                        print("user " + username + "is now following you")

                    if len(all_followers) < len(first_file):
                        print("user " + username + "is no longer following you")