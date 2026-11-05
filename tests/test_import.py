import unittest

import pyroai


class PackageSmokeTests(unittest.TestCase):
    def test_package_imports(self):
        self.assertEqual(pyroai.__version__, "0.1.0.dev0")


if __name__ == "__main__":
    unittest.main()
