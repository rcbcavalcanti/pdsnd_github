import datetime
import pandas as pd

# Creates dictionaries that are used over various functions
CITY_DATA = {1: ['Chicago', 'chicago.csv'],
             2: ['New York City', 'new_york_city.csv'],
             3: ['Washington, DC', 'washington.csv']}

MONTH_LIST = {0: 'All months', 1: 'January', 2: 'February', 3: 'March',
              4: 'April', 5: 'May', 6: 'June'}

DAY_LIST = {0: 'All days', 1: 'Mondays', 2: 'Tuesdays', 3: 'Wednesdays',
            4: 'Thursdays', 5: 'Fridays', 6: 'Saturdays', 7: 'Sundays'}

DATA_LIST = {0: 'Raw data', 1: 'Popular times of travel',
             2: 'Popular stations and trip', 3: 'Trip duration',
             4: 'User info'}


def select_city():
    """
    Asks user to specify a city.

    Returns:
        (int) city_number   => number of the city in the list
        (str) city_file     => CSV file name with the city data
        (str) selected_city => text to message to user, showing selected city
    """

    prompt_question_01 = "\n" \
                         " Would you like to see data for which city? \n" \
                         " Enter the corresponding city number: \n" \
                         "\n" \
                         "    Type '1' to: Chicago \n" \
                         "    Type '2' to: New York City \n" \
                         "    Type '3' to: Washington, DC \n \n"

    while True:
        try:
            # Asks user to input a city number
            city_number = int(input(prompt_question_01))

        # if the input is not an integer
        except (TypeError, ValueError):
            print('\n Please type a valid city number \n')

        # if the input is an integer...
        else:
            # ...checks if the number exists in the city list
            if CITY_DATA.get(city_number) != None:
                break  # if number exists, breaks the while loop
            print('\n \'{}\' is not a valid city number \n'.format(city_number))

    # Print the selected city to the user and returns the city data file name
    selected_city = "\n...[{} selected]...\n".format(CITY_DATA[city_number][0])
    city_file = CITY_DATA[city_number][1]
    print(selected_city)
    return city_number, city_file, selected_city


