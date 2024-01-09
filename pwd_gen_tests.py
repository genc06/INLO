import unittest
from password_generator import PasswordGenerator


class TestPwdGenerator(unittest.TestCase):

    def test_basic_pwd_only_strings(self):
        gen_pwd = PasswordGenerator()
        self.assertEqual(gen_pwd.generate_password(),"motdepasse")

    def test_basic_pwd_strings_n_numbers(self):
        gen_pwd = PasswordGenerator()
        self.assertEqual(gen_pwd.robusterator_de_mot_de_passe(),"motdepasse3") 
    def test_basic_pwd_strings_n_numbers(self):
        gen_pwd = PasswordGenerator()
        self.assertEqual(gen_pwd.mot_de_passe_plus_robuste(),"Motdepasse3")













if __name__ == '__main__':
    unittest.main()