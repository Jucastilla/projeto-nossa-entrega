from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / 'data' / 'processed'
LOGO = ROOT / 'assets' / 'logo_nossa_entrega.png'
st.set_page_config(page_title='Projeto Nossa Entrega | Análise de Dados', page_icon=str(LOGO) if LOGO.exists() else '🤝', layout='wide', initial_sidebar_state='expanded')
TEAL = '#019CB2'  # Turquesa da identidade visual
CORAL = '#F65F42'  # Coral da identidade visual: apenas destaques pontuais
NEUTRAL = '#A9BAC2'  # Categoria de comparação, sem sugerir alerta

st.markdown('''<style>
/* Oculta controles técnicos do Streamlit no cabeçalho. */
[data-testid="stAppDeployButton"],
[data-testid="stMainMenu"],
[data-testid="stToolbarActions"] {display:none !important;}
.block-container{padding-top:1.7rem;max-width:1350px}
[data-testid="stMetric"]{background:#F2FAFB;border:1px solid #D8EEF1;padding:18px 18px;border-radius:12px}
[data-testid="stMetricLabel"]{font-size:0.9rem}
h1,h2,h3{letter-spacing:-.02em}
.small-note{color:#687781;font-size:.9rem}
.page-subtitle{font-size:1.12rem;line-height:1.55;color:#526171;margin-top:-.35rem;margin-bottom:1.3rem;font-weight:400}
.sidebar-about{font-size:.89rem;line-height:1.6;color:#44515e;margin-top:1.6rem;margin-bottom:1.8rem}
.sidebar-about strong{color:#343C49;display:block;margin-top:1.2rem;margin-bottom:.45rem}.sidebar-about strong:first-child{margin-top:0}.sidebar-about p{margin:.2rem 0 1.2rem!important}[data-testid="stSidebar"] [data-testid="stRadio"]{margin-top:1rem} [data-testid="stSidebar"] [data-testid="stRadio"] label{padding-top:.25rem;padding-bottom:.25rem}
[data-testid='stSidebar'] [data-testid='stImage']{max-width:75px}
[data-testid='stSidebar'] [data-testid='stMarkdownContainer'] p{line-height:1.45}
h1{font-size:2.1rem!important;font-weight:650!important;margin-bottom:.35rem!important}
h2,h3{font-weight:650!important;font-size:1.25rem!important;line-height:1.3!important} [data-testid="stMetricLabel"] p{font-size:.86rem!important;line-height:1.3!important;font-weight:600!important;white-space:normal!important;overflow:visible!important;text-overflow:clip!important;display:block!important;-webkit-line-clamp:unset!important} [data-testid="stMetricLabel"]{height:auto!important;min-height:2.35rem;overflow:visible!important;align-items:flex-start!important} [data-testid="stMetricLabel"]>div{overflow:visible!important;white-space:normal!important} [data-testid="stMetricValue"]{font-size:1.85rem!important} [data-testid="stMetric"]{min-height:130px} .block-container [data-testid="stVerticalBlock"]{row-gap:.45rem}
.page-subtitle{font-size:1.14rem!important}
.reco{border:1px solid #D8EEF1;border-left:4px solid #019CB2;border-radius:11px;padding:13px 16px;margin:10px 0;background:#FFFBF8}
.reco-title{font-weight:700;font-size:1.04rem;color:#343C49;margin-bottom:5px}
.reco-body{font-size:.96rem;color:#44535e;line-height:1.55}
.analysis{background:#F2FAFB;border-radius:11px;padding:15px 17px;margin-bottom:12px;color:#354650;line-height:1.55}
.analysis strong{color:#343C49}
[data-testid='stSidebar'] [data-testid='stRadio'] [aria-checked='true']{accent-color:#019CB2}
[data-testid='stMetricValue']{color:#343C49}
[data-testid='stMetric']{border-top:3px solid #019CB2}
[data-testid='stSidebar'] [data-testid='stRadio'] [aria-checked='true']{color:#019CB2}
@media(max-width:800px){.block-container{padding-left:1rem;padding-right:1rem}.analysis,.reco{padding:12px 13px}.page-subtitle{font-size:1rem!important}}

.monthly-table-wrap{width:100%;overflow-x:auto;border:1px solid #D8EEF1;border-radius:10px;margin-bottom:1.4rem}
.monthly-table{width:100%;border-collapse:collapse;font-size:.95rem;color:#263746}
.monthly-table thead th{background:#fff;color:#019CB2;font-weight:700;padding:12px 16px;text-align:left;border-bottom:2px solid #D8EEF1}
.monthly-table thead th:not(:first-child),.monthly-table tbody td:not(:first-child){text-align:right}
.monthly-table tbody td{padding:9px 16px;border-bottom:1px solid #D8EEF1;background:#fff}
.monthly-table tbody tr:nth-child(even) td{background:#F7FCFD}
.monthly-table tbody tr.total-row td{font-weight:700;background:#E7F5F7;border-bottom:0}
</style>''', unsafe_allow_html=True)

