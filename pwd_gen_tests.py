import unittest
from password_generator import PasswordGenerator


class TestPwdGenerator(unittest.TestCase):

    def test_basic_pwd_only_strings(self):
        gen_pwd = PasswordGenerator()
        self.assertEqual(gen_pwd.generate_password(),"motdepasse")

    def test_basic_pwd_strings_n_numbers(self):
        gen_pwd = PasswordGenerator()
        self.assertEqual(gen_pwd.robusterator_de_mot_de_passe(),"motdepasse3") 

    def test_basic_pwd_strings_n_numbers_caps(self):
        gen_pwd = PasswordGenerator()
        self.assertEqual(gen_pwd.mot_de_passe_plus_robuste(),"Motdepasse3")

    def test_generate_different_passwords_successively(self):
        gen_pwd = PasswordGenerator()
        pwd1 = gen_pwd.generate_password()
        pwd2 = gen_pwd.generate_password()
        self.assertNotEqual(pwd1, pwd2)

    def test_generate_complex_password_with_special_chars(self):
        gen_pwd = PasswordGenerator()
        complex_pwd = gen_pwd.combinaison_pwd_complexe()
        self.assertTrue(self.check_complexity(complex_pwd))

    def test_generate_unique_complex_passwords_successively(self):
        gen_pwd = PasswordGenerator()
        complex_pwd1 = gen_pwd.combinaison_pwd_complexe()
        complex_pwd2 = gen_pwd.combinaison_pwd_complexe()
        self.assertNotEqual(complex_pwd1, complex_pwd2)












if __name__ == '__main__':
    unittest.main()