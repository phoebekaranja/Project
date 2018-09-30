import unittest # Importing the unittest module
from userAccounts import UserAccounts
# from socialAccounts import userAccounts

class TestUserAccounts(unittest.TestCase):
    def setUp(self):
        '''
        Function to help create user a/c details before each test
        '''
        self.new_user = UserAccounts("phoebe", "1998")

    def test_init_(self):
        '''
        Test to check creation of new user instance
        '''
        self.assertEqual(self.new_user.account_name, "phoebe")
        self.assertEqual(self.new_user.account_password, "1998")
        def test_save_account_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple account
            objects to our user_list
            '''
            self.new_contact.save_user()
            # test_contact = user("name","password) # new contact
            test_contact.save_user()
            self.assertEqual(len(User.user_list),2)


    def test_confirm_app_user(self):
        '''
        Function to confirm login details to current user
        '''
        self.new_user = UserAccounts("phoebe" ,"1998")
        self.new_user.save_user_account()
        test_user= UserAccounts("phoebe" ,"1998")
        test_user.save_user_account()
        active_user = UserAccounts.confirm_app_user("phoebe" ,"1998")
        self.assertTrue(active_user)


if __name__ == '__main__':
    unittest.main()
