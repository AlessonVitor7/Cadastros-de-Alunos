lista_estudante=[]

def criarDocumento(arquivo):
    try:
        a = open (arquivo, 'wt+')
        a.close()
    except:
        print('erro ao criar o arquivo')
    else:
        print(f'arquivo criado{arquivo}')


def abrirDocumento(arquivo):
    try:
        a = open(arquivo,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def lerDocumento(arquivo):
    try:
        with open(arquivo, 'rt', encoding='utf-8') as a:
            print_magico("----------- ALUNOS CADASTRADOS ----------\n")
            conteudo = a.readlines()
            
            if not conteudo:
                print("Nenhum aluno cadastrado até o momento.")
            else:
                for linha in conteudo:
                    print(linha.strip())  # .strip() evita pular duas linhas entre um aluno e outro
                    
    except FileNotFoundError:
        print("Erro: O arquivo ainda não foi criado!")
    except Exception as erro:
        print(f"Erro ao ler o arquivo: {erro}")


doc='documentação.txt'
if not abrirDocumento(doc):
    criarDocumento(doc)

def cadastrarAluno(arquivo, aluno):
    try:
        a = open(arquivo, 'at', encoding='utf-8')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        try:
            a.write(f"Matrícula: {aluno['matricula']} | Nome: {aluno['nome']} | Ano: {aluno['ano_nascimento']}\n")
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            a.close()



def print_magico(texto):
    import time
    for letra in str(texto):
        print(f"{letra}", end='', flush=True)
        time.sleep(0.1)



def linha(txt):
    tan=len(txt)
    print('='*tan)
    print(txt)
    print('='*tan)


print("-----------CADASTRO DE ALUNOS ----------\n")

contador_matricula=1
print('''1-matricular um aluno
2-lista aluno 
3-dados do aluno 
4-desmatricular aluno\n''' )






while True:
#condições de escolhas do sistema
    dados_alunos={}


    escolha=int(input("digite a opção desejada: "))
    if escolha == 1:
    
        dados_alunos["matricula"] = contador_matricula
        contador_matricula += 1
        dados_alunos['nome']=str(input('nome do aluno:'))
        dados_alunos['ano_nascimento']=str(input('ano de nascimento:')).strip().split('/')[0]
        cadastrarAluno(doc, dados_alunos)
        contador_matricula = dados_alunos["matricula"] + 1
        lista_estudante.append(dados_alunos.copy())
        

        print_magico("-----------ALUNO MATRICULADO ----------\n")
        linha(f'o numero da matricula é : {dados_alunos["matricula"]}')

    elif escolha == 2:
        # Mostrando os alunos cadastrados com o efeito mágico
        lerDocumento(doc)
    elif escolha == 3: 
        busca=int(input('digite a matricula do aluno: '))
        for pessoa in lista_estudante:
            if busca == pessoa['matricula']:
                print(f"nome:{pessoa['nome']}|data de nascimento:{pessoa['ano_nascimento']}")
            else:
                print('numero da matricula não encontrado!')


    
    print("-"*10)
    para=str(input("deseja parar (s/n) "))
    if para in 'Ss':
        break


