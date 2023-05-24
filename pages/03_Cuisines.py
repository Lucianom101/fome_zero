# ========================================================================================================================================#
# 1. Bibliotecas
# ========================================================================================================================================#
import pandas as pd
import inflection
import numpy as np
import streamlit as st
import folium
import plotly.express as px
import plotly.graph_objects as go
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

# ========================================================================================================================================#
# 2. Importando a base de dados
# ========================================================================================================================================#
df = pd.read_csv('dataset/zomato.csv')

# ========================================================================================================================================#
# 3. Funções e dicionários
# ========================================================================================================================================#

# 3.1 Criação do nome das Cores
COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]

# 3.2 Preenchimento do nome dos países
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}

def country_name(country_id):
    return COUNTRIES[country_id]

# 3.3 Criação do Tipo de Categoria de Comida
def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

# 3.4 Renomear as colunas do DataFrame    
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new

    return df

# 3.5 Total de tipos de culinárias disponíveis
def fnc_tot_tp_culinaria( df ):
    vListaCuisines = ( set( df['cuisines'] ) )
    vListaTotalCuisine = []
    
    for vCuisine in vListaCuisines:
        vTeste = vCuisine.split(',')
        # print(vTeste)
        for vPalavra in vTeste:
            vPalavra = vPalavra.strip()
            # print(vPalavra)
            if vPalavra in vListaTotalCuisine:
                None
            
            else:
                vListaTotalCuisine.append( vPalavra )

    df_aux = pd.DataFrame(vListaTotalCuisine)
    
    return df_aux.count()

# 3.6 Calculos por país
def fnc_calc_per_country( flag, tp_calc, df ):
    v01 = 0
    v02 = 0
    vList01 = []
    vList02 = []

    # Quantidade de cidades registradas por pais
    if flag == 1:
        for i in df['country_code'].unique():
            df_aux01 = df.loc[ ( df['country_code'] == i ), [ 'city' ] ]
            v01 = len( df_aux01[ 'city' ].unique() )

            vList01.append( country_name( i ) )
            vList02.append( v01 )
            data = { 'countries': vList01,
                     'num_cities' : vList02 }

            df_return = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            return df_return
        
        elif tp_calc == 'maior':
            return country_name( vMaiorPais )

    # Quantidade de restaurantes registrados por pais    
    elif flag == 2:
        for i in df['country_code'].unique():
            df_aux01 = df.loc[ ( df['country_code'] == i ), [ 'restaurant_id' ] ]
            v01 = len( df_aux01[ 'restaurant_id' ].unique() )

            vList01.append( country_name( i ) )
            vList02.append( v01 )

            data = { 'countries': vList01,
                     'num_restaurants' : vList02 }

            df_return = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            return df_return
        
        elif tp_calc == 'maior':
            return country_name( vMaiorPais )

    # Quantidade de restaurantes com nivel de preço igual a 4 (gourmet)    
    elif flag == 3:
        for i in df['country_code'].unique():
            df_aux01 = df.loc[ ( ( df['country_code'] == i) & ( df[ 'price_range' ] == 4 ) ), [ 'restaurant_id' ] ]
            v01 = len( df_aux01[ 'restaurant_id' ].unique() )

            vList01.append( country_name( i ) )
            vList02.append( v01 )

            data = { 'countries': vList01,
                     'num_restaurants' : vList02 }

            df_return = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            return df_return
        
        elif tp_calc == 'maior':
            return country_name( vMaiorPais )
    
    # Quantidade de culinarias unicas
    if flag == 4:
        for i in df['country_code'].unique():
            df_aux01 = df.loc[ ( df['country_code'] == i ), [ 'cuisines' ] ]
            v01 = len( df_aux01[ 'cuisines' ].unique() )

            vList01.append( country_name( i ) )
            vList02.append( v01 )
            data = { 'countries': vList01,
                     'num_cuisines' : vList02 }

            df_return = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            return df_return
        
        elif tp_calc == 'maior':
            return country_name( vMaiorPais )
        
    # Soma de avaliações por país
    if flag == 5:
        for i in df['country_code'].unique():
            df_aux01 = df.loc[ ( df['country_code'] == i ), [ 'votes' ] ]
            v01 = df_aux01[ 'votes' ].sum()

            vList01.append( country_name( i ) )
            vList02.append( v01 )
            data = { 'countries': vList01,
                     'qt_votes' : vList02 }

            df_return = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            return df_return
        
        elif tp_calc == 'maior':
            return country_name( vMaiorPais )
        
    # Quantidade de restaurantes que fazem entrega
    if flag == 6:
        for i in df['country_code'].unique():
            df_aux01 = df.loc[ ( ( df['country_code'] == i) & ( df[ 'is_delivering_now' ] == 1 ) ), : ]
            v01 = len( df_aux01 )

            vList01.append( country_name( i ) )
            vList02.append( v01 )
            data = { 'countries': vList01,
                     'qt_delivery' : vList02 }

            df_return = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            return df_return
        
        elif tp_calc == 'maior':
            return country_name( vMaiorPais )
        
    # Quantidade de restaurantes que aceitam reservas
    if flag == 7:
        for i in df['country_code'].unique():
            df_aux01 = df.loc[ ( ( df['country_code'] == i) & ( df[ 'has_table_booking' ] == 1 ) ), : ]
            v01 = len( df_aux01 )

            vList01.append( country_name( i ) )
            vList02.append( v01 )
            data = { 'countries': vList01,
                     'qt_booking' : vList02 }

            df_return = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            return df_return
        
        elif tp_calc == 'maior':
            return country_name( vMaiorPais )
        
