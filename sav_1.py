from datetime import datetime

def send_api_calls(timestamps: list):
    times = [datetime.strptime(timestamp, "%H:%M:%S") for timestamp in timestamps]
    return(times)


t = ['09:15:25','11:58:23','13:45:09','13:45:09','13:45:09','17:22:00','17:22:00']
print(send_api_calls(t))
