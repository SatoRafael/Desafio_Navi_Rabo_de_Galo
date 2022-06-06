# Desafio_Navi_Rabo_de_Galo

Inicialmente, importamos as bibliotecas necessárias: Pandas para análise dos dados, especificamente das tarifas, streamlit para criar uma interface interativa, streamlit_lottie para adicionar recursos visuais e request para extrair informações e imagens da internet.

Com o streamlit criamos a página do E-Cred a partir de containers, e cada container possui funções ou informações distintas. No primeiro momento adicionamos o título e definimos o layout da página em seguida adicionamos recursos visuais por meio do request e streamlit_lottie.

Construímos cada modulo, sendo o primeiro um texto da CCEE sobre as vantagens deste modelo de negócio para o consumidor e produtor de energia.
O segundo container traz as vantagens do modelo de negócios para os consumidores, acrescentando mais um recurso visual neste container.
O terceiro container apresenta as vantagens para quem venderá na plataforma, ou seja, o gerador distribuído.

O próximo container contém um link que direciona para o nosso vídeo com a proposta do nosso modelo de negócios para o público.
No quinto container montamos uma calculadora de créditos disponíveis, na visão do vendedor, em base a produção de kWh, horas produzidas no mês e a tarifa dependendo de sua distribuidora de energia.

Para definir a produção montamos um slider que varia entre 0 e 1000 kWh e para as horas também é um slider que varia entre 0 720 horas. Fizemos uma selectbox para selecionar a distribuidora local, com isso, o script irá selecionar essa informação do arquivo RankingB1-23-12-2021 extraído do site da ANEEL. Ao pressionar o botão de cálculo, será executada a função de calculo que se baseia na multiplicação das variáveis apresentadas. E as o cálculo final é apresentado para o usuário.

O container seguinte apresenta a visão do comprador, que traz a informação compilada.

Por ultimo fizemos um modelo de login para utilizar a plataforma.