def select_date(skip_question_01=False):
    """
    Asks user to specify a month or a day of the week.

    Args:
        (boolean) skip_question_01 => if this function was called to change
                                      the filter, the first question is skipped

    Returns:
        (int) month_number         => number of month to filter by,
                                      or "0" to apply no month filter
        (str) selected_month       => text to message to user, showing
                                      selected month
        (int) day_number           => number of the day of week to filter by
                                      1=Monday through 7=Sunday
                                      or "0" to apply no day
        (str) selected_day         => text to message to user, showing selected
                                      day of the week
    """

    prompt_question_01 = "\n Would you like to filter the data by" \
                         " month or day? [y/n] \n \n"

    prompt_question_02 = "\n" \
                         " Would you like to filter data for which month? \n" \
                         " Enter the corresponding number: \n" \
                         "\n" \
                         "    Type '0' to: All (no filter) \n" \
                         "    Type '1' to: January \n" \
                         "    Type '2' to: February \n" \
                         "    Type '3' to: March \n" \
                         "    Type '4' to: April \n" \
                         "    Type '5' to: May \n" \
                         "    Type '6' to: June\n \n"

    prompt_question_03 = "\n" \
                         " Would you like to filter data by a day of the week? \n" \
                         " Enter the corresponding number: \n" \
                         "\n" \
                         "    Type '0' to: All (no filter) \n" \
                         "    Type '1' to: Mondays \n" \
                         "    Type '2' to: Tuesdays \n" \
                         "    Type '3' to: Wednesdays \n" \
                         "    Type '4' to: Thrusdays \n" \
                         "    Type '5' to: Fridays \n" \
                         "    Type '6' to: Saturdays \n" \
                         "    Type '7' to: Sundays \n \n"

    # checks if question 01 should be skipped
    if skip_question_01:
        filter_selected = True

    else:
        # Checks the user input:
        while True:
            # Asks if user wants to filter date
            filter_data = input(prompt_question_01).lower()

            if filter_data in ['n', 'no']:  # if the input is 'no', exits def
                # indicates that user did not choose to filter data
                filter_selected = False
                month_number = 0
                day_number = 0
                break

            # if the input is 'yes', continues def
            elif filter_data in ['y', 'yes']:
                filter_selected = True  # indicates that user chose to filter data
                break

            else:  # if the input was not a 'yes' or 'no' answer, warns user
                print("\n Please type 'y' if you want to filter the data by \n"
                      "month or day of the week or type 'n' to no "
                      "filter at all \n")

    # checks user input for the month filter
    # if user chose to filter data, proceed with while loop
    while filter_selected:
        try:
            # Asks user to input a month number
            month_number = int(input(prompt_question_02))

        # if the input is not an integer
        except (TypeError, ValueError):
            print('\n Please type a valid month number \n')

        # if the input is an integer...
        else:
            # ...checks if the number exists in the month list
            if MONTH_LIST.get(month_number) != None:
                break  # if number exists, breaks the while loop
            print('\n \'{}\' is not a valid month number \n' \
                  .format(month_number))

    # Print the selected month to the user and returns the month number
    selected_month = "\n...[{} selected]...\n".format(MONTH_LIST[month_number])
    if filter_selected:
        print(selected_month)

    # checks user input for the day of the week filter
    # if user chose to filter data, proceed with while loop
    while filter_selected:
        try:
            # Asks user to input a day number
            day_number = int(input(prompt_question_03))

        # if the input is not an integer
        except (TypeError, ValueError):
            print('\n Please type a valid day number \n')

        # if the input is an integer...
        else:
            # ...checks if the number exists in the days list
            if DAY_LIST.get(day_number) != None:
                break  # if number exists, breaks the while loop
            print('\n \'{}\' is not a valid day number \n'.format(day_number))

    # Print the selected day to the user and returns the day number
    selected_day = "\n...[{} selected]...\n".format(DAY_LIST[day_number])
    if filter_selected:
        print(selected_day)

    return month_number, selected_month, day_number, selected_day


def load_file(city_file, month_number, day_number):
    """
    Loads data for the specified city and filters by month and
    day if applicable.

    Args:
        (str) city_file    => CSV file name of the city to analyze
        (int) month_number => number of month to filter by,
                              or "0" to apply no month filter
        (int) day_number   => number of the day of week to filter by,
                              Monday=1 through Sunday=7 or "0" to apply
                              no day filter
    Returns:
        (DataFrame) df     => Pandas DataFrame containing city data filtered
                              by month and day
    """

    # loads file
    df = pd.read_csv(city_file)

    # converts date fields from string to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # adds month and day of the week coluns (based on start time)
    # Monday=0, Sunday=6
    df.insert(1, 'Day of the Week', df['Start Time'].dt.dayofweek)
    # Jan=1, Dec=12
    df.insert(1, 'Month', df['Start Time'].dt.month)

    # apply month filter
    if month_number != 0:  # checks if user selected '0' (no filter)
        df = df.loc[df['Month'] == (month_number)]

    # apply day filter
    if day_number != 0:  # checks if user selected '0' (no filter)
        df = df.loc[df['Day of the Week'] == (day_number - 1)]

    # Resets index row counter
    counter = df['Start Time'].count()
    df.index = range(0, counter)

    return df


