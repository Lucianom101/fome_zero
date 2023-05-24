# ========================================================================================================================================#
# 1. Bibliotecas
# ========================================================================================================================================#
import pandas as pd
import inflection
import numpy as np
import streamlit as st
import folium
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

# st.dataframe(df)

# ========================================================================================================================================#
# 5. Barra Lateral
# ========================================================================================================================================#

vImagemIcon = Image.open( 'images/home.png' )
st.set_page_config( page_title='Home', page_icon=vImagemIcon, layout='wide' )

# st.sidebar.divider()

with st.sidebar.container():
 
    col1, col2 = st.sidebar.columns( 2, )

    with col1:
        vImagem = Image.open( 'images/logo.png' )
        st.image( vImagem, width=140 )

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
# 6. Main Page
# ========================================================================================================================================#

with st.container():
    st.markdown( '# Fome Zero Company' )
    st.markdown( '## O Melhor lugar para encontrar seu mais novo restaurante favorito!' )

with st.container():
    st.markdown( '### Temos as seguintes marcas dentro da nossa plataforma:' )

    col1, col2, col3, col4, col5 = st.columns( spec=5, gap='medium' )

    with col1:
        st.metric( 'Restaurantes Cadastrados', df1[ 'restaurant_id' ].nunique() )

    with col2:
        st.metric( 'Países Cadastrados', df1[ 'country_code' ].nunique() )

    with col3:
        st.metric( 'Cidades Cadastrados', df1[ 'city' ].nunique() )

    with col4:
        st.metric( 'Avaliações feitas na palataforma', '{:_}'.format( df1[ 'votes' ].sum() ).replace( '.', '.' ).replace( '_', '.' ) )

    with col5:
        st.metric( 'Tipos de culinárias oferecidas', df1[ 'cuisines' ].nunique() )

with st.container():
    cols = [ 'restaurant_name', 'rating_color','average_cost_for_two', 'currency', 'cuisines', 'aggregate_rating', 'latitude', 'longitude' ]
    df_aux = df.loc[ :, cols ].groupby( [ 'restaurant_name', 'rating_color','average_cost_for_two', 'currency', 'cuisines', 'aggregate_rating' ] ).median().reset_index()

    map = folium.Map( zoom_start=100 )
    marker_cluster = MarkerCluster().add_to(map)

    for index, location_info in df_aux.iterrows():
        html = ('<strong>' + location_info['restaurant_name'] + '</strong><br><br>'
              + 'Price: ' + str( '{:.2f}'.format( location_info['average_cost_for_two'] ).replace('.', ',') ) + ' ('
              + location_info['currency'] + ') for two<br>'
              + 'Type: ' + location_info['cuisines'] + '<br>'
              + 'Aggregate Rating: ' + str( location_info['aggregate_rating'] ) + '/5.0')
        
        iframe = folium.IFrame(html=html, width=280, height=150)
        
        popup = folium.Popup( html=iframe, max_width=280 )
        
        folium.Marker( location=[ location_info['latitude'],
                        location_info['longitude'] ],
                       popup=popup,
                       icon=folium.Icon(icon='glyphicon glyphicon-cutlery', color=color_name( location_info['rating_color'] )) ).add_to( marker_cluster )

    folium.LayerControl().add_to( map )
    folium_static( map, width=1024, height=600 )

#     📊
# Main Page
# 🌍
# Countries
# 🏙️
# Cities
# 🍽️
# Cuisines