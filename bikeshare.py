import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city name:").lower()
    while city not in CITY_DATA.keys():
        city = input("Please enter valid city name").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter month").lower()
    valid_month = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in valid_month:
        month = input("Please enter valid month").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of week").lower()
    valid_day_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in valid_day_week:
        day = input("Please enter valid day of week").lower()

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  # acquire month value
        df = df[df['month'] == month]   # filter dataframe by values of column using boolean expression

    if day != 'all':
        df = df[df['day_of_week'] == day.title()] # as above

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['start_hour'] = df['Start Time'].dt.hour
    most_common_month_number = df['month'].mode() # find the most common month number
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = months[most_common_month_number[0] - 1]
    print('The most common month: {}'.format(most_common_month))


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    most_common_start_hour = df['start_hour'].mode()[0]
    print('The most common start hour: {}'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station: {}'.format(most_commonly_start_station))

    # TO DO: display most commonly used end station
    most_commonly_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: {}'.format(most_commonly_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    """combine columns of start station and end station"""

    df['station_combination_trip'] = df['Start Station'].astype(str).apply(lambda s: s + ' - ') + df['End Station'].astype(str)

    most_frequent_trip = df['station_combination_trip'].mode()[0]
    print('The most frequent combination of start station and end station trip: {}'.format(most_frequent_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].iloc[:].sum(axis=0)
    print('The total travel time: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].iloc[:].mean()
    print('The mean travel time: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The counts of user types:\n{}'.format(user_type))
    # TO DO: Display counts of gender
    """There are no columns of 'Gender' and 'Birth Year' in washington.csv,
    therefore use an conditional statement as followed"""

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('The counts of gender:\n{}'.format(gender))
    else:
        print('Column \'Gender\' doesn\'t exist.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth = df['Birth Year'].min()
        print('The earliest year of birth: {}'.format(earliest_birth))
        most_recent_birth = df['Birth Year'].max()
        print('The most recent year of birth: {}'.format(most_recent_birth))
        most_common_birth = df['Birth Year'].mode().iloc[0]
        print('The most common year of birth: {}'.format(most_common_birth))
    else:
        print('Column \'Birth Year\' doesn\'t exist.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
