from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Efetuar_Login_Page import Fazer_Login
from pages.pages.Consulta_Conteudo_Page import Consulta_Conteudo

from pages.pages.Inclui_Conteudo_Page import Inclui_Conteudo
from pages.pages.Exclui_Conteudo_Page import Exclui_Conteudo
from pages.pages.Altera_Conteudo_Page import Altera_Conteudo
###################################################################

#@given(u'eu esteja na pagina inicial do site da 4YOUSEE {url}')
# def step_impl(context, url):
#    context.app.navigate(url)
#    context.home.abrir_site()

@when(u'digitar conteudo já cadastrado consultar')
def step_impl(context):
   context.consultaconteudo.consultar_conteudo()

@when(u'clicar na lupa consultar')
def step_impl(context):
   pass

@then(u'aparecerá conteudo cadastrado consultar')
def step_impl(context):
   pass


