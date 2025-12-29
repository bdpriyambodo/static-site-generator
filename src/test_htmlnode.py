import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_001(self):
        node = HTMLNode('h1','This is an H1 heading',None,None)
        html = node.props_to_html()
        self.assertEqual(html,'')

    def test_002(self):
        prop = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode('h1','This is an H1 heading',None,prop)
        html = node.props_to_html()
        self.assertEqual(html,' href="https://www.google.com" target="_blank"')
        
    def test_003(self):
        node = HTMLNode('h1','This is an H1 heading',None,None)
        node2 = HTMLNode('h1','This is an H1 heading',None,None)
        self.assertEqual(node, node2)
 
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(
            node.to_html(),
            "<p>Hello, world!</p>"
            )

    def test_leaf_to_html_p2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
            )

    def test_leaf_to_html_p3(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!") 

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()