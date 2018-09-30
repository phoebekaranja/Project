import pyperclip
import unittest # Importing the unittest module
from socialAccounts import SocialAccounts

class TestSocialAccounts(unittest.TestCase):
    '''
    Test class that we define and test methods to use in the SocialAccount class
    '''
    def tearDown(self):
        '''
        this is to ensure each time the app is executed the list is clean
        '''
        SocialAccounts.social_accounts_list=[]

    def setUp(self):
        '''
        this setup method is run before each test case is executed
        '''
        self.new_social_account= SocialAccounts("facebook", "phoebe", "facebookPassword", "4") #creating the social account object

    def test_init(self):
        '''
        testing to ensure the social account object is initialized correctly
        '''
        self.assertEqual(self.new_social_account.social_account,"facebook")
        self.assertEqual(self.new_social_account.social_account_username,"phoebe")
        self.assertEqual(self.new_social_account.social_account_password,"facebookPassword")
        self.assertEqual(self.new_social_account.password_length,"4")


    def test_save_social_account(self):
        '''
        test case to see if the social account details are being saved to the list
        '''
        self.new_social_account.save_social_account() #saving the social account
        self.assertEqual(len(SocialAccounts.social_accounts_list),1)

    def test_save_multiple_social_account(self):
        '''
        test to check if we can save multiple social account details
        '''
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("video","phoebe", "passvideo", "4") #new account to save
        test_social_account.save_social_account()
        self.assertEqual(len(SocialAccounts.social_accounts_list),2)

    def test_delete_social_account(self):
        '''
        this is to ensure we can remove a social account from our list
        '''
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("video","phoebe", "passvideo", "4") #new account to save
        test_social_account.save_social_account()

        self.new_social_account.delete_social_account()
        self.assertEqual(len(SocialAccounts.social_accounts_list),1)

    def test_find_account_by_name(self):
        '''
        this is to enable users search their credentials by social account name e.g twitter and display the logins
        '''import pyperclip
import unittest # Importing the unittest module
from socialAccounts import SocialAccounts

class TestSocialAccounts(unittest.TestCase):
    '''
    Test class that we define and test methods to use in the SocialAccount class
    '''
    def tearDown(self):
        '''
        this is to ensure each time the app is executed the list is clean
        '''
        SocialAccounts.social_accounts_list=[]

    def setUp(self):
        '''
        this setup method is run before each test case is executed
        '''
        self.new_social_account= SocialAccounts("facebook", "phoebe", "facebookPassword", "4") #creating the social account object

    def test_init(self):
        '''
        testing to ensure the social account object is initialized correctly
        '''
        self.assertEqual(self.new_social_account.social_account,"facebook")
        self.assertEqual(self.new_social_account.social_account_username,"phoebe")
        self.assertEqual(self.new_social_account.social_account_password,"facebookPassword")
        self.assertEqual(self.new_social_account.password_length,"4")


    def test_save_social_account(self):
        '''
        test case to see if the social account details are being saved to the list
        '''
        self.new_social_account.save_social_account() #saving the social account
        self.assertEqual(len(SocialAccounts.social_accounts_list),1)

    def test_save_multiple_social_account(self):
        '''
        test to check if we can save multiple social account details
        '''
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("video","phoebe", "passvideo", "4") #new account to save
        test_social_account.save_social_account()
        self.assertEqual(len(SocialAccounts.social_accounts_list),2)

    def test_delete_social_account(self):
        '''
        this is to ensure we can remove a social account from our list
        '''
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("video","phoebe", "passvideo", "4") #new account to save
        test_social_account.save_social_account()

        self.new_social_account.delete_social_account()
        self.assertEqual(len(SocialAccounts.social_accounts_list),1)

    def test_find_account_by_name(self):
        '''
        this is to enable users search their credentials by social account name e.g twitter and display the logins
        '''
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("video","phoebe", "passvideo", "4") #new account to save
        test_social_account.save_social_account()

        found_social_account= SocialAccounts.find_account_by_name('video')
        self.assertEqual(found_social_account.social_account_username, test_social_account.social_account_username)

    def test_social_account_exists(self):
        '''
        we want to return a boolean if we cannot find a contact
        '''
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("video","phoebe", "passvideo", "4") #new account to save
        test_social_account.save_social_account()

        account_exists= SocialAccounts.social_account_exists("video")
        self.assertTrue(account_exists)

    def test_display_all_social_accounts(self):
        '''
        method to show all the saved social accounts
        '''
        self.assertEqual(SocialAccounts.display_social_accounts(), SocialAccounts.social_accounts_list)



    # def test_copy_username(self):
    #     '''
    #     Test to confirm we are copying the username from a found account
    #     '''
    #     self.new_social_account.save_social_account()
    #     SocialAccounts.copy_username("facebook")
    #
    #     self.assertEqual(self.new_social_account.social_account_username,pyperclip.paste())

if __name__=='__main__':
    unittest.main()
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("video","phoebe", "passvideo", "4") #new account to save
        test_social_account.save_social_account()

        found_social_account= SocialAccounts.find_account_by_name('video')
        self.assertEqual(found_social_account.social_account_username, test_social_account.social_account_username)

    def test_social_account_exists(self):
        '''
        we want to return a boolean if we cannot find a contact
        '''
        self.new_social_account.save_social_account()
        test_social_account = SocialAccounts("video","phoebe", "passvideo", "4") #new account to save
        test_social_account.save_social_account()

        account_exists= SocialAccounts.social_account_exists("video")
        self.assertTrue(account_exists)

    def test_display_all_social_accounts(self):
        '''
        method to show all the saved social accounts
        '''
        self.assertEqual(SocialAccounts.display_social_accounts(), SocialAccounts.social_accounts_list)



    # def test_copy_username(self):
    #     '''
    #     Test to confirm we are copying the username from a found account
    #     '''
    #     self.new_social_account.save_social_account()
    #     SocialAccounts.copy_username("facebook")
    #
    #     self.assertEqual(self.new_social_account.social_account_username,pyperclip.paste())

if __name__=='__main__':
    unittest.main()
