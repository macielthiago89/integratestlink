*** Settings ***
# Importa as bibliotecas necessárias para o teste usando o Robot Framework
Library    SeleniumLibrary  # Biblioteca para automação de testes web com Selenium
Library    ../../IntegraTestlink/integratest.py  # Biblioteca personalizada para integração com o TestLink

Resource    ../../main/main.robot  # Recurso contendo palavras-chave e configurações específicas do teste

*** Keywords ***
# Define uma palavra-chave personalizada para realizar ações de teardown no teste
Realizar o test teardown
    [Arguments]    ${EVIDENCIA}    ${CASODETESTE}    ${CASOTESTINTEGRACAO}
    Capture Page Screenshot    ${EVIDENCIA}-${CASODETESTE}.png    # Captura uma screenshot da página e renomeia com o nome do caso de teste
    Close Browser    # Fecha o navegador
    Validastatus "${CASOTESTINTEGRACAO}"  # Chama a palavra-chave Validastatus para validar o status do teste de integração


# Define uma palavra-chave para validar o status do teste no TestLink
Validastatus "${TestCaseFullExtID}" 
    Run Keyword If Test Passed    Resultado "${TestCaseFullExtID}", "p"  # Chama a palavra-chave Resultado se o teste passar
    Run Keyword If Test Failed    Resultado "${TestCaseFullExtID}", "f"  # Chama a palavra-chave Resultado se o teste falhar


# Define uma palavra-chave para relatar o resultado do teste no TestLink
Resultado "${TestCaseFullExtID}", "${status}"
    ${CONTEUDO_HASH}    status_tl    ${TestCaseFullExtID}    ${status}  # Chama a função status_tl para reportar o resultado do teste
    Log    ${CONTEUDO_HASH}  # Registra o conteúdo retornado pela função status_tl
