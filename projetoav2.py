usuarios = {'rene@gmail.com':{'Email': 'rene@gmail.com','Senha': 'rene12345', 'Nome': 'rene de sousa', 'Reservas': []}}
caronas = {}
motoristas = {}
carona_id = 1
nao_pode = ['(', ')', '[', ']', '{', '}', '<', '>', ',', ';', ':', '\\', '"', "'", '`', ' ', '\t', '\n','!', '#', '$', '%', '^', '&', '*', '=', '+', '/', '?', '|', '~']
op = 99
while op != 0:
    print('   MENU(BLABLACAR)   ')
    print('-='*10)
    print('1 - CADASTRAR USUÁRIO ')
    print('2 - FAZER LOGIN ')
    print('3 - SAIR DO PROGRAMA ')
    print('-='*10)
    entrada = input('DIGITE A OPÇÃO DESEJADA ^-^: ')
    if entrada in ['1', '2', '3']:
        op = int(entrada)
    else:
        print('OPÇÃO INVÁLIDA! DIGITE 1, 2 OU 3.')
        continue
    if op == 1:
        nome = input('DIGITE O SEU NOME COMPLETO: ')
        email_valido = False
        while not email_valido:
            email = input('DIGITE O SEU EMAIL: ')
            if email in usuarios:
                print('ESSE EMAIL JÁ ESTÁ CADASTRADO!')
                continue
            tem_proibido = False
            for caractere in email:
                for proibido in nao_pode:
                    if caractere == proibido:
                        tem_proibido = True
            if '@' not in email or '.com' not in email:
                tem_proibido = True
            else:
                partes_email = email.split('@')
                if len(partes_email) != 2 or not partes_email[0]:
                    tem_proibido = True
                else:
                    dominio = partes_email[1].split('.')
                    if len(dominio) < 2 or not dominio[0] or dominio[1] != 'com':
                        tem_proibido = True
                    elif len(dominio) > 2:
                        tem_proibido = True
            if not tem_proibido:
                email_valido = True
            else:
                print('EMAIL INVÁLIDO! TENTE NOVAMENTE.')
        while True:
            senha = input('DIGITE UMA SENHA: ')
            if len(senha) < 8:
                print('SENHA INVALIDA. O NÚMERO DE CARACTERES NÃO É SUFICIENTE')
            else:
                break
        usuarios[email] = {'Email': email, 'Senha': senha, 'Nome': nome, 'Reservas': []}
        print('CADASTRO REALIZADO COM SUCESSO!')
    elif op == 2:
        login_correto = False
        while not login_correto:
            email_user = input('DIGITE SEU LOGIN: ')
            senha_user = input('DIGITE SUA SENHA: ')
            voltar = input('GOSTARIA DE VOLTAR PARA O MENU? [S/N]: ').upper()[0]
            while voltar not in 'SN':
                print('DIGITE UMA OPÇÃO VALIDA!')
                voltar = input('GOSTARIA DE VOLTAR PARA O MENU? [S/N]: ').upper()[0]
            if voltar == 'S':
                break
            if email_user in usuarios and usuarios[email_user]['Senha'] == senha_user:
                print('O LOGIN FOI REALIZADO COM SUCESSO')
                login_correto = True
                op2 = 99
                while op2 != 0:
                    print('-=' * 10)
                    print('   MENU DO USUÁRIO   ')
                    print('1 - CADASTRAR CARONA ')
                    print('2 - LISTAR CARONAS DISPONÍVEIS ')
                    print('3 - BUSCAR E RESERVAR CARONA')
                    print('4 - CANCELAR RESERVA')
                    print('5 - REMOVER CARONA(MOTORISTA)')
                    print('6 - SUAS CARONAS(MOTORISTA)')
                    print('7 - SUAS RESERVAS(PASSAGEIRO)')
                    print('0 - LOGOUT ')
                    print('-=' * 10)
                    entrada2 = input('ESCOLHA A OPÇÃO DESEJADA: ')
                    if entrada2 in ['0', '1', '2', '3','4','5','6','7']:
                        op2 = int(entrada2)
                    else:
                        print('OPÇÃO INVÁLIDA! DIGITE 0, 1, 2, 3, 4,5,6, OU 7')
                        continue
                    if op2 == 1:
                        se_tornar_motorista = input('PARA CADASTRAR UMA CARONA, VOCÊ DEVE SE TORNAR UM MOTORISTA, GOSTARIA DE CONTINUAR?[S/N]: ').upper()[0]
                        while se_tornar_motorista not in 'SN':
                            print('DIGITE UMA OPÇÃO VALIDA!')
                            se_tornar_motorista = input('PARA CADASTRAR UMA CARONA, VOCÊ DEVE SE TORNAR UM MOTORISTA, GOSTARIA DE CONTINUAR?[S/N]: ').upper()[0]
                        if se_tornar_motorista == 'S':
                            if email_user not in motoristas:
                                motoristas[email_user] = {'Nome': usuarios[email_user]['Nome'], 'Caronas': []}
                                print('AGORA VOCÊ É UM MOTORISTA, CADASTRE SUA CARONA!')
                            else:
                                print('VOCÊ JA É UM MOTORISTA! CADASTRE SUA CARONA!')
                        elif se_tornar_motorista == 'N':
                            continue
                        local = input('DIGITE O LOCAL DE ORIGEM: ')
                        while True:
                            destino = input('DIGITE O DESTINO DA CARONA: ')
                            if destino == local:
                                print('DESTINO INVALIDO. TENTE NOVAMENTE!')
                            else:
                                break
                        while True:
                            data = input('DIGITE A DATA DA CARONA [DD/MM/AAAA]: ')
                            if len(data) == 10:
                                dia = data.split('/')[0]
                                mes = data.split('/')[1]
                                ano = data.split('/')[2]
                                dia = int(dia)
                                mes = int(mes)
                                ano = int(ano)
                                if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano == 2025:
                                    break
                                else:
                                    print('DATA INVALIDA. DIGITE NOVAMENTE!')
                            else:
                                print('DATA INVALIDA. DIGITE NOVAMENTE')
                        carona_mesma_data = False
                        for cid in motoristas[email_user]['Caronas']:
                            if caronas[cid]['Data'] == data:
                                carona_mesma_data = True
                                break
                        if carona_mesma_data:
                            print('VOCÊ JÁ POSSUI UMA CARONA CADASTRADA NESSA DATA!')
                            continue
                        while True:
                            horario = input('DIGITE O HORARIO DA CARONA [HH:MM]: ')
                            if len(horario) == 5:
                                hora, min = horario.split(':')
                                hora, min = int(hora), int(min)
                                if hora >=0 and hora <= 23 and min >= 0 and min <= 59:
                                    break
                            else:
                                print('HORARIO INVALIDO. TENTE NOVAMENTE: ')
                        carona_duplicada = False
                        for cid in motoristas[email_user]['Caronas']:
                            c = caronas[cid]
                            if c['Motorista'] == email_user and c['Local'] == local and c['Destino'] == destino and c['Data'] == data and c['Horario'] == horario:
                                carona_duplicada = True
                                break
                        if carona_duplicada:
                            print('VOCÊ JÁ CADASTROU UMA CARONA COM ESSAS INFORMAÇÕES!')
                            continue
                        vagas = int(input('DIGITE A QUANTIDADE DE VAGAS: '))
                        valor = float(input('DIGITE O VALOR POR VAGAS: '))
                        caronas[carona_id] = {'Local': local, 'Destino': destino, 'Data': data, 'Horario': horario, 'Vagas': vagas, 'Valor': valor, 'Motorista': email_user, 'Passageiros': []}
                        motoristas[email_user]['Caronas'].append(carona_id)
                        print(f'{carona_id} CARONA CADASTRADA COM SUCESSO!')
                        carona_id += 1
                    elif op2 == 2:
                        print('CARONAS DISPONIVEIS:')
                        if len(caronas) == 0:
                            print('AINDA NÃO TEM CARONAS DISPONIVEIS!')
                        for carona_disp in caronas:
                            disponivel = caronas[carona_disp]
                            print(f'ID: {carona_disp} | Origem: {disponivel['Local']} | Destino: {disponivel['Destino']} | Data: {disponivel['Data']} | Horário: {disponivel['Horario']}h | Vagas: {disponivel['Vagas']} | Valor: R${disponivel['Valor']:.2f} | Motorista: {motoristas[disponivel['Motorista']]['Nome']}')
                    elif op2 == 3:
                        if email_user in motoristas:
                            print('VOCÊ NÃO PODE BUSCAR CARONAS COMO MOTORISTA!')
                        else:
                            buscar_local = input('DIGITE O LOCAL: ')
                            buscar_destino = input('DIGITE O DESTINO QUE QUER BUSCAR: ')
                            encontrou = False
                            for carona_ld in caronas:
                                dados = caronas[carona_ld]
                                if dados['Local'] == buscar_local and dados['Destino'] == buscar_destino:
                                    print(f'TEM CARONAS DISPONIVEIS!')
                                    encontrou = True
                                    detalhes = input('GOSTARIA DE VER OS DETALHES?[S/N]: ').upper()[0]
                                    while detalhes not in 'SN':
                                        print('DIGITE UMA OPÇÃO VALIDA!')
                                        detalhes = input('GOSTARIA DE VER OS DETALHES?[S/N]: ').upper()[0]
                                    if detalhes == 'S':
                                        print(f'Email Do Motorista: {dados['Motorista']} | Origem: {dados['Local']} | Destino: {dados['Destino']} | Data: {dados['Data']} | Horário: {dados['Horario']}h | Vagas: {dados['Vagas']} | Valor: R${dados['Valor']:.2f} | Motorista: {motoristas[dados['Motorista']]['Nome']}')
                                        reservar = input('GOSTARIA DE RESERVAR ESTA CARONA?[S/N] ').upper()[0]
                                        while reservar not in 'SN':
                                            print('DIGITE UMA OPÇÃO VALIDA!')
                                            reservar = input('GOSTARIA DE RESERVAR ESTA CARONA?[S/N] ').upper()[0]
                                        if reservar == 'S':
                                            if dados['Vagas'] == 0:
                                                print('NÃO É POSSÍVEL RESERVAR. TODAS AS VAGAS JÁ FORAM PREENCHIDAS!')
                                                break
                                            if dados['Motorista'] == email_user:
                                                print('VOCÊ NÃO PODE FAZER UMA RESERVA SENDO MOTORISTA!')
                                                continue
                                            reserva_email = input('DIGITE O EMAIL DO MOTORISTA: ')
                                            data_carona = input('DIGITE A DATA DA CARONA [DD/MM/AAAA]: ')
                                            if reserva_email != dados['Motorista'] or data_carona != dados['Data']:
                                                print('EMAIL OU DATA INCORRETOS! RESERVA NÃO EFETUADA.')
                                                continue
                                            valor_original = dados['Valor']
                                            num_reservas = len(usuarios[email_user]['Reservas'])
                                            if num_reservas >= 2:
                                                desconto = valor_original * 0.10
                                                valor_com_desconto = valor_original - desconto
                                                print(f'VOCÊ POSSUI MAIS DE 2 CARONAS RESERVADAS E GANHOU UM DESCONTO DE 10%! O VALOR A PAGAR É R${valor_com_desconto:.2f}')
                                            else:
                                                valor_com_desconto = valor_original
                                            pagar = float(input('DIGITE O VALOR A SER PAGO NA PASSAGEM: '))
                                            if pagar == valor_com_desconto:
                                                caronas[carona_ld]['Vagas'] -= 1
                                                usuarios[email_user]['Reservas'].append(carona_ld)
                                                caronas[carona_ld]['Passageiros'].append(email_user)
                                                print(f'CARONA RESERVADA COM SUCESSO PARA {usuarios[email_user]['Nome']}')
                                            elif pagar < valor_com_desconto:
                                                print(f'VALOR INSUFICIENTE. A CARONA CUSTA R${valor_com_desconto:.2f}')
                                            elif pagar > valor_com_desconto:
                                                troco = pagar - valor_com_desconto
                                                caronas[carona_ld]['Vagas'] -= 1
                                                usuarios[email_user]['Reservas'].append(carona_ld)
                                                caronas[carona_ld]['Passageiros'].append(email_user)
                                                print(f'CARONA RESERVADA COM SUCESSO PARA {usuarios[email_user]['Nome']}')
                                                print(f'TROCO: R${troco:.2f}')
                                        elif reservar == 'N':
                                            continue
                                    elif detalhes == 'N':
                                        continue
                            if not encontrou:
                                print('NÃO TEM CARONAS PARA ESSES LOCAIS!')
                    elif op2 == 4:
                        email_passageiro = input('DIGITE O SEU EMAIL PARA CANCELAR A RESERVA: ')
                        reserva_cancelada = False
                        if email_user == email_passageiro:
                            for id_carona in caronas:
                                dados = caronas[id_carona]
                                if email_user in dados['Passageiros']:
                                    dados['Passageiros'].remove(email_user)
                                    dados['Vagas'] += 1
                                    if id_carona in usuarios[email_user]['Reservas']:
                                        usuarios[email_user]['Reservas'].remove(id_carona)
                                    print(f'RESERVA CANCELADA! ID Carona: {id_carona} | VAGAS AGORA: {dados["Vagas"]}')
                                    reserva_cancelada = True
                                    break
                            if not reserva_cancelada:
                                print('VOCÊ NÃO POSSUI NENHUMA RESERVA PARA CANCELAR.')
                        else:
                            print('O EMAIL INFORMADO NÃO CORRESPONDE AO USUÁRIO LOGADO!')
                    elif op2 == 5:
                        if email_user not in motoristas:
                            print('VOCÊ PRECISA SER UM MOTORISTA PARA REMOVER A CARONA!')
                        else:
                            while True:
                                data_remover = input('DIGITE A DATA DA CARONA QUE VOCÊ QUER REMOVER [DD/MM/AAAA]: ')
                                if len(data_remover) == 10:
                                    dia = data_remover.split('/')[0]
                                    mes = data_remover.split('/')[1]
                                    ano = data_remover.split('/')[2]
                                    dia = int(dia)
                                    mes = int(mes)
                                    ano = int(ano)
                                    if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and ano == 2025:
                                        break
                                    else:
                                        print('DATA INVALIDA. DIGITE NOVAMENTE!')
                                else:
                                    print('DATA INVALIDA. DIGITE NOVAMENTE!')
                            carona_encontrada = False
                            for carona_id in motoristas[email_user]['Caronas']:
                                if caronas[carona_id]['Data'] == data_remover:
                                    del caronas[carona_id]
                                    motoristas[email_user]['Caronas'].remove(carona_id)
                                    print('CARONA REMOVIDA COM SUCESSO!')
                                    carona_encontrada = True
                                    break
                            if not carona_encontrada:
                                print('NENHUMA CARONA SUA ENCONTRADA NESSA DATA!')
                    elif op2 == 6:
                        if email_user not in motoristas or len(motoristas[email_user]['Caronas']) == 0:
                            print('VOCÊ AINDA NÃO CADASTROU NENHUMA CARONA!')
                        else:
                            print('SUAS CARONAS CADASTRADAS:')
                            for carona_id in motoristas[email_user]['Caronas']:
                                carona = caronas[carona_id]
                                print(f'ID: {carona_id} | Origem: {carona['Local']} | Destino: {carona['Destino']} | Data: {carona['Data']} | Horário: {carona['Horario']}h | Vagas: {carona['Vagas']} | Valor: R${carona['Valor']:.2f} | Passageiros: {carona['Passageiros']}')
                    elif op2 == 7:
                        if email_user in motoristas:
                            print('VOCÊ NÃO PODE VER AS RESERVAS DOS PASSAGEIROS')
                        else:
                            if not usuarios[email_user]['Reservas']:
                                print('VOCÊ NÃO TEM NENHUMA CARONA RESERVADA.')
                            else:
                                print('SUAS CARONAS RESERVADAS:')
                                for cod in usuarios[email_user]['Reservas']:
                                    if cod in caronas:
                                        dados = caronas[cod]
                                        print(
                                            f'ID: {cod} | Origem: {dados['Local']} | Destino: {dados['Destino']} | Data: {dados['Data']} | Horário: {dados['Horario']}h | Valor: R${dados['Valor']:.2f} | Motorista: {motoristas[dados['Motorista']]['Nome']}')
                                    else:
                                        print(f'ID: {cod} | ESTA CARONA FOI CANCELADA PELO MOTORISTA.')
            else:
                print('USUÁRIO NÃO ENCONTRADO!')