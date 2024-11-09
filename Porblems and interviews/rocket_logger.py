def calculate_rocket_milage():
    n = int(input())
    rockets_log = []
    for _ in range(n):
        day, hour, minute, rocket_id, status = input().split(' ')
        rockets_log.append({
            'day': int(day),
            'hour': int(hour),
            'minute': int(minute),
            'id': int(rocket_id),
            'status': status,
        })
    rockets_log = sorted(rockets_log, key=lambda x: (
        x['id'], x['day'], x['hour'], x['minute']))
    local_id = 0
    res: list = []
    time_stamp = 0
    for action in rockets_log:
        if local_id == 0:
            local_id: int = action['id']
            time_traveled: int = 0
        if local_id != action['id']:
            local_id = action['id']
            res.append(time_traveled)
            time_traveled = 0

        match (action['status']):
            case 'B':
                time_traveled += ((action['day']*24*60) +
                                  (action['hour'] * 60) + action['minute']) - time_stamp
            case 'S':
                time_traveled += ((action['day']*24*60) +
                                  (action['hour'] * 60) + action['minute']) - time_stamp

            case 'C':
                time_traveled += ((action['day']*24*60) +
                                  (action['hour'] * 60) + action['minute']) - time_stamp
                time_stamp = 0
        time_stamp = int((action['day']*24*60) +
                         (action['hour'] * 60) + action['minute'])
    res.append(time_traveled)
    return ' '.join([str(x) for x in res])


print(calculate_rocket_milage())
