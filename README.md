# Stock Dashboard

Mostra os valores dos últimos sete dias de uma ação e calcula o valor e a porcentagem de variação, geralmente
usados para a avaliação de desempenho de uma ação, mostra também informações da companhia e as notícias
recentes relacionadas obtidas através da News API.

Devido ao limite de requisições do plano gratuito para a API da Alpha Vantage eu limitei apenas para
mostrar as ações de uma empresa, porém pode ser modificado facilmente para mostrar outras ações
alterando o código da rota no arquivo views.py como mostrado abaixo.

```

@app.route("/stocks/<id>")
@cache.cached(timeout=60)
def stock(id):

    id = id

```

Esse mini app foi criado usando minha imagem docker-flask <a href="https://github.com/MayconPCampos/Ambiente-docker-flask">link aqui</a>.

Para executar clone este repositório com o comando `git clone https://github.com/MayconPCampos/Mini-dashboard.git` no git bash
e se você tiver o `Docker` instalado é só executar o comando `docker-compose up` no console no diretório do repositório, 
caso contrário instale as dependências com o comando `pip install -r requirements.txt` dentro do diretório `app` em seguida inicie com `flask run`.

Acesse pela URL localhost:5000/stocks/TSLA.



<img src="https://github.com/MayconPCampos/Mini-dashboard/blob/main/flask/app/static/image/dashboard.jpg?raw=true">
