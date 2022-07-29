import unittest

from cache.holder.RedisCacheHolder import RedisCacheHolder
from cache.provider.RedisCacheProviderWithHash import RedisCacheProviderWithHash

from processrepo.ProcessRunProfile import ProcessRunProfile, RunProfile
from processrepo.repository.ProcessRunProfileRepository import ProcessRunProfileRepository


class ProcessRunProfileRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        options = {
            'REDIS_SERVER_ADDRESS': '10.104.71.60',
            'REDIS_SERVER_PORT': 6379,
            'PROCESS_RUN_PROFILE_KEY': 'test:process:mv:run-profile'
        }
        self.cache = RedisCacheHolder(options, held_type=RedisCacheProviderWithHash)
        self.repository = ProcessRunProfileRepository(options)

    def tearDown(self):
        self.cache.delete('test:process:mv:run-profile')

    def test_should_store_and_retrieve_process_run_profile(self):
        process_run_profile = ProcessRunProfile('test', 'conductor', RunProfile.MINUTE)
        self.repository.store(process_run_profile)
        stored_process_run_profile = self.repository.retrieve('conductor', 'test')
        self.assertEqual(process_run_profile, stored_process_run_profile)

    def test_should_store_and_retrieve_enabled_process_run_profile(self):
        process_run_profile = ProcessRunProfile('test', 'conductor', RunProfile.MINUTE, True)
        self.repository.store(process_run_profile)
        stored_process_run_profile = self.repository.retrieve('conductor', 'test')
        self.assertEqual(process_run_profile, stored_process_run_profile)


if __name__ == '__main__':
    unittest.main()
