# 🚀 Alura Space

Galeria de imagens do espaço desenvolvida com **Django**, como projeto prático de aprendizado de desenvolvimento back-end. O front-end foi fornecido pronto; o foco do desenvolvimento foi na estruturação do projeto Django, configuração de rotas, views e renderização dinâmica de templates.

![Preview do projeto](https://imgur.com/a/bK5Z0JA.png)

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Back-end — Como foi desenvolvido](#back-end--como-foi-desenvolvido)
- [Como rodar o projeto](#como-rodar-o-projeto)
- [Próximos passos](#próximos-passos)

---

## Sobre o Projeto

O **Alura Space** é uma galeria web de fotografias astronômicas — imagens de nebulosas, estrelas, galáxias e planetas. O usuário pode navegar pela galeria e visualizar detalhes de cada imagem.

O projeto foi desenvolvido como exercício prático para aprender os fundamentos do Django: criação de apps, URLs, views e sistema de templates.

---

## Tecnologias

- **Python 3**
- **Django** — framework back-end principal
- **SQLite** — banco de dados (padrão Django para desenvolvimento)
- **HTML5 + CSS3** — front-end (fornecido pronto)
- **Django Template Language (DTL)** — renderização dinâmica das páginas

---

## Estrutura do Projeto

```
alura-space/
│
├── setup/                  # Configurações globais do projeto
│   ├── settings.py         # Configurações: apps, banco, static files
│   ├── urls.py             # Roteamento principal
│   ├── asgi.py
│   └── wsgi.py
│
├── galeria/                # App principal
│   ├── migrations/         # Histórico de migrações do banco
│   ├── templates/
│   │   └── galeria/
│   │       ├── partials/
│   │       │   ├── _menu.html      # Componente: menu lateral + header
│   │       │   └── _footer.html    # Componente: rodapé
│   │       ├── base.html           # Template base (herança)
│   │       ├── index.html          # Página: galeria principal
│   │       └── imagem.html         # Página: detalhe da imagem
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py             # Rotas do app galeria
│   └── views.py            # Lógica das views
│
├── static/                 # Arquivos estáticos (CSS, imagens, ícones)
├── templates/              # Diretório raiz de templates
├── manage.py               # CLI do Django
├── requirements.txt        # Dependências do projeto
├── .env                    # Variáveis de ambiente (não versionado)
└── db.sqlite3              # Banco de dados SQLite
```

---

## Back-end — Como foi desenvolvido

Esta foi a parte central do meu aprendizado no projeto. Abaixo estão as principais decisões e implementações.

### 1. Configuração do App Django

O app `galeria` foi criado com `python manage.py startapp galeria` e registrado no `settings.py` dentro de `INSTALLED_APPS`:

```python
# setup/settings.py
INSTALLED_APPS = [
    ...
    'galeria',
]
```

O arquivo `apps.py` define o app:

```python
# galeria/apps.py
from django.apps import AppConfig

class GaleriaConfig(AppConfig):
    name = 'galeria'
```

---

### 2. Roteamento de URLs

O projeto usa dois níveis de roteamento: o **roteador principal** em `setup/urls.py` que delega para o **roteador do app** em `galeria/urls.py`.

```python
# galeria/urls.py
from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),        # Rota: /  → página da galeria
    path('imagem/', imagem, name='imagem'), # Rota: /imagem/ → detalhe da foto
]
```

O uso de `name=` nas rotas permite referenciá-las nos templates com `{% url 'index' %}` e `{% url 'imagem' %}`, sem depender de caminhos fixos.

---

### 3. Views

As views recebem a requisição HTTP e retornam a resposta renderizando o template correspondente:

```python
# galeria/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
```

Ambas usam `render()`, que combina o `request`, o template e (futuramente) um contexto com dados do banco para gerar o HTML final.

---

### 4. Sistema de Templates com Herança

Um dos conceitos mais importantes implementados foi a **herança de templates** do Django, que evita repetição de código HTML.

**`base.html`** — template pai com a estrutura comum a todas as páginas:

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    ...
    <link rel="stylesheet" href="{% static 'styles/style.css' %}">
</head>
<body>
    {% include 'galeria/partials/_menu.html' %}

    {% block content %}{% endblock %}  <!-- as páginas filhas preenchem aqui -->

    {% include 'galeria/partials/_footer.html' %}
</body>
</html>
```

**`index.html`** — template filho que herda o base e preenche o bloco:

```html
{% extends 'galeria/base.html' %}
{% load static %}

{% block content %}
    <!-- conteúdo específico da página de galeria -->
{% endblock %}
```

Esse padrão significa que menu, footer e estrutura HTML geral são escritos **uma única vez**.

---

### 5. Partials (Componentes reutilizáveis)

O menu lateral e o rodapé foram separados em arquivos parciais com `{% include %}`:

```
templates/galeria/partials/
    ├── _menu.html    → header + barra de busca + menu lateral
    └── _footer.html  → rodapé com links de redes sociais
```

Incluídos no `base.html` com:

```html
{% include 'galeria/partials/_menu.html' %}
{% include 'galeria/partials/_footer.html' %}
```

---

### 6. Arquivos Estáticos

O Django gerencia CSS, imagens e ícones via `{% load static %}` e a tag `{% static %}`:

```html
<img src="{% static 'assets/logo/Logo(2).png' %}" alt="Logo da Alura Space" />
<link rel="stylesheet" href="{% static 'styles/style.css' %}">
```

Isso garante que os caminhos funcionem independentemente do ambiente (desenvolvimento ou produção).

---

## Como rodar o projeto

**Pré-requisitos:** Python 3 instalado.

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/alura-space.git
cd alura-space

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações
python manage.py migrate

# 5. Rode o servidor
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000`

---

## Próximos passos

- [ ] Criar o model `Fotografia` com campos: nome, legenda, fonte, data, tag, imagem
- [ ] Integrar o banco de dados às views (passar contexto para os templates)
- [ ] Implementar busca por nome e filtro por tags
- [ ] Adicionar autenticação de usuários (login/logout)
- [ ] Implementar sistema de favoritos

---

## Aprendizados

Este projeto foi desenvolvido durante minha transição de carreira da Engenharia Química para o desenvolvimento back-end. Os principais conceitos praticados foram:

- Estruturação de um projeto Django do zero
- Criação de apps, URLs e views
- Sistema de templates com herança e partials
- Gerenciamento de arquivos estáticos
- Padrão MVT (Model-View-Template)

---

*Projeto desenvolvido como parte do curso Django da Alura.*
