
import random
import string

class PasswordGenerator:
    def generate_password(self, length=12):
        char = string.ascii_letters + string.digits + string.punctuation
        pwd = ''.join(random.choice(char) for _ in range(length))

        
        while pwd == self.previous_password:
            pwd = ''.join(random.choice(char) for _ in range(length))

        self.previous_password = pwd
        return pwd
    
    def generate_password_red(self):
        return " "
        
        
    def generate_password_green(self):
        return 'motdepasse'
    
    
    def robusterator_de_mot_de_passe_red(self):
        return 'motdepasse'
        
    def robusterator_de_mot_de_passe_green(self):
        mdp_sans = "motdepasse"
        # chiffre = "3"
        # mdp_avec = mdp_sans + chiffre
        # return mdp_sans + chiffre
        return 'motdepasse3'
    
    def mot_de_passe_plus_robuste_red(self):
        mdp_sans = "motdepasse"
        chiffre = "3"
        mdp_avec = mdp_sans + chiffre
        return mdp_avec
    
    def mot_de_passe_plus_robuste_green(self):
        mdp_sans = "motdepasse"
        chiffre = "3"
        mdp_avec = mdp_sans.capitalize + chiffre
        return mdp_avec
    
    def mdp_encore_plus_robuste_red(self):
        mdp_sans = "motdepasse"
        chiffre = "3"
        char = ""
        #mdp_robuste = char + mdp_sans.capitalize() + chiffre 
        return char + mdp_sans.capitalize() + chiffre 
    
    def mdp_encore_plus_robuste_green(self):
        mdp_sans = "motdepasse"
        chiffre = "3"
        char = "@"
        #mdp_robuste = char + mdp_sans.capitalize() + chiffre 
        return char + mdp_sans.capitalize() + chiffre 
    
    def combinaison_pwd_complexe(self):
        lettres = string.ascii_letters
        nums = string.digits
        special_char = "@#$%^&*()_+=-<>?!"
        all_chars = lettres + nums + special_char
        lng_spec = random.randint(10, 15)  
        complex_pwd = ''.join(random.choice(all_chars) for _ in range(lng_spec))
        return complex_pwd

    def check_complexity(self, password):
    
        return any(char.isdigit() for char in password) \
            and any(char.isupper() for char in password) \
            and any(char in "@#$%^&*()_+=-<>?!" for char in password)