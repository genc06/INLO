import unittest
from password_generator import PasswordGenerator


class TestPwdGenerator(unittest.TestCase):

    def test_basic_pwd_only_strings_red(self):
        gen_pwd = PasswordGenerator()
        self.assertEqual(gen_pwd.generate_password(),"motdepasse")

    













if __name__ == '__main__':
    unittest.main()