# Importa os módulos necessários para o teste unitário e integração com o TestLink
import unittest
from testlink import TestlinkAPIClient, TestLinkHelper
from testlink.testlinkerrors import TLResponseError
import os
from datetime import datetime

# Carrega as variáveis de ambiente para conexão com o TestLink
os.environ["TESTLINK_API_PYTHON_SERVER_URL"] = 'http://localhost/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
os.environ["TESTLINK_API_PYTHON_DEVKEY"] = '2da55ef457d3741267bcb1ec89d258f7'

# Nome do Projeto no TestLink
Projeto = "Test"
# Nome do Plano de teste no TestLink
TestPlanName = "TestIntegra"
# Nome da build que está sendo testada
BuildName = "TestIntegra"
# Nota que pode ser adicionada ao reportar o resultado do teste
Note = "Teste automatizado executado via Robot Framework integrado com Testlink"
# Sobrescrever o resultado do teste ou adicionar na lista existente
OverWrite = False
# URL da API do TestLink
UrlTestLink = 'http://localhost/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
TimeExec = '1'

# Função para reportar o status do teste para o TestLink
def status_tl(TestCaseFullExtID, Status):
    try:
        print("Conectando ao TestLink...")
        # Estabelece conexão com o TestLink
        tl_helper = TestLinkHelper()
        myTestLink = tl_helper.connect(TestlinkAPIClient)
        print("Conexão bem sucedida!")

        # Obtém a data e hora atual
        DateExec = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        print(f"Obtendo ID do plano de teste '{TestPlanName}'...")
        # Obtém o ID do plano de teste pelo nome
        TestPlan = myTestLink.getTestPlanByName(Projeto, TestPlanName)
        TestPlanID = TestPlan[0]['id']
        print(f"ID do plano de teste '{TestPlanName}': {TestPlanID}")

        # Verifica se existem plataformas associadas ao plano de teste
        platforms = myTestLink.getTestPlanPlatforms(TestPlanID)
        if platforms:
            platform_name = platforms[0]['name']
            print(f"Plataforma encontrada: {platform_name}")
        else:
            platform_name = ''  # Fornecer um valor vazio para platformname
            print("Nenhuma plataforma associada ao plano de teste. Fornecendo platformname vazio no payload.")

        print(f"Reportando resultado do caso de teste {TestCaseFullExtID}...")

        # Constrói o payload para reportar o resultado do teste
        payload = {
            'testcaseexternalid': TestCaseFullExtID,
            'testplanid': TestPlanID,
            'buildname': BuildName,
            'status': Status,
            'notes': Note,
            'execduration': TimeExec,
            'timestamp': DateExec,
            'overwrite': OverWrite,
            'platformname': platform_name,
        }

        # Reporta o resultado do teste para o TestLink
        newResult = myTestLink.reportTCResult(**payload)

        print("Resposta da API:", newResult)
    except TLResponseError as e:
        print("Erro na resposta do TestLink:", e)
    except Exception as e:
        print("Erro inesperado:", e)

# Classe de exemplo para automação do teste
class AutomatedUpdateExample(unittest.TestCase):

    # Método de teste
    def test1(self):
        test_project = Projeto
        test_plan = TestPlanName
        test_case = "TestCaseFullExtID"  # O ID completo do caso de teste
        build = BuildName
        notes = Note
        result = "p"

        try:
            # Simula o teste bem-sucedido
            print("Executando o teste simulado...")
            notes = "Executado com sucesso"
        except Exception as e:
            result = "f"
            notes = "Falha na execução"
        finally:
            # Reporta o status do teste para o TestLink
            status_tl(test_case, result)

# Executa os testes
if __name__ == "__main__":
    unittest.main()
