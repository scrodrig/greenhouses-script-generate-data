import datetime
import pandas as pd


def group_by_hours_temperature_error(path, input_file, minutes, time_behind_hours, training_percentage):
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

    ticks_2 = pd.DataFrame()
    result_1 = pd.DataFrame()
    ticks_2['error_temperature'] = df['error_temperature']

    for x in range(0, ticks_2['error_temperature'].size):
        result_1 = result_1.append(ticks_2.head(registers_before + 1).transpose())
        ticks_2.drop(ticks_2.index[0], inplace=True)
        ticks_2.reset_index(inplace=True, drop=True)
        result_1.reset_index(inplace=True, drop=True)

    # result = result.dropna()
    # result_1 = result_1.dropna()
    result.reset_index(inplace=True, drop=True)
    result_1.reset_index(inplace=True, drop=True)
    result_1.drop(result_1.columns[len(result_1.columns) - 1], axis=1, inplace=True)

    result = result.rename_axis(lambda x: 2 * x, axis=1)
    result_1 = result_1.rename_axis(lambda x: 2 * x + 1, axis=1)

    result_2 = pd.concat([result, result_1], axis=1)
    result_2 = result_2.sort_index(axis=1)

    # PRODUCE ERROR PORQYE SE ESTAN TOMANDO REGISTROS DE UNA SET QUE NO FUERON REMOVIDOS
    # LOS N/A DE LA COLECION QUE ES EL CASO DE DG START TIME
    result['start_time'] = df['start_time']

    result_2['hour'] = pd.to_datetime(result['start_time']).dt.hour + \
                       pd.to_datetime(result['start_time']).dt.minute / 60 + \
                       pd.to_datetime(result['start_time']).dt.second / 3600

    result_2['day_year'] = pd.to_datetime(result['start_time']).dt.dayofyear

    result_2.dropna(inplace=True)
    result_2.reset_index(drop=True, inplace=True)
    training = len(result_2.index) * training_percentage / 100
    test = len(result_2.index) - training
    training_data = result_2.head(training)
    result_2 = result_2.ix[training:]
    result_2.reset_index(drop=True, inplace=True)
    test_data = result_2.head(test)

    training_data.to_csv(path + 'grouped-no-gaps-temperature-range-results_training.csv', index=False, header=True)
    test_data.to_csv(path + 'grouped-no-gaps-temperature-range-results_test.csv', index=False, header=True)


def group_by_hours_environment_humidity_error(path, input_file, minutes, time_behind_hours, training_percentage):
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

    ticks_2 = pd.DataFrame()
    result_1 = pd.DataFrame()
    ticks_2['error_environment_humidity'] = df['error_environment_humidity']

    for x in range(0, ticks_2['error_environment_humidity'].size):
        result_1 = result_1.append(ticks_2.head(registers_before + 1).transpose())
        ticks_2.drop(ticks_2.index[0], inplace=True)
        ticks_2.reset_index(inplace=True, drop=True)
        result_1.reset_index(inplace=True, drop=True)

    # result = result.dropna()
    # result_1 = result_1.dropna()
    result.reset_index(inplace=True, drop=True)
    result_1.reset_index(inplace=True, drop=True)
    result_1.drop(result_1.columns[len(result_1.columns) - 1], axis=1, inplace=True)
    result = result.rename_axis(lambda x: 2 * x, axis=1)
    result_1 = result_1.rename_axis(lambda x: 2 * x + 1, axis=1)

    result_2 = pd.concat([result, result_1], axis=1)
    result_2 = result_2.sort_index(axis=1)
    result['start_time'] = df['start_time']

    result_2['hour'] = pd.to_datetime(result['start_time']).dt.hour + \
                       pd.to_datetime(result['start_time']).dt.minute / 60 + \
                       pd.to_datetime(result['start_time']).dt.second / 3600

    result_2['day_year'] = pd.to_datetime(result['start_time']).dt.dayofyear

    result_2.dropna(inplace=True)
    result_2.reset_index(drop=True, inplace=True)
    training = len(result_2.index) * training_percentage / 100
    test = len(result_2.index) - training
    training_data = result_2.head(training)
    result_2 = result_2.ix[training:]
    result_2.reset_index(drop=True, inplace=True)
    test_data = result_2.head(test)

    training_data.to_csv(path + 'grouped-no-gaps-environment-humidity-range-results_training.csv', index=False,
                         header=True)
    test_data.to_csv(path + 'grouped-no-gaps-environment-humidity-range-results_test.csv', index=False, header=True)


