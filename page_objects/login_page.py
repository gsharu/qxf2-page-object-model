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
        result_flag &= self.set_password(password)
        result_flag &= self.click_submit()
        #Verifies if login happened
        logout_link_present = self.check_element_present(self.LOGOUT_LINK)  
        result_flag &= logout_link_present
        if logout_link_present:
            self.switch_page('Tutorials page')

        return result_flag

    @Wrapit._screenshot
    def set_username(self,username):
        "Set the username field"
        result_flag = self.set_text(self.USERNAME,username)
        self.conditional_write(result_flag,
        positive='Set the username field to: %s'%username,
        negative='Could not set the username field to: %s'%username,
        level='debug')
        
        return result_flag

    @Wrapit._screenshot
    def set_password(self,password):
        "Set the password field"
        result_flag = self.set_text(self.PASSWORD,password)
        self.conditional_write(result_flag,
        positive='Set the password',
        negative='Could not set the password',
        level='debug')

        return result_flag

    @Wrapit._screenshot
    def click_submit(self):
        "Click the submit button of the login form"
        result_flag = self.click_element(self.SUBMIT_BUTTON)
        self.conditional_write(result_flag,
        positive='Clicked the submit button',
        negative='Could not click the submit button',
        level='debug')

        return result_flag