# ========================================================================================================================================#
# 4. Limpezas
# ========================================================================================================================================#

# 4.1. Renomeando as colunas
df = rename_columns( df )

# 4.2. Removenco as linhas em branco
# cuisines
df.dropna( subset=[ 'cuisines' ], inplace=True )

# 4.3. Criando a coluna cuisine_category

# 4.4. Criando a coluna country_name
df[ 'country_name' ] = df[ 'country_code' ].apply( lambda x: country_name( x ) )

# 4.5. Categorizando os restaurantes para somente um tipo de culinária(cuisines)
df['cuisines'] = df['cuisines'].astype(str)
df['cuisines'] = df.loc[ :, 'cuisines' ].apply( lambda x: x.split( ',' )[0] )

# 4.6. Removendo Cuisines do tipo Mineira e Drinks Only
df = df.loc[( df['cuisines'] != 'Drinks Only') & ( df['cuisines'] != 'Mineira' ) & ( df['cuisines'] != 'NaN' ), : ]

# 4.7. Removendo linhas duplicadas
df = df.drop_duplicates()

# ========================================================================================================================================#
# 5. Barra Lateral
# ========================================================================================================================================#

vImagemIcon = Image.open( 'images/home.png' )
st.set_page_config( page_title='Home', page_icon=vImagemIcon, layout='wide' )

col1, col2 = st.sidebar.columns( 2, )

with col1:
    vImagem = Image.open( 'images/logo.png' )
    st.image( vImagem, width=100 )

with col2: 
    st.markdown( '# Fome Zero' )

with st.sidebar.container():
    st.markdown( '## Filtros' )

    vRestUnique = df[ 'country_name' ].unique()

    vPaises_select = st.sidebar.multiselect(
        'Escolha os países que deseja visualizar os restaurantes',
        vRestUnique,
        default=[ 'Brazil', 'Canada', 'England', 'South Africa', 'Qatar', 'Australia' ]
    )

    vQtdeRestaurantes = int( st.sidebar.slider(
        label='Selecione a quantidade de Restaurantes que deseja visualizar',
        value=10,
        min_value=1,
        max_value=20
    ))

    vCuisineUnique = df[ 'cuisines' ].unique()

    vCuisine_select = st.sidebar.multiselect(
        'Escolha os países que deseja visualizar os restaurantes',
        vCuisineUnique,
        default=[ 'Home-made', 'BBQ', 'Japanese', 'Brazilian', 'Arabian', 'American', 'Italian' ]
    )

