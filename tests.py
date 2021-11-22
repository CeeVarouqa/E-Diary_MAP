import datetime
import unittest

from posts import add_post


class MyTestCase(unittest.TestCase):
    def test_adding_posts(self):
        posts = []

        res = add_post(posts, id=len(posts), title='test', content='test content',
                       date_posted=datetime.datetime.now().date())

        self.assertGreater(len(res), 0)


if __name__ == '__main__':
    unittest.main()
