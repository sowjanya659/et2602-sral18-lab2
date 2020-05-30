import unittest
from main import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            get_index = a.get('/')
            self.assertEqual(get_index._status_code, 200)
            post_index_add = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Add'})
            post_index_sub = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Sub'})
            post_index_mul = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Mul'})
            post_index_div = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Div'})
            self.assertEqual(post_index_add._status_code, 302)
            self.assertEqual(post_index_sub._status_code, 302)
            self.assertEqual(post_index_mul._status_code, 302)
            self.assertEqual(post_index_div._status_code, 302)

    def test_add(self):
        with app.test_client() as a:
            get_add = a.get('/add', query_string={'A':'4', 'B':'2'})
            self.assertEqual(get_add._status_code, 200)
            result_string = get_add.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 6)

    def test_sub(self):
        with app.test_client() as a:
            get_sub = a.get('/sub', query_string={'A':'4', 'B':'2'})
            self.assertEqual(get_sub._status_code, 200)
            result_string = get_sub.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 2)

    def test_mul(self):
        with app.test_client() as a:
            get_mul = a.get('/mul', query_string={'A':'4', 'B':'2'})
            self.assertEqual(get_mul._status_code, 200)
            result_string = get_mul.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 8)

    def test_div(self):
        with app.test_client() as a:
            get_div = a.get('/div', query_string={'A':'4', 'B':'2'})
            self.assertEqual(get_div._status_code, 200)
            result_string = get_div.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
