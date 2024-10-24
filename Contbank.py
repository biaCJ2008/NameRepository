from contaBancaria import ContaCorrente,CartaoCredito

conta_lira = ContaCorrente("Lira", "111.222.333-45", "Banco do Brasil", "212121")

cartao_lira = CartaoCredito("Lira", conta_lira)

print(cartao_lira.conta_corrente._num_conta)

print(cartao_lira.numero,
      cartao_lira.titular,
      cartao_lira.validade,
      cartao_lira.cod_seguranca,
      cartao_lira.limite)

