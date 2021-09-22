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
         city =str(input("please choose a city from chicago, new york city, washington: ")).lower()
         if city not in CITY_DATA:
             print("invalid city name,choose a correct one")
         else:
             break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month =str(input("input all or a month from a list of months below: ")).lower()
        months = [ 'january' , 'february' , 'march' , 'april' , 'may' , 'june']
        if month != 'all' and month not in months:
            print('invalid month , write a valid one')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day =str(input("input all or a day from days list below: ")).lower()
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if day != 'all' and day not in days:
            print('invalid input , enter correct day name')
        else:
            break
        
    print('-'*40)
    return city, month, day


#*******************************************************************************************


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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    
    # extract  day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.day_name()              #weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of the week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]     #first day capitalize

    return df


#*******************************************************************************************

def display_raw_data(df):
    
    r = 0
    reply = input("do you wanna display first five rows ? yes/no:  ").lower()
    
    pd.set_option('display.max_columns',None)
    
    while True:
        if reply == 'no' :
            break
        
        print(df[r:r+5])
        reply = input("do you wanna display next five rows ? yes/no:  ").lower()
        r = r + 5
    

#*******************************************************************************************


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    #df['Start Time']=pd.to_datetime(df['Start Time'])      #already used before
    #df['month']=df['Start Time'].dt.month                  #already used before
    common_month=df['month'].mode()[0]
    if common_month == 1 :
        print('Most common month:', 'january')
    elif common_month == 2 :
        print('Most common month:', 'february')
    elif common_month == 2 :
        print('Most common month:', 'march')
    elif common_month == 2 :
        print('Most common month:', 'april')
    elif common_month == 2 :
        print('Most common month:', 'may')
    else:
        print('Most common month:', 'june')
        


    # TO DO: display the most common day of week
    
    #df['Start Time']=pd.to_datetime(df['Start Time'])      #already used before
    df['day']=df['Start Time'].dt.day
    common_day=df['day'].mode()[0]
    print('Most common day:',common_day)


    # TO DO: display the most common start hour
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('Most common start hour:',common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#*******************************************************************************************


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('common used start station: ', common_start )
    

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('common used end station: ', common_end )


    # TO DO: display most frequent combination of start station and end station trip
    comb_start_end =(df['Start Station'] + "," +df['End Station']).mode()[0]
    print('most frequent comb between start and end stations: ' ,comb_start_end )
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#*******************************************************************************************


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    print('total_travel_time: ' , total_travel_time , 'seconds') 
    print('total_travel_time in hours: ' , total_travel_time/3600 , 'hours')   #hours = total_travel_time/3600


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean_travel_time: ' , mean_travel_time , 'seconds') 
    print('mean_travel_time in hours: ' , mean_travel_time/3600 , 'hours')    #hours = mean_travel_time/3600
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#*******************************************************************************************


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('user_types: ' , user_types)
    
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('counts of Gender: ' , gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birthYear=int(df['Birth Year']).min()
        print('earliest_birthYear: ',earliest_birthYear)
        
        recent_birthYear=int(df['Birth Year']).max()
        print('recent_birthYear: ',recent_birthYear)
        
        mostCommon_birthYear=int(df['Birth Year']).mode()[0]
        print('most_common_birth_Year: ',mostCommon_birthYear)
        
        #year_of_birth =df['Birth Year'].value_counts()
        #print('year_of_birth: ' , year_of_birth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#*******************************************************************************************


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


