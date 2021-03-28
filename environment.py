
"""		Pyautomator Framework de teste 

			saraivatestes"""

from selenium import webdriver
from Pyautomators import fixture
from webautomators import WebChromeDriver
from webautomators.extended_options import WebChromeOptions
##from pages.pages.HomeSaraivaPage import Procura_Compra_Produto
##from pages.pages.LoginSaraivaPage import Fazer_Login_Saraiva
##from pages.pages.FreteSaraivaPage import Escolher_Frete
##from pages.pages.PagamentoPage import Fazer_Pagamento

from pages.pages.Abrir_Site_Page  import Abrir_Site
from pages.pages.Efetuar_Login_Page import Fazer_Login
from pages.pages.Consulta_Conteudo_Page import Consulta_Conteudo

from pages.pages.Inclui_Conteudo_Page import Inclui_Conteudo
from pages.pages.Exclui_Conteudo_Page import Exclui_Conteudo
from pages.pages.Altera_Conteudo_Page import Altera_Conteudo

##from pages.pages.EdicaoUsuarioPage import Selecionar_Informacao_Alterar
##from pages.pages.EdicaoEnderecoPage import Alterar_Endereco
##from pages.pages.CadastroUsuarioPage import Cadastrar_Usuario

def before_all(context):
	options = WebChromeOptions()
	options.maximized()
	#context.app = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
	#context.app = WebChromeDriver(executable_path='../driver/chromedriver.exe', options=options)
	#context.app = WebChromeDriver(executable_path='../driver/chromedriver.exe', options=options)
	context.app = WebChromeDriver(executable_path='C:\drivers\chromedriver.exe', options=options)
	#context.app = WebChromeDriver(executable_path='C:\Users\Ludmila\Documents\A4_YOU_SEE\DESAFIO_4_YOU_SEE\saraivatestes\driver\chromedriver.exe', options=options)
	##HOJE context.home  = Procura_Compra_Produto(context.app)
	##HOJE login = Fazer_Login_Saraiva(context.app)
	##HOJE context.frete = Escolher_Frete(context.app)
	##HOJE context.pagamento = Fazer_Pagamento(context.app) 

	
	context.abresite  = Abrir_Site(context.app)
	context.login = Fazer_Login(context.app)
	context.consultaconteudo  = Consulta_Conteudo(context.app)
	
	context.excluiconteudo  = Exclui_Conteudo(context.app)
	context.incluiconteudo  = Inclui_Conteudo(context.app)
	context.alteraconteudo  = Altera_Conteudo(context.app)

	# HOJE context.edicaousuario = Selecionar_Informacao_Alterar(context.app)
	# HOJE context.edicaoendereco = Alterar_Endereco(context.app) 
	
	##HOJE #context.cadastrousuario = Cadastrar_Usuario(context.app) 

	context.pages = {
	    "login": "https://qa3.4yousee.com.br/"
	#	"login": "https://www.saraiva.com.br/checkout/onepage/"
	#	"login": "https://www.saraiva.com.br/checkout/onepage/",
	#	"frete": "https://www.saraiva.com.br/checkout/onepage/",
	#	"pagamento": "https://www.saraiva.com.br/checkout/onepage/"
	}

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

#def after_all(context):
#	context.driver.quit()

#def before_all(context):
#	context.app=webdriver.Chrome('driver/chromedriver.exe')
#	context.page=HomeSaraiva(context.app)