@st.cache_data
def load():
    a = pd.read_csv(BASE / 'acoes.csv', parse_dates=['Data'])
    p = pd.read_csv(BASE / 'participacoes.csv', parse_dates=['Data'])
    return a, p

a_all, p_all = load()

with st.sidebar:
    logo_col, title_col = st.columns([1.25, 3.75], gap='small', vertical_alignment='center')
    with logo_col:
        if LOGO.exists():
            st.image(str(LOGO), use_container_width=True)
        else:
            st.markdown('🤝')
    with title_col:
        st.markdown('<span style="font-size:23px;font-weight:750;color:#343C49;line-height:1.15">Projeto Nossa Entrega</span>', unsafe_allow_html=True)
st.sidebar.markdown('''<div class="sidebar-about"><strong>Sobre o projeto</strong><p>Projeto voluntário de análise de dados desenvolvido para o Projeto Nossa Entrega, iniciativa que realiza ações semanais de apoio a pessoas em situação de rua.</p><strong>Objetivo da análise</strong><p>Analisar aproximadamente um ano de registros para acompanhar a participação, a frequência e a recorrência dos voluntários, além da logística de transporte das ações.</p></div>''', unsafe_allow_html=True)
st.sidebar.caption('Os nomes dos voluntários foram substituídos por nomes fictícios para preservar sua privacidade.')
page = st.sidebar.radio('Navegação', ['Visão Geral', 'Atuação dos Voluntários', 'Logística das Ações', 'Análise dos Resultados', 'Recomendações Estratégicas'])
a = a_all.copy()
p = p_all.copy()

def heading(title, subtitle):
    st.title(title)
    st.markdown(f'<p class="page-subtitle">{subtitle}</p>', unsafe_allow_html=True)

def metric_row(items):
    cols = st.columns(len(items), gap='medium')
    for col, (name, value, help_text) in zip(cols, items):
        with col:
            st.metric(name, value, help=help_text)

def chart(fig, key=None):
    fig.update_layout(template='plotly_white', margin=dict(l=15,r=15,t=35,b=15), font=dict(family='Arial', size=13), colorway=[TEAL, NEUTRAL, '#439CB0', '#343C49'])
    st.plotly_chart(fig, use_container_width=True, key=key)

def month_counts(frame):
    if frame.empty:
        return pd.DataFrame(columns=['Mês','Quantidade'])
    return frame.assign(Mês=frame.Data.dt.to_period('M').astype(str)).groupby('Mês').size().reset_index(name='Quantidade').sort_values('Mês')

if a.empty and p.empty:
    st.warning('Não há registros disponíveis nas bases.')
    st.stop()

