def add_time(start, duration, day=False):
    from datetime import datetime as dt
    import datetime

    # DATA MANIPULATION
    st_time = start[-2:]
    st = start[:-3]
    st_h = st.split(':')

    h,m = int(st_h[0]),int(st_h[1])

    dur = duration.split(':')
    h_dur,m_dur = int(dur[0]),int(dur[1])
  
    # DATE TIME MODULE
    if type(day)==str:
        
        day_1= day.lower()

        if h<9:
            start = '0'+start
        s_1 = dt.strptime(start, '%I:%M %p')
        s_2 = datetime.timedelta(hours= h_dur,minutes= m_dur)
        s_3 = s_1 + s_2

        s_time = s_3.strftime('%-I:%M %p')
        
        day_num_1 = s_1.strftime('%-d')
        day_num_3 = s_3.strftime('%-d')

        count_day = int(day_num_3)-int(day_num_1)
      
        day_week_inx = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
                        "friday": 4, "saturday": 5, "sunday": 6}
        day_week_arr = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                        "Saturday", "Sunday"]
      
        ind = int((day_week_inx[day_1])+ count_day)%7
        s_day = day_week_arr[ind]

        if count_day ==0:
            obs=''
        elif count_day ==1:
            obs = ' (next day)'
        else:
            obs= f' ({count_day} days later)'
        new_time = s_time+', '+s_day+obs

    else:
        if h<9:
            start = '0'+start
        s_1 = dt.strptime(start,'%I:%M %p')
        s_2 = datetime.timedelta(hours= h_dur,minutes= m_dur)
        s_3 = s_1 + s_2

        s_time = s_3.strftime('%-I:%M %p')
      
        day_num_1 = s_1.strftime('%-d')
        day_num_3 = s_3.strftime('%-d')
        
        count_day = int(day_num_3)-int(day_num_1)

        if count_day ==0:
            obs=''
        elif count_day ==1:
            obs = ' (next day)'
        else:
            obs= f' ({count_day} days later)'
        new_time = s_time+obs

    return new_time