import unittest
from cal import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            get_index = a.get('/')
            self.assertEqual(get_index._status_code, 200)
            post_index_add = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Add'})
            self.assertEqual(post_index_add._status_code, 302)
   

    def test_add(self):
        with app.test_client() as a:
            get_add = a.get('/add', query_string={'A':'4', 'B':'2'})
            self.assertEqual(get_add._status_code, 200)
            result_string = get_add.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main()
