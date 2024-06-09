*** Settings ***
# Define as configurações do teste, como bibliotecas, documentação e recursos necessários
Library    SeleniumLibrary  # Biblioteca para automação de testes web com Selenium


Documentation    Este caso de teste tem como objetivo realizar o login no site do Swag Labs  # Documentação do teste, explicando seu propósito

Metadata        Ambiente     ${AMBIENTE}  # Metadados do teste, como ambiente de execução

Resource    ../../main/main.robot  # Recurso contendo palavras-chave e configurações específicas do teste

Test Teardown    Realizar o test teardown    TEST_SETUP_PASSOU    CT0001    Test-1  # Define a palavra-chave de teardown e seus argumentos


Test Timeout    2 minutes  # Define o tempo limite do teste para 2 minutos

*** Test Cases ***
# Define o caso de teste
Test-1
    [Documentation]
    ...    Pré condição:
    ...    
    ...    Usuario e senha cadastrados  # Documentação detalhando a pré-condição do teste

    [Tags]    test_setup    regression  # Tags para classificação e organização do teste

    Acessar o site "Swag Labs"  # Passos do teste: acessa o site Swag Labs
    Inserir no campo "Username" o username do usuario     ${USERNAME}    # Insere o nome de usuário no campo de login
    Inserir no campo "Password" a senha do usuario    ${PASSWORD}     # Insere a senha no campo de login
    Clique em login  # Clica no botão de login
    Verificar o login no site "Swag Labs"  # Verifica se o login foi bem-sucedido no site Swag Labs
