from cryptography.fernet import Fernet
class PasswordManager:
    def __init__(self):
        self.key = None
        self.pw_file = None
        self.pw_dict = {}
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)
    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()
    def create_pw_file(self, path, initial_values= None):
        self.pw_file = path
        if initial_values is not None:
            for key, values in initial_values.items():
                self.add_pw(key, values)
    def load_pw_file(self, path):
        self.pw_file = path
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(': ')
                self.pw_dict[site] = Fernet(self.key).decrypt(encrypted.encode('utf-8')).decode('utf-8')
    def add_pw(self, site, password):
        self.pw_dict[site] = password
        
        if self.pw_file is not None:
            with open(self.pw_file , 'a') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                enc_hex = encrypted.hex()
                f.write(site + ':' + enc_hex +"\n")
    def get_pw(self, site):
        return self.pw_dict[site]

def main():
    password = {
        "kdrilkr@hotmail": "ilker2122",
        "instagram": "ilker2122",
        "github": "Ilker2122"
    }
    pm = PasswordManager()
    print("""What do you want to do?
    (1) Create New Key
    (2) Load Existing Key
    (3) Create New Password File
    (4) Load Existing Password File
    (5) Add New Password
    (6) Get a Password
    """)

    done = False
    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter Path:")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter Path:")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter Path: ")
            pm.create_pw_file(path, password)
        elif choice == "4":
            path = input("Enter Path: ")
            pm.load_pw_file(path)
        elif choice == "5":
            site = input("Enter Site: ")
            password = input("Enter the Password: ")
            pm.add_pw(site, password)
        elif choice == "6":
            site = input("Enter Site: ")
            print(f"Password for {site} is {pm.get_pw(site)}")
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
