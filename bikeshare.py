import sys
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

days = ['all', 'monday', 'tuesday', 'wednesday', 'thuesday', 'friday', 'saturday', 'sunday']


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
    city = input("Select the city :\n(chicago, new york city, washington): ").lower()
    if CITY_DATA.get(city) is None:
        print("invalid city input")
        sys.exit()
    else:
        pass
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Select the month :\n(all, january, february, ... , june)").lower()
    if month not in months:
        print("invalid month input")
        sys.exit()
    else:
        pass

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Select the day :\n(all, monday, tuesday, ... sunday)").lower()
    if day not in days:
        print("invalid day input")
        sys.exit()
    else:
        pass

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
    df['day_of_week'] = df['Start Time'].dt.day_name()

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

    df.info()
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The Most Common Month: ", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The Most Common Day: ", most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("The Most Common Hour: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    value_counts = df["Start Station"].value_counts()
    most_start_station = value_counts[value_counts == value_counts.max()]
    print("The most commonly used start station : ", most_start_station)

    # TO DO: display most commonly used end station
    value_counts1 = df["End Station"].value_counts()
    most_end_station = value_counts1[value_counts1 == value_counts1.max()]
    print("The most commonly used end station : ", most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is:")
    print("Start Station:", most_common_trip[0])
    print("End Station:", most_common_trip[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travrl_time = df["Trip Duration"].sum()
    print("total travel time : ", total_travrl_time)

    # TO DO: display mean travel time
    mean_travrl_time = df["Trip Duration"].mean()
    print("mean travel time : ", mean_travrl_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type:\n", user_types)
    
    if 'Gender' in df.columns:
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("Gender:\n", gender)
    else:
        print("Gender: Un-Available")
        
    if 'Birth Year' in df.columns:
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("Earliest birth year:\n", earliest_year)

        most_recent_year = df['Birth Year'].max()
        print("Most recent birth year:\n", most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print("Most Common birth year:\n", most_common_year)
    else:
        print("Birth Year: Un-Available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    start_loc = 0
    view_data = input('\nWould you like to view 5 rows of data? Enter yes or no.\n')
    if view_data.lower() != 'yes':
        pass
    else:
        while view_data.lower() == 'yes':
            value = df.iloc[start_loc:start_loc+5]
            print(value)
            start_loc += 5
            view_data = input('\nDo you wish to continue? Enter yes or no.\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
