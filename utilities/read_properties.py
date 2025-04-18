import configparser
"""
Ease of Use: Configuration files are simpler to maintain than hardcoded values in scripts.
Flexibility: You can separate configuration from code, improving maintainability.
Cross-Platform: .ini files are widely used and compatible with most systems.
"""
# Create a ConfigParser instance
config = configparser.RawConfigParser()
# Read the .ini file
"""
Verify File Path: Double-check that 
you are reading the correct file and that it contains the necessary sections.
"""
config.read("D:\\PytestPython\\NopCommerceAutomation\\configurations\\configuration.ini")
class ReadConfig:
    @staticmethod
    def get_url():
        url = config.get("Admin Login Info","url")
        return url
    @staticmethod
    def get_username():
        username= config.get("Admin Login Info","username")
        return username
    @staticmethod
    def get_password():
        password = config.get("Admin Login Info","password")
        return password

    @staticmethod
    def get_invalid_username():
        invalid_user = config.get("Admin Login Info","invalid_username")
        return invalid_user
    @staticmethod
    def get_expected_title():
        expected_title=config.get("Admin Login Info","expected_title")
        return expected_title
