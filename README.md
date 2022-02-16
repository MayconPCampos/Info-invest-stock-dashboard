## docker-flask-mysql

Imagem Docker com Flask e MySQL para aplicações web com Python.

# Descrição

Com essa imagem você pode criar um ou vários ambientes de desenvolvimento.

O único requisito é ter o `Docker` instalado e configurado.

Para criar o ambiente clone este repositório com `git clone <repositório>` no git bash
e abra com o seu Visual Studio Code.

Você vai encontrar a seguinte estrutura de arquivos:

```
.
├── flask
│    ├── app
│    │    ├─── __init__.py
│    │    ├── views.py
│    ├── .dockerignore
│    ├── dockerfile
│    ├── requirements.txt
│    ├── run.py
├── .env
├── docker-compose.yaml

```

Dentro do diretório `app` é onde o web aplicativo é desenvolvido, como a pasta contem o arquivo `__init__.py`
esse diretório agora serve como um pacote permitindo o acesso à instancia criada do Flask em
qualquer parte do projeto usando `from app import app`.

o arquivo `run.py` é o arquivo que serve como entrada e inicia o aplicativo flask

Os arquivos `dockerfile` são usados para construir as imagens e `docker-compose.yaml`
é o arquivo usado no gerenciamento dos containers.

`.dockerfile` funciona exatamente igual ao `.gitignore` controlando o que será copiado para dentro dos container.

O arquivo `.env` é usado para as variáveis de ambiente e é acessado dentro do `docker-composer.yaml`
    
```
   environment:
      - FLASK_APP=${FLASK_APP}
      - FLASK_ENV=${FLASK_ENV}
```

Para criar a imagem e ativar os containers basta usar o comando `docker-composer up` no terminal.
O app flask inicia com o modo DEBUG ligado na porta 5000 do localhost pronto para o desenvolvimento.
