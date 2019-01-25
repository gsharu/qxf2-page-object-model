"""
The class modeling the login page 
"""
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators

class Login_Page(Base_Page):
    "Class representation for the login page"
    USERNAME = locators.USERNAME 
    PASSWORD = locators.PASSWORD
    SUBMIT_BUTTON = locators.SUBMIT_BUTTON
    LOGOUT_LINK = locators.LOGOUT_LINK 

    def start(self):
        "The login page"
        url = "/"
        self.open(url)

    def login(self, username, password):
        "Login to the application" 
        result_flag = self.set_username(username)
        result_flag = result_flag & self.set_password(password)
        result_flag = result_flag & self.click_submit()
        #4. Verifies if login happened
        return result_flag

    def set_username(self,username):
        "Set the username field"
        result_flag = self.set_text(self.USERNAME,username)
        self.conditional_write(result_flag,
        positive='Set the username field to: %s'%username,
        negative='Failed to set the username field to: %s'%username,
        level='debug')
        
        return result_flag

    def set_password(self,password):
        "Set the password field"
        return True 

    def click_submit(self):
        "Click the submit button of the login form"
        return True 