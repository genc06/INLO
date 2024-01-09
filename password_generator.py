




class PasswordGenerator:

    
    def generate_password(self):
        # return " "
        return 'motdepasse'
        # /refactor moment/
        # return robusterator_de_mot_de_passe()
        
    def robusterator_de_mot_de_passe(self):
        # return "motdepasse3"
        mdp_sans = "motdepasse"
        chiffre = "3"
        # mdp_avec = mdp_sans + chiffre
        return mdp_sans + chiffre
    
    def mot_de_passe_plus_robuste(self):
        mdp_sans = "motdepasse"
        chiffre = "3"
        # mdp_avec = mdp_sans.capitalize() + chiffre
        return mdp_sans.capitalize() + chiffre

    def mdp_encore_plus_robuste(self)
        mdp_sans = "motdepasse"
        chiffre = "3"
        char = "@"
        #mdp_robuste = char + mdp_sans.capitalize() + chiffre 
        return char + mdp_sans.capitalize() + chiffre 