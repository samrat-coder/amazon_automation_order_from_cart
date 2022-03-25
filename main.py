from pytest_bdd import scenarios
from Pages.login import *
from Pages.Home_page import *
from Pages.Delivery_address import *
from Pages.Payment_page import *
from Config.driver import *
scenarios('feature_files')