# Garantindo os números sem aplicar o filtro
df1 = df.copy()
df2 = df.copy()

# Filtro de País
linhas_selecionadas = df['country_name'].isin( vPaises_select )
df = df.loc[ linhas_selecionadas, : ]
df2 = df.loc[ linhas_selecionadas, : ]

# Filtro de culinárias
linhas_selecionadas = df['cuisines'].isin( vCuisine_select )
df2 = df.loc[ linhas_selecionadas, : ]

# Filtro de quantidade de restaurantes
df = df.iloc[0:vQtdeRestaurantes].sort_values( 'aggregate_rating' )
df2 = df.iloc[0:vQtdeRestaurantes].sort_values( 'aggregate_rating' )

# ========================================================================================================================================#
# 6. Countries
# ========================================================================================================================================#

with st.container():
    st.markdown( '# Visão Tipos de Cozinhas' )
    

with st.container():
    st.markdown( '## Melhores Restaurantes dos Principais tipos Culinários' )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        cols = [ 'aggregate_rating', 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ]
        df_aux = ( df1.loc[ ( df1[ 'cuisines' ] == 'Italian' ), cols ].groupby( [ 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ] )
                                                                     .mean()
                                                                     .sort_values( [ 'aggregate_rating', 'restaurant_id' ], ascending=[ False, True ] )
                                                                     .reset_index() )
        
        st.metric( label='Italiana: ' + df_aux['restaurant_name'][0],
                   value=df_aux[ 'aggregate_rating' ][0].astype(str) + '/5.0',
                   help='País: ' +  df_aux['country_name'][0] + '  \n\n' +
                        'Cidade: ' + df_aux['city'][0] + '  \n\n' +
                        'Média valor para dois: ' + df_aux['average_cost_for_two'][0].astype(float).astype(str) + '(' + df_aux['currency'][0] + ')' )
    
    with col2:
        cols = [ 'aggregate_rating', 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ]
        df_aux = ( df1.loc[ ( df1[ 'cuisines' ] == 'American' ), cols ].groupby( [ 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ] )
                                                                     .mean()
                                                                     .sort_values( [ 'aggregate_rating', 'restaurant_id' ], ascending=[ False, True ] )
                                                                     .reset_index() )
        
        st.metric( label='Italiana: ' + df_aux['restaurant_name'][0],
                   value=df_aux[ 'aggregate_rating' ][0].astype(str) + '/5.0',
                   help='País: ' +  df_aux['country_name'][0] + '  \n\n' +
                        'Cidade: ' + df_aux['city'][0] + '  \n\n' +
                        'Média valor para dois: ' + df_aux['average_cost_for_two'][0].astype(float).astype(str) + '(' + df_aux['currency'][0] + ')' )

    with col3:
        cols = [ 'aggregate_rating', 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ]
        df_aux = ( df1.loc[ ( df1[ 'cuisines' ] == 'Arabian' ), cols ].groupby( [ 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ] )
                                                                     .mean()
                                                                     .sort_values( [ 'aggregate_rating', 'restaurant_id' ], ascending=[ False, True ] )
                                                                     .reset_index() )
        
        st.metric( label='Italiana: ' + df_aux['restaurant_name'][0],
                   value=df_aux[ 'aggregate_rating' ][0].astype(str) + '/5.0',
                   help='País: ' +  df_aux['country_name'][0] + '  \n\n' +
                        'Cidade: ' + df_aux['city'][0] + '  \n\n' +
                        'Média valor para dois: ' + df_aux['average_cost_for_two'][0].astype(float).astype(str) + '(' + df_aux['currency'][0] + ')' )

    with col4:
        cols = [ 'aggregate_rating', 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ]
        df_aux = ( df1.loc[ ( df1[ 'cuisines' ] == 'Japanese' ), cols ].groupby( [ 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ] )
                                                                     .mean()
                                                                     .sort_values( [ 'aggregate_rating', 'restaurant_id' ], ascending=[ False, True ] )
                                                                     .reset_index() )
        
        st.metric( label='Italiana: ' + df_aux['restaurant_name'][0],
                   value=df_aux[ 'aggregate_rating' ][0].astype(str) + '/5.0',
                   help='País: ' +  df_aux['country_name'][0] + '  \n\n' +
                        'Cidade: ' + df_aux['city'][0] + '  \n\n' +
                        'Média valor para dois: ' + df_aux['average_cost_for_two'][0].astype(float).astype(str) + '(' + df_aux['currency'][0] + ')' )

    with col5:
        cols = [ 'aggregate_rating', 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ]
        df_aux = ( df1.loc[ ( df1[ 'cuisines' ] == 'Brazilian' ), cols ].groupby( [ 'restaurant_name', 'restaurant_id', 'country_name', 'city', 'average_cost_for_two', 'currency' ] )
                                                                     .mean()
                                                                     .sort_values( [ 'aggregate_rating', 'restaurant_id' ], ascending=[ False, True ] )
                                                                     .reset_index() )
        
        st.metric( label='Italiana: ' + df_aux['restaurant_name'][0],
                   value=df_aux[ 'aggregate_rating' ][0].astype(str) + '/5.0',
                   help='País: ' +  df_aux['country_name'][0] + '  \n\n' +
                        'Cidade: ' + df_aux['city'][0] + '  \n\n' +
                        'Média valor para dois: ' + df_aux['average_cost_for_two'][0].astype(float).astype(str) + '(' + df_aux['currency'][0] + ')' )

