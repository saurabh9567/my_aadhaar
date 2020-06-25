from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from . import captcha
from . import models
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
from .captcha import GetCaptcha

#GET API to read files from text_files folder and will return response to browser
@api_view(['POST'])
def aadhaar(request):
    try:
        print('saurabh')
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        uid_no = request.data['uid']
        getcaptcha = GetCaptcha()
        driver = webdriver.Chrome(executable_path="myapp\driver\chromedriver.exe", options=chrome_options)
        driver.get("https://resident.uidai.gov.in/verify")
        getcaptcha.download_captcha(driver)
        captcha_text = getcaptcha.get_captcha_text()
        driver.implicitly_wait(5)
        uid = driver.find_element_by_xpath('//*[@id="uidno"]')
        captcha = driver.find_element_by_xpath('//*[@id="security_code"]')
        uid.send_keys(uid_no)
        captcha.send_keys(captcha_text)
        driver.find_element_by_xpath('//*[@id="submitButton"]').click()
        elements = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div[1]/div[3]')
        txt = elements.text
        return Response(txt)
    except Exception as ex: #if any other exception 
        print(ex)
        return ex