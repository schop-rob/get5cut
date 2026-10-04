"""Languages of get5cut.com. Add a language here and in its own module."""
import importlib

# (code, directory, hreflang, label in the language menu). The code is also
# the module name in this package, lower case, with "-" written as "_".
LANGS = [
    ("en", ".", "en", "EN"),
    ("de", "de", "de", "DE"),
    ("zh", "zh", "zh-Hans", "ZH"),
    ("fr", "fr", "fr", "FR"),
    ("vi", "vi", "vi", "VI"),
    ("es", "es", "es", "ES"),
    ("it", "it", "it", "IT"),
    ("ja", "ja", "ja", "JA"),
    ("ko", "ko", "ko", "KO"),
    ("pt-BR", "pt-br", "pt-BR", "PT"),
]


def module(code):
    return importlib.import_module(f"i18n.{code.replace('-', '_').lower()}")


def site_url(directory, page_path=""):
    """Absolute path of a page in one language, e.g. /de/study-abroad/."""
    prefix = "" if directory == "." else f"/{directory}"
    return f"{prefix}/{page_path}/" if page_path else f"{prefix}/"


def hreflang_links(page_path=""):
    lines = [f'    <link rel="alternate" hreflang="{h}" href="https://get5cut.com{site_url(d, page_path)}">' for _, d, h, _ in LANGS]
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="https://get5cut.com{site_url(".", page_path)}">')
    return "\n".join(lines)


def lang_switch(active_code, page_path=""):
    links = [f'        <a href="{site_url(d, page_path)}" class="{"active" if c == active_code else ""}">{label}</a>' for c, d, _, label in LANGS]
    return " | \n".join(links)


def faq_details(items):
    return "\n".join(
        f"            <details>\n                <summary>{i['q']}</summary>\n                <p>{i['a']}</p>\n            </details>"
        for i in items
    )
