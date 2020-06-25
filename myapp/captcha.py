from anticaptchaofficial.imagecaptcha import *
import base64
# from selenium import webdriver

class GetCaptcha():
    def get_captcha_text(self):
        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key("0f3b306e9364e3faac083b49a11dd525")
        captcha_text = solver.solve_and_return_solution("captcha.jpg")
        if captcha_text != 0:
            print("captcha text "+captcha_text)
            return captcha_text
        else:
            print("task finished with error "+solver.error_code)

    def download_captcha(self, driver):
        # driver = webdriver.Chrome(executable_path="D:\Projects_django\sel\chromedriver\chromedriver.exe")
        # driver.set_script_timeout(10)
        # driver.get("https://resident.uidai.gov.in/verify")
        ele_captcha = driver.find_element_by_xpath("//*[@id='captcha-img']")

        # get the captcha as a base64 string
        img_captcha_base64 = driver.execute_async_script("""
            var ele = arguments[0], callback = arguments[1];
            ele.addEventListener('load', function fn(){
            ele.removeEventListener('load', fn, false);
            var cnv = document.createElement('canvas');
            cnv.width = this.width; cnv.height = this.height;
            cnv.getContext('2d').drawImage(this, 0, 0);
            callback(cnv.toDataURL('image/jpeg').substring(22));
            }, false);
            ele.dispatchEvent(new Event('load'));
            """, ele_captcha)

        # save the captcha to a file
        with open(r"captcha.jpg", 'wb') as f:
            f.write(base64.b64decode(img_captcha_base64))