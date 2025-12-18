

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Optional error message") 
    
    def props_to_html(self):
        if not self.props:
            return ''
        combined = ''
        for key, value in self.props.items():
            combined = combined + f' {key}="{value}"'
        return combined

    def __repr__(self):
        return (f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})')
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )    
    
