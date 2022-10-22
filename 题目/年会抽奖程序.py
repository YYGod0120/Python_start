import random
import time
#员工列表
employee = []
employee_remove = []
for i in range(1,301):
    employee.append(i)
#第一次抽奖名单
third = random.sample(employee,30)
print('三等奖名单:')
for n3 in third:
    employee_remove.append(n3)
    print(f'中三等奖的员工号是{n3}')
print('接下来是二等奖名单')
time.sleep(10)
# 删除中奖名单
for r3 in employee_remove:
    employee.remove(r3)

#重复操作
second = random.sample(employee,6)
employee_remove = []
for n2 in second:
    employee_remove.append(n2)
    print(f'中二等奖的员工号是{n2}')
for r2 in employee_remove:
    employee.remove(r2)
time.sleep(3)
first = random.sample(employee,3)
employee_remove = []
print('接下来一等奖名单')
for n1 in first:
    employee_remove.append(n1)
    print(f'中一等奖的员工号是{n1}')
for r1 in employee_remove:
    employee.remove(r1)




