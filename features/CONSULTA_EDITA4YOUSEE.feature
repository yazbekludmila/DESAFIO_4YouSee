@Consulta_Edicao_dados_4SEE

Feature: Ediçao de Informações do Usuário 

    Eu como usuario já cadastrado no site da 4YOUSEE queroo acessar o site 
    
    """Feature Description"""

   Background: Estar no site da 4YOUSEE
   Given eu esteja na Home Page do site da 4YOUSEE https://qa3.4yousee.com.br/
   When fizer login com usuário já cadastrado 
   Then usuário estará logado 
   
   @ConsultaConteudo
   Scenario: Consultar conteudo já cadastrado
        When digitar conteudo já cadastrado consultar
        When clicar na lupa consultar
        Then aparecerá conteudo cadastrado consultar


   @AlteraConteudo
   Scenario: Alteraçao de conteúdo já Cadastrado alterar 
        When digitar conteudo já cadastrado alterar
        When clicar na lupa alterar
        Then aparecerá conteudo cadastrado alterar
       
        When digitar informações corretamente do conteudo alterar 
        When clicar botão alterar
        Then aparecerá mensagem de registro alterado

   @ExcluiConteudo
   Scenario: Exclusão
        When digitar conteudo já cadastrado excluir
        When clicar na lupa excluir
        Then aparecerá conteudo cadastrado excluir
       
        When selecionar a lixeira 
        When clicar botão confirmar exclusão 
        Then aparecerá mensagem de registro excluido 


   @IncluiConteudo 
   Scenario: Inclusão de novo conteudo
        When selecionar opção Adicionar conteúdo 
        When digitar as informações corretamente do conteudo a ser inserido 
        Then aparecerá mensagem de registro incluido