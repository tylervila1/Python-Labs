

current_population = 380123456
seconds_per_year = 60*24*7*4*12 #483840
print(seconds_per_year)
births = seconds_per_year / 6 * 3 #241920
deaths = seconds_per_year / 12 * 3 #120960
immigrants = seconds_per_year / 40 * 3 #36288
expected_growth = current_population + births - deaths + immigrants

print(expected_growth)