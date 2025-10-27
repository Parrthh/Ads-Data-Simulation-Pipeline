# Creates fake but realistic data (e.g. country codes, names, addresses)
from faker import Faker
import pandas as pd
import random
import time
import os
# Generates unique IDs for each ad event
import uuid
# Used to create timestamps so each event has a realistic time of occurrence.
from datetime import datetime

#Intialize Faker instance
fake = Faker()

# Define ad event generator
def generate_event():
    event_types = ['impression', 'click', 'conversion']
    return {
        # Generates a unique ID for each event
        'event_id': str(uuid.uuid4()),
        # Each campaign can have multiple events, so we need to specify the type of event.
        'event_type': random.choice(event_types),
        # Captures the current time when the event was created.
        'timestamp': fake.date_time_this_year(),
        # Creates a fake user IDs
        'campaign_id': fake.random_int(min=1000, max=9999),
        # Simulates multiple ad campaigns
        'ad_id': fake.random_int(min=1000, max=9999),
        # Captures the current time when the event was created in readable ISO format
        'user_id': str(uuid.uuid4()),
        # To get country code
        'country': fake.country_code(),
        # To add device context, which is common in ad analytics.
        'device': fake.random_element(elements=('mobile', 'desktop', 'tablet')),
        # Assigns random ad cost between 10 cents and $2, rounded to 2 decimal places.
        'cost': round(random.uniform(0.1, 2.0), 2),
    }

# Generate and save dataset
# Here, n is the default value if we don't provide a specifc number of events to generate.
def generate_data(n=1000):
    data = [generate_event() for _ in range(n)]
    df = pd.DataFrame(data)
    
    # Ensure the directory exists
    os.makedirs('data/raw', exist_ok=True)
    
    # Save the data
    output_path = 'data/raw/ads_events.csv'
    df.to_csv(output_path, index=False)
    print(f'Generated {n} ad events and saved to {output_path}')

if __name__ == '__main__':
    generate_data(10000)


