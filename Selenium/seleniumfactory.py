from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# from selenium import webdriver

# PROXY = "23.23.23.23:3128" # IP:PORT or HOST:PORT

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)

# chrome = webdriver.Chrome(options=chrome_options)
# chrome.get("http://whatismyipaddress.com")

class ChromeSelenium(object):

    @classmethod
    def init_webdirver(cls,headless=False):
        options = Options()
        ua =  UserAgent()
        if headless:
            options.add_argument("--headless")
        # PROXY = "60.5.254.169:8081"
        options.add_argument("--start-maximized")
        options.add_argument(f"user-agent={ua.random}")
        # options.add_argument('--proxy-server=%s' % PROXY)
      
        return webdriver.Chrome(executable_path='C:/Users/Kevin/Desktop/PythonProject/Selenium/chromedriver.exe',chrome_options=options)
