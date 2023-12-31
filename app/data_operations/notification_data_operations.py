import pandas as pd
from datetime import timedelta
from utils.type_conversion import convert_date
import calendar

def filter_notifications(notifications, start_date=None, end_date=None, states=None):
    filtered_notifications = []
    
    if start_date:
        start_date = convert_date(start_date)
    if end_date:
        end_date = convert_date(end_date)
        last_day = calendar.monthrange(end_date.year, end_date.month)[1]
        end_date = end_date.replace(day=last_day)
    
    for notification in notifications:
        send_date = notification.send_date  
        state = notification.state  
        
        if (start_date and send_date <= start_date) or (end_date and send_date >= end_date):
            continue
        if states and state not in states:
            continue
        
        filtered_notifications.append(notification)
    
    return filtered_notifications


def group_notifications_by_type_and_date(notifications, granularity='monthly'):
    # Expected return types
    return_types = ["positiva", "negativa", "notificando"]
    grouped_data = {}
    totals_by_date = {}

    for notification in notifications:
        
        send_date = notification.send_date  
        # Adjusting the date to include only year and month
        if granularity == 'monthly':
            send_date = send_date.strftime('%Y-%m')

        return_type = notification.return_type  
        
        key = (send_date, return_type)

        if key not in grouped_data:
            grouped_data[key] = 0
        grouped_data[key] += 1

        # Accumulating totals by date
        if send_date not in totals_by_date:
            totals_by_date[send_date] = 0
        totals_by_date[send_date] += 1

    # Converting the grouped dictionary into a DataFrame
    df_grouped = pd.DataFrame(list(grouped_data.items()), columns=['SendDate_Type', 'Count'])
    df_grouped[['SendDate', 'ReturnType']] = pd.DataFrame(df_grouped['SendDate_Type'].tolist(), index=df_grouped.index)
    df_grouped.drop(columns=['SendDate_Type'], inplace=True)

    # Restructuring the DataFrame
    df_grouped = df_grouped.pivot_table(index='SendDate', columns='ReturnType', values='Count', fill_value=0)

    # Ensuring all return types and totals are present
    for return_type in return_types:
        if return_type not in df_grouped.columns:
            df_grouped[return_type] = 0
    df_grouped['todas'] = df_grouped.sum(axis=1)

    # Including totals by send date
    for date, total in totals_by_date.items():
        df_grouped.at[date, 'todas'] = total

    return df_grouped


def group_notifications_by_state(notifications):
    state_grouping = {}
    
    for notification in notifications:
        state = notification.state 
        return_type = notification.return_type 
        
        if state not in state_grouping:
            state_grouping[state] = {'todas': 0, 'positiva': 0, 'negativa': 0, 'notificando': 0}
        
        state_grouping[state]['todas'] += 1
        if return_type == 'positiva':
            state_grouping[state]['positiva'] += 1
        elif return_type == 'negativa':
            state_grouping[state]['negativa'] += 1
        elif return_type == 'notificando':
            state_grouping[state]['notificando'] += 1
    
    return state_grouping
