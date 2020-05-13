from unittest import TestCase, main
from validacpf_luciano import retira_formatacao, valida_cpf

class TesteCPF(TestCase):
    
    def teste_formatacao(self):   
        self.assertEqual(retira_formatacao("386.196.518-62"), "38619651862")
        self.assertEqual(retira_formatacao("031.283.128-50"), "03128312850")
        self.assertEqual(retira_formatacao("123.456.789-10"), "12345678910")
        self.assertEqual(retira_formatacao("987.654.321-00"), "98765432100")
        
    def teste_valida(self):
        self.assertEqual(valida_cpf("386.196.518-62"), "CPF VÁLIDO")
        self.assertEqual(valida_cpf("222.222.222-22"), "CPF INVÁLIDO")
        self.assertEqual(valida_cpf("111.111.111-11"), "CPF INVÁLIDO")
        self.assertEqual(valida_cpf("031.283.128-50"), "CPF VÁLIDO")
        self.assertEqual(valida_cpf("123.456.789-10"), "CPF INVÁLIDO")
        
        
if __name__ == '__main__':
    main()
