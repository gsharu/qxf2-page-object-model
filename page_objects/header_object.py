"""
This class models the Qxf2 Trainer's header as a Page Object.
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Header_Object():
    "Page Object for the header class"

    #locators
    LOGOUT_LINK = locators.LOGOUT_LINK
    USERNAME = locators.USERNAME

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def logout(self):
        "Click on the logout link"
        result_flag = self.click_element(self.LOGOUT_LINK)
        self.conditional_write(result_flag,
        positive='Clicked on the logout link',
        negative='Could not click on the logout link',
        level='debug')
        result_flag &= self.check_element_present(self.USERNAME)

        return result_flag