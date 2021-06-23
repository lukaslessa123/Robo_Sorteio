from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Fiz algumas modificações


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"C:\Users\Lucas\Desktop\TUDO\bot_comentarios_instagram-master\geckodriver.exe")
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        #login_button.click()
        time.sleep(3)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos_com_a_perfil("CN3Tr4sFyIH")  
        
        # Altere aqui para a perfil que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 1) / 30)

    def comente_nas_fotos_com_a_perfil(self, perfil):
        links_de_posts = []
        driver = self.driver
        driver.get("https://www.instagram.com/p/" + perfil + "/")
        time.sleep(5)
        for i in range(1, 5):  
            
            # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: 
            # quer que ele desça 5 páginas então você deve alterar de range(1,5) para range(1,5)

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(perfil + " fotos: " + str(len(pic_hrefs)))
        for link in pic_hrefs:
            try:
                if link.index("/p/") != -1:
                    links_de_posts.append(link)
            except:
                pass

        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                comments = [
                    "😀",
                    " AUHuehuaheuaehuae"
                ] 
                # Remova esses comentários e insira os seus comentários aqui
                
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))
                self.type_like_a_person(random.choice(comments), comment_input_box)
                time.sleep(random.randint(3, 5))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(random.randint(3, 5))
                driver.find_element_by_class_name('fr66n').click()
                #driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                #time.sleep(1)
                driver.find_element_by_xpath('//button[text()="Follow"]').click()

            except Exception as e:
                print(e)
                time.sleep(9)
            
    


# Entre com o usuário e senha aqui
robo_sorteio = InstagramBot("usuname", "password")
robo_sorteio.login()
