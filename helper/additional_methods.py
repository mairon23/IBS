from src.data.routes import Routes


def merge_link(url: str) -> str:
    """
    Объединяет доменное имя и путь URL
    :param url: путь URL.
    """
    return Routes.api_main_page + url


def splitter(text: str) -> str:
    """
    Преобразует текст
    :param text: Входной текст
    """
    original_text = text.split()
    text_after = ''.join(original_text)
    return text_after
