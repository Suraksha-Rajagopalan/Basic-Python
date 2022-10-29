import re
import os
import datetime
import timeit


my_pattern = r'N\w{3}\-\d{5}'

def search_pattern(pattern):
   count = 0
   for root, dirs, files in os.walk("F:\Personal Files\Project+Day+9", topdown=False):
      for name in files:
         path = os.path.join(root, name)
         if '.txt' in path:
            file = open(path, 'r')
            data = file.read()
            check_pattern = re.search(my_pattern, data)
            if check_pattern:
               count +=1
               print(name, check_pattern.group())
   print('Number of times:', count)


print(datetime.date.today())
search_pattern(my_pattern)
print(f'Duration of time is {timeit(search_pattern(my_pattern))}')
