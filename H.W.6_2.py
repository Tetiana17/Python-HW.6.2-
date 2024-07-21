seconds = int(input("Введи секунди: "))
print(seconds)
if 0 <= seconds < 8640000:
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    # додаємо 0 до результату
    result_hours = str(hours).zfill(2)
    result_minutes = str(minutes).zfill(2)
    result_seconds = str(seconds).zfill(2)
    # виводио результати з умовою про дні
    if days % 10 == 1 and days % 100 != 11:
        print(f"{days} день {result_hours}:{result_minutes}:{result_seconds}")
    elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
        print(f"{days} дні {result_hours}:{result_minutes}:{result_seconds}")
    else:
        print(f"{days} днів {result_hours}:{result_minutes}:{result_seconds}")
else:
    print("секунди мають бути > або = і <8640000")
