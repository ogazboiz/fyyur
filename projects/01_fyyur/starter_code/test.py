
# nums = [1, 3, 6]

# def square(num):
#     return num * num





# if __name__ == "__main__":
#     squared_nums = list(map(square, nums))
#     print(squared_nums)

start_time = "2022-08-05 12:25:31"
start_time_split = start_time.split()
year, month, day = start_time_split[0].split("-")
hours, minutes, seconds = start_time_split[1].split(":")
from datetime import datetime as me


start_time_obj = me(
     year = int(year),
     month=int(month),
     day=int(day),
     hour=int(hours),
     minute=int(minutes),
     second=int(seconds)
     )

print(type(start_time_obj))
print("start_time_obj: ", start_time_obj)