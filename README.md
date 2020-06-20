# Odoo Get Starter

Este repositório contém um tutorial para instalação e configuração do [Odoo](http://www.odoo.com). Além disso, é disponibilizado uma estrutura de projeto e exemplo de módulo customizado.

Se você é iniciante no Odoo e quer meter a mão na massa rapidamente, esse tutorial vai deixar o seu ambiente pronto para o desenvolvimento Odoo com seus próprios módulos customizados.

![Odoo Logo](https://odoocdn.com/openerp_website/static/src/img/assets/png/odoo_logo.png?a=b)

![Odoo Image](https://odoocdn.com/openerp_website/static/src/img/2020/home/screens-mockup.png)

---

## Instalação e Configuração

Esse tutorial é baseado em uma instalação para ambiente `Windows`.

### Pré-Requisitos

* [Git](https://git-scm.com/downloads)
* [Python v3.7](https://www.python.org/downloads/)
* [VSCode](https://code.visualstudio.com/download) [Pycharm Community](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows)
* [Postgres 9.6](https://www.postgresql.org/download/windows/)
* [PgAdmin](https://www.pgadmin.org/download/) ou [DBEAVER](https://dbeaver.io/download/)

### Instalaçãos

#### Estrutura de Pastas

A estrutura de pastas abaixo é um padrão adotado para atender um ambiente de desenvolvimento local e docker ao mesmo tempo. A estrutura também permite trabalhar direrentes conjuntos de módulos que podem atender a projetos/clientes diferentes, utilizando a mesma versão base do Odoo.

```
odoo (WorkspaceFolder)
|_ 13.0/
  |_ root/
    |_ project/
    | |_ addons/
    |   |_ <client_name>/
    |     |_ .venv/
    |     |_ <custom_module_a>/
    |     |_ <custom_module_b>/
    | |_ odoo/
    |_ cache/
    |_ db/
    |_ storage/
```

### Configuração

#### Baixar código fonte do Odoo

Clonar o repositório do [`Odoo`](https://github.com/odoo/odoo) para pasta `odoo\13.0\root\project\`:

```
git clone https://github.com/odoo/odoo.git -b 13.0
```

Baixar o [tema](https://apps.odoo.com/apps/themes/13.0/backend_theme_v13/) para Odoo:

```
https://apps.odoo.com/apps/themes/13.0/backend_theme_v13/
```

Descompactar arquivo na pasta `root\13.0\root\project\addons\<client_name>\`.

#### Instalar dependências do odoo

Criar o ambiente virtual python na pasta do pacote do cliente específico `root\13.0\root\project\addons\<client_name>\.venv\`:

```
virtualenv .venv -p c:\\Path\To\Python\python.exe
```

Ativar o ambiente virtual:

```
source odoo\13.0\root\project\addons\<client_name>\.venv\Scripts\activate.bat
```

Instalar os pacotes requeridos para execução do Odoo presente na pasta `root\13.0\root\project\odoo\`:

```
pip install -r requirements.txt
```

Caso os módulos customizados possuam requisitos específicos estes também devem ser instalados nesse ambiente virtual. Para isso repita o passo acima para cada `requirements.txt` presente nos módulos customizados.

#### Configurar VSCode para executar o Odoo

Crie o arquivo `odoo\13.0\root\project\.vscode\launch.json` com o conteúdo abaixo. É necessário ajustar a propriedade `pythonPath` com o caminho do python do ambiente virtual criado na pasta `odoo\13.0\root\project\addons\<client_name>\.venv\`.

```conf
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Init Odoo",
            "type": "python",
            "request": "launch",
            "pythonPath": "${workspaceFolder}\\13.0\\root\\project\\addons\\<client_name>\\.venv\\python.exe",
            "program": "${workspaceFolder}\\13.0\\root\\project\\odoo-bin",
            "cwd": "${workspaceFolder}\\13.0\\root\\project\\odoo",
            "console": "internalConsole",
            "args": [
                "--config=./odoo.conf",
                "--dev=xml,qweb,reload",
                "-i",
                "base"
            ]
        },
        {
            "name": "Run Odoo",
            "type": "python",
            "request": "launch",
            "pythonPath": "${workspaceFolder}\\13.0\\root\\project\\addons\\<client_name>\\.venv\\python.exe",
            "program": "${workspaceFolder}\\13.0\\root\\project\\odoo-bin",
            "cwd": "${workspaceFolder}\\13.0\\root\\project\\odoo",
            "console": "internalConsole",
            "args": [
                "--config=./odoo.conf",
                "--dev=xml,qweb,reload"
            ]
        },
        {
            "name": "Update Odoo",
            "type": "python",
            "request": "launch",
            "pythonPath": "${workspaceFolder}\\13.0\\root\\project\\addons\\<client_name>\\.venv\\python.exe",
            "program": "${workspaceFolder}\\13.0\\root\\project\\odoo-bin",
            "cwd": "${workspaceFolder}\\13.0\\root\\project\\odoo",
            "console": "internalConsole",
            "args": [
                "--config=./odoo.conf",
                "--dev=xml,qweb,reload",
                "--update=module_name"
            ]
        }
    ]
}
```

#### Arquivo de configuração do Odoo

Crie o arquivo `odoo\13.0\root\project\odoo\odoo.conf` com o conteúdo a seguir. Este arquivo possui as principais configurações para execução do Odoo. As propriedades que encontram-se `descomentadas` necessitam ser revisadas para o seu ambiente.

```conf
[options]

# ***************************************
# Admin
# ***************************************

admin_passwd = Odoo@Password

# ***************************************
# Database
# ***************************************

db_name = odoo13
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
dbfilter = ^odoo13.*$
list_db = True
# db_maxconn = 64
# db_template = template1

# ***************************************
# Folders
# ***************************************

addons_path = ./addons,./odoo/addons,../addons/client_name
# data_dir = /var/lib/Odoo
pg_path = C:/Program Files/PostgreSQL/9.6/bin

# ***************************************
# Log Settings
# ***************************************

logfile = c:/Temp/odoo/odoo.log
# log_level = debug
# log_db = False
# log_db_level = warning
# log_handler = :INFO
# logrotate = True

# ***************************************
# Server Modes
# ***************************************

# proxy_mode = True
debug_mode = True
auto_reload = True

# ***************************************
# Ports
# ***************************************

# xmlrpc = True
# xmlrpc_interface =
xmlrpc_port = 8069
# xmlrpcs = True
# xmlrpcs_interface =
xmlrpcs_port = 8071
longpolling_port = 8072

# ***************************************
# Hardware
# limit_memory_soft = 640MB * cores/workers * 1024 * 1024
# limit_memory_hard = # 768MB * cores/workers * 1024 * 1024
# workers = CPU cores * 2 + 1
# ***************************************

# limit_memory_hard = 1677721600
# limit_memory_soft = 629145600
# limit_request = 8192
# limit_time_cpu = 60
limit_time_real = 99999999
max_cron_threads = 0
# workers = 5

# ***************************************
# Others
# ***************************************

# csv_internal_sep = ,
# email_from = False
# osv_memory_age_limit = 1.0
# osv_memory_count_limit = False
# smtp_password = False
# smtp_port = 25
# smtp_server = localhost
# smtp_ssl = False
# smtp_user = False
```

#### Adicionando saída do log ao debug

Para adicionar a saída do log ao console do debug altere o arquivo `odoo\13.0\root\project\odoo\odoo-bin` conforme abaixo:

```python
#!/usr/bin/env python3

# set server timezone in UTC before time module imported
__import__('os').environ['TZ'] = 'UTC'
import odoo

# TODO : TRICK -> Add this line below for log print in console
import logging
logging.getLogger().addHandler(logging.StreamHandler())


if __name__ == "__main__":
    odoo.cli.main()
```

#### Inicializando o banco de dados

Na primeira execução é necessário criar o banco de dados da aplicação. Para isso, execute o debug do VSCode com a configuração `Init Odoo`.

Após a inicialização, tente acessar a aplicação pelo navegador:

```
http://localhost:8069
```

### Executando a aplicação em modo normal

Inicie o debug do VSCode com a configuração `Run Odoo` e em seguida tente acessar a aplicação pelo navegador:

```
http://localhost:8069
```

### Executando a aplicação em modo update

Algumas modificações realizadas nos modelos e visões do odoo necessitam ser aplicados no banco de dados da aplicação. Para isso, 
ajuste a configuração `Update Odoo` no arquivo `launch.json` para informar quais os módulos customizados precisam ser atualizados:

```conf
            ...
            "console": "internalConsole",
            "args": [
                "--config=./odoo.conf",
                "--dev=xml,qweb,reload",
                "--update=module_name"
            ]
            ...

```

Inicie o debug do VSCode com a configuração `Update Odoo`. Em seguida tente acessar a aplicação pelo navegador:

```
http://localhost:8069
```

---

## Criando módulo customizado

#### Estrutura de Pastas

Abaixo é apresenta uma estrutura de pastas padrão para criação de um módulo customizado Odoo. Um exemplo completo pode ser encontrado neste repositório.

```
module_name/
|_ data/
|_ hooks/
|_ models/
| |_ model_name/
|   |_ __init__.py
|   |_ business_logic.py
|   |_ model.py
|_ views/
|  |_ model_name_view.xml
|_ security/
| |_ ir.model.access.csv
| |_ ir.rules.access.xml
|_ static/
| |_ description
|   |_ icon.png
|_ tools/
|_ module_name.xml
|_ __init__.py
|_ __manifest.py__
```

Baixe o código fonte disponível e altere os dados iniciais para customizar o seu módulo Odoo.

#### Instalando um módulo customizado

Para instalar o módulo customizado:

1. Inicie a aplicação Odoo e acesse-a pelo navegador.
1. Ative o modo desenvolvedor em `Menu Principal > Configurações > Ativar modo desenvolvedor`.
1. Acesse `Menu Principal > Apps > Atualizar lista de módulos`.
1. Localize o módulo customizado na caixa de pesquisa.
1. Clique no botão `Instalar`.

---

## Criando uma página básica no Odoo

Uma aplicação Odoo segue o padrão `MVC (Model-View-Controller)`. O Odoo estabelece um padrão para criação dos modelos e views. A seguir segue um exemplo para criação de um modelo e visão básica.

### Criando um modelo

Crie o arquivo `13.0\root\project\addons\<client_name>\<module_name>\models\sale\model.py` com o conteúdo abaixo:

```python
# -*- coding: utf-8 -*-

from odoo import api, models, fields, tools, _


class SaleModel(models.Model):

    # ----------------------------------------------------
    # Model Definition
    # ----------------------------------------------------

    _name = 'gonzaga.sale'
    _description = 'Venda'

    # ----------------------------------------------------
    # Fields
    # ----------------------------------------------------

    sale_date = fields.Datetime(
        string='Data da Venda'
    )

    payment_condition = fields.Char(
        string='Condições de Pagamento',
        size=100,
        default='A VISTA'
    )

    partner_id = fields.Many2one(
        string='Cliente',
        comodel_name='res.partner'
    )

    sale_items = fields.One2many(
        string='Items',
        comodel_name='gonzaga.sale.item',
        inverse_name='sale_id'
    )


class SaleModelItem(models.Model):

    # ----------------------------------------------------
    # Model Definition
    # ----------------------------------------------------

    _name = 'gonzaga.sale.item'
    _description = 'Itens da Venda'

    # ----------------------------------------------------
    # Fields
    # ----------------------------------------------------

    sale_id = fields.Many2one(
        string='Venda',
        comodel_name='gonzaga.sale'
    )

    product_code = fields.Char(
        string='Codigo',
        size=10
    )

    description = fields.Char(
        string='Descrição'
        size=100
    )

    price = fields.Float(
        string='Valor'
    )

```

### Adicionando modelo ao módulo python

Altere o arquivo `13.0\root\project\addons\<client_name>\<module_name>\__init__.py` para importar o modulo `sale.py`:

```python
from .models.sale import model
```

### Criando uma visão

Crie o arquivo `13.0\root\project\addons\<client_name>\<module_name>\views\sale_view.xml` com o conteúdo abaixo:

```xml
<?xml version="1.0"?>
<openerp>
    <data>

        <!-- BLOCK : Sale -->

        <!-- Search -->
        <record id="view_search_gonzaga_sale" model="ir.ui.view">
            <field name="name">Vendas</field>
            <field name="model">gonzaga.sale</field>
            <field name="arch" type="xml">
                <search>
                    <field name="id"/>
                    <field name="sale_date"/>
                    <field name="payment_condition"/>
                    <field name="partner_id"/>
                </search>
            </field>
        </record>

        <!-- Tree -->
        <record id="view_tree_gonzaga_sale" model="ir.ui.view">
            <field name="name">Vendas</field>
            <field name="model">gonzaga.sale</field>
            <field name="arch" type="xml">
                <tree string="Brand">
                    <field name="id"/>
                    <field name="sale_date"/>
                    <field name="payment_condition"/>
                    <field name="partner_id"/>
                </tree>
            </field>
        </record>

        <!-- Form -->
        <record id="view_form_gonzaga_sale" model="ir.ui.view">
            <field name="name">Vendas</field>
            <field name="model">gonzaga.sale</field>
            <field name="arch" type="xml">
                <form>
                    <sheet>
                        <group>
                            <field name="id"/>
                            <field name="sale_date"/>
                            <field name="payment_condition"/>
                            <field name="partner_id"/>
                            <field name="sale_items">
                            <tree create="true" delete="true" edit="true" editable="bottom">
                                <field name="product_code">
                                <field name="description">
                                <field name="price">
                            </tree>
                            </field>
                        </group>
                    </sheet>
                </form>
            </field>
        </record>

        <!-- Actions -->
        <record model="ir.actions.act_window" id="action_gonzaga_sale">
            <field name="name">Vendas</field>
            <field name="type">ir.actions.act_window</field>
            <field name="res_model">gonzaga.sale</field>
            <field name="view_mode">tree,form,kanban</field>
            <field name="search_view_id" ref="view_search_gonzaga_sale"/>
            <field name="context">{}</field>
            <field name="domain">[]</field>
            <field name="limit">50</field>
        </record>
        <record id="action_gonzaga_sale_tree_view" model="ir.actions.act_window.view">
            <field name="sequence" eval="0"/>
            <field name="view_mode">tree</field>
            <field name="view_id" ref="view_tree_gonzaga_sale"/>
            <field name="act_window_id" ref="action_gonzaga_sale"/>
        </record>
        <record id="action_gonzaga_sale_form_view" model="ir.actions.act_window.view">
            <field name="sequence" eval="1"/>
            <field name="view_mode">form</field>
            <field name="view_id" ref="view_form_gonzaga_sale"/>
            <field name="act_window_id" ref="action_gonzaga_sale"/>
        </record>

        <!-- END BLOCK : Sale -->

    </data>
</openerp>
```

### Adicionando a visão ao menu principal

Crie o arquivo `13.0\root\project\addons\<client_name>\<module_name>\gonzaga_sales.xml` com o conteúdo abaixo:

```xml
<?xml version="1.0"?>
<openerp>
    <data>

      <!-- BLOCK : MENU -->

      <!-- Main Menu -->
      <menuitem id="menu_gonzaga_sales"
                  name="Gonzaga Vendas"
                  parent=""
                  sequence="3"
                  web_icon="gonzaga_sales,static/description/icon.png"
                  groups="base.group_user,base.group_system" />

            <!-- Register -->
            <menuitem id="menu_gonzaga_sales_register"
                  name="Cadastros"
                  parent="menu_gonzaga_sales"
                  sequence="1"
                  groups="base.group_user,base.group_system"/>

                  <!-- Vendas -->
                  <menuitem id="menu_gonzaga_sales_register_general_sales"
                              name="Vendas"
                              parent="menu_gonzaga_sales_register"
                              sequence="1"
                              action="action_gonzaga_vendas"
                              groups="base.group_user,base.group_system" />

            <!-- END : Register -->

      <!-- END BLOCK : MENU -->

    </data>
</openerp>
```

### Adicionado arquivos ao manifest do modulo

Ajuste o arquivo `13.0\root\project\addons\<client_name>\<module_name>\views\__manifest__.py` para refenciar os arquivos abaixo. A versão completa do arquivo pode ser encontrada no repositório.

```
{
    ...
    'data': [
        'views/sale_view.xml',
        'gonzaga_sales.xml',
    ],
}
```

### Atualizar a aplicação

Após realizar as alterações no seu módulo customizado, execute a etapa para atualização (update) da aplicação Odoo.

## Referências

* https://www.odoo.com/documentation/13.0/setup/install.html
* https://www.odoo.com/documentation/13.0/index.html
