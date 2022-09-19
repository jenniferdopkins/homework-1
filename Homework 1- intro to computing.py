#1.
nums = list(range(30, 65, 5))
print(nums)
nums.reverse()
print(nums)
nums.insert (0, 65)
print(nums)



#2
sample_list2 = []
x = list(range(21))
sample_list2.extend(x)
print(sample_list2)

sample_list2.remove(0)
print(sample_list2)

print(len(sample_list2))
print(max(sample_list2))
print(min(sample_list2))
print(sum(sample_list2))



#3

weather = {'Sunny': 'play', 'Rainy': 'watch TV', 'Cloudy': 'walk'}

for weather_forecast, activity in weather.items():
    print(f'When {weather_forecast} let us {activity}')

weather['snowy']='ski'
print(weather)



