import unittest
import vocab

class VocabTest(unittest.TestCase):

    def test_init(self):
        # v0 = vocab.Vocab('bitch', [
            # ('hi', '1101'),
            # ('goodbye', '1000029'),
            # ('au revoir', 'shit')
            # ])
        name = 'test'
        dict1 = {'hi': '1101',
                 'goodbye': '1000029',
                 'au revoir': 'shit'
                }

        v0 = vocab.Vocab(name, dict1)

        self.assertEqual(v0.get_name(), 'test')
        # self.assertTrue(False)
        list0 = v0.get_vocab_list()
        self.assertIsInstance(v0.get_name(), str)
        self.assertIsInstance(list0, dict)
        self.assertIn('hi', list0)
        self.assertEqual(list0['hi'], '1101')
        self.assertIn('goodbye', list0)
        self.assertEqual(list0['goodbye'], '1000029')
        self.assertIn('au revoir', list0)
        self.assertEqual(list0['au revoir'], 'shit')

        v_blank = vocab.Vocab()

        self.assertEqual(v_blank.get_name(), 'default name')
        self.assertEqual(v_blank.get_vocab_list(), {})
        self.assertIsInstance(v_blank.get_name(), str)
        self.assertIsInstance(list0, dict)


        #holy mother of
        

    def test_holy_mother_of_symbols(self):
        v = vocab.Vocab('[[[[]gorp!@)(87845,./;[]|\\-_=+)]][][]', {})
        self.assertEqual(v.get_name(), '[[[]gorp!@)(87845,./;[]|\\-_=+)]][][')

    def test_get_name(self):
        name = 'test'
        dict1 = {'hi': '1101',
                 'goodbye': '1000029',
                 'au revoir': 'shit'
                }
        v = vocab.Vocab(name, dict1)

        self.assertIsInstance(v.get_name(), str)
        self.assertEqual(v.get_name(), 'test')

    def test_get_vocab_list(self):
        name = 'test'
        dict1 = {'hi': '1101',
                 'goodbye': '1000029',
                 'au revoir': 'shit'
                }
        v = vocab.Vocab(name, dict1)

        # self.assertTrue(isinstance(v.get_vocab_list(), dict))
        self.assertIsInstance(v.get_vocab_list(), dict)
        self.assertEqual(v.get_vocab_list(), {'hi': '1101', 'goodbye': '1000029', 'au revoir': 'shit'})

    def test_set_name(self):
        name = 'test'
        dict1 = {'hi': '1101',
                 'goodbye': '1000029',
                 'au revoir': 'shit'
                }
        v = vocab.Vocab(name, dict1)

        self.assertEqual(v.get_name(), 'test')
        v.set_name('billy bob')
        self.assertEqual(v.get_name(), 'billy bob')
        self.assertEqual(v.get_vocab_list(), {'hi': '1101', 'goodbye': '1000029', 'au revoir': 'shit'})

    def test_set_vocab_list(self):
        name = 'test'
        dict1 = {'hi': '1101',
                 'goodbye': '1000029',
                 'au revoir': 'shit'
                }
        v = vocab.Vocab(name, dict1)

        self.assertEqual(v.get_vocab_list(), {'hi': '1101', 'goodbye': '1000029', 'au revoir': 'shit'})
        v.set_vocab_list({'hi': '1101', 'goodbye': '1000029', 'au revoir': 'shit'})
        self.assertEqual(v.get_name(), 'test')

    def test_check(self):
        name = 'test'
        dict1 = {'hi': '1101',
                 'goodbye': '90210',
                 'au revoir': 'goodbye',
                 'weeaboo shit': 'domo arigatou mr roboto'
                }
        v = vocab.Vocab(name, dict1)
        self.assertTrue(v.check('hi', '1101'))
        self.assertFalse(v.check('hi', 1101))
        self.assertFalse(v.check('hi', []))
        self.assertFalse(v.check('hi', {}))

        self.assertTrue(v.check('goodbye', '90210'))
        self.assertTrue(v.check('au revoir', 'goodbye'))
        self.assertTrue(v.check('weeaboo shit', 'domo arigatou mr roboto'))
        self.assertFalse(v.check('kboo shit', 'domo arigatou mr roboto'))


if __name__ == '__main__':
    unittest.main()