if page == 'Visão Geral':
    heading('Visão Geral', 'Panorama das ações realizadas e da participação dos voluntários')
    n_actions = len(a)
    n_part = len(p)
    n_people = p['Nome e Sobrenome'].nunique()
    avg = a['Participantes'].mean() if n_actions else 0
    metric_row([
        ('Ações realizadas', f'{n_actions}', 'Quantidade de registros de ações no período'),
        ('Participações', f'{n_part}', 'Registros de voluntários nas ações'),
        ('Voluntários únicos', f'{n_people}', 'Pessoas distintas por nome e sobrenome'),
        ('Média por ação', f'{avg:.1f}'.replace('.', ','), 'Média da coluna Participantes de acoes.csv'),
    ])
    st.subheader('Participantes por ação')
    if not a.empty:
        fig=px.line(a.sort_values('Data'), x='Data', y='Participantes', markers=True, labels={'Data':'Data da ação','Participantes':'Participantes'}, color_discrete_sequence=[TEAL])
        fig.update_traces(line_width=3, marker_size=7)
        fig.add_hline(y=avg, line_color='#718D98', line_dash='dash', line_width=1.5,
                      annotation_text=f'Média: {avg:.1f}'.replace('.', ','),
                      annotation_position='top left',
                      annotation_font_color='#526171', annotation_font_size=12)
        # Linha vertical de referência acompanha a data sob o cursor.
        fig.update_layout(hovermode='x unified')
        fig.update_xaxes(showspikes=True, spikemode='across', spikesnap='cursor',
                         spikedash='dot', spikecolor='#718096', spikethickness=1)
        # Rótulos do eixo em português, sem alterar as datas originais.
        meses_pt = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
                    'jul', 'ago', 'set', 'out', 'nov', 'dez']
        inicio = a['Data'].min().to_period('M').to_timestamp()
        fim = a['Data'].max().to_period('M').to_timestamp()
        marcas = pd.date_range(inicio, fim, freq='2MS')
        fig.update_xaxes(tickmode='array', tickvals=marcas,
                         ticktext=[f'{meses_pt[d.month - 1]} {d.year}' for d in marcas])
        chart(fig)

elif page == 'Atuação dos Voluntários':
    heading('Atuação dos Voluntários', 'Participação, frequência, entrada e retorno dos voluntários')
    freq = p['Nome e Sobrenome'].value_counts()
    once = int((freq == 1).sum())
    top7_share = freq.head(7).sum() / len(p) * 100 if len(p) else 0
    flagged = p[p['Primeira participação?'].astype(str).str.strip().str.casefold().eq('sim')].sort_values('Data')
    newcomers = flagged.drop_duplicates('Nome e Sobrenome', keep='first').copy()
    last_seen = p.groupby('Nome e Sobrenome')['Data'].max()
    newcomers['Retornou'] = newcomers.apply(lambda r: bool(last_seen.get(r['Nome e Sobrenome'], r['Data']) > r['Data']), axis=1)
    returned = int(newcomers['Retornou'].sum())
    metric_row([
        ('Voluntários com uma participação', str(once), 'Voluntários com apenas uma participação registrada; representam {:.1f}% dos voluntários diferentes.'.format(once / len(freq) * 100 if len(freq) else 0)),
        ('Participações dos 7 mais frequentes', f'{top7_share:.1f}%'.replace('.', ','), 'Parcela das participações atribuída aos sete voluntários mais frequentes'),
        ('Retorno de voluntários', f'{returned / len(newcomers) * 100:.1f}%'.replace('.', ',') if len(newcomers) else '—', f'{returned} de {len(newcomers)} voluntários identificados como novos retornaram em data posterior; entradas recentes tiveram menos tempo para retornar'),
    ])
    ranking_col, retorno_col = st.columns([1.12, 1], gap='large')
    with ranking_col:
        st.subheader('Voluntários mais frequentes')
        top = freq.head(10).sort_values().reset_index()
        top.columns = ['Voluntário', 'Participações']
        fig = px.bar(top, x='Participações', y='Voluntário', orientation='h', color_discrete_sequence=[TEAL], text='Participações')
        fig.update_layout(yaxis_title='Voluntários', xaxis_title='Total de participações', height=410, margin=dict(l=10,r=25,t=15,b=15))
        fig.update_traces(textposition='outside', textfont_color='#343C49', cliponaxis=False)
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=True, gridcolor='#E2EAF0', gridwidth=1)
        chart(fig)
    with retorno_col:
        st.subheader('Retorno após a primeira participação')
        if len(newcomers):
            ret = pd.DataFrame({'Situação':['Retornaram','Sem retorno'], 'Pessoas':[returned, len(newcomers)-returned]})
            fig = px.bar(ret, x='Situação', y='Pessoas', text='Pessoas', color='Situação', color_discrete_map={'Retornaram':TEAL,'Sem retorno':NEUTRAL})
            fig.update_layout(showlegend=False, xaxis_title=None, height=410)
            fig.update_traces(textposition='outside', textfont_color='#343C49', cliponaxis=False)
            fig.update_yaxes(range=[0, 12], tickmode='array', tickvals=[0, 2, 4, 6, 8, 10, 12])
            chart(fig)
        else:
            st.info('Não há primeiros registros sinalizados para acompanhar.')
    # Comparativo mensal: uma tabela única substitui os dois gráficos de colunas.
    months = pd.period_range(p['Data'].min().to_period('M'), p['Data'].max().to_period('M'), freq='M')
    month_keys = months.astype(str).tolist()
    monthly_p = month_counts(p).set_index('Mês')['Quantidade'].reindex(month_keys, fill_value=0)
    monthly_new = month_counts(newcomers).set_index('Mês')['Quantidade'].reindex(month_keys, fill_value=0)
    monthly_table = pd.DataFrame({
        'Mês': [f'{m.strftime("%m/%Y")}' for m in months],
        'Participações': monthly_p.to_numpy(dtype=int),
        'Novos voluntários': monthly_new.to_numpy(dtype=int),
    })
    st.subheader('Evolução mensal de novos voluntários')
    meses_pt = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    monthly_table['Mês'] = [f'{meses_pt[m.month - 1]}/{m.year}' for m in months]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly_table['Mês'],
        y=monthly_table['Novos voluntários'],
        mode='lines+markers',
        line=dict(color=TEAL, width=3),
        marker=dict(color=TEAL, size=9),
        name='Novos voluntários',
        hovertemplate='Mês: %{x}<br>Novos voluntários: %{y}<extra></extra>',
    ))
    fig.update_layout(height=390, showlegend=False, hovermode='x unified')
    fig.update_yaxes(title_text='Novos voluntários', range=[0, 4], tickmode='array', tickvals=[0, 1, 2, 3, 4])
    fig.update_xaxes(title_text='Mês de entrada', type='category')
    chart(fig)

