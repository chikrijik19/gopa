def time_seconds(num) -> list:
    hours = time_seconds // 3600
    minutes = time_seconds - int(hours) // 60
    seconds = time_seconds - int(hours) - int(minutes)
    print(hours, ':', minutes, ':', seconds)



time_seconds(3666)
time_seconds(120)
time_seconds(300)