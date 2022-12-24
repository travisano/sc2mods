import random
import os
out = []
pointer = 0
ind = []
path = r'C:\Users\theory\'
hotkeys = list(range(8))
random.shuffle(hotkeys)
ctrl = 'ControlGroupAssign{}=Control+{}'
select = 'ControlGroupRecall{}={}'
print(hotkeys)
for i in range(8):
    ctrl_suffix = ',Control+ForwardMouseButton' if not hotkeys[i] else ''
    select_suffix = ',ForwardMouseButton' if not hotkeys[i] else ''
    out.append(ctrl.format(i, str(hotkeys[i]) + ctrl_suffix + '\n'))
    out.append(select.format(i, str(hotkeys[i]) + select_suffix + '\n'))
with open(path, 'rt') as file:
    data = file.readlines()
for i, line in enumerate(data):
    if 'ControlGroupAssign' in line or 'ControlGroupRecall' in line:
        ind.append(i)
    if '[Hotkeys]' in line:
        pointer = i
for i in ind[::-1]:
    data.pop(i)
for line in out[::-1]:
    data.insert(pointer + 1, line)
os.remove(path)
with open(path, "w") as t:
    t.write(''.join(data))
