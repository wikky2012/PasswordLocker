import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User('Wycliffe','Ronoh')

    def test_init(self):
        
        self.assertEqual(self.new_user.username,'Wycliffe')
        self.assertEqual(self.new_user.password,'Ronoh')
        
    def test_save_user(self):
        
        self.new_user.save_created_credential() 
        self.assertEqual(len(User.user_list),1)  

if __name__ == '__main__':
    unittest.main()