import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# cores heineken

heineken_green = '#007A33'
heineken_light = '#A9DFBF'
heineken_gray = '#F5F5F5'
text_secondary = '#555555'

# ler dados

df = pd.read_excel('sustentabilidade_heineken.xlsx')
df = df.rename(columns={'Emissões de CO₂ ': 'Emissões de CO₂(t)'})
df = df.dropna(subset=[
    'Mês', 'Emissões de CO₂(t)', 'Consumo de água (L/hl)', 'Energia renovável (%)',
    'Mulheres na liderança (%)', 'Pessoas negras na liderança (%)', 'Retornabilidade (%)'
])

# gráfico 1: emissões de co2

fig_co2 = px.line(df, x='Mês', y='Emissões de CO₂(t)',
                  title='🌱 Emissões de CO₂ - Evolução',
                  labels={'Emissões de CO₂(t)': 'Toneladas de CO₂', 'Mês': 'Mês'},
                  line_shape='spline')
fig_co2.update_traces(mode='lines+markers', line_color='#2E8B57', fill='tozeroy')
fig_co2.update_layout(hoverlabel=dict(bgcolor=heineken_green, font_size=14))

# gráfico 2: consumo de água

fig_agua = px.line(df, x='Mês', y='Consumo de água (L/hl)',
                   title='💧 Consumo de Água - Evolução',
                   labels={'Consumo de água (L/hl)': 'Litros por hectolitro', 'Mês': 'Mês'},
                   line_shape='spline')
fig_agua.update_traces(mode='lines+markers', line_color='#00BFFF', fill='tozeroy')

# gráfico 3: energia renovável

fig_energia = px.line(df, x='Mês', y='Energia renovável (%)',
                      title='⚡ Energia Renovável - Evolução',
                      labels={'Energia renovável (%)': 'Percentual (%)', 'Mês': 'Mês'},
                      line_shape='spline')
fig_energia.update_traces(mode='lines+markers', line_color='#FFD700', fill='tozeroy')
fig_energia.add_shape(type='line',
                      x0=df['Mês'].iloc[0], x1=df['Mês'].iloc[-1],
                      y0=100, y1=100,
                      line=dict(color='red', dash='dash'))

# gráfico 4: retornabilidade

fig_retornabilidade = px.bar(df, x='Mês', y='Retornabilidade (%)',
                             title='🔄 Retornabilidade de Embalagens',
                             labels={'Retornabilidade (%)': 'Percentual (%)', 'Mês': 'Mês'},
                             color_discrete_sequence=[heineken_green])

# gráfico 5: diversidade

fig_diversidade = px.line(df, x='Mês',
                          y=['Mulheres na liderança (%)', 'Pessoas negras na liderança (%)'],
                          title='🎯 Diversidade na Liderança',
                          labels={'value': 'Percentual (%)', 'Mês': 'Mês'},
                          line_shape='spline')
fig_diversidade.update_traces(mode='lines+markers', line_color='#FF69B4')

# iniciador

app = dash.Dash(__name__)
app.title = "Dashboard Sustentabilidade Heineken (Protótipo Não Oficial)"

# layout do app 

app.layout = html.Div(style={
    'backgroundImage': 'url("https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80")',
    'backgroundSize': 'cover',
    'backgroundPosition': 'center',
    'fontFamily': 'Arial',
    'minHeight': '100vh',
    'padding': '20px'
}, children=[
    html.Div(style={
        'backgroundColor': 'rgba(255,255,255,0.95)',
        'padding': '30px',
        'borderRadius': '12px',
        'boxShadow': '0 0 20px rgba(0,0,0,0.2)',
        'maxWidth': '1200px',
        'margin': 'auto'
    }, children=[
        html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0HmqwPyWTrKgLooqG3ZMrLd9OAXRayLgxEQ&s',
                 style={'height': '80px', 'margin': '20px auto', 'display': 'block'}),

        html.H1("🌿 Dashboard de Sustentabilidade – Heineken Brasil", style={
            'textAlign': 'center',
            'color': heineken_green
        }),

        html.H4("“Brewing a Better World”", style={
            'textAlign': 'center',
            'color': text_secondary,
            'fontStyle': 'italic',
            'marginBottom': '30px'
        }),

        html.P("Este painel interativo apresenta a evolução de indicadores ambientais e sociais da Heineken Brasil. "
               "Os dados simulados refletem metas reais da companhia, alinhadas à estratégia global EverGreen. "
               "O objetivo é facilitar o acompanhamento de desempenho ESG de forma visual, acessível e estratégica.",
               style={'textAlign': 'justify', 'color': text_secondary, 'fontSize': '16px', 'marginBottom': '30px'}),

        html.Div([
            html.Div([
                html.H4("🌱 CO₂ Atual"),
                html.P(f"{df['Emissões de CO₂(t)'].iloc[-1]} toneladas", style={'fontSize': '24px', 'color': heineken_green})
            ], style={'width': '30%', 'display': 'inline-block', 'backgroundColor': heineken_light,
                      'padding': '20px', 'margin': '10px', 'borderRadius': '10px'}),

            html.Div([
                html.H4("⚡ Energia Renovável"),
                html.P(f"{df['Energia renovável (%)'].iloc[-1]}%", style={'fontSize': '24px', 'color': heineken_green})
            ], style={'width': '30%', 'display': 'inline-block', 'backgroundColor': heineken_light,
                      'padding': '20px', 'margin': '10px', 'borderRadius': '10px'}),

            html.Div([
                html.H4("🎯 Diversidade"),
            html.P(f"{df['Mulheres na liderança (%)'].iloc[-1]}% mulheres • {df['Pessoas negras na liderança (%)'].iloc[-1]}% negras",
                       style={'fontSize': '18px', 'color': heineken_green})
            ], style={'width': '30%', 'display': 'inline-block', 'backgroundColor': heineken_light,
                      'padding': '20px', 'margin': '10px', 'borderRadius': '10px'})
        ], style={'textAlign': 'center'}),

        html.Hr(style={'margin': '40px 0'}),

        html.Div([
            html.H3("📊 Indicadores por Categoria", style={'color': heineken_green, 'textAlign': 'center'}),
            dcc.Tabs([
                dcc.Tab(label='🌱 Ambientais', children=[
                    dcc.Graph(figure=fig_co2, style={'transition': 'opacity 1s ease-in-out'}),
                    dcc.Graph(figure=fig_agua, style={'transition': 'opacity 1s ease-in-out'}),
                    dcc.Graph(figure=fig_energia, style={'transition': 'opacity 1s ease-in-out'})
                ]),
                dcc.Tab(label='🔄 Embalagens', children=[
                    dcc.Graph(figure=fig_retornabilidade, style={'transition': 'opacity 1s ease-in-out'})
                ]),
                dcc.Tab(label='🎯 Diversidade', children=[
                    dcc.Graph(figure=fig_diversidade, style={'transition': 'opacity 1s ease-in-out'})
                ])
            ])
        ], style={'padding': '0 40px'}),

        html.Footer("Desenvolvido por Alline • Analista de Planejamento Júnior", style={
            'textAlign': 'center',
            'padding': '20px',
            'color': text_secondary,
            'fontSize': '14px'
        })
    ])
])

# executar

if __name__ == "__main__":
    app.run(debug=True)
