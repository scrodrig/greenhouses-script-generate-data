import unittest
import manager_util as manager_util


class ManagerUtilTestCase(unittest.TestCase):
    def test_data_in_minutes(self):
        path = '/Users/SchubertDavidRodriguez/Projects/Python/DataManager/Data/'
        input_file = 'raw_data.csv'
        minutes = 30
        file = manager_util.get_generate_minutes_splited(path=path, minutes=minutes, input_file=input_file)
        self.assertEqual(file, 'raw_data_minutes.csv')

    def test_data_grouped_in_minutes(self):
        path = '/Users/SchubertDavidRodriguez/Projects/Python/DataManager/Data/'
        input_file = 'raw_data_minutes.csv'
        minutes = 30
        time_behind_hours = 2
        manager_util.group_by_hours_temperature(path=path, minutes=minutes,
                                                input_file=input_file, time_behind_hours=time_behind_hours)
        self.assertEqual(True, True)

    def test_data_luminosity_grouped_in_minutes(self):
        path = '/Users/SchubertDavidRodriguez/Projects/Python/DataManager/Data/'
        input_file = 'raw_data_minutes.csv'
        minutes = 30
        time_behind_hours = 2
        manager_util.group_by_hours_luminosity(path=path, minutes=minutes,
                                               input_file=input_file, time_behind_hours=time_behind_hours)
        self.assertEqual(True, True)

    def test_data_ground_humidity_grouped_in_minutes(self):
        path = '/Users/SchubertDavidRodriguez/Projects/Python/DataManager/Data/'
        input_file = 'raw_data_minutes.csv'
        minutes = 30
        time_behind_hours = 2
        manager_util.group_by_hours_ground_humidity(path=path, minutes=minutes,
                                                    input_file=input_file, time_behind_hours=time_behind_hours)
        self.assertEqual(True, True)

    def test_data_ground_humidity_grouped_in_minutes(self):
        path = '/Users/SchubertDavidRodriguez/Projects/Python/DataManager/Data/'
        input_file = 'raw_data_minutes.csv'
        minutes = 30
        time_behind_hours = 2
        manager_util.group_by_hours_environment_humidity(path=path, minutes=minutes,
                                                         input_file=input_file, time_behind_hours=time_behind_hours)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
