import datetime
import pandas as pd


def get_generate_minutes_splited(path, input_file, minutes):
    df = pd.read_csv(path + input_file)
    df = df.set_index(['start_time'])
    columns = ['end_time', 'temperature', 'luminosity', 'ground_humidity', 'environment_humidity']
    df.index = pd.to_datetime(df.index, unit='s')
    ticks = df.ix[:, ['temperature1',
                      'temperature2',
                      'luminosity',
                      'ground_humidity1',
                      'ground_humidity2',
                      'ground_humidity3',
                      'environment_humidity1',
                      'environment_humidity2']]
    ticks = ticks.resample(str(minutes) + 'min').mean()
    ticks['temperature'] = ticks[['temperature1', 'temperature2']].mean(axis=1)
    ticks['luminosity'] = ticks[['luminosity']].mean(axis=1)
    ticks['ground_humidity'] = ticks[['ground_humidity1', 'ground_humidity2', 'ground_humidity3']].mean(axis=1)
    ticks['environment_humidity'] = ticks[['environment_humidity1', 'environment_humidity2']].mean(axis=1)
    ticks['end_time'] = ticks.index + datetime.timedelta(minutes=minutes)
    ticks.to_csv(path + 'raw_data_minutes.csv', index=True, na_rep='N/A', columns=columns)
    return 'raw_data_minutes.csv'


def group_by_hours_temperature(path, input_file, minutes, time_behind_hours):
    df = pd.read_csv(path + input_file)
    period = minutes
    hours = time_behind_hours
    registers_before = (60 * hours) / period
    ticks = pd.DataFrame()
    ticks['temperature'] = df['temperature']
    result = pd.DataFrame()
    for x in range(0, ticks['temperature'].size):
        result = result.append(ticks.head(registers_before + 1).transpose())
        ticks.drop(ticks.index[0], inplace=True)
        ticks.reset_index(inplace=True, drop=True)
        result.reset_index(inplace=True, drop=True)
    result['start_time'] = df['start_time']
    result['end_time'] = pd.to_datetime(result['start_time']) + datetime.timedelta(minutes=60 * hours)
    result = result.dropna()
    result.to_csv(path + 'grouped-temperature-range-results.csv', index=False, header=False)


def group_by_hours_luminosity(path, input_file, minutes, time_behind_hours):
    df = pd.read_csv(path + input_file)
    period = minutes
    hours = time_behind_hours
    registers_before = (60 * hours) / period
    ticks = pd.DataFrame()
    ticks['luminosity'] = df['luminosity']
    result = pd.DataFrame()
    for x in range(0, ticks['luminosity'].size):
        result = result.append(ticks.head(registers_before + 1).transpose())
        ticks.drop(ticks.index[0], inplace=True)
        ticks.reset_index(inplace=True, drop=True)
        result.reset_index(inplace=True, drop=True)
    result['start_time'] = df['start_time']
    result['end_time'] = pd.to_datetime(result['start_time']) + datetime.timedelta(minutes=60 * hours)
    result = result.dropna()
    result.to_csv(path + 'grouped-luminosity-range-results.csv', index=False, header=False)


def group_by_hours_ground_humidity(path, input_file, minutes, time_behind_hours):
    df = pd.read_csv(path + input_file)
    period = minutes
    hours = time_behind_hours
    registers_before = (60 * hours) / period
    ticks = pd.DataFrame()
    ticks['ground_humidity'] = df['ground_humidity']
    result = pd.DataFrame()
    for x in range(0, ticks['ground_humidity'].size):
        result = result.append(ticks.head(registers_before + 1).transpose())
        ticks.drop(ticks.index[0], inplace=True)
        ticks.reset_index(inplace=True, drop=True)
        result.reset_index(inplace=True, drop=True)
    result['start_time'] = df['start_time']
    result['end_time'] = pd.to_datetime(result['start_time']) + datetime.timedelta(minutes=60 * hours)
    result = result.dropna()
    result.to_csv(path + 'grouped-ground-humidity-range-results.csv', index=False, header=False)


def group_by_hours_environment_humidity(path, input_file, minutes, time_behind_hours):
    df = pd.read_csv(path + input_file)
    period = minutes
    hours = time_behind_hours
    registers_before = (60 * hours) / period
    ticks = pd.DataFrame()
    ticks['environment_humidity'] = df['environment_humidity']
    result = pd.DataFrame()
    for x in range(0, ticks['environment_humidity'].size):
        result = result.append(ticks.head(registers_before + 1).transpose())
        ticks.drop(ticks.index[0], inplace=True)
        ticks.reset_index(inplace=True, drop=True)
        result.reset_index(inplace=True, drop=True)
    result['start_time'] = df['start_time']
    result['end_time'] = pd.to_datetime(result['start_time']) + datetime.timedelta(minutes=60 * hours)
    result = result.dropna()
    result.to_csv(path + 'grouped-environment-humidity-range-results.csv', index=False, header=False)
