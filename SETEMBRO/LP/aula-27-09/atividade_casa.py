# escreva("[ 1 ] para gasolina, [ 2 ] para alcool : ")
# leia respostaCliente
# escreva("Quantos litros de combustivel voce quer? ")
# leia qtdeLitros

# se respostaCliente == 1 entao
#     precoComb = 5,82
#     valorTotal = precoComb * qtdeLitros
    
# seNao entao
#     precoComb = 2,51
#     valorTotal = precoComb * qtdeLitros
# fimSe

# escreva("O total foi de R$", valorTotal)

resposta_cliente = int(input('[ 1 ] para gasolina, [ 2 ] para alcool : '))
qtde_litros = float(input('Digite quantos litros o cliente deseja? '))

preco_comb = 0

if resposta_cliente == 1:
    preco_comb = 5.82
else :
    preco_comb = 2.51

valor_total = preco_comb * qtde_litros

print(f'O valor total eh: R$ {valor_total}')
