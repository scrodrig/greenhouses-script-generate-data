import unittest
import manager


class ManagerTestCase(unittest.TestCase):
    def test_manager_file(self):
        path = '/Users/SchubertDavidRodriguez/Projects/Python/DataManager/Data/'
        input_file = 'raw_data.csv'
        minutes = 30
        time_behind_hours = 4
        training_percentage = 70
        manager.prepare_data_from_row(path=path,
                                      minutes=minutes,
                                      input_file=input_file,
                                      time_behind_minutes=time_behind_hours,
                                      training_percentage=training_percentage)

        self.assertEqual(True, True)

    def test_manager_file_std(self):
        path = '/Users/SchubertDavidRodriguez/Projects/Python/DataManager/Data/'
        input_file = 'raw_data.csv'
        minutes = 30
        time_behind_hours = 4
        training_percentage = 70
        manager.prepare_data_from_row_std(path=path,
                                          minutes=minutes,
                                          input_file=input_file,
                                          time_behind_minutes=time_behind_hours,
                                          training_percentage=training_percentage)

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
