import unittest

from cache.holder.RedisCacheHolder import RedisCacheHolder

from processrepo.Process import Process, ProcessStatus
from processrepo.repository.ProcessRepository import ProcessRepository


class ProcessRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        options = {
            'REDIS_SERVER_ADDRESS': '192.168.1.90',
            'REDIS_SERVER_PORT': 6379,
            'PROCESS_KEY': '{}:process:status:{}'
        }
        self.cache = RedisCacheHolder(options)
        self.repository = ProcessRepository(options)

    def tearDown(self):
        self.cache.delete('test:process:status:conductor')
        self.cache.delete('test:process:status:a')
        self.cache.delete('test:process:status:b')

    def test_should_store_and_retrieve_process(self):
        process = Process('test', 'conductor', 1, ProcessStatus.RUNNING)
        self.repository.store(process)
        stored_process = self.repository.retrieve(process.name, process.market)
        self.assertEqual(process, stored_process)

    def test_should_store_multiple_processes_and_retrieve_all(self):
        process_a = Process('test', 'a', 1, ProcessStatus.RUNNING)
        process_b = Process('test', 'b', 1, ProcessStatus.RUNNING)
        self.repository.store(process_a)
        self.repository.store(process_b)
        stored_processes = self.repository.retrieve_all('test')
        self.assertEqual([process_a, process_b], stored_processes)


if __name__ == '__main__':
    unittest.main()
