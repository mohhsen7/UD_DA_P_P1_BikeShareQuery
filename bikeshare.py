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
    print('Data is available for the following cities Chicago, New York & Washington.')
    city = input('which city data would you like to explore? please enter the name of the city \n').lower()
    while city != 'chicago' and city != 'new york' and city != 'washington' :
        city = input('please enter the city name correctly \n').lower()
    if city == 'new york':
        city = 'new_york_ciy' #for file names
	#which filter
    print('would you like to filter your data by month, day or do you want it unfiltered?')
    choice = input('enter month to filter by month day to filter by day and none for unfiltered data \n').lower()
    while choice != 'month' and choice != 'day' and choice != 'none' :
        choice = input('please re enter the filter correctly \n').lower()
    if choice == 'month' :	
        # TO DO: get user input for month (all, january, february, ... , june)
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        print('Data is available for the following months.\n  january, february, march, april, may & june.')
        month = input('please enter the full name of the month you wold like to see data for. \n').lower()
        while month not in	months :
            month = input('please enter the full name of the month correctly. \n').lower()
        day = 'all'
    elif choice == 'day' :	
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        day = input('please enter the full name for the day of the week you wold like to see data for. \n').lower()
        while day not in days :
            day = input('please enter the full name of the day correctly. \n').lower()
        month = 'all'
    else :
        month = 'all'
        day = 'all'
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
    path = './'+ city +'.csv'
    df = pd.read_csv(path)
    f_month = {'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6}
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    ########################################################### DATA LOADED YET TO BE FILTERED
    if month != 'all':
        by_month = df['month']==f_month[month]
        ndf = df[by_month]
    elif day != 'all':
        by_day = df['day']== str(day).title()
        ndf = df[by_day]
    else:
        ndf =df
    return ndf


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    f_month = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june'}
    # TO DO: display the most common month
    if month != 'all':
        print('Displaying data for:', month)
    else:
        m_c_month = df['month'].mode()[0]
        print('Most common month:', f_month[m_c_month])
    # TO DO: display the most common day of week
    if day != 'all':
        print('Displaying data for:', day)
    else:
        m_c_day = df['day'].mode()[0]
        print('Most common day of week:', m_c_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    m_c_hour = df['hour'].mode()[0]
    if m_c_hour < 13 :
        m_c_hour_s = str(m_c_hour) + " am"
    else :
        m_c_hour -= 12
        m_c_hour_s = str(m_c_hour) + " pm"
    print('Most common start hour:', m_c_hour_s)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    st_station = df['Start Station'].mode()[0]
    print("most commonly used start station : \n", st_station)
    # TO DO: display most commonly used end station
    e_station = df['End Station'].mode()[0]
    print("most commonly used end station : \n", e_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + "$" + df['End Station']
    trip = df['trip'].mode()[0]
    print("most frequent combination of start station and end station trip : \n", str(trip).split('$'))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_s = df['Trip Duration'].sum() #in seconds
    total_time_m = int(total_time_s / 60)
    total_time_s %= 60
    print('total travel time = {} minuts and {} seconds'.format(total_time_m,int(total_time_s)))
    # TO DO: display mean travel time
    m_time = df['Trip Duration'].mean()
    print('mean travel time =', m_time, 'seconds')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Displaying counts of user types')
    print(user_types.to_string(header=False))
    if city == 'washington':
        print("washington doesn't have more detailed user data \n")
    # TO DO: Display counts of gender
    while city != 'washington':
        gender_types = df['Gender'].value_counts()
        print('Displaying counts of gender types')
        print(gender_types.to_string(header=False))
        # TO DO: Display earliest, most recent, and most common year of birth
        e_y = df['Birth Year'].min()
        print('earliest year of birth:', int(e_y))
        m_r_y = df['Birth Year'].max()
        print('most recent year of birth:', int(m_r_y))
        m_c_y = df['Birth Year'].mode()[0]
        print('most common year of birth:', int(m_c_y))
        break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_raw_data(df):
    '''views five raws of raw data repeatedly'''
    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no \n').lower()
    while view_data != 'yes' and view_data != 'no':
        view_data = input('Please Enter yes or no \n').lower()
    df.pop('month')
    df.pop('day')
    df.pop('hour')
    df.trip('trip')
    if view_data == 'yes':
        flag = True
    else :
        flag = False
    start_loc = 0
	tc_index = df.index
    length = len(tc_index)
    while flag:
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        if start_loc > length :
            start_loc = start_loc - length
        view_display = input('Do you wish to continue?: Yes or No \n').lower()
        if view_display != 'yes':
            flag = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        view_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
