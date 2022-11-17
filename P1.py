#---Text Justifier---

def limpa_texto(texto):
    """
    
    devolve um texto limpo.
    
    Argumentos:
        texto: cadeia de carateres
    No fundo, remove todos os carateres brancos e elimina repetições
    de espaços seguidos e espaços iniciais e finais.
    
    limpa_texto: cad. carateres --> cad. carateres
    """

    texto=texto.split()
    return ' '.join(texto)


def corta_texto(texto, largura):
    """
    Devolve um tuplo constituído por 2 cadeias de carateres, que correspondem ao texto cortado em 2.

    Argumentos:
        texto:cadeia de carateres
        largura:inteiro (positivo)
    No fundo, o texto é cortado em 2 partes, consoante a largura
    recebida em que a primeira parte tem um comprimento máximo
    igual à largura, e a outra contém o resto do texto.

    corta_texto: cad. carateres x inteiro --> tuplo
    """
    
    if len(texto)==largura or ' ' not in texto:
        return (texto,'') 
        #Texto tem tamanho igual à largura ou é vazio ou contém apenas uma palavra
    
    elif texto[largura-1]==' ':
        return (texto[:largura-1],texto[largura:])
        #O carater onde o texto tem tamanho igual à largura é um espaço

    elif texto[largura]==' ': 
        return (texto[:largura],texto[largura+1:])
        #O carater onde o texto tem tamanho igual à largura constitui o fim de
        #uma palavra.
    
    elif texto[largura]!=' ':
        texto_cortado=texto[:largura]
        #O carater onde o texto tem tamanho igual à largura é uma letra e não
        #constitui o fim de uma palvra.    

        for i in range(largura-1,0,-1): #Procura-se o espaço anterior mais próximo
            if texto_cortado[i]==' ':
                i_espaco_mais_proximo=i
                break
        
        return (texto[:i_espaco_mais_proximo],texto[i_espaco_mais_proximo+1:])
        #O texto é cortado no espaço anterior mais próximo de modo a não cortar
        #uma palavra.

def insere_espacos(texto, largura):
    """
    Devolve um novo texto com comprimento igual à largura, inserindo espaços.

    Argumentos:
        texto:cadeia de carateres
        largura: inteiro (positivo)
    No fundo, insere-se espaços entre as palavras do texto de modo
    uniforme da esquerda para a direita até ter o tamanho pretendido.
    Se o texto for apenas uma palavra, então os espaços são
    adicionados no fim.

    insere_espacos: cad. carateres x inteiro --> cad. carateres
    """      

    if ' ' in texto: #O texto tem mais de uma palavra
        lista_espacos_a_adicionar=[0]*(len(texto)-len(texto.replace(' ','')))
        #É criada uma lista de tamanho igual ao número de espaços iniciais cujos
        #elementos são zero.
        soma=0
        
        while soma!=(largura-len(texto)): 
            
            for i in range(len(lista_espacos_a_adicionar)):
                soma=0
                lista_espacos_a_adicionar[i]+=1
                
                for elementos in lista_espacos_a_adicionar:
                    soma+=elementos
                
                if soma==largura-len(texto):
                    break
        #A cada elemento da lista adiciona-se +1 até que a soma dos elementos da
        #lista seja igual à diferença entre a largura e o comprimento do texto,
        #verificando sempre esta condição após cada adição de "+1".

        texto=texto.split()
        texto_final=''
        iterador_lista=iter(lista_espacos_a_adicionar)
        
        for i in range(len(texto)):
            
            if texto[i]!=texto[-1]:
                texto_final+=texto[i]+' '*(next(iterador_lista)+1)
            
            else:
                texto_final+=texto[i]
        #O texto final é formado adicionando-se ora uma palavra ora o número de
        #espaços necessários (elemento da lista +1), até se chegar à palavra
        #final onde se apenas adiciona esta.
    
    else: #O texto tem apenas uma palavra.
        texto_final=texto.ljust(largura)
    return texto_final


def justifica_texto(texto, largura):
    """
    Devolve um tuplo de cadeias de carateres justificadas.

    Argumentos:
        texto: cadeia de carateres (não vazia, com palavras de tamanho menor que
                                    a largura)
        largura: inteiro (positivo)
    Aplicam-se funções anteriores (limpa_texto, corta_texto, insere_espacos)
    de modo justificá-lo. É também verificado os argumentos recebidos,
    gerando um ValueError com a mensagem:"justifica_texto: argumentos
    inválidos" em caso de argumento(s) errados.
    
    justifica_texto: cad. carateres x inteiro --> tuplo
    """ 
    
    if not isinstance(texto,str) or texto=='' or not isinstance(largura,int) or largura<0:
        raise ValueError ('justifica_texto: argumentos invalidos')
        #Verifica se o texto de entrada é uma cadeia de carateres, não vazio e
        #se a largura é um inteiro positivo.
    
    texto_verifica_palavras=texto.split()
    for palavras in texto_verifica_palavras:
        if len(palavras)>largura:
                raise ValueError ('justifica_texto: argumentos invalidos')
                #Verifica se todas as palavras do texto têm um comprimento menor do que a
                #largura recebida
    
    texto=limpa_texto(texto)
        
    if len(texto)>largura:
        texto=corta_texto(texto,largura)
        resto_do_texto=texto[-1] 
        i=0
        while len(resto_do_texto)>largura:
            texto=texto[:i+1]+corta_texto(resto_do_texto,largura)
            resto_do_texto=texto[-1]
            i+=1
        #O texto é todo cortado, pelo que cada parte do texto tem um comprimento
        #máximo igual à largura.
        texto_final=()
            
        for i in range(len(texto)):
                
            if texto[i]!=texto[-1]:
                texto_espacos=insere_espacos(texto[i],largura)
                texto_final+=(texto_espacos,)
            #São inseridos espaços de modo a que todos os elementos tenham um
            #comprimento igual à largura.
            else:
                texto_final+=(texto[i].ljust(largura),)
            #É a última cadeia do tuplo, logo os espaços são inseridos no fim.
    else:
        texto_final=(texto.ljust(largura),)
        #O tamanho do texto é inferior à largura (o tuplo tem um único elemento),
        #logo os espaços são adicionados no fim
    return texto_final
