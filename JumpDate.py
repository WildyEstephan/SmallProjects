# This program is to know the date given the number of months to implement,
# if it will be once or twice a month and start date
# It serve in case of loans, discounts and wage increases in payroll

import datetime


def _get_date(meses, date):
    dias = meses * 30.44
    Start = datetime.datetime.strptime(date[0] + '-' + date[1] + '-' + date[2], '%Y-%m-%d')
    fechaDias = Start + datetime.timedelta(days=dias)

    return str(fechaDias).split('-')


def _get_date_end(frecuency_number, apply_on, start_date, ):
    date = start_date.split('-')  # Convert the String of start_date to list
    final_date = date  # For init

    mesStr = ''  # For convert the new date to String

    # If apply_on have 1 or 2 plus to the month less 1, else div frecuency_number between 2 after plus
    if apply_on == 1 or apply_on == 2:
        mesInt = frecuency_number - 1
    else:
        mesInt = int((frecuency_number / 3) + int(date[1]) - 2)

    end_date = _get_date(mesInt, date)

    # Create date from start_date adding to mesStr as the month
    final_date = end_date[0] + '-' + end_date[1] + '-' + date[2]

    return final_date

print _get_date_end(8, 1, '2016-08-15', ) # The format date %Y-%m-%d