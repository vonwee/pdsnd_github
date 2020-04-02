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
    while True:
        city = input("\n>>>There is data for Chicago, New York City and Washington. Which city are you interested in?\n").lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("That is not a valid city name, please try again")
            continue
        else:
            break
        


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("\n>>> Which month are you interested in? January, February, March, April, May, June or all?\n").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("That is not a valid month, please try again")
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\n>>> Which day of the week are you interested in? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n").lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all'):
            print("That is not a valid day of the week, please try again")
            continue
        else:
            break


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
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]

    print('Most Common Day:', common_day)


    # TO DO: display the most common start hour
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (round(time.time() - start_time, 3)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Common Start Station:', start_station)


    # TO DO: display most commonly used end station

    end_station = df['End Station'].value_counts().idxmax()
    print('Most Common End Station:', end_station)
    
    # TO DO: display most frequent combination of start station and end station trip

    start_end = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most Frequent Start and End Station Combination:', start_end)
    
        
    print("\nThis took %s seconds." % (round(time.time() - start_time, 3)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = sum(df['Trip Duration'])
    print('Total Travel Time:', total_travel_time)


    # TO DO: display mean travel time

    mean_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_time)


    print("\nThis took %s seconds." % (round(time.time() - start_time, 3)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('Counts of User Type:', user_types)


    # TO DO: Display counts of gender

    try:
      gender = df['Gender'].value_counts()
      print('Counts of Gender:', gender)
    except KeyError:
      print("Gender Types:No data available for Washington.")

    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
      earliest_year = df['Birth Year'].min()
      print('Earliest Year:', earliest_year)
    except KeyError:
      print("Birth Year:No data available for Washington.")
              
    try:
      recent_year = df['Birth Year'].max()
      print('Recent Year:', recent_year)
    except KeyError:
      print("Birth Year:No data available for Washington.")
    
    try:
      common_year = df['Birth Year'].mode()[0]
      print('Common Year:', common_year)
    except KeyError:
      print("Birth Year:No data available for Washington.")


    print("\nThis took %s seconds." % (round(time.time() - start_time, 3)))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_input = input('\nWould you like see a raw data sample? Enter yes or no.\n').lower()
        i = 5
        while raw_input == 'yes':
            print(df.head(i))
            raw_input2 = input('\nWould you like see more raw data samples? Enter yes or no.\n').lower
            i += 5
            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
