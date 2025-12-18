import unittest

from htmlnode import HTMLNode

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
 
        


if __name__ == "__main__":
    unittest.main()