#from selenium import webdriver
from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Efetuar_Login_Page import Fazer_Login
from pages.pages.Consulta_Conteudo_Page import Consulta_Conteudo

from pages.pages.Inclui_Conteudo_Page import Inclui_Conteudo
from pages.pages.Exclui_Conteudo_Page import Exclui_Conteudo
from pages.pages.Altera_Conteudo_Page import Altera_Conteudo


###################################################################

  
@when(u'digitar conteudo já cadastrado alterar')
def step_impl(context):
    context.consultaconteudo.consultar_conteudo()
    context.alteraconteudo.alterar_conteudo()
   
@when(u'clicar na lupa alterar')
def step_impl(context):
    pass
 
@then(u'aparecerá conteudo cadastrado alterar') 
def step_impl(context):
    pass    
   
@when(u'digitar informações corretamente do conteudo alterar')
def step_impl(context):
    pass
    
@when(u'clicar botão alterar')
def step_impl(context):
    pass

@then(u'aparecerá mensagem de registro alterado')
def step_impl(context):
     pass
