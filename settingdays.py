import datetime
import itertools

# Функція
def raspisanie(date_start, date_end, days_work, days_skip):
    startDate = datetime.datetime.strptime(date_start, '%Y-%m-%d').date()
    endDate = datetime.datetime.strptime(date_end, '%Y-%m-%d').date()
    alldays = endDate - startDate

    data = []
    # Додаєм в список всі дні між вказаними датами
    for y in range(alldays.days + 1):
        calendarDate = startDate + datetime.timedelta(days=y)
        data.append(calendarDate.isoformat())



    newData = []

    while (len(data) > 0):

        for num in  range(days_work):
            if (len(data) > 0):

                item = data[:1:]
                newData.append(str(item[0]))
                data.pop(0)

        for num in  range(days_skip):
            if (len(data) > 0):
                data.pop(0)
    print(newData)

# Виклик функції
raspisanie("2022-04-20", "2022-04-23", 1, 1)
raspisanie("2022-04-25", "2022-06-26", 0, 4)
raspisanie("2022-05-14", "2022-05-24", 1, 95)