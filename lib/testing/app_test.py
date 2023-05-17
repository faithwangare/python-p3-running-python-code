import io
import sys
import runpy
import unittest

class TestAppPy(unittest.TestCase):

    def test_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        captured_out = io.BytesIO()  # Update to BytesIO
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")

        sys.stdout = sys.__stdout__  # Reset stdout
        output = captured_out.getvalue().strip()
        expected_output = b"Hello World! Pass this test, please."
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
