from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    # PLAIN_TEXT = 'plain text'
    # BOLD_TEXT = 'bold text'
    # ITALIC_TEXT = 'italic text'
    # CODE_TEXT = 'code text'
    # LINK = 'link'
    # IMAGE = 'image'
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self):
        return (f'TextNode({self.text}, {self.text_type.value}, {self.url})')


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text, None )
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None )
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None )
        case TextType.CODE:
            return LeafNode("code", text_node.text, None )
        case TextType.LINK:
            prop = {
                "href": {text_node.url}
            }
            return LeafNode("a", text_node.text, prop )
        case TextType.IMAGE:
            prop = {
                "src": text_node.url,
                "alt": text_node.text          
            }
            return LeafNode("img", "", prop )
        case _:
            raise Exception('Text Type is not recognized')