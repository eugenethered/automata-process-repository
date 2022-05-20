import unittest

from cache.holder.RedisCacheHolder import RedisCacheHolder

from processrepo.Process import Process, ProcessStatus
from processrepo.repository.ProcessRepository import ProcessRepository


class ProcessRepositoryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        options = {
            'REDIS_SERVER_ADDRESS': '192.168.1.90',
            'REDIS_SERVER_PORT': 6379,
            'PROCESS_KEY': 'test:process:status:{}'
        }
        self.cache = RedisCacheHolder(options)
        self.repository = ProcessRepository(options)

    def tearDown(self):
        self.cache.delete('test:process:status:conductor')

    def test_should_store_and_retrieve_process(self):
        process = Process('conductor', 1, ProcessStatus.RUNNING)
        self.repository.store(process)
        stored_process = self.repository.retrieve(process.name)
        self.assertEqual(process, stored_process)


if __name__ == '__main__':
    unittest.main()