def raw_data(df):
    """
    Exibits raw DataFrame data (5 rows at a time)

    Args:
        (DataFrame) df => city DataFrame with filters applied
    """

    start_row = 0
    rows_per_time = 5  # n rows to show at a time
    proceed = True

    while proceed:

        # Returns a n row table
        five_rows = df.loc[start_row:start_row + rows_per_time - 1]

        msg = '================================================== \n' \
              '    Showing raw data from row {} to {} \n' \
              '================================================== \n'

        msg = msg.format(start_row, start_row + rows_per_time - 1)

        # change option to show all table columns
        pd.set_option('display.max_columns', None)

        print(msg, '\n\n', five_rows)  # print the n rows

        while True:
            # Asks if user wants to show n more rows
            prompt_question = "\n Do you want to show {} more rows? [y/n]\n\n" \
                              .format(rows_per_time)

            show_more = input(prompt_question).lower()

            # if the input is 'no', exits def
            if show_more in ['n', 'no', 'cancel', 'exit', 'stop']:
                # indicates that user did not choose to continue
                proceed = False
                break

            # if the input is 'yes', continues def
            elif show_more in ['y', 'yes', '']:  
                proceed = True  # indicates that user chose to continue
                start_row += rows_per_time
                break

            else:  # if the input was not a 'yes' or 'no' answer, warns user
                print("\n Please type 'y' or hit ENTER if you want to show " \
                      "the next {} rows \n or type 'n' to stop. \n" \
                      .format(rows_per_time))


def time_stats(df, city_number, month_number, day_number):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (DataFrame) df     => city DataFrame with filters
        (int) city_number  => number of the city in the data
        (int) month_number => number of month filtered,
                              or "0" to all months
        (int) day_number   => number of the day of week filtered,
                              Monday=1 through Sunday=7 or "0" to all days
    """

    city_name = CITY_DATA[city_number][0]
    month_name = MONTH_LIST[month_number]
    day_name = DAY_LIST[day_number]

    msg_header = "\n | \n | Time stats for {}: [{}] [{}]\n |" \
                 .format(city_name, month_name, day_name)
    msg_dow = ''
    msg_month = ''

    # display the most common month
    if month_number == 0:  # if all months where selected
        popular_month = MONTH_LIST[df['Month'].mode()[0]]

        msg_month = "\n | >> Most popular month: " + popular_month

    # display the most common day of week
    if day_number == 0:  # if all days where selected
        popular_dow = DAY_LIST[df['Day of the Week'].mode()[0] + 1]

        msg_dow = "\n | >> Most popular day of the week: " + popular_dow

    # display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    if popular_hour > 12:
        popular_hour = str(popular_hour - 12) + ' pm'
    else:
        popular_hour = str(popular_hour) + ' am'

    msg_hour = "\n | >> Most popular hour: " + popular_hour

    print(msg_header, msg_month, msg_dow, msg_hour, '\n |\n')


def station_stats(df, city_number, month_number, day_number):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        (DataFrame) df     => city DataFrame with filters
        (int) city_number  => number of the city in the data
        (int) month_number => number of month filtered,
                              or "0" to all months
        (int) day_number   => number of the day of week filtered,
                              Monday=1 through Sunday=7 or "0" to all days
    """

    city_name = CITY_DATA[city_number][0]
    month_name = MONTH_LIST[month_number]
    day_name = DAY_LIST[day_number]

    msg_header = "\n | \n | Station stats for {}: [{}] [{}]\n |" \
                 .format(city_name, month_name, day_name)

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    msg_start_station = "\n | >> Most popular start station: " \
                        + popular_start_station

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    msg_end_station = "\n | >> Most popular end station: " \
                        + popular_end_station

    # display most frequent combination of start station and end station trip
    trips = df['Start Station'] + ' to ' + df['End Station']

    popular_trip = trips.mode()[0]

    msg_trip = "\n | >> Most popular trip: " + popular_trip

    print(msg_header, msg_start_station, msg_end_station, msg_trip, '\n |\n')


