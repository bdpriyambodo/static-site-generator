import unittest

from split_blocks import markdown_to_blocks, block_to_blocktype, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_newlines(self):
            md = """
    This is **bolded** paragraph




    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

class TestBlockType(unittest.TestCase):
     def test_heading(self):
        block = '# TITLE'
        result = block_to_blocktype(block)
        self.assertEqual(
             result, 
             BlockType.HEADING
        )

     def test_code(self):
        block = '```` TITLE````'
        result = block_to_blocktype(block)
        self.assertEqual(
             result, 
             BlockType.CODE
        )

     def test_unorderedlist(self):
        block = '- This is a list\n- with items'
        result = block_to_blocktype(block)
        self.assertEqual(
             result, 
             BlockType.ULIST
        )

     def test_orderedlist(self):
        block = '1. This is a list\n2. with items'
        result = block_to_blocktype(block)
        self.assertEqual(
             result, 
             BlockType.OLIST
        )      

     def test_quote(self):
        block = '> TITLE'
        result = block_to_blocktype(block)
        self.assertEqual(
             result, 
             BlockType.QUOTE
        )

     def test_quote(self):
        block = 'TITLE'
        result = block_to_blocktype(block)
        self.assertEqual(
             result, 
             BlockType.PARAGRAPH
        )

     ## Additional:
     def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_blocktype(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_blocktype(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()