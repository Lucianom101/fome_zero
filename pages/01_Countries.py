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
# df = pd.read_csv('dataset/zomato.csv')

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
        for i in df['country_name'].unique():
            df_aux01 = df.loc[ ( df['country_name'] == i ), [ 'city' ] ]
            v01 = len( df_aux01[ 'city' ].unique() )

            vList01.append( i )
            vList02.append( v01 )
            data = { 'countries': vList01,
                     'num_cities' : vList02 }

            data = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            data.columns = [ 'Países', 'Quantidade de Cidades' ]
            fig = go.Figure()
            fig = ( px.bar(data,
                           text='Quantidade de Cidades',
                           x='Países', y='Quantidade de Cidades').update_traces( marker_color='#66b3ff' )
                                                                      .update_layout( plot_bgcolor='white',
                                                                                      barmode='stack',
                                                                                      title_text='Quantidade de Cidades Registradas por País',
                                                                                      title_x=0.3,
                                                                                      xaxis={'categoryorder': 'total descending'} )
                                                                    )
            return fig
        
        elif tp_calc == 'maior':
            return vMaiorPais

    # Quantidade de restaurantes registrados por pais    
    elif flag == 2:
        for i in df['country_name'].unique():
            df_aux01 = df.loc[ ( df['country_name'] == i ), [ 'restaurant_id' ] ]
            v01 = len( df_aux01[ 'restaurant_id' ].unique() )

            vList01.append( i )
            vList02.append( v01 )

            data = { 'countries': vList01,
                     'num_restaurants' : vList02 }

            data = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        data.columns = [ 'Países', 'Quantidade de Restaurantes' ]
        if tp_calc == 'grafico':
            
            fig = go.Figure()
            fig = ( px.bar(data,
                           text='Quantidade de Restaurantes',
                           x='Países', y='Quantidade de Restaurantes').update_traces( marker_color='#66b3ff' )
                                                                      .update_layout( plot_bgcolor='white',
                                                                                      barmode='stack',
                                                                                      title_text='Quantidade de Restaurantes Registrados por País',
                                                                                      title_x=0.3,
                                                                                      xaxis={'categoryorder': 'total descending'} )
                                                                    )
            return fig
        
        elif tp_calc == 'maior':
            return vMaiorPais

    # Média de avaliações por país
    if flag == 5:
        for i in df['country_name'].unique():
            df_aux01 = df.loc[ ( df['country_name'] == i ), [ 'votes' ] ]
            v01 = df_aux01[ 'votes' ].mean().round(2)

            vList01.append( i )
            vList02.append( v01 )
            data = { 'countries': vList01,
                     'qt_votes' : vList02 }

            data = pd.DataFrame( data )

            if v01 > v02:
                v02 = v01
                vMaiorPais = i

        if tp_calc == 'grafico':
            data.columns = [ 'Países', 'Quantidade de Avaliações' ]
            fig = go.Figure()
            fig = ( px.bar(data,
                           text='Quantidade de Avaliações',
                           text_auto='f.2',
                           x='Países', y='Quantidade de Avaliações').update_traces( marker_color='#66b3ff' )
                                                                      .update_layout( plot_bgcolor='white',
                                                                                      barmode='stack',
                                                                                      title_text='Quantidade de Avaliações feitas por País',
                                                                                      title_x=0.3,
                                                                                      xaxis={'categoryorder': 'total descending',
                                                                                             'tickformat': '.0%'} )
                                                                                      )
            return fig
        
    # Média de Preço de um prato para duas pessoas por País
    if flag == 6:
        df_aux01 = ( df.loc[ :, [ 'average_cost_for_two', 'country_name' ] ].groupby( [ 'country_name' ] )
                                                                            .mean()
                                                                            .sort_values( 'average_cost_for_two', ascending=False )
                                                                            .reset_index()
                                                                            .round(2) )
        
        df_aux01.columns = [ 'Países', 'Média de prato para duas Pessoas' ]
        fig = go.Figure()
        fig = ( px.bar(df_aux01,
                       text='Média de prato para duas Pessoas',
                       x='Países', y='Média de prato para duas Pessoas').update_traces( marker_color='#66b3ff' )
                                                                        .update_layout( plot_bgcolor='white',
                                                                                        title_text='Média de prato para duas Pessoas',
                                                                                        title_x=0.3,
                                                                                        xaxis={'categoryorder': 'total descending'} )
                                                                                    )
        return fig
        
# ========================================================================================================================================#
# 4. Limpezas
# ========================================================================================================================================#
df = pd.read_csv('dataset/zomato.csv')
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

with st.sidebar.container():
    st.markdown( '## Dados Tratados' )
    
    st.download_button( label=':arrow_down: Download', data=df.to_csv().encode('utf-8'), file_name='ZeroHungryCo.csv', mime='text/csv' )

# Garantindo os números sem aplicar o filtro
df1 = df.copy()

# Filtro de País
linhas_selecionadas = df['country_name'].isin( vPaises_select )
df = df.loc[ linhas_selecionadas, : ]

# ========================================================================================================================================#
# 6. Countries
# ========================================================================================================================================#

with st.container():
    st.markdown( '# Visão Países' )
    

with st.container():
    fig = fnc_calc_per_country( 2, 'grafico', df )
    st.plotly_chart( fig, use_container_width=True )

with st.container():
    fig = fnc_calc_per_country( 1, 'grafico', df )
    st.plotly_chart( fig, use_container_width=True )

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        fig = fnc_calc_per_country( 5, 'grafico', df )
        st.plotly_chart( fig, use_container_width=True )
    
    with col2:
        fig = fnc_calc_per_country( 6, 'grafico', df )
        st.plotly_chart( fig, use_container_width=True )