elif page == 'Logística das Ações':
    heading('Logística das Ações', 'Distribuição dos transportes e atuação dos motoristas nas ações')
    transports = int(a['Transportes'].sum())
    cars = int(a['Carros'].sum())
    bikes = int(a['Bicicletas'].sum())
    bike_actions = int((a['Bicicletas'] > 0).sum())
    drivers = p[(p['Função'].astype(str).str.strip().str.casefold() == 'motorista') & (p['Tipo de transporte'].astype(str).str.strip().str.casefold() == 'carro')]
    d = drivers['Nome e Sobrenome'].value_counts()
    metric_row([
        ('Transportes registrados', str(transports), 'Soma do campo Transportes. Há 1 transporte sem classificação entre carros e bicicletas em 25/11/2025; os registros originais foram mantidos.'),
        ('Ações com bicicleta', f'{bike_actions}', 'Ações com pelo menos uma bicicleta registrada'),
        ('Motoristas únicos', str(len(d)), 'Pessoas diferentes registradas como motoristas de carro'),
    ])
    c1, c2 = st.columns(2, gap='large')
    with c1:
        st.subheader('Motoristas mais frequentes')
        if not d.empty:
            top = d.head(10).sort_values().reset_index()
            top.columns = ['Motorista', 'Atuações']
            fig = px.bar(top, x='Atuações', y='Motorista', orientation='h', text='Atuações', color_discrete_sequence=[TEAL])
            fig.update_layout(yaxis_title='Motoristas', xaxis_title='Participações como motorista', height=410)
            fig.update_traces(textposition='outside', textfont_color='#343C49', cliponaxis=False)
            fig.update_xaxes(showgrid=False, zeroline=False)
            fig.update_yaxes(showgrid=True, gridcolor='#E2EAF0', gridwidth=1)
            chart(fig)
        else:
            st.info('Não há motoristas de carro identificados no período.')
    with c2:
        st.subheader('Transportes utilizados')
        modals = pd.DataFrame({'Modal':['Carros','Bicicletas'], 'Registros':[cars,bikes]})
        fig = px.bar(modals, x='Modal', y='Registros', text='Registros', color='Modal',
                     color_discrete_map={'Carros':TEAL,'Bicicletas':NEUTRAL})
        fig.update_layout(showlegend=False, height=410)
        fig.update_traces(textposition='outside', textfont_color='#343C49', cliponaxis=False)
        fig.update_xaxes(title_text='Meio de transporte')
        fig.update_yaxes(title_text='Quantidade')
        chart(fig)

