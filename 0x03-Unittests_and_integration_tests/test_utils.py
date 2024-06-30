import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing access_nested_map"""
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str],
                               expected_output: Union[Dict, int]) -> None:
        """Test output of access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)


if __name__ == "__main__":
    unittest.main()
