- _  Exercício 1 - Faça a instalação do django utilizando o poetry com o python na versão 3.9.5.
```sh
poetry new atv26-05
poetry add django
poetry add psycopg2-binary
poetry env use 3.9.5
```

- _  Exercício 2 - Crie um contêiner com a imagem do postgres para utilizar no projeto django.
```sh
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres
```

- _  Exercício 3 - Crie um projeto Django e  altere as configurações para utilizar o banco de dados postgres
```sh
django-admin startproject atv2605 .
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- _  Exercício 4 - Execute as migrations e crie um superuser
```sh
python manage.py showmigrations
python manage.py migrate
python manage.py showmigrations
python manage.py createsuperuser
```

- _  Exercício 5 - Crie uma app para cadastro de produtos.
```sh
python manage.py startapp product
adicionado no settings.py
```

- _  Exercício 6 - Crie um arquivo de rotas para a app.
```sh
criado urls.py no app

from django.urls import path

urlpatterns = [
    path('', views.index),
]
```

- _  Exercício 7 - Altere as rotas do projeto para utilizar as rotas da app.
```sh
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls'))
]
```

- _  Exercício 8 - Adicione um template para página inicial da app.
```sh
criado pasta templates dentro do app
criado index.html
criado em views.py do app a função

def index(request):
    return render(request, 'index.html')
```

- _  Exercício 9 - Adicione template para listagem e para o formulário de produtos
```sh
criado product_form.html e product_list.html em templates
adicionado funções em views.py do app

def product_list(request):
    return render(request, 'product_list.html')

def product_form(request):
    return render(request, 'product_form.html')
```

- _  Exercício 10 - Adicione template para listagem e para o formulário de categorias
```sh
criado product_form.html e product_list.html em templates
adicionado funções em views.py do app

def categories_list(request):
    return render(request, 'categories_list.html')

def categories_form(request):
    return render(request, 'categories_form.html')
```

- _  Exercício 11 - A página inicial da app deve ter um menu para as demais páginas
```sh
    <ul>
        <li><a href="/product">Index</a></li>
        <li><a href="/product/list">Lista de Produto</a></li>
        <li><a href="/product/form">Form de Produto</a></li>
        <li><a href="/product/categories/list">Lista de Categorias</a></li>
        <li><a href="/product/categories/form">Form de Categorias</a></li>
    </ul>
```

- _  Exercício 12 - Todas as páginas devem ser acessíveis por rotas.
```sh
urlpatterns = [
    path('', views.index),
    path('list', views.product_list),
    path('form', views.product_form),
    path('categories/list', views.categories_list),
    path('categories/form', views.categories_form),
]
```
