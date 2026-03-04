from elements import *

class Page:
    VALID_TYPES = ['html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br']
    ALLOWED_TYPES_IN_DIV = [H1, H2, Div, Table, Ul, Ol, Span, Text]

    def __init__(self, elem):
        self.error_message = ""
        self.elem = elem
    
    def __validate_element(self, elem):
        if (type(elem) == Text):
            return True

        etag = elem.tag
        econtent = elem.content
        
        # Si pendant le parcours de l’arbre, un noeud n’est pas de type [VALID_TYPES] ou Text, l'arbre est invalide
        if (not etag in self.VALID_TYPES and type(elem) != Text):
            self.error_message = "Unvalid type: " + etag
            return False
        
        # Html doit contenir exactement un Head, puis un Body
        if (etag == "html" and not(econtent and type(econtent) == list and len(econtent) == 2 
            and econtent[0].tag == "head" and econtent[1].tag == "body")):
            self.error_message = "<html> tag must contain a <head> followed by a <body>"
            return False
        
        # Head ne doit contenir qu’un unique Title et uniquement ce Title.
        if (etag == "head" and not(econtent and len(econtent) == 1 and type(econtent[0]) == Title)):
            self.error_message = "<head> tag must contain a <title>, and only one"
            return False

        # Body et Div ne doivent contenir que des éléments des types suivant : H1, H2, Div, Table, Ul, Ol, Span, ou Text.
        if (etag in ["body", "div"] and econtent and not (all([type(subelem) in self.ALLOWED_TYPES_IN_DIV for subelem in econtent]))):
            self.error_message = "<" + etag + "> tag can only contain these tag types: H1, H2, Div, Table, Ul, Ol, Span, or Text"
            return False

        # Title, H1, H2, Li, Th, Td ne doivent contenir qu’un unique Text et uniquement ce Text.
        if (etag in ["title", "h1", "h2", "li", "th", "td"] and econtent and not (len(econtent) == 1 and type(econtent[0]) == Text)):
            self.error_message = "<" + etag + "> tag can only contain one Text element and nothing else"
            return False
        
        # P ne doit contenir que des Text.
        # (should be the other way around -> P should be able to contain text or spans, while span can only contain Text)
        if (etag == "p" and econtent and not (type(econtent) == list and all([type(subelem) == Text for subelem in econtent]))):
            self.error_message = "<p> tag can only contain one or multiple Text element and nothing else"
            return False
        
        # Span ne doit contenir que des Text ou des P.
        if (etag == "span" and econtent and not ((type(econtent) == list 
            and all([type(subelem) in [Text, P] for subelem in econtent])) or (type(econtent) in [Text, P]))):
            self.error_message = "<span> tag can only contain one or multiple Text or <p> element and nothing else"
            return False

        # Ul et Ol doivent contenir au moins un Li et uniquement des Li.
        if (etag in ["ul", "ol"] and not (len(econtent) >= 1 and all([type(subelem) == Li for subelem in econtent]))):
            self.error_message = "<" + etag + "> tag must contain one or multiple <li> tags and nothing else"
            return False
        
        # Tr doit contenir au moins un Th ou Td et uniquement des Th ou des Td. Les Th et les Td doivent être mutuellement exclusifs.
        if (etag == "tr" and not (len(econtent) >= 1 and 
            (all([type(subelem) == Th for subelem in econtent]) or all([type(subelem) == Td for subelem in econtent])))):
            self.error_message = "<tr> tag must contain one or multiple <th> OR <td> tags and nothing else"
            return False
        
        # Table : ne doit contenir que des Tr et uniquement des Tr.
        if (etag == "table" and econtent and not (type(econtent) == Tr or (type(econtent) == list 
            and all([type(subelem) == Tr for subelem in econtent])))):
            self.error_message = "<table> tag can only contain one or multiple <tr> tags and nothing else"
            return False

        if (type(elem.content) == list):
            for subelem in elem.content:
                if (not self.__validate_element(subelem)):
                    return False
        elif (isinstance(elem.content, Elem)):
            if (not self.__validate_element(elem.content)):
                return False
        elif (type(elem.content) != Text):
            return False

        return True

    def is_valid(self):
        return self.__validate_element(self.elem)
    
    def __str__(self):
        result = str(self.elem)
        if self.elem.tag == "html":
            result = "<!DOCTYPE html>\n" + result
        return result
    
    def write_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))


def should_be_valid(elem):
    page = Page(elem)
    if (not page.is_valid()):
        raise Exception(page.error_message)

