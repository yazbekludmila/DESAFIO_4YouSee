#from selenium import webdriver
from pages.pages.Abrir_Site_Page import Abrir_Site
from pages.pages.Efetuar_Login_Page import Fazer_Login

#from pages.pages.EdicaoLoginSaraivaPage import Fazer_Login_Saraiva
#from pages.pages.EdicaoEnderecoSaraivaPage import Edicao_Endereco
#from pages.pages.EdicaoUsuarioPage import Fazer_Pagamento
###################################################################
    
@given(u'eu esteja na Home Page do site da 4YOUSEE {url}')
def step_impl(context, url):
    context.app.navigate(url)
    context.abresite.abrir_home()

@when(u'fizer login com usuário já cadastrado')
def step_impl(context):
  # context.edicaohome.fazer_login_edicao()
   context.login.efetuar_login()

@then(u'usuário estará logado')
def step_impl(context):
     pass
#    context.edicaologin.validar_login_efetuado()