elif page == 'Análise dos Resultados':
    heading('Análise dos Resultados', 'Principais conclusões sobre a participação dos voluntários, a continuidade das ações e a logística')
    freq = p['Nome e Sobrenome'].value_counts()
    n_people = len(freq)
    once = int((freq == 1).sum())
    once_share = once / n_people * 100 if n_people else 0
    top7_share = freq.head(7).sum() / len(p) * 100 if len(p) else 0
    drivers = p[(p['Função'].astype(str).str.strip().str.casefold() == 'motorista') & (p['Tipo de transporte'].astype(str).str.strip().str.casefold() == 'carro')]
    d = drivers['Nome e Sobrenome'].value_counts()
    top2_share = d.head(2).sum() / len(drivers) * 100 if len(drivers) else 0
    n_actions = len(a)
    n_part = len(p)
    avg_per_action = a['Participantes'].mean() if n_actions else 0
    min_per_action = int(a['Participantes'].min()) if n_actions else 0
    max_per_action = int(a['Participantes'].max()) if n_actions else 0
    flagged = p[p['Primeira participação?'].astype(str).str.strip().str.casefold().eq('sim')].sort_values('Data')
    newcomers = flagged.drop_duplicates('Nome e Sobrenome', keep='first').copy()
    last_seen = p.groupby('Nome e Sobrenome')['Data'].max()
    returned = int(sum(last_seen.get(r['Nome e Sobrenome'], r['Data']) > r['Data'] for _, r in newcomers.iterrows()))
    new_total = len(newcomers)
    return_share = returned / new_total * 100 if new_total else 0
    monthly_new = newcomers.groupby(newcomers['Data'].dt.to_period('M')).size()
    max_new = int(monthly_new.max()) if not monthly_new.empty else 0
    meses_pt = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    peak_months = [f'{meses_pt[m.month-1]}/{m.year}' for m, count in monthly_new.items() if count == max_new]
    peak_label = ' e '.join(peak_months) if peak_months else 'nenhum mês'
    n_transports = int(a['Transportes'].sum())

    st.markdown(f"""<div class="analysis"><strong>Regularidade das ações</strong><p>Ao longo do período analisado, o projeto realizou {n_actions} ações, somando {n_part} participações e uma média de {avg_per_action:.1f} voluntários por ação. As equipes variaram entre {min_per_action} e {max_per_action} participantes, o que evidencia diferenças na disponibilidade de pessoas entre as entregas. Acompanhar essas oscilações pode contribuir para uma distribuição mais adequada das tarefas, especialmente nos dias com equipes menores. Os registros, porém, não permitem identificar as causas dessa variação.</p></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="analysis"><strong>Frequência e continuidade dos voluntários</strong><p>Entre os {n_people} voluntários identificados, {once} participaram de apenas uma ação ({once_share:.1f}%), enquanto os sete mais frequentes concentraram {top7_share:.1f}% das participações registradas. Essa distribuição mostra a importância de um grupo recorrente para a continuidade do projeto, mas também revela uma concentração das atividades entre os participantes mais assíduos. Ampliar a frequência de outros voluntários pode ajudar a distribuir melhor as responsabilidades ao longo do tempo.</p></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="analysis"><strong>Entrada e retorno de novos voluntários</strong><p>Dos {new_total} voluntários identificados nos registros como novos participantes, {returned} voltaram em outra data, correspondendo a {return_share:.1f}%. A entrada de novos voluntários foi mais expressiva em {peak_label}, com {max_new} registros em cada mês. Embora esses dados indiquem capacidade de atrair pessoas, o retorno observado sugere uma oportunidade de fortalecer o acompanhamento após a primeira participação. É importante considerar que quem ingressou perto do fim do período teve menos tempo para retornar; portanto, a taxa não permite concluir que houve desinteresse ou insatisfação.</p></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="analysis"><strong>Logística e disponibilidade dos motoristas</strong><p>As ações contabilizaram {n_transports} transportes registrados (um deles sem classificação entre carro e bicicleta) e a participação de {len(d)} motoristas de carro diferentes. Os dois mais frequentes responderam por {top2_share:.1f}% das {len(drivers)} participações nessa função, indicando uma concentração que pode tornar a organização dos deslocamentos mais sensível à disponibilidade dessas pessoas. Segundo informações da equipe, a dificuldade de estacionamento em Copacabana, a distância percorrida por alguns voluntários e o horário noturno das entregas levam parte dos participantes a optar por metrô ou transporte por aplicativo. Esse contexto ajuda a compreender os desafios de mobilização de veículos, embora tais motivos não sejam medidos diretamente pela base de dados.</p></div>""", unsafe_allow_html=True)

