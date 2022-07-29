import unittest

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash

from processrepo.Process import Process, ProcessStatus
from processrepo.ProcessRunProfile import RunProfile
from processrepo.repository.ProcessRepository import ProcessRepository


class ProcessRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        options = {
            'REDIS_SERVER_ADDRESS': '10.104.71.60',
            'REDIS_SERVER_PORT': 6379,
            'PROCESS_KEY': 'test:process:mv:status'
        }
        self.cache = RedisCacheHolder(options, held_type=RedisCacheProviderWithHash)
        self.repository = ProcessRepository(options)

    def tearDown(self):
        self.cache.delete('test:process:mv:status')

    def test_should_store_and_retrieve_process(self):
        process = Process('test', 'conductor', '0.0.1', 1, RunProfile.MINUTE, ProcessStatus.RUNNING)
        self.repository.store(process)
        stored_process = self.repository.retrieve(process.name, process.market)
        self.assertEqual(process, stored_process)

    def test_should_store_multiple_processes_and_retrieve_all(self):
        process_a = Process('test', 'a', '0.0.1', 1, RunProfile.ASAP, ProcessStatus.RUNNING)
        process_b = Process('test', 'b', '1.1.0', 1, RunProfile.MINUTE, ProcessStatus.RUNNING)
        self.repository.store(process_a)
        self.repository.store(process_b)
        stored_processes = self.repository.retrieve_all()
        self.assertEqual([process_b, process_a], stored_processes)


if __name__ == '__main__':
    unittest.main()
