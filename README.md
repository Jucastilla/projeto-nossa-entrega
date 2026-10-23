# Projeto Nossa Entrega — Dashboard (nomes fictícios)

Versão de apresentação do dashboard original. Os nomes dos voluntários nos dados de participação foram substituídos por nomes fictícios. As demais colunas dos CSVs foram mantidas.

## Executar

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

O arquivo `dashboard/app.py` lê `dados/acoes.csv` e `dados/participacoes.csv`. Para usar o logotipo original, coloque `logo_nossa_entrega.png` na pasta `assets/`. Sem ele, o aplicativo usa um ícone alternativo.

Antes de publicar, revise outras informações eventualmente identificáveis nos dados e confirme a autorização de uso dos materiais.
