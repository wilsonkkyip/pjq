import unittest
from pjq import pjq

test_object = {
    "menu": {
        "header": "SVG Viewer",
        "items": [
            {"id": "Open"},
            {"id": "OpenNew", "label": "Open New"},
            None,
            {"id": "ZoomIn", "label": "Zoom In"},
            {"id": "ZoomOut", "label": "Zoom Out"},
            {"id": "OriginalView", "label": "Original View"},
            None,
            {"id": "Quality"},
            {"id": "Pause"},
            {"id": "Mute"},
            None,
            {"id": "Find", "label": "Find..."},
            {"id": "FindAgain", "label": "Find Again"},
            {"id": "Copy"},
            {"id": "CopyAgain", "label": "Copy Again"},
            {"id": "CopySVG", "label": "Copy SVG"},
            {"id": "ViewSVG", "label": "View SVG"},
            {"id": "ViewSource", "label": "View Source"},
            {"id": "SaveAs", "label": "Save As"},
            None,
            {"id": "Help"},
            {"id": "About", "label": "About Adobe CVG Viewer..."}
        ]
    }
}

test_list = [
    {"name": "Gilbert", "wins": [["straight", "7♣"], ["one pair", "10♥"]]},
    {"name": "Alexa", "wins": [["two pair", "4♠"], ["two pair", "9♠"]]},
    {"name": "May", "wins": []},
    {"name": "Deloise", "wins": [["three of a kind", "5♣"]]}
]

class TestPJQ(unittest.TestCase):
    def test_json_object(self):
        self.assertEqual(pjq(test_object, "menu.header"), "SVG Viewer")
        self.assertEqual(pjq(test_object, "menu.items.1"), {"id": "OpenNew", "label": "Open New"})

    def test_json_list(self):
        self.assertEqual(pjq(test_list, ".name"), ["Gilbert", "Alexa", "May", "Deloise"])
        self.assertEqual(pjq(test_list, ".wins.0.1"), ["7♣", "4♠", None, "5♣"])

if __name__ == "__main__": 
    unittest.main()