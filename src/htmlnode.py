

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("will be implemented in Child class") 
    
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
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, children = None, props = props)

    def to_html(self):
        if not self.value:
            raise ValueError('All leaf nodes must have value')
        if not self.tag:
            return self.value
        return (f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>')
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag = tag, value = None, children = children, props = props)

    def to_html(self):
        if not self.tag:
            raise ValueError('All tags must have value')
        if not self.children:
            raise ValueError('All children must have value')
        for child in self.children:
            temp = child
            return (f'<{self.tag}{self.props_to_html()}>{temp.to_html()}</{self.tag}>')
            # return child.to_html()

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