def trip_duration_stats(df, city_number, month_number, day_number):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (DataFrame) df     => city DataFrame with filters
        (int) city_number  => number of the city in the data
        (int) month_number => number of month filtered,
                              or "0" to all months
        (int) day_number   => number of the day of week filtered,
                              Monday=1 through Sunday=7 or "0" to all days
    """

    city_name = CITY_DATA[city_number][0]
    month_name = MONTH_LIST[month_number]
    day_name = DAY_LIST[day_number]

    msg_header = "\n | \n | Trip duration stats for {}: [{}] [{}]\n |" \
                 .format(city_name, month_name, day_name)

    # display total travel time
    travel_time = int(df['Trip Duration'].sum())

    msg_travel_time = "\n | >> Total travel time (days, h:mm:ss): " \
                      + str(datetime.timedelta(seconds=travel_time))

    # display mean travel time
    avg_time = int(df['Trip Duration'].mean())

    msg_avg_time = "\n | >> Average travel time (h:mm:ss): " \
                   + str(datetime.timedelta(seconds=avg_time))

    print(msg_header, msg_travel_time, msg_avg_time, '\n |\n')


def user_stats(df, city_number, month_number, day_number):
    """
    Displays statistics on bikeshare users.

    Args:
    (DataFrame) df     => city DataFrame with filters
    (int) city_number  => number of the city in the data
    (int) month_number => number of month filtered,
                          or "0" to all months
    (int) day_number   => number of the day of week filtered,
                          Monday=1 through Sunday=7 or "0" to all days
    """

    city_name = CITY_DATA[city_number][0]
    month_name = MONTH_LIST[month_number]
    day_name = DAY_LIST[day_number]

    msg_header = "\n | \n | Users stats for {}: [{}] [{}]\n |" \
                 .format(city_name, month_name, day_name)


    # Counts per user types
    count_per_user = pd.DataFrame(df['User Type'].value_counts())
    # Changes column name from 'User Type' to 'Count'
    count_per_user = count_per_user.rename(columns={'User Type': 'Count'})
    # includes a percent column
    count_per_user['Percent'] = df['User Type'].value_counts(normalize=True) \
                                * 100

    # register the message to user
    msg_count_user = "\n | >> Travels quantity per user type: \n\n"

    # 'try' checks if there is a 'Gender' column in the data file
    try:
        # Counts per user gender
        count_per_gender = pd.DataFrame(df['Gender'].value_counts())
        # Changes column name from 'User Type' to 'Count'
        count_per_gender = count_per_gender.rename(columns={'Gender':'Count'})
        # includes a percent column 
        count_per_gender['Percent'] = df['Gender'].value_counts(normalize=True) \
                                      * 100
        # return message to user
        msg_count_gender = ("\n" * 4) + " | >> Travels quantity per "\
                           "user gender: \n\n"

    except (KeyError):
        # If 'Gender' column does not exist, return message to user
        count_per_gender = ("\n" * 4) + " |\n | >> No gender data available in " \
                           + city_name + " data file\n"
        msg_count_gender = ''


    # 'try' checks if there is a 'Birth Year' column in the data file
    try:
        # identifies oldest year of birth
        earliest_year = df['Birth Year'].min()

        msg_earliest_year = ("\n" * 4) + " |\n | >> Year of birth of the " \
                             "oldest user: " + str(int(earliest_year))

        # identifies youngest year of birth
        recent_year = df['Birth Year'].max()

        msg_recent_year = ("\n" * 1) + " | >> Year of birth of the "\
                          "youngest user: " + str(int(recent_year))

        # identifies most common year of birth
        common_year = df['Birth Year'].mode()[0]

        msg_common_year = ("\n" * 1) + " | >> Most common year of birth: " \
                          + str(int(common_year))

    except (KeyError):
        # If 'Birth Year' column does not exist, return message to user
        msg_earliest_year = "|\n | >> No year of birth data available in " \
                            + city_name + " data file"
        msg_recent_year = ''
        msg_common_year = ''

    # prints all msg to user
    print(msg_header,
          msg_count_user,
          count_per_user,
          msg_count_gender,
          count_per_gender,
          msg_earliest_year,
          msg_recent_year,
          msg_common_year, '\n |\n')


def main():
    # call function to select CSV city file
    city_number, city_file, selected_city = select_city()

    # calls functio to select month and day filters
    month_number, selected_month, day_number, selected_day = select_date()

    city_name = CITY_DATA[city_number][0]
    month_name = MONTH_LIST[month_number]
    day_name = DAY_LIST[day_number]

    # returns to user city, month and day selection
    print('\n Loading file... \n' +
          selected_city + selected_month + selected_day)

    # calls functionn to load CSV city file with filters applied
    df = load_file(city_file, month_number, day_number)

    prompt_question_01 = "\n What data do you want to visualize? \n" \
                         "\n" \
                         "    Type '0' to: Raw data (table) \n" \
                         "    Type '1' to: Popular times of travel \n" \
                         "    Type '2' to: Popular stations and trip \n" \
                         "    Type '3' to: Trip duration \n" \
                         "    Type '4' to: User info \n \n"

    prompt_question_02 = "\n Would you like to: \n" \
                         "\n" \
                         "    Type '1' to: Visualize other data for [{0}] [{1}] [{2}] \n" \
                         "    Type '2' to: Change month or day filter for [{0}] \n" \
                         "    Type '3' to: Change city \n" \
                         "    Type '4' to: Terminate\n \n"

    keep_running = True

    # loop to check if user wants to keeping visualizing data
    while keep_running:

        # checks if user input is valid
        while True:  # if user chose to filter data, proceed with while loop
            try:
                # asks user what data to display (data selection menu)
                data_to_display = int(input(prompt_question_01))

            # if the input is not an integer
            except (TypeError, ValueError):
                print('\n Please choose a valid option \n')

            # if the input is an integer...
            else:
                # ...checks if the number exists in the data list
                if DATA_LIST.get(data_to_display) is not None:
                    break  # if number exists, breaks the while loop
                print('\n \'{}\' is not a valid option \n'
                      .format(data_to_display))

        # calls the function correspoding to data selected by user
        if data_to_display == 0:
            raw_data(df)
        elif data_to_display == 1:
            time_stats(df, city_number, month_number, day_number)
        elif data_to_display == 2:
            station_stats(df, city_number, month_number, day_number)
        elif data_to_display == 3:
            trip_duration_stats(df, city_number, month_number, day_number)
        elif data_to_display == 4:
            user_stats(df, city_number, month_number, day_number)

        # checks user input for how to proceed after seeing chosen data
        # if user chose to filter data, proceed with while loop
        while True:
            try:
                # Asks user to input a month number
                visualize_more = int(input(prompt_question_02 \
                                     .format(city_name, month_name, day_name)))

            # if the input is not an integer
            except (TypeError, ValueError):
                print('\n Please type a valid option \n')

            # if the input is an integer...
            else:
                # ...checks if the number exists in the option list
                if visualize_more in [1, 2, 3, 4]:
                    break  # if number exists, breaks the while loop
                print('\n \'{}\' is not a valid option \n' \
                      .format(visualize_more))

        # checks user answer
        if visualize_more == 1:  # Visualize other data for the current df
            keep_running = True

        elif visualize_more == 2:  # Change month or day filter
            # Calls function to update filters
            month_number, selected_month, day_number, selected_day = \
                select_date(skip_question_01=True)
            # Calls function to reload df
            df = load_file(city_file, month_number, day_number)

            # Updates month and day, accordingly to selected filters
            month_name = MONTH_LIST[month_number]
            day_name = DAY_LIST[day_number]

            # Exits if and go back to data selection menu
            keep_running = True

        elif visualize_more == 3:  # Change city
            # Calls function to update selected city and filters
            city_number, city_file, selected_city = select_city()
            month_number, selected_month, day_number, selected_day = \
                select_date()

            # Calls function to reload df
            df = load_file(city_file, month_number, day_number)

            # Updates city, month and day, accordingly to selected filters
            city_name = CITY_DATA[city_number][0]
            month_name = MONTH_LIST[month_number]
            day_name = DAY_LIST[day_number]

            # Exits if and go back to data selection menu
            keep_running = True

        elif visualize_more == 4: # Terminate
            # Exits if and terminates data selection while loop
            keep_running = False


if __name__ == "__main__":
    main()
