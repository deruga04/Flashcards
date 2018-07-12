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

        self.assertTrue(v0.get_name() == 'test')
        # self.assertTrue(False)
        list0 = v0.get_vocab_list()
        self.assertTrue(isinstance(v0.get_name(), str))
        self.assertTrue(isinstance(list0, dict))
        self.assertTrue('hi' in list0)
        self.assertTrue(list0['hi'] == '1101')
        self.assertTrue('goodbye' in list0)
        self.assertTrue(list0['goodbye'] == '1000029')
        self.assertTrue('au revoir' in list0)
        self.assertTrue(list0['au revoir'] == 'shit')

        v_blank = vocab.Vocab()

        self.assertTrue(v_blank.get_name() == 'default name')
        self.assertTrue(v_blank.get_vocab_list() == {})
        self.assertTrue(isinstance(v_blank.get_name(), str))
        self.assertTrue(isinstance(list0, dict))

    def test_accessor(self):
        name = 'test'
        dict1 = {'hi': '1101',
                 'goodbye': '1000029',
                 'au revoir': 'shit'
                }
        v = vocab.Vocab(name, dict1)

        self.assertTrue(isinstance(v.get_name(), str))
        self.assertTrue(isinstance(v.get_vocab_list(), dict))
        self.assertTrue(v.get_name() == 'test')
        self.assertTrue(v.get_vocab_list() == {'hi': '1101', 'goodbye': '1000029', 'au revoir': 'shit'})

    def test_mutator(self):
        name = 'test'
        dict1 = {'hi': '1101',
                 'goodbye': '1000029',
                 'au revoir': 'shit'
                }
        v = vocab.Vocab(name, dict1)

        self.assertTrue(v.get_name() == 'test')
        v.set_name('billy bob')
        self.assertTrue(v.get_name() == 'billy bob')

        self.assertTrue(v.get_vocab_list() == {'hi': '1101', 'goodbye': '1000029', 'au revoir': 'shit'})
        v.set_vocab_list({'hi': '1101', 'goodbye': '1000029', 'au revoir': 'shit'})
        self.assertTrue(v.get_name() == 'billy bob')

if __name__ == '__main__':
    unittest.main()