def should_be_unvalid(elem):
    page = Page(elem)
    if (page.is_valid()):
        raise Exception("Should be unvalid")

if __name__ == "__main__":

    # Si pendant le parcours de l’arbre, un noeud n’est pas de type [VALID_TYPES] ou Text, l'arbre est invalide
    should_be_valid(Html([Head(Title()), Body()]))
    should_be_unvalid(Html(
        Elem("bipbop")
    ))

    # Head ne doit contenir qu’un unique Title et uniquement ce Title.
    should_be_unvalid(Html([Head(), Body()]))
    should_be_unvalid(Html([Head([Title(), Title()]), Body()]))
    should_be_unvalid(Html([Head(P()), Body()]))

    # Body et Div ne doivent contenir que des éléments des types suivant : H1, H2, Div, Table, Ul, Ol, Span, ou Text.
    should_be_valid(Html([Head(Title()), Body([H1(), H2(), Div(), Table(), Ul(Li()), Ol(Li()), Span(), Text()])]))
    should_be_valid(Html([Head(Title()), Body(Div([H1(), H2(), Div(), Table(), Ul(Li()), Ol(Li()), Span(), Text()]))]))
    
    should_be_unvalid(Html([Head(), Body(Title())]))
    should_be_unvalid(Html([Head(), Body(Div(Title()))]))
    should_be_unvalid(Html([Head(), Body(Div(Div([H1(), H2(), Tr()])))]))

    # Title, H1, H2, Li, Th, Td ne doivent contenir qu’un unique Text et uniquement ce Text.
    should_be_valid(Html([Head(Title(Text("a"))), Body([H1(Text("a")), H2(Text("a")), Table([Tr(Th(Text("a"))), Tr(Td(Text("a")))]), Ul(Li(Text("a")))])]))

    should_be_unvalid(Html([Head([Title([Text("a"), Text("a")])]), Body([])]))
    should_be_unvalid(Html([Head([Title(H1())]), Body([])]))

    # P ne doit contenir que des Text.
    should_be_valid(Html([Head(Title()), Body(Div(Span(P([Text("Hello"), Text("World")]))))]))

    should_be_unvalid(Html([Head(Title()), Body(Div(Span(P(Div()))))]))
    should_be_unvalid(Html([Head(Title()), Body(Div(Span(P([P(), H1()]))))]))

    # Span ne doit contenir que des Text ou des P.
    should_be_valid(Html([Head(Title()), Body(Div(Span([P(Text("Hello")), Text("World")])))]))

    should_be_unvalid(Html([Head(Title()), Body(Div(Span(Div())))]))
    should_be_unvalid(Html([Head(Title()), Body(Div(Span([Text("Hello world"), Th()])))]))

    # Ul et Ol doivent contenir au moins un Li et uniquement des Li.
    should_be_valid(Html([Head(Title()), Body(Div(Ul([Li(), Li(), Li()])))]))
    should_be_valid(Html([Head(Title()), Body(Div(Ul(Li())))]))
    should_be_valid(Html([Head(Title()), Body(Div(Ol(Li())))]))

    should_be_unvalid(Html([Head(), Body(Ul(P()))]))
    should_be_unvalid(Html([Head(), Body(Ul([Li(), P()]))]))
    should_be_unvalid(Html([Head(), Body(Ul())]))
    should_be_unvalid(Html([Head(), Body(Ol([Li(), P()]))]))

    # Tr doit contenir au moins un Th ou Td et uniquement des Th ou des Td. Les Th et les Td doivent être mutuellement exclusifs.
    should_be_valid(Html([Head(Title()), Body(Table([Tr([Th(), Th()]), Tr([Td(), Td()])]))]))
    should_be_valid(Html([Head(Title()), Body(Table([Tr(Th()), Tr([Td(), Td()])]))]))

    should_be_unvalid(Html([Head(Title()), Body(Table([Tr([Th(), Td()]), Tr([Td(), Td()])]))]))
    should_be_unvalid(Html([Head(Title()), Body(Table([Tr(), Tr([Td(), Td()])]))]))

    # Table : ne doit contenir que des Tr et uniquement des Tr.
    should_be_valid(Html([Head(Title()), Body(Table(Tr([Th(), Th()])))]))
    
    should_be_unvalid(Html([Head(Title()), Body(Table(Td()))]))
    should_be_unvalid(Html([Head(Title()), Body(Table([Tr(Th()), P(Text("Hello world"))]))]))

    print("Everything's good :)")