def group_by_hours_ground_humidity_error(path, input_file, minutes, time_behind_hours, training_percentage):
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

    ticks_2 = pd.DataFrame()
    result_1 = pd.DataFrame()
    ticks_2['error_ground_humidity'] = df['error_ground_humidity']

    for x in range(0, ticks_2['error_ground_humidity'].size):
        result_1 = result_1.append(ticks_2.head(registers_before + 1).transpose())
        ticks_2.drop(ticks_2.index[0], inplace=True)
        ticks_2.reset_index(inplace=True, drop=True)
        result_1.reset_index(inplace=True, drop=True)

    # result = result.dropna()
    # result_1 = result_1.dropna()
    result.reset_index(inplace=True, drop=True)
    result_1.reset_index(inplace=True, drop=True)
    result_1.drop(result_1.columns[len(result_1.columns) - 1], axis=1, inplace=True)

    result = result.rename_axis(lambda x: 2 * x, axis=1)
    result_1 = result_1.rename_axis(lambda x: 2 * x + 1, axis=1)

    result_2 = pd.concat([result, result_1], axis=1)
    result_2 = result_2.sort_index(axis=1)
    result['start_time'] = df['start_time']

    result_2['hour'] = pd.to_datetime(result['start_time']).dt.hour + \
                       pd.to_datetime(result['start_time']).dt.minute / 60 + \
                       pd.to_datetime(result['start_time']).dt.second / 3600

    result_2['day_year'] = pd.to_datetime(result['start_time']).dt.dayofyear

    result_2.dropna(inplace=True)
    result_2.reset_index(drop=True, inplace=True)
    training = len(result_2.index) * training_percentage / 100
    test = len(result_2.index) - training
    training_data = result_2.head(training)
    result_2 = result_2.ix[training:]
    result_2.reset_index(drop=True, inplace=True)
    test_data = result_2.head(test)

    training_data.to_csv(path + 'grouped-no-gaps-ground-humidity-range-results_training.csv', index=False,
                         header=True)
    test_data.to_csv(path + 'grouped-no-gaps-ground-humidity-range-results_test.csv', index=False,
                     header=True)


def group_by_hours_luminosity_error(path, input_file, minutes, time_behind_hours, training_percentage):
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

    ticks_2 = pd.DataFrame()
    result_1 = pd.DataFrame()
    ticks_2['error_luminosity'] = df['error_luminosity']
    ticks_2.fillna(value=0, inplace=True)
    for x in range(0, ticks_2['error_luminosity'].size):
        result_1 = result_1.append(ticks_2.head(registers_before + 1).transpose())
        ticks_2.drop(ticks_2.index[0], inplace=True)
        ticks_2.reset_index(inplace=True, drop=True)
        result_1.reset_index(inplace=True, drop=True)

    # result = result.dropna()
    # result_1 = result_1.dropna()
    result.reset_index(inplace=True, drop=True)
    result_1.reset_index(inplace=True, drop=True)
    result_1.drop(result_1.columns[len(result_1.columns) - 1], axis=1, inplace=True)
    result = result.rename_axis(lambda x: 2 * x, axis=1)
    result_1 = result_1.rename_axis(lambda x: 2 * x + 1, axis=1)

    result_2 = pd.concat([result, result_1], axis=1)
    result_2 = result_2.sort_index(axis=1)
    result['start_time'] = df['start_time']
    result_2['hour'] = pd.to_datetime(result['start_time']).dt.hour + \
                       pd.to_datetime(result['start_time']).dt.minute / 60 + \
                       pd.to_datetime(result['start_time']).dt.second / 3600

    result_2['day_year'] = pd.to_datetime(result['start_time']).dt.dayofyear

    result_2.dropna(inplace=True)
    result_2.reset_index(drop=True, inplace=True)
    training = len(result_2.index) * training_percentage / 100
    test = len(result_2.index) - training
    training_data = result_2.head(training)
    result_2 = result_2.ix[training:]
    result_2.reset_index(drop=True, inplace=True)
    test_data = result_2.head(test)

    training_data.to_csv(path + 'grouped-no-gaps-luminosity-range-results_training.csv', index=False,
                         header=True)
    test_data.to_csv(path + 'grouped-no-gaps-luminosity-range-results_test.csv', index=False,
                     header=True)


