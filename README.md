# Fome Zero Company
## Projeto de dados para Dashboard com gráficos Fome Zero Company
## 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.

Você acaba de ser contratado como Cientista de Dados da empresa
Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra
a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer
utilizando dados.

O CEO Guerra também foi recém contratado e precisa entender melhor o negócio
para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards a partir dessas análises, para responder
às seguintes perguntas:

Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

Pais
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisadessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas do CEO e criar o dashboard solicitado.

## 2. Premissas do negócio
1. O modelo de negócio é de um marketplace.
2. Foram solicitadas visões de negócio específicas que são: Visão Geral, Visão por País, Visão por Cidade, Visão por Restaurantes e Visão por Tipos de Colunária.

## 3. Estratégia da solução
O dashboard desenvolvido foi montado utilizando as métricas que reflatem as visões principais do modelo de negócio da empresa:
1. Visão Geral
2. Visão por País
3. Visão por Cidade
4. Visão por Restaurantes
5. Visão por Tipos de Colunária

Cada visão mostra um conjunto de métricas a seguir:
1. Visão Geral:
    a. Restaurantes Cadastrados
    b. Países Cadastrados
    c. Cidades Cadastradas
    d. Avaliações feitas na palataforma
    e. Tipos de culinárias oferecidas
    f. Mapa gráfico de localização de todos os restaurantes cadastrados

2. Visão por País:
    a. Quantidade de restaurantes registrados por País
    b. Quantidade de cidades registradas por País
    c. Quantidade de avaliações feitas por País
    d. Média de valor de prato para duas pessoas

3. Visão por Cidade
    a. Top 10 cidades com mais restaurantes na base de dados
    b. Top 7 cidades com restaurantes com média de avaliação acima de 4
    c. Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5
    d. Top 10 cidades com mais restaurantes com tipos culinários distintos

5. Visão por Tipos de Colunária
    a. Melhores restaurantes dos principais tipos culinários
    b. Top restaurantes por votação
    c. Top melhores tipos de culinária
    d. Top piores tipos de culinária

## 4. Top 3 Insights de dados
1. Apesar da Índia possuir o maior número de cidades e restaurantes cadastrados disparado, o país que mais possui avaliações é a Indonésia.
2. A Inglaterra é o país que mais oferece tipos de culinária distintos entre todos os países da base.
3. Todos os 20 melhores restaurantes cadastrados na base são das Filipinas.

## 5. O produto Final do projeto
Painel online, hospedado em uma cloud e disponível para acesso em qualquer dispotitivo conectado à internet.

O painel pode ser acessado através desse link: https://lucianom101-fome-zero.streamlit.app/

## 6. Conclusão
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO Guerra.

É possível concluir que na Indonésia e na Australia são cobrados os maiores valores médios de um prato para duas pessoas dentre todos os países que possuem restaurantes registrados na Fome Zero. Sendo assim o ticket médio nestes países é disparado o maior entre os países que possuem clientes na empresa.

## 7. Próximos passos
1. Criar novos gráficos buscando relacionar outras informações disponíveis afim de encontrar mais insights de negócio para o CEO Guerra.
2. Melhorar a disposição dos gráficos nas páginas para melhor compreensão
