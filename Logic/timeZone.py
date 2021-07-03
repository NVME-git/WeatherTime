def timeZone(UserTimeZone):
    try:
        # Convert UserTimeZone from minutes to hours as integer
        UserTimeZone = int(UserTimeZone)/60
    except:
        raise Exception('Invalid UserTimeZone')

    if UserTimeZone not in range(-11,14+1): 
        raise Exception('Invalid UserTimeZone')
    
    return UserTimeZone
