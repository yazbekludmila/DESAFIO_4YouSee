#from selenium import webdriver
from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Efetuar_Login_Page import Fazer_Login
from pages.pages.Consulta_Conteudo_Page import Consulta_Conteudo

from pages.pages.Inclui_Conteudo_Page import Inclui_Conteudo
from pages.pages.Exclui_Conteudo_Page import Exclui_Conteudo
from pages.pages.Altera_Conteudo_Page import Altera_Conteudo

###################################################################
  
@when(u'selecionar opção Adicionar conteúdo')
def step_impl(context):
    context.incluiconteudo.incluir_conteudo()

@when(u'digitar as informações corretamente do conteudo a ser inserido')
def step_impl(context):
    pass
 
@then(u'aparecerá mensagem de registro incluido') 
def step_impl(context):
    pass    