"""
 Documentando funções com Docstrings

 OBS: Podemos ter acesso á dociumentação de uma função em python
 utilizando a propriedade especial __doc__

 Podemos ainda fazer acesso a documentação com a função help()

"""

def diz_oi():
    """ Uma função que retorna a string 'oi'!"""
    return 'oi!'

def exponencial(numero, potencia=2):
    """
    FUNÇÃO QUE RETORNA POR PADRÃO O QUADRADO DE 'NÚMERO' OU 'NÚMERO' Á POTÊNCIA INFORMADA.
    :param numero: Número que desejamos gerar o exponencial.
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'

    """
    return numero == potencia