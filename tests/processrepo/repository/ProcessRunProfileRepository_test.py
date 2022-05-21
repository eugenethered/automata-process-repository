import unittest

from cache.holder.RedisCacheHolder import RedisCacheHolder

from processrepo.ProcessRunProfile import ProcessRunProfile
from processrepo.repository.ProcessRunProfileRepository import ProcessRunProfileRepository


class ProcessRunProfileRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        options = {
            'REDIS_SERVER_ADDRESS': '192.168.1.90',
            'REDIS_SERVER_PORT': 6379,
            'PROCESS_RUN_PROFILE_KEY': '{}:process:run-profile:{}'
        }
        self.cache = RedisCacheHolder(options)
        self.repository = ProcessRunProfileRepository(options)

    def tearDown(self):
        self.cache.delete('test:process:run-profile:conductor')

    def test_should_store_and_retrieve_process_run_profile(self):
        process_run_profile = ProcessRunProfile('test', 'conductor', 'minute')
        self.repository.store(process_run_profile)
        stored_process_run_profile = self.repository.retrieve('conductor', 'test')
        self.assertEqual(process_run_profile, stored_process_run_profile)


if __name__ == '__main__':
    unittest.main()
