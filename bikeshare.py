import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all','january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
    
    CITY = ''
    while CITY.lower() not in CITY_DATA:
        CITY = input("\n Enter the name of the city to analyze data?\n (E.g. chicago or new york city or washington)\n Your input is not case sensitive (chicago/CHICAGO/Chicago)\n ")
        if CITY.lower() in CITY_DATA:
            city = CITY_DATA[CITY.lower()]
        else:
            print("Please check your input and enter either chicago, new york city or washington.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    
    MONTH = ''
    while MONTH.lower() not in MONTH_DATA:
        MONTH = input("\n Enter the month, between january to june for which you want to analyze the data \n Your input should be complete month name and is not case sensitive\n You can enter in any format june/June/JUNE\n If you want to analyze all the months just enter all/ALL/All\n")
        if MONTH.lower() in MONTH_DATA:
            month = MONTH.lower()
        else:
            print(" Please input the month name in full or just enter all \n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    DAY = ''
    while DAY.lower() not in DAY_DATA:
        DAY = input("\n Enter the day of the week, between Monday to Sunday for which you want to analyze the data \n Your input should be complete day name and is not case sensitive\n You can enter in any format Sunday/SUNDAY/sunday\n If you want to analyze all the days just enter all/ALL/All\n")
        if DAY.lower() in DAY_DATA:
            day = DAY.lower()
        else:
            print("Please input the day name in full or just enter all.\n")

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
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    print("The most common month is: " + MONTH_DATA[common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is: " + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print(f"The total travel time is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean())
    mins, sec = divmod(mean_travel_time, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe mean travel time is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe mean travel time is {mins} minutes and {sec} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
        
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("\nThe count of user gender is: \n" + str(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\nEarliest birth year is: {}\n'.format(earliest_birth_year))
        print('Most recent birth year is: {}\n'.format(most_recent_birth_year))
        print('Most common birth year is: {}\n'.format(most_common_birth_year) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """This is to display raw data.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_data.lower() != 'yes':
                break
            display_raw_data(df)
            break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
    main()
