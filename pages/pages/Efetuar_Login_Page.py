from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Fazer_Login():

    def __init__(self, app):
        self.app = app
        
    def efetuar_login(self):

        #DIGITAR EMAIL E SENHA 
        #campo_email = self.app.find_element_by_id('email')
        campo_email = self.app.find_element_by_xpath('//*[@id="nav-horizontal"]/div/div[2]/form/fieldset/div[1]/input')
        campo_email.send_keys('ludmilayazbek')
        
        #campo_senha = self.app.find_element_by_id('pass')
        campo_senha = self.app.find_element_by_xpath('//*[@id="nav-horizontal"]/div/div[2]/form/fieldset/div[2]/input')
        campo_senha.send_keys('27vbqu')
        
        #CLICAR NO BOTÃO CONTINUAR PARA EFETUAR LOGIN === vai para pagina usuario 
        #botao_continuar_login = self.app.find_element_by_id('send2').click()
        botao_continuar_login = self.app.find_element_by_xpath('//*[@id="nav-horizontal"]/div/div[2]/form/fieldset/input').click()
        sleep(5)
        botao_fechar_janela_aviso_user = self.app.find_element_by_xpath("/html/body/div[6]/div[3]/div/button[2]").click()
        # botao_pesquisa.submit()   
        #  /html/body/div[6]/div[3]/div/button[2]
        ## <button type="button" class="btn-default">Fechar</button>

#def validar_login_efetuado(self):   
        #valido_login = self.app.find('link_text',"Olá, Ludmila")
        #element_2 = self.app.find_element_by_class_name('nm-searched-term')
 #       login_valido = self.app.find_element_by_class_name('ellipsis-text')
        #print(login_valido.text)
  #      assert  login_valido.text == 'Olá, Ludmila'    
        #resultado = element_2
        # print(resultado.text)
        # print(total)
        #assert resultado.text == 'Resultados para: Gestão da Emoção'