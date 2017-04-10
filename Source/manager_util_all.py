import pandas as pd


def group_by_hours_all(path):
    group_by_hours_temperature_all_parameters(path=path)
    group_by_hours_temperature_all_parameters_test(path=path)
    group_by_hours_environment_humidity_all_parameters(path=path)
    group_by_hours_environment_humidity_all_parameters_test(path=path)
    group_by_hours_ground_humidity_all_parameters(path=path)
    group_by_hours_ground_humidity_all_parameters_test(path=path)
    group_by_hours_luminosity_all_parameters(path=path)
    group_by_hours_luminosity_all_parameters_test(path=path)


def group_by_hours_temperature_all_parameters(path):
    df_temp = pd.read_csv(path + 'grouped-no-gaps-temperature-range-results_training.csv')
    df_eh = pd.read_csv(path + 'grouped-no-gaps-environment-humidity-range-results_training.csv')
    df_gh = pd.read_csv(path + 'grouped-no-gaps-ground-humidity-range-results_training.csv')
    df_lum = pd.read_csv(path + 'grouped-no-gaps-luminosity-range-results_training.csv')

    df_temp = df_temp.rename_axis(lambda x: 'temp - ' + x, axis=1)

    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh = df_eh.rename_axis(lambda x: 'eh - ' + x, axis=1)

    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh = df_gh.rename_axis(lambda x: 'gh - ' + x, axis=1)

    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum = df_lum.rename_axis(lambda x: 'lum - ' + x, axis=1)

    result_2 = pd.concat([df_eh, df_gh, df_lum, df_temp], axis=1)
    result_2.to_csv(path + 'temperature-parameter_training.csv', index=False, header=True)


def group_by_hours_temperature_all_parameters_test(path):
    df_temp = pd.read_csv(path + 'grouped-no-gaps-temperature-range-results_test.csv')
    df_eh = pd.read_csv(path + 'grouped-no-gaps-environment-humidity-range-results_test.csv')
    df_gh = pd.read_csv(path + 'grouped-no-gaps-ground-humidity-range-results_test.csv')
    df_lum = pd.read_csv(path + 'grouped-no-gaps-luminosity-range-results_test.csv')

    df_temp = df_temp.rename_axis(lambda x: 'temp - ' + x, axis=1)

    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh = df_eh.rename_axis(lambda x: 'eh - ' + x, axis=1)

    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh = df_gh.rename_axis(lambda x: 'gh - ' + x, axis=1)

    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum = df_lum.rename_axis(lambda x: 'lum - ' + x, axis=1)

    result_2 = pd.concat([df_eh, df_gh, df_lum, df_temp], axis=1)
    result_2.to_csv(path + 'temperature-parameter_test.csv', index=False, header=True)


def group_by_hours_environment_humidity_all_parameters(path):
    df_temp = pd.read_csv(path + 'grouped-no-gaps-temperature-range-results_training.csv')
    df_eh = pd.read_csv(path + 'grouped-no-gaps-environment-humidity-range-results_training.csv')
    df_gh = pd.read_csv(path + 'grouped-no-gaps-ground-humidity-range-results_training.csv')
    df_lum = pd.read_csv(path + 'grouped-no-gaps-luminosity-range-results_training.csv')

    df_eh = df_eh.rename_axis(lambda x: 'eh - ' + x, axis=1)

    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp = df_temp.rename_axis(lambda x: 'temp - ' + x, axis=1)

    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh = df_gh.rename_axis(lambda x: 'gh - ' + x, axis=1)

    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum = df_lum.rename_axis(lambda x: 'lum - ' + x, axis=1)

    result_2 = pd.concat([df_temp, df_gh, df_lum, df_eh], axis=1)
    result_2.to_csv(path + 'environment-humidity-parameter_training.csv', index=False, header=True)


def group_by_hours_environment_humidity_all_parameters_test(path):
    df_temp = pd.read_csv(path + 'grouped-no-gaps-temperature-range-results_test.csv')
    df_eh = pd.read_csv(path + 'grouped-no-gaps-environment-humidity-range-results_test.csv')
    df_gh = pd.read_csv(path + 'grouped-no-gaps-ground-humidity-range-results_test.csv')
    df_lum = pd.read_csv(path + 'grouped-no-gaps-luminosity-range-results_test.csv')

    df_eh = df_eh.rename_axis(lambda x: 'eh - ' + x, axis=1)

    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp = df_temp.rename_axis(lambda x: 'temp - ' + x, axis=1)

    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh = df_gh.rename_axis(lambda x: 'gh - ' + x, axis=1)

    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum = df_lum.rename_axis(lambda x: 'lum - ' + x, axis=1)

    result_2 = pd.concat([df_temp, df_gh, df_lum, df_eh], axis=1)
    result_2.to_csv(path + 'environment-humidity-parameter_test.csv', index=False, header=True)


