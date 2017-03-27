import unittest
from StringIO import StringIO

import datetime

import re

import numpy
from numpy.matlib import randn

import manager_util as mn
import time
import pandas as pd
import nil as nil
from querycsv.querycsv import (query_csv, query_csv_file,
                               query_sqlite, import_csv,
                               pretty_print, as_connection,
                               import_array, write_csv)

TEST_DIR = 'test_files'


def to_csv_rows(content):
    return [[col.strip() for col in row.split(',')]
            for row in content.strip().split('\n')]


def is_in_range(x):
    if 1478624006 < x < 1478624039:
        return 1
    else:
        return 0


def transform_start_time(x):
    y = re.sub(r'([()])', '', x)
    y = y.split(',')
    new_date = datetime.datetime.now()
    if len(y) == 4:
        new_date = datetime.datetime(int(y[0]), int(y[1]), int(y[2]), int(y[3]))
    else:
        new_date = datetime.datetime(int(y[0]), int(y[1]), int(y[2]), int(y[3]), int(y[4]))
    return new_date


class SpikeTestCase(unittest.TestCase):
    def assertMatch(self, results, content):
        rows = to_csv_rows(content)
        self.assertEqual(len(results), len(rows))
        for y in xrange(0, len(rows)):
            rowA = rows[y]
            rowB = results[y]
            self.assertEqual(len(rowA), len(rowB))
            for x in xrange(0, len(rowA)):
                a = str(rowA[x])
                b = str(rowB[x])
                self.assertEqual(a, b)

    def test_read_csv(self):
        foo = u'test_files/foo.csv'
        results = query_csv('select * from foo', foo)
        self.assertTrue(results != nil)

    def test_print_test_data(self):
        testdata = u'../Data/testdata.csv'
        fp = StringIO()
        results = query_csv('select * from testdata', testdata)
        pretty_print(results, fp)
        self.assertNotEqual(results, nil)

    def test_write_file(self):
        testdata = u'../Data/testdata.csv'
        results = query_csv('select * from testdata', testdata)
        df = pd.DataFrame(results)
        df.to_csv('output/list.csv', index=False, header=False)
        self.assertEquals(True, True)

    def test_first_results(self):
        raw_data = u'../Data/raw_data.csv'
        results = query_csv('select * from raw_data WHERE temperature1="27.1" limit 100', raw_data)
        df = pd.DataFrame(results)
        df.to_csv('output/first-results.csv', index=False, header=False)
        self.assertEquals(True, True)

    def test_pandas_read_write_clause(self):
        df = pd.read_csv('../Data/raw_data.csv')
        df = df[df['temperature1'] == 27.1]
        df.to_csv('output/other-full-results.csv', index=False)
        self.assertEquals(True, True)

    def test_date_transform_pandas(self):
        df = pd.read_csv('../Data/raw_data.csv')
        df['start_time'] = pd.to_datetime(df["start_time"], unit='s')
        df.to_csv('output/other-full-results.csv', index=False)
        self.assertEquals(True, True)

    def test_average_pandas_no_filter(self):
        df = pd.read_csv('../Data/raw_data.csv')
        df = df[["temperature1", "temperature2"]].mean()
        # df["temperature2"] = df["temperature2"].mean()
        df.to_csv('output/other-full-results.csv', index=False)
        self.assertEquals(True, True)

    def test_group_by_hours(self):
        df = pd.read_csv('../Data/raw_data.csv')
        df['start_time'] = pd.to_datetime(df["start_time"], unit='s')
        # grouped = df.groupby([times.hour, times.minute])
        grouped = df.groupby(by=[df.start_time.map(lambda x: (x.year, x.month, x.day, x.hour))])
        # grouped[["temperature1","temperature2"]].mean()
        print grouped.size()
        # df.to_csv('output/other-full-results.csv', index=False)
        self.assertEquals(True, True)

    def test_group_by_minutes_average_temperature(self):
        df = pd.read_csv('../Data/raw_data.csv')
        df = df.set_index(['start_time'])
        df.index = pd.to_datetime(df.index, unit='s')
        ticks = df.ix[:, ['temperature1',
                          'temperature2',
                          'luminosity',
                          'ground_humidity1',
                          'ground_humidity2',
                          'ground_humidity3',
                          'environment_humidity1',
                          'environment_humidity2']]
        ticks = ticks.resample('30min').mean()
        ticks['temperature'] = ticks[['temperature1', 'temperature2']].mean(axis=1)
        ticks['error_temperature'] = ticks[['temperature1', 'temperature2']].std(axis=1)
        ticks['luminosity'] = ticks[['luminosity']].mean(axis=1)
        ticks['error_luminosity'] = ticks[['luminosity']].std(axis=1)
        ticks['ground_humidity'] = ticks[['ground_humidity1', 'ground_humidity2', 'ground_humidity3']].mean(axis=1)
        ticks['error_ground_humidity'] = ticks[['ground_humidity1', 'ground_humidity2', 'ground_humidity3']].std(axis=1)
        ticks['environment_humidity'] = ticks[['environment_humidity1', 'environment_humidity2']].mean(axis=1)
        ticks['error_environment_humidity'] = ticks[['environment_humidity1', 'environment_humidity2']].std(axis=1)

        ticks['end_time'] = ticks.index + datetime.timedelta(hours=0, minutes=15)

        ticks.to_csv('output/raw_data_minutes.csv', index=True, na_rep='N/A', columns=['temperature',
                                                                                       'error_temperature',
                                                                                       'environment_humidity',
                                                                                       'error_environment_humidity',
                                                                                       'ground_humidity',
                                                                                       'error_ground_humidity',
                                                                                       'luminosity',
                                                                                       'error_luminosity',
                                                                                       'end_time'])
        self.assertEquals(True, True)

    def test_group_by_hours_temperature(self):
        df = pd.read_csv('../Data/raw_data.csv')
        df['start_time'] = pd.to_datetime(df["start_time"], unit='s')
        # grouped = df.groupby([times.hour, times.minute])
        grouped = df.groupby(by=[df.start_time.map(lambda x: (x.year, x.month, x.day, x.hour))]).mean()
        grouped['start'] = grouped.index.map(lambda x: (transform_start_time(format(x))))
        grouped.to_csv('output/grouped-hour-results.csv', index=True, na_rep='N/A')
        self.assertEquals(True, True)

    def test_group_by_hours_average_temperature(self):
        df = pd.read_csv('../Data/raw_data_minutes.csv')
        columns = ['start_time', 'end_time'].append(list('01234'))
        period = 30
        hours = 2
        # period = 60*2 + 30

        registresBefore = (60 * hours) / period
        ticks = pd.DataFrame()
        ticks['temperature'] = df['temperature']
        result = pd.DataFrame()
        for x in range(0, ticks['temperature'].size):
            result = result.append(ticks.head(registresBefore + 1).transpose())
            # result.reset_index(inplace=True, drop=True)
            ticks.drop(ticks.index[0], inplace=True)
            ticks.reset_index(inplace=True, drop=True)
            result.reset_index(inplace=True, drop=True)
        result['start_time'] = df['start_time']
        result['end_time'] = pd.to_datetime(result['start_time']) + datetime.timedelta(minutes=60 * hours)
        result = result.dropna()
        print result
        result.to_csv('output/grouped-no-gaps-range-results.csv', index=False, columns=columns)
        self.assertEquals(True, True)

    def test_group_by_hours_average_temperature_error(self):
        df = pd.read_csv('output/raw_data_minutes.csv')
        period = 30
        hours = 4
        # period = 60*2 + 30

        registresBefore = (60 * hours) / period
        ticks = pd.DataFrame()
        ticks['temperature'] = df['temperature']
        # ticks['error_temperature'] = df['error_temperature']
        dates = pd.DataFrame()
        result = pd.DataFrame()
        for x in range(0, ticks['temperature'].size):
            result = result.append(ticks.head(registresBefore + 1).transpose())
            # result.reset_index(inplace=True, drop=True)
            ticks.drop(ticks.index[0], inplace=True)
            ticks.reset_index(inplace=True, drop=True)
            result.reset_index(inplace=True, drop=True)


        # result['end_time'] = pd.to_datetime(result['start_time']) + datetime.timedelta(minutes=60 * hours)
        result = result.dropna()

        ticks_2 = pd.DataFrame()
        result_1 = pd.DataFrame()
        ticks_2['error_temperature'] = df['error_temperature']
        for x in range(0, ticks_2['error_temperature'].size):
            result_1 = result_1.append(ticks_2.head(registresBefore + 1).transpose())
            ticks_2.drop(ticks_2.index[0], inplace=True)
            ticks_2.reset_index(inplace=True, drop=True)
            result_1.reset_index(inplace=True, drop=True)
        result = result.dropna()
        result_1 = result_1.dropna()
        result.reset_index(inplace=True, drop=True)
        result_1.reset_index(inplace=True, drop=True)

        result_1.drop(result_1.columns[len(result_1.columns) - 1], axis=1, inplace=True)

        #print result

        result = result.rename_axis(lambda x: 2 * x, axis=1)
        result_1 = result_1.rename_axis(lambda x: 2 * x + 1, axis=1)
        result['start_time'] = df['start_time']

        result_2 = pd.concat([result, result_1], axis=1)

        result_2 = result_2.sort_index(axis=1)

        print result_2

        result_2.reset_index(inplace=True, drop=True)

        result_2['hour'] = pd.to_datetime(result['start_time']).dt.hour + \
                           pd.to_datetime(result['start_time']).dt.minute / 60 + \
                           pd.to_datetime(result['start_time']).dt.second / 3600

        result_2['day_year'] = pd.to_datetime(result['start_time']).dt.dayofyear

        training = len(result_2.index) * 70 / 100
        test = len(result_2.index) - training
        training_data = result_2.head(training)
        result_2 = result_2.ix[training:]
        result_2.reset_index(drop=True, inplace=True)
        test_data = result_2.head(test)

        training_data.to_csv('output/grouped-no-gaps-range-results_training.csv', index=False, header=False)
        test_data.to_csv('output/grouped-no-gaps-range-results_test.csv', index=False, header=False)

        self.assertEquals(True, True)

    def test_append(self):
        df = pd.DataFrame([[1, 2], [3, 4]])
        print df

        # frm = frm.take([1, 4, 3])
        df2 = pd.DataFrame([[5, 6], [7, 8]])
        print df2

        df3 = df.append(df2, ignore_index=True)
        print df3

        self.assertEquals(True, True)

    def test_invert_temperature(self):
        frm = pd.DataFrame(randn(5, 2))
        print frm
        df2 = pd.DataFrame([[5, 6], [7, 8]])
        print df2
        # frm = frm.take()
        frm = frm.transpose().append(df2)
        print frm

        # frm = frm.take([0, 2], axis=1)
        # print frm

        self.assertEquals(True, True)

    def test_remove_first(self):
        frm = pd.DataFrame(randn(5, 1))
        print frm

        # frm = frm.take([1, 4, 3])
        frm = frm.drop(frm.index[0])
        frm.reset_index(inplace=True, drop=True)
        print frm

        # frm = frm.take([0, 2], axis=1)
        # print frm

        self.assertEquals(True, True)


if __name__ == '__main__':
    unittest.main()
