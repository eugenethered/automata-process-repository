import unittest

from processrepo.Process import ProcessStatus


class ProcessStatusTestCase(unittest.TestCase):

    def test_should_parse_status(self):
        status = ProcessStatus.parse('running')
        self.assertEqual(status, ProcessStatus.RUNNING)

    def test_something(self):
        checks = [ProcessStatus.RUNNING, ProcessStatus.ERROR]
        self.assertTrue(ProcessStatus.RUNNING in checks)
        self.assertTrue(ProcessStatus.ERROR in checks)
        self.assertFalse(ProcessStatus.INITIALIZED in checks)


if __name__ == '__main__':
    unittest.main()
