#from selenium import webdriver
from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Efetuar_Login_Page import Fazer_Login
from pages.pages.Consulta_Conteudo_Page import Consulta_Conteudo


from pages.pages.Inclui_Conteudo_Page import Inclui_Conteudo
from pages.pages.Exclui_Conteudo_Page import Exclui_Conteudo
from pages.pages.Altera_Conteudo_Page import Altera_Conteudo

       

@when(u'digitar conteudo já cadastrado excluir')
def step_impl(context):
   pass

@when(u'clicar na lupa excluir')
def step_impl(context):
   context.consultaconteudo.consultar_conteudo()

@then(u'aparecerá conteudo cadastrado excluir')
def step_impl(context):
   pass

@when(u'selecionar a lixeira')
def step_impl(context):
   pass

@when(u'clicar botão confirmar exclusão')
def step_impl(context):
   context.excluiconteudo.excluir_conteudo()
   
@then(u'aparecerá mensagem de registro excluido')
def step_impl(context):
   pass
 
