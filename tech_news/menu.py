import sys

from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories

# Requisitos 11 e 12

# menu = {
#     "options": {
#         0: {
#             "title": "Popular o banco com notícias;",
#             "question": "Digite quantas notícias serão buscadas:",
#             "function": get_tech_news,
#         },
#         1: {
#             "title": "Buscar notícias por título;",
#             "question": "Digite o título:",
#             "function": search_by_title,
#         },
#         2: {
#             "title": "Buscar notícias por data;",
#             "question": "Digite a data no formato aaaa-mm-dd:",
#             "function": search_by_date,
#         },
#         3: {
#             "title": "Buscar notícias por categoria;",
#             "question": "Digite a categoria:",
#             "function": search_by_category,
#         },
#         4: {
#             "title": "Listar top 5 categorias;",
#             "question": False,
#             "function": top_5_categories,
#         },
#         5: {
#             "title": "Sair.",
#             "question": "Encerrando script",
#             "function": False,
#         },
#     },
# }

options = {
    0: {
        "title": "Popular o banco com notícias;",
        "question": "Digite quantas notícias serão buscadas:",
        "function": get_tech_news,
    },
    1: {
        "title": "Buscar notícias por título;",
        "question": "Digite o título:",
        "function": search_by_title,
    },
    2: {
        "title": "Buscar notícias por data;",
        "question": "Digite a data no formato aaaa-mm-dd:",
        "function": search_by_date,
    },
    3: {
        "title": "Buscar notícias por categoria;",
        "question": "Digite a categoria:",
        "function": search_by_category,
    },
    4: {
        "title": "Listar top 5 categorias;",
        "question": False,
        "function": top_5_categories,
    },
    5: {
        "title": "Sair.",
        "question": False,
        "function": "Encerrando script",
    },
}


# def create_menu():
#     menu_options = "Selecione uma das opções a seguir:\n"

#     for option in menu["options"]:
#         menu_options += f" {option} - {menu['options'][option]['title']}\n"

#     return menu_options


# def run_option(option):
#     if menu["options"][option]["question"]:
#         return menu["options"][option]["function"](
#             input(menu["options"][option]["question"])
#         )
#     else:
#         return menu["options"][option]["function"]


# def analyzer_menu():
#     menu_options_number = len(menu["options"]) - 1
#     menu_options_range = range(0, menu_options_number)
#     menu_options = create_menu()

#     try:
#         option = int(input(menu_options))
#         if option in menu_options_range:
#             result = run_option(option)
#         elif option == menu_options_number:
#             result = menu["options"][option]["question"]
#         else:
#             raise ValueError

#         print(f"{result}", file=sys.stdout)
#     except ValueError:
#         print("Opção inválida", file=sys.stderr)


class Menu:
    def __init__(self):
        self.options = options

    def get_title(self, option):
        return self.options[option]["title"]

    def get_question(self, option):
        return self.options[option]["question"]

    def get_function(self, option):
        return self.options[option]["function"]

    def create_menu(self):
        menu_options = "Selecione uma das opções a seguir:\n"

        for option in self.options:
            menu_options += f" {option} - {self.options[option]['title']}\n"

        return menu_options

    def check_choice(self, option):
        if option in self.options:
            return True
        return False


# def analyzer_menu():
#     try:
#         menu = Menu()
#         user_option = int(input(menu.create_menu()))

#         if menu.get_question(user_option):
#             run_option = menu.get_function(user_option)
#             result = run_option(input(menu.get_question(user_option)))
#         elif hasattr(menu.get_function(user_option), "__call__"):
#             run_option = menu.get_function(user_option)
#             result = run_option()
#         else:
#             result = menu.get_function(user_option)

#         print(f"{result}", file=sys.stdout)
#     except (ValueError, KeyError):
#         print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    menu = Menu()
    user_option = input(menu.create_menu())
    result = ""

    try:
        user_option = int(user_option)
        if not menu.check_choice(user_option):
            raise ValueError
    except (ValueError, KeyError):
        print("Opção inválida", file=sys.stderr)

    match user_option:
        case 0:
            result = get_tech_news(input(menu.get_question(user_option)))
        case 1:
            result = search_by_title(input(menu.get_question(user_option)))
        case 2:
            result = search_by_date(input(menu.get_question(user_option)))
        case 3:
            result = search_by_category(input(menu.get_question(user_option)))
        case 4:
            result = top_5_categories()
        case 5:
            result = "Encerrando script"

    print(f"{result}", file=sys.stdout)
