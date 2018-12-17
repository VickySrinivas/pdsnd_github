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
    print("Hello! Let's explore some US bikeshare data!")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('\nEnter the name of the city:\n').lower()
    while not (city=='chicago' or city=='new york city' or city=='washington'):
        city=input('\nEnter the name of one of the cities \'chicago\',\'new york city\',\'washington\':\n').lower()


    pd.read_csv(CITY_DATA[city])

    # TO DO: get user input for month (all, january, february,march, april,may, june)
    month=input('\nEnter the name of the month or enter "all" if no filter is required:\n').lower()
    while not (month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june' or month=='all'):
        month=input('\nEnter the name of the month or enter "all" if no filter is required:\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('\nEnter the day or enter "all" if no filter is required:\n').lower()
    while not (day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday' or day=='all'):
        day=input('\nEnter the day or enter "all" if no filter is required:\n').lower()

    print('-'*35)
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name

    if month !='all':
        months=['january','february','march','april','may','june']
        month=[months.index(month)+1]
        df=df[df['month']==month]

    if day !='all':
        df=df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*35)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print("The most commonly used start station is: "+start_station)

    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print("The most commonly used end station is: "+end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_route = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is: {} to {}".format(popular_route[0], popular_route[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*35)


def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = str(df['Trip Duration'].sum())
    print("Total travel time is: " +total_time)

    # TO DO: display mean travel time
    mean_time=str(df['Trip Duration'].mean())
    print('Mean travel time is: '+mean_time)

    # TO DO: Display counts of user types
    user_types=str(df['User Type'].value_counts())
    print("The count of user types are: \n " + user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*35)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of gender
    print("The counts of gender are: "+str(df['Gender'].value_counts()))
    common_year = str(df['Birth Year'].mode()[0])
    min_year = str(df['Birth Year'].min())
    max_year = str(df['Birth Year'].max())
    # TO DO: Display earliest, most recent, and most common year of birth
    print("The earliest year of birth is: "+ min_year)
    print("The most recent year of birth is: "+ max_year)
    print("The most common year of birth is: "+ common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*35)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city=='chicago' or city=='new york city':
            user_stats(df)

        rawdata = input('\nWould you like to see the raw data? Enter yes or no.\n')
        while rawdata.lower() != 'no':
            print(df.head())
            rawdata = input('\nWould you like to see the raw data? Enter yes or no.\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