def group_by_hours_ground_humidity_all_parameters(path):
    df_temp = pd.read_csv(path + 'grouped-no-gaps-temperature-range-results_training.csv')
    df_eh = pd.read_csv(path + 'grouped-no-gaps-environment-humidity-range-results_training.csv')
    df_gh = pd.read_csv(path + 'grouped-no-gaps-ground-humidity-range-results_training.csv')
    df_lum = pd.read_csv(path + 'grouped-no-gaps-luminosity-range-results_training.csv')

    df_gh = df_gh.rename_axis(lambda x: 'gh - ' + x, axis=1)

    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp = df_temp.rename_axis(lambda x: 'temp - ' + x, axis=1)

    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh = df_eh.rename_axis(lambda x: 'eh - ' + x, axis=1)

    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum = df_lum.rename_axis(lambda x: 'lum - ' + x, axis=1)

    result_2 = pd.concat([df_temp, df_eh, df_lum, df_gh], axis=1)
    result_2.to_csv(path + 'ground-humidity-parameter_training.csv', index=False, header=True)


def group_by_hours_ground_humidity_all_parameters_test(path):
    df_temp = pd.read_csv(path + 'grouped-no-gaps-temperature-range-results_test.csv')
    df_eh = pd.read_csv(path + 'grouped-no-gaps-environment-humidity-range-results_test.csv')
    df_gh = pd.read_csv(path + 'grouped-no-gaps-ground-humidity-range-results_test.csv')
    df_lum = pd.read_csv(path + 'grouped-no-gaps-luminosity-range-results_test.csv')

    df_gh = df_gh.rename_axis(lambda x: 'gh - ' + x, axis=1)

    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp = df_temp.rename_axis(lambda x: 'temp - ' + x, axis=1)

    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh = df_eh.rename_axis(lambda x: 'eh - ' + x, axis=1)

    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum.drop(df_lum.columns[len(df_lum.columns) - 1], axis=1, inplace=True)
    df_lum = df_lum.rename_axis(lambda x: 'lum - ' + x, axis=1)

    result_2 = pd.concat([df_temp, df_eh, df_lum, df_gh], axis=1)
    result_2.to_csv(path + 'ground-humidity-parameter_test.csv', index=False, header=True)


def group_by_hours_luminosity_all_parameters(path):
    df_temp = pd.read_csv(path + 'grouped-no-gaps-temperature-range-results_training.csv')
    df_eh = pd.read_csv(path + 'grouped-no-gaps-environment-humidity-range-results_training.csv')
    df_gh = pd.read_csv(path + 'grouped-no-gaps-ground-humidity-range-results_training.csv')
    df_lum = pd.read_csv(path + 'grouped-no-gaps-luminosity-range-results_training.csv')

    df_lum = df_lum.rename_axis(lambda x: 'lum - ' + x, axis=1)

    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp = df_temp.rename_axis(lambda x: 'temp - ' + x, axis=1)

    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh = df_eh.rename_axis(lambda x: 'eh - ' + x, axis=1)

    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh = df_gh.rename_axis(lambda x: 'gh - ' + x, axis=1)

    result_2 = pd.concat([df_temp, df_eh, df_gh, df_lum], axis=1)
    result_2.to_csv(path + 'luminosity-parameter_training.csv', index=False, header=True)


def group_by_hours_luminosity_all_parameters_test(path):
    df_temp = pd.read_csv(path + 'grouped-no-gaps-temperature-range-results_test.csv')
    df_eh = pd.read_csv(path + 'grouped-no-gaps-environment-humidity-range-results_test.csv')
    df_gh = pd.read_csv(path + 'grouped-no-gaps-ground-humidity-range-results_test.csv')
    df_lum = pd.read_csv(path + 'grouped-no-gaps-luminosity-range-results_test.csv')

    df_lum = df_lum.rename_axis(lambda x: 'lum - ' + x, axis=1)

    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp.drop(df_temp.columns[len(df_temp.columns) - 1], axis=1, inplace=True)
    df_temp = df_temp.rename_axis(lambda x: 'temp - ' + x, axis=1)

    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh.drop(df_eh.columns[len(df_eh.columns) - 1], axis=1, inplace=True)
    df_eh = df_eh.rename_axis(lambda x: 'eh - ' + x, axis=1)

    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh.drop(df_gh.columns[len(df_gh.columns) - 1], axis=1, inplace=True)
    df_gh = df_gh.rename_axis(lambda x: 'gh - ' + x, axis=1)

    result_2 = pd.concat([df_temp, df_eh, df_gh, df_lum], axis=1)
    result_2.to_csv(path + 'luminosity-parameter_test.csv', index=False, header=True)
