#   O \n é bastante utilizado na momento da escrita do arquivo para pular linha
#   se utilizarmos o print para mostrar a linha, teriamos duas quebras de linha
#   já que o print executa uma quebra de linha por padrão
#   A funcao strip() remove os espacos em branco do começo e final da string
#   ela tambem remove todos os caracateres de escape \n \t \r
#   Desta forma podemos imprimir o dado "limpo" do arquivo

arquivo = open('arquivo3.txt', 'r')
for linha in arquivo:
    linha_limpa = linha.strip()
    print(linha_limpa)
arquivo.close()
