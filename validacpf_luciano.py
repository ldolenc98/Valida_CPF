def retira_formatacao(num_cpf):
    cpf_ponto = num_cpf.replace(".", "")
    cpf_traco = cpf_ponto.replace("-", "")
    num_cpf = cpf_traco
    return(num_cpf)

def valida_cpf(num_cpf):
    if num_cpf[0] == num_cpf[1] and num_cpf[1] == num_cpf[2] and num_cpf[2] == num_cpf[4] and num_cpf[4] == num_cpf[5] and num_cpf[5] ==     num_cpf[6] and num_cpf[6] == num_cpf[8] and num_cpf[8] == num_cpf[9] and num_cpf[9] == num_cpf[10] and num_cpf[10] == num_cpf[12] and num_cpf[12] == num_cpf[13]:
        return "CPF INVÁLIDO"

    else:
        num_cpf = retira_formatacao(num_cpf)
        soma = int(num_cpf[0])*10 + int(num_cpf[1])*9 + int(num_cpf[2])*8 + int(num_cpf[3])*7 + int(num_cpf[4])*6 + int(num_cpf[5])*5 + int(num_cpf[6])*4 + int(num_cpf[7])*3 + int(num_cpf[8])*2
        resto = soma%11
        if resto > 2:
            DV1 = 11 - resto
        else:
            DV1 = 0

        num_cpf2 = num_cpf + str(DV1)
        soma2 = int(num_cpf2[0])*11 + int(num_cpf2[1])*10 + int(num_cpf2[2])*9 + int(num_cpf2[3])*8 + int(num_cpf2[4])*7 + int(num_cpf2[5])*6 + int(num_cpf2[6])*5 + int(num_cpf2[7])*4 + int(num_cpf2[8])*3 + int(num_cpf2[9])*2
        resto2 = soma2%11
        if resto2 > 2:
            DV2 = 11 - resto2
        else:
            DV2 = 0
        if str(DV1) == num_cpf[9] and str(DV2) == num_cpf[10]:
            
            return"CPF VÁLIDO"
        else:
            return"CPF INVÁLIDO"

#num_cpf = str(input("Digite o número de CPF: "))
#print(valida_cpf(num_cpf))
