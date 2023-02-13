import sys

from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories

# Requisitos 11 e 12

menu_options = {
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


class Menu:
    def __init__(self):
        self.options = menu_options

    def get_title(self, option):
        return self.options[option]["title"]

    def get_question(self, option):
        return self.options[option]["question"]

    def get_function(self, option):
        return self.options[option]["function"]

    def create(self):
        menu = "Selecione uma das opções a seguir:\n"

        for option in self.options:
            menu += f" {option} - {self.options[option]['title']}\n"

        return menu

    def check_choice(self, option):
        if option in self.options:
            return True
        return False


def analyzer_menu():
    menu = Menu()
    user_option = input(menu.create())
    result = str()

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
