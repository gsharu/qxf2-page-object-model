"""
This is a simple test we wrote to demo using Qxf2's automation framework.
In this test, we will:
* Visit base url (e.g.: http://qxf2trainer.pythonanywhere.com)
* Login
* Click the logout link
"""

import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.login_logout_conf as conf


def test_login_logout(base_url,browser,browser_version,os_version,os_name,remote_flag):
    "The login and logout test"
    #try:
    if True:
        expected_pass = 0
        actual_pass = -1
        test_obj = PageFactory.get_page_object("Login Page",base_url=base_url)
        test_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,None,None)
        result_flag = test_obj.login(conf.USERNAME,conf.PASSWORD)
        test_obj.log_result(result_flag,
                            positive="Successfully logged into the application",
                            negative="Failed to login to the application")
        
    """
    except Exception,e:
        print "Exception when trying to run test:%s"%__file__
        print "Python says:%s"%str(e)
    """

    assert expected_pass == actual_pass

#---START OF SCRIPT
if __name__=='__main__':
    print ("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        test_login_logout(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag) 
    else:
        print ('ERROR: Received incorrect comand line input arguments')
        print (option_obj.print_usage())