elif page == 'Recomendações Estratégicas':
    heading('Recomendações Estratégicas', 'Ações viáveis para responder aos desafios identificados e acompanhar seus resultados')
    recommendations = [
        ('01', 'Planejamento e organização das ações', 'Manter a confirmação antecipada de presença, já realizada pelo projeto, e adotar um planejamento flexível para lidar com desistências ou mudanças de disponibilidade de última hora. Acompanhar as oscilações da equipe para orientar a organização das próximas entregas.', 'Comparar a quantidade de voluntários confirmados com o número de participantes efetivos em cada ação, mediante registro das confirmações.'),
        ('02', 'Captação e continuidade dos voluntários', 'Após a primeira participação, enviar um agradecimento e um convite para a próxima ação. Utilizar um formulário breve para conhecer a experiência, a disponibilidade e eventuais dificuldades de retorno. Incentivar os voluntários a compartilhar suas experiências nas próprias redes sociais, marcando o perfil do Projeto Nossa Entrega e convidando amigos e familiares a participar, ampliando o alcance da divulgação já realizada pelo projeto.', 'Quantidade mensal de novos voluntários, percentual de retorno após a primeira participação e respostas ao formulário.'),
        ('03', 'Distribuição e continuidade dos transportes', 'Ampliar gradualmente a participação de voluntários que possam atuar como motoristas, buscando reduzir a concentração das viagens nos mesmos participantes. Considerar a criação de uma lista de motoristas de apoio para situações de imprevisto, respeitando a disponibilidade de cada pessoa e as dificuldades de deslocamento e estacionamento em Copacabana.', 'Quantidade de motoristas ativos por mês e percentual das participações concentradas nos dois motoristas mais frequentes.'),
        ('04', 'Captação de recursos e parcerias locais', 'Buscar possíveis parcerias com restaurantes, padarias, mercados e outros estabelecimentos de Copacabana, apresentando o trabalho realizado pelo Projeto Nossa Entrega e propondo contribuições pontuais, como doações de refeições, alimentos ou materiais utilizados nas entregas. Priorizar inicialmente colaborações de pequeno porte, considerando que o projeto ainda não possui CNPJ, e avaliar a viabilidade de cada apoio conforme as necessidades e a capacidade operacional da equipe.', 'Quantidade de estabelecimentos contatados, parcerias estabelecidas e doações recebidas.'),
        ('05', 'Monitoramento e melhoria contínua', 'Manter os registros das ações e participações padronizados, com cuidado no tratamento dos dados pessoais e no consentimento dos voluntários. Revisar periodicamente os indicadores para identificar mudanças na participação, no retorno de novos voluntários e na disponibilidade de motoristas, utilizando os resultados para orientar o planejamento das próximas ações.', 'Acompanhamento mensal da participação, recorrência, entrada de voluntários e disponibilidade de motoristas.'),
    ]
    for number, title, body, indicator in recommendations:
        st.markdown(f'<div class="reco"><div class="reco-title">{number} · {title}</div><div class="reco-body">{body}<p style="margin:10px 0 0"><strong>Como acompanhar:</strong> {indicator}</p></div></div>', unsafe_allow_html=True)