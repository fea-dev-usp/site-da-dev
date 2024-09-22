<strong> Dúvidas sobre criar e ativar o ambiente: </strong>

[Assista o Vídeo](https://youtu.be/8eWQNNtBsYs)

<strong> Dúvidas sobre Django : </strong>

[Leia a Documetação](https://docs.djangoproject.com/en/4.2/)

<strong> Para criar um novo ambiente virtual : </strong>

```bash
python -m venv venv
```

<br><strong> Para ativar o ambiente virtual no Windows: </strong>

```bash
venv\Scripts\activate
```

<br><strong> Para ativar o ambiente virtual no macOS e Linux: </strong>

```bash
source venv/bin/activate
```

<br>
Após ativar o ambiente virtual você pode usar o pip para instalar os requisitos a partir de um arquivo requirements.txt.

Execute o seguinte comando no terminal para instalar todas as dependências do projeto que constam no arquivo requirements.txt
<br><br>

```bash
pip install -r requirements.txt
```

<br><strong> Iniciar a aplicação </strong><br><br>

```bash
py manage.py runserver
```

ou

```bash
python manage.py runserver
```

<br><strong> Para conseguir ver as alterações no site ao salvar o arquivo e sem precisar recarregar a página </strong><br><br>

```bash
python manage.py livereload
python manage.py runserver
```

<br><strong> OBSERVAÇÕES IMPORTANTES </strong><br><br>

Tem Scripts no 'HTML'  é desta forma mesmo.
Não modifique.
