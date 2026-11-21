import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
	cities = {'chicago', 'new york city', 'washington'}
	city = input("What city would you like to look into, chicago, new york city, washington?")
	while city not in cities:
		city = input("I did not recognize that, please try again. What city would you like to look into?")
    # TO DO: get user input for month (all, january, february, ... , june)
	months = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}
	month = input("What month interests you?")
	while month not in months:
		month = input("I did not recognize that, please try again. What month would you like to explore?)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
	days_week = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
	day = input("What day interests you?")
	while day not in days_week:
		day = input("I did not recognize that, please try again. What day would you like to explore?")
    print('-'*40)
    return city, month, day

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_Frequency = df['month'].value_counts(normalize=True)
        top_month = month_Frequency.index[0]        # most common month value
        m_freq_pct = month_Frequency.iloc[0] * 100   # as percentage
        months = ['january', 'february', 'march', 'april', 'may', 'june']  # only 6 entries shown
        if top_month in range(1, 7):
            month_name = months[top_month - 1]   # convert 1 -> 'january' and the like
    print(f"The most common month is {month_name}, accounting for {m_freq_pct}% of trips.")    
    # TO DO: display the most common day of week
day_Frequency = df['day'].value_counts(normalize=True)
		top_day = day_Frequency.index[0]     # most common month value
		d_freq_pct = day_Frequency.iloc[0] * 100   # as percentage
		days_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
		if top_day in range (1, 6):
			day_name = days_week[top_day]   # convert 1 -> 'monday' and the like
		print(f"{d_freq_pct}% of trips were taken on {day_name}.")
    # TO DO: display the most common start hour
hour_freq = df["hour"].value_counts(normalize=True)
    top_hour_val = hour_freq.index[0]            
    h_pct = hour_freq.iloc[0] * 100
	print(f"Most common start hour {top_hour_val}, with {h_pct}% of trips starting at this time.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
print("Most commonly used start station: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
print("Most commonly used end station: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"Most frequent trip combination: Start: {combo[0]}, End: {combo[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
total_time = df['Trip Duration'].sum()
    print(f"\nTotal travel time: {total_time} seconds")

    # TO DO: display mean travel time
mean_time = df['Trip Duration'].mean()
    print(f"\nMean travel time: {mean_time:.2f} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
print("\nCounts of user types:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
if 'Gender' in df.columns:
        print("\nCounts of gender:")
        print(df['Gender'].value_counts())
    else:
        print("\nGender data not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {most_recent_year}")
        print(f"Most common year of birth: {most_common_year}")
    else:
        print("\nBirth year data not available for this city.")


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
