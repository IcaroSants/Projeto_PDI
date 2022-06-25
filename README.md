# Proj2_PDI_IA

1. Fundo: branco
2. Distância: 10 cm
3. Iluminação: Luz natural (entre 9h e 16h)
4. Posição: Horizontal (talo na horizontal)
4.0. baixar imagem como exemplo (https://static.todamateria.com.br/upload/57/d9/57d91894e93bc-folhas.jpg?auto_optimize=low)
4.1. da esquerda para direita
5. Foto exclusiva de uma folha
6. Resolução: 224 x 224, 1 mb

Carlos Estelita
@IcaroSants
IcaroSants
Pedro Elias
@LeandroScript
LeandroScript

 
Instituto Atlântico Academy Bootcamp


Squad 2

José Ícaro Santana Bernardes Leandro de Sousa Gonçalves Pedro Elias Ribeiro dos Santos Carlos Estellita Neto







Segmentação de Folhas de Plantas













2022
 
Resumo

Neste presente estudo, a partir de conhecimentos de processamento de imagens, a equipe elaborou um algoritmo que é capaz de medir atributos de folhas coletadas pelos integrantes. Desta forma, o projeto envolve em desenvolver uma função capaz de receber o caminho do diretório com qualquer quantidade de imagens de folhas e retornar suas características.
 

Sumário
Introdução	4
Objetivos	4
Metodologia	5
Aquisição de Imagens	5
Pré-Processamento de Imagens	5
Segmentação de Imagens	7
Métricas	10
Resultados e Discussões	12
Conclusões	13
Referências Bibliográficas	14
 
1.	Introdução

A área da visão computacional tem sido bastante popularizada, surgindo cada vez mais projetos que aplicam os seus princípios. O objetivo desta tecnologia está em equipar software e computadores com a capacidade de interpretar informação do mundo real, convertendo-a em dados legíveis e trabalháveis. Uma das áreas mais estudadas deste domínio é a de sistemas óticos, cuja função é a de detectar áreas, anomalias e propriedades presentes numa imagem.
Para o presente trabalho foram coletadas fotos de diversos tipos de folhas. Porém, no momento da aquisição das imagens, algums ruídos foram gerados, como sombras e até mesmo picos de claridade, o que dificulta um pouco o resultado final, fazendo com que seja necessário o pré-processamento, para a remoção dos ruídos. 
O desenvolvimento inicial da pesquisa consistiu em conhecer os principais conceitos que englobam o processamento digital de imagens (PDI), como por exemplo, a forma de representação digital de imagens coloridas e em tons de cinza, quais as principais técnicas e operadores utilizados para análise de imagens digitais,
Existem diversos métodos para a remoção e correção destes ruídos nas imagens, mas, nem sempre a aplicação destes acaba sendo uma atividade rápida e fácil, por conta das diversas etapas que alguns métodos apresentam.

1.1.	Objetivos

Desenvolver e testar técnicas e que facilitem a seleção, aquisição e pré-processamento de imagens e dados visuais envolvidos nas pesquisas desenvolvidas pelos pesquisadores do Curso de Computação Cognitiva do Instituto Atlântico.
O trabalho   envolve, em sua base de dados, 100 imagens de folhas, dentre as quais  serão  escolhidas 20 imagens para a execução do projeto inicial e determinação do padrão ouro para enfim,  após a escolha da melhor técnica de segmentação,  aplicarmos a melhor técnica ao corpo das 100 imagens. Para uma avaliação quantitativa teremos a elaboração de uma tabela resultante dos cálculos atribuídos à técnica de segmentação escolhida. 
É parte do objetivo a obtenção das medidas das larguras, alturas e áreas de cada folha nas imagens. 
Uma das ferramentas usadas para a obtenção da melhor técnica será a Intersection Over Union (IOU) que nos traz dados métricos comparativos. Essa será uma avaliação qualitativa das segmentações. 
 

2.	Metodologia

Neste Capítulo inicialmente são apresentadas as aquisições das imagens, as técnicas de pré-processamentos e segmentações das imagens.

2.1.	Aquisição de Imagens

No processo de obtenção das imagens, primeiramente, foram coletadas 100 folhas e em seguida, foi utilizado as seguintes etapas para a padronização do dataset: O fundo da imagem deve ser branco; a câmera deve estar a 10 centímetros de distância da folha, posicionada horizontalmente da esquerda para a direita e estar na resolução de 224x244 pixels, 1mb. A Figura 1 ilustra um exemplo de uma imagem original da folha. A imagem original da folha possui 3 cores do padrão RGB (red = vermelho, green = verde e blue = azul) e cada pixel pode ter valores entre 0 a
255. Além disso, ao final da criação do dataset, foi feito o padrão ouro em 20 imagens selecionadas, ou seja, a equipe manualmente binarizou as imagens para futuramente serem usadas como base para a identificação das acurácias de cada método de segmentação.

Figura 1: Exemplo de uma imagem da folha da planta.


Fonte: Autores.

2.2.	Pré-Processamento de Imagens

Nesta seção são abordados o pré-processamento das 3 técnicas propostas para a segmentação de imagens.

2.2.1.	Técnica 1
 
Na técnica 1, o pré-processamento é realizado na folha (Figura 2a) para obter a média dos tons de cinza do R, G e B. O Resultado é uma imagem com apenas 1 canal de cor conforme ilustrado na Figura 2b.

Figura 2: Exemplo do pré processamento da técnica 1: (a) imagem de original com canais RGB da folha e (b) imagem com a média dos canais RGB.


(a)	(b)

Fonte: Autores.

2.2.2.	Técnica 2

Percebe-se visualmente que todas as imagens das folhas utilizadas neste trabalho possuem cor predominante verde. Portanto, o pré-processamento da técnica tem como objetivo obter uma imagem que representa o canal verde da imagem original da folha (Figura 3a). O Resultado é uma imagem com apenas o canal de cor verde conforme ilustrado na Figura 3b.

Figura 3: Exemplo do pré processamento da técnica 2: (a) imagem de original com canais RGB da folha e (b) imagem com canal de cor verde.


(a)	(b)

Fonte: Autores.



2.2.3.	Técnica 3
 

Na técnica 3, o pré-processamento é realizado na folha (Figura 1) para obter a média dos tons de cinza do R, G e B. O Resultado é uma imagem com apenas 1 canal de cor conforme ilustrado na Figura 4a. Em seguida, é realizada uma operação por meio de um filtro gaussiano, com kernel 3x3 pixels, com intuito de remover ruídos na imagem (Figura 4a). A Figura 4b ilustra o resultado do filtro gaussiano.

Figura 4: Exemplo do pré processamento da técnica 3: (a) imagem com a média dos canais RGB e
(b)	imagem com a suavização gaussiana aplicada na imagem média dos canais RGB.


(a)	(b)

Fonte: Autores.


2.3.	Segmentação de Imagens

Nesta seção são apresentados os métodos de segmentação utilizados nas técnicas 1, 2 e 3.

2.3.1.	Técnica 1

Na técnica 1, foi utilizado o algoritmo de Chan-Vese para a segmentação. Esse método de segmentação ajusta de maneira ideal um modelo constante de duas fases para a imagem fornecida o limite de segmentação é representado implicitamente com uma função de conjunto de níveis, que permite que a segmentação lide com mudanças topológicas. Neste trabalho, aplica-se o método Chan-Vese na imagem da folha (Figura 5a) e o resultado pode ser observado na Figura 5b. A Figura 5c e Figura 5d ilustram outro exemplo da segmentação pelo método Chan-Vese.


Figura 5: Exemplo da segmentação da técnica 1: (a) imagem com a média dos canais RGB e (b) imagem resultado da segmentação com o método Chan-Vese, (c) média dos canais RGB e (d)
 

segmentação com o método Chan-Vese.


(a)	(b)


(c)	(d)

Fonte: Autores.


2.3.2.	Técnica 2

Na técnica 2, o método é baseado na detecção de contornos. Para isso, inicialmente, utiliza-se o método de limiarização de Otsu para determinar um valor de tom de cinza. O tom de cinza é utilizado como referência para separar regiões na imagem.
Os pixels de tons de cinza maiores que o tom de cinza definido pelo o método de Otsu são classificados com a cor branco (255) e os demais pixels são fundo da imagem (0). O Método é aplicado na imagem (Figura 6a) e o resultado pode ser observado na Figura 6b. Em seguida, a detecção de contornos é realizada no resultado da limiarização (Figura 6b) e o resultado pode ser observado na Figura 6c. Percebe-se na Figura 6c que o contorno de maior área interna é representado pelas bordas da folha. Portanto, o contorno de maior área interna representa a segmentação da folha e isso pode ser observado na Figura 6d.


Figura 6: Exemplo da segmentação da técnica 2: (a) imagem com canal de cor verde (b) imagem resultado da limiarização pelo método Otsu, (c) imagem detecção de contornos e (d) imagem do contorno de maior área interna.
 

 	 

(a)	(b)


(c)	(d)

Fonte: Autores.

2.3.3.	Técnica 3

Inicialmente, utiliza-se o método de limiarização de Otsu para determinar um valor de tom de cinza. O tom de cinza é utilizado como referência para separar regiões na imagem. Os pixels de tons de cinza maiores que o tom de cinza definido pelo o método de Otsu são classificados com a cor branco (255) e os demais pixels são fundo da imagem (0). O Método é aplicado no resultado do pré-processamento da técnica 3 (Figura 4b) e o resultado pode ser observado na Figura 7a.
Para minimizar ruídos na imagem, utiliza-se duas operações morfológicas: fechamento e abertura. O fechamento representa uma erosão seguida de dilatação e contribui para minimizar a presença de ruídos. A abertura representa dilatação seguida de erosão e tem o objetivo de fechar pequenos orifícios que podem ocorrer na segmentação da folha. A abertura deve ser aplicada no resultado do fechamento. Portanto, a Figura 7b representa um exemplo do fechamento e a Figura 7c representa a abertura, ou seja, a segmentação da folha.

Figura 7: Exemplo da segmentação da técnica 3: (a) imagem resultado da limiarização pelo método Otsu, (b) imagem resultado da operação de fechamento e (c) imagem resultado da segmentação pelo o método da abertura.
 

 	 	 

(a)		(b)	(c) Fonte: Autores.


2.4.	Métricas

Nesta seção são abordados os atributos de aŕea, comprimento, largura em pixels na imagem da folha de forma automática. A qualidade da segmentação é baseada na operação de intersection over union (IOU).

2.4.1.	Cálculo de Atributos

Existem 3 atributos que são obtidos no resultado da segmentação automática da folha, sendo estes a área, comprimento e largura em pixels. A área é definida pelo número de pixels que representa a segmentação da folha.
O comprimento e a largura são definidos pela distância euclidiana entre pontos. No total, existem 4 pontos que estão localizados nas bordas da folha. Neste caso, um ponto A é definido como sendo o mais próximo da primeira linha da imagem e o ponto B é o mais próximo da última linha da imagem. Um ponto C é definido como sendo o mais próximo da primeira coluna da imagem e o ponto D é o mais próximo da última coluna da imagem. Em seguida, é determinada a distância euclidiana de A para B e C para D. A maior distância representa o comprimento e a menor representa a largura. A Figura 7 ilustra linhas cinzas indicando a representação dessas medidas.


Figura 7: Exemplo do comprimento e largura: (a) imagem original da folha e (b) imagem da segmentação com linhas cinzas indicando o comprimento e largura.
 

 	 


(a)	(b)

Fonte: Autores.
	


2.4.2.	Avaliação Qualitativa da Segmentação

Adotando uma imagem que representa a segmentação automática da folha (
𝐼 ) e outra imagem representada pelo a segmentação manual da folha realizada no
𝑠
padrão ouro (𝐼 ). A qualidade da segmentação é avaliada pela a técnica IOU. IOU é
𝑅
a relação entre a interseção (𝐼  ∩ 𝐼 ) e a união (𝐼  ∪ 𝐼 ), conforme a equação 2.1.
𝑅	𝑠	𝑅	𝑠

𝐼 ∩𝐼
 
𝐼𝑂𝑈 =   𝑅	𝑠 
 
2.1
 
𝐼 ∪𝐼
𝑅	𝑠
 
3.	Resultados e Discussões

Os sistemas de aquisição e os algoritmos geraram diferentes resultados sobre os modelos testados que podem então ser usadas para comparar e escolher o melhor modelo para a aplicação apresentada.

3.1	Resultado do Cálculo de Atributos


A tabela 1 trata da avaliação quantitativa do projeto com relação aos cálculos atribuídos para a extração da largura, altura e área em pixels.

Tabela 1: Resultados dos valores métricos das imagens obtidos com dados sobre largura, altura e área em pixels.


Amostra	Largura(px)	Altura(px)	Área(px²)
1	folha 7	92	71	4002
2	folha 3	224	10	18319
3	folha 11	165.58	102	10122
4	folha 12	91	43	2918
5	folha 13	147.73	96	9003
6	folha 14	224	190	34965
7	folha 25	194	179	27004
8	folha 16	203	178	25448
9	folha 17	103	57	4066
10	folha 19	195	142	18344
11	folha 20	171.30	61	11659
12	folha 21	155.23	102	9444
13	folha 22	218	200	33858
14	folha 27	224	165	28548
15	folha 28	208	194	31133
16	folha 29	166.48	105	11834
17	folha 30	124	113	9716
18	folha 32	111	212	18212
19	folha 33	108.47	67	4546
20	folha 34	168.12	103	11218


Fonte: Autores.


3.2	Resultados da Avaliação Qualitativa da Segmentação                                                                                                                                                                                                                                                                                                                

	
O gráfico 1 mostra os resultados em valores percentuais de cada técnica de segmentação aplicada.




Gráfico 1: Resultado comparativo para detecção da melhor acurácia apresentada pelas segmentações.



Fonte: Autores.

A tabela 2 mostra os resultados em valores de  0,0 a 1 de cada técnica de segmentação aplicada.

Tabela 2: Resultado comparativo para detecção da melhor acurácia apresentada pelas segmentações em valores de 0 a 1.



IOU	Tec 01	Tec 02	Tec 03
Máximo	0,959	0,978	0,978
Desv. Padrão	0,273	0,128	0,083
Mínimo	0,131	0,494	0,679















Fonte: Autores 
4.	Conclusões
Com base nos resultados, a técnica 3 obteve resultados satisfatórios em relação às demais técnicas, pois obteve menor desvio padrão (0,083) e o valor mínimo (0,679) é superior às demais técnicas.
Sugestões de melhorias para cada técnica:
●	Técnica 1: Durante o método, nota-se que sombras também foram segmentadas. Logo, é considerável usar técnicas de detecção de contornos para poder aumentar a acurácia do algoritmo.
●	Técnica 2: Para que possa haver uma maior acurácia, pode ser útil utilizar operações morfológicas para remover os ruídos da folha segmentada.
●	Técnica 3: Uma hipótese para que a técnica de segmentação 3 seja melhor, é que possa ser usado novos parâmetros do elemento estruturador ou usar um diferente, como um disco, durante as operações morfológicas.
 
Referências Bibliográficas

MAREGONI, M.; STRINGHINI, D.. Tutorial: Introdução à Visão Computacional usando OpenCV. Revista RITA, v. XVI, n. 1, 2009.

Paul Viola and Michael J. Jones. Rapid Object Detection using a Boosted Cascade of Simple Features. IEEE CVPR, 2001.

Waithira, Sharon Immaculate. Getting started with OpenCV and Python. Medium. Disponível em: https://medium.com/the-andela-way/simple-operations-on-images-using-opencv-d37b26e6e3ab. Acessado em 20/06/2022.

Sheremet Oleksii. Intersection over union (IoU) calculation for evaluating an image segmentation model.  Disponível em: Intersection over union (IoU) calculation for evaluating an image segmentation model | by Oleksii Sheremet | Towards Data Science. Acessado em 01/06/2022.



