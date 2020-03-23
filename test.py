import unittest
from Color import Color
from Country import Country
from Setup_editor import new_country_file


class TestColor(unittest.TestCase):
    """Testing the color module"""

    def test_from_csv(self):
        c1 = "rgb { 235 132 240 }\t\t\tcolor2"
        c2 = "rgb { 47 142 209 }\t\t\tcolor3"
        color = Color()
        # We change the value of the attributes of color according to c1 and c2.
        color.from_csv(c1, c2)
        self.assertEqual(color.red1, 235)
        self.assertEqual(color.green1, 132)
        self.assertEqual(color.blue1, 240)
        self.assertEqual(color.red2, 47)
        self.assertEqual(color.green2, 142)
        self.assertEqual(color.blue2, 209)
    
    def test_str(self):
        c1 = "rgb { 235 132 240 }\t\t\tcolor2"
        c2 = "rgb { 47 142 209 }\t\t\tcolor3"
        color = Color()
        color.from_csv(c1, c2)
        expected_string = """color = rgb { 235 132 240 }\n"""\
        """color2 = rgb { 47 142 209 }\n"""
        self.assertEqual(str(color), expected_string)
    
    def test_Setup_editor(self):
        c1 = "rgb { 235 132 240 }\t\t\tcolor2"
        c2 = "rgb { 47 142 209 }\t\t\tcolor3"
        country = Country("TST")
        color = Color()
        color.from_csv(c1, c2)
        country.color = color
        country.gender_equality = True
        new_country_file(country, "countries\\iberia\\")
        expected_content = ['color = rgb { 235 132 240 }\n',
                            'color2 = rgb { 47 142 209 }\n',
                            '\n', 'gender_equality = yes\n', '\n',
                            'ship_names = {\n', '\t#\n', '}']
        new_country_file(country, "")
        with open("TST.txt", "r") as file:
            content = file.readlines()
        self.assertEqual(content, expected_content)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()