with st.container():
    st.markdown( '### Top ' + str( len( df2 ) ) + ' Restaurantes' )
    cols = [ 'restaurant_id', 'restaurant_name', 'country_name', 'city', 'cuisines', 'average_cost_for_two', 'aggregate_rating', 'votes' ]
    st.dataframe( df2.loc[ :, cols ].sort_values( [ 'aggregate_rating', 'votes' ], ascending=False ).head(len( df )).reset_index() )

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        cols = [ 'cuisines', 'aggregate_rating' ]
        df_aux = df.loc[ :, cols ].groupby( [ 'cuisines' ] ).mean().round(2).sort_values( 'aggregate_rating', ascending=False ).reset_index().head(10)
        fig = px.bar(df_aux,
                     y='aggregate_rating', x='cuisines',
                     labels={ 'aggregate_rating': 'Média da Avaliação Média',
                              'cuisines': 'Tipos de Culinária' },
                     text='aggregate_rating',
                     title='Top 10 melhores tipos de culinária').update_layout( plot_bgcolor='white',
                                                                                barmode='stack',
                                                                                title_text='Top ' + str( len( df ) ) + ' melhores tipos de culinária',
                                                                                title_x=0.2)
        st.plotly_chart( fig, use_container_width=True )
    
    with col2:
        cols = [ 'cuisines', 'aggregate_rating' ]
        df_aux = df.loc[ :, cols ].groupby( [ 'cuisines' ] ).mean().round(2).sort_values( 'aggregate_rating' ).reset_index().head(10)
        fig = px.bar(df_aux,
                     y='aggregate_rating', x='cuisines',
                     labels={ 'aggregate_rating': 'Média da Avaliação Média',
                              'cuisines': 'Tipos de Culinária' },
                     text='aggregate_rating',
                     title='Top 10 piores tipos de culinária').update_layout( plot_bgcolor='white',
                                                                              barmode='stack',
                                                                              title_text='Top ' + str( len( df ) ) + ' piores tipos de culinária',
                                                                              title_x=0.2)
        st.plotly_chart( fig, use_container_width=True )
