
import unittest
from cal import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            get_index = a.get('/')
            self.assertEqual(get_index._status_code, 200)
           
            post_index_mul = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Mul'})
        
            
            self.assertEqual(post_index_mul._status_code, 302)
           



    def test_mul(self):
        with app.test_client() as a:
            get_mul = a.get('/mul', query_string={'A':'4', 'B':'2'})
            self.assertEqual(get_mul._status_code, 200)
            result_string = get_mul.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 8)

  
if __name__ == '__main__':
    unittest.main()
