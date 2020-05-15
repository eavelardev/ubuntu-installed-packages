import pandas as pd


netboot1804cinnamon = set(pd.read_csv('data/ubuntu-18.04-hwe-netboot(2020-01-30)_cinnamon.csv',header=None)[0].values.tolist())
deskmin1804 = set(pd.read_csv('data/ubuntu-18.04.4-desktop-minimal.csv',header=None)[0].values.tolist())

netboot2004cinnamon = set(pd.read_csv('data/ubuntu-20.04-netboot(2020-04-21)_cinnamon.csv',header=None)[0].values.tolist())
deskmin2004 = set(pd.read_csv('data/ubuntu-20.04-desktop-minimal.csv',header=None)[0].values.tolist())
desk2004 = set(pd.read_csv('data/ubuntu-20.04-desktop.csv',header=None)[0].values.tolist())


print(f'netboot1804cinnamon:                {len(netboot1804cinnamon)} packages')
print(f'deskmin1804:                        {len(deskmin1804)} packages')
print(f'netboot2004cinnamon:                {len(netboot2004cinnamon)} packages')
print(f'deskmin2004:                        {len(deskmin2004)} packages')
print(f'desk2004:                           {len(desk2004)} packages')

deskmin1804_netboot1804cinnamon = deskmin1804 - netboot1804cinnamon
deskmin1804_deskmin2004 = deskmin1804 - deskmin2004
deskmin2004_netboot2004cinnamon = desk2004 - netboot2004cinnamon
desk2004_deskmin2004 = desk2004 - deskmin2004
desk2004_netboot2004cinnamon = desk2004 - netboot2004cinnamon
deskmin2004_deskmin1804 = deskmin2004 - deskmin1804
# netboot2004cinnamon_netboot1804cinnamon = netboot2004cinnamon - netboot1804cinnamon
# netboot1804cinnamon_netboot2004cinnamon = netboot1804cinnamon - netboot2004cinnamon

print(f'deskmin1804_netboot1804cinnamon:    {len(deskmin1804_netboot1804cinnamon)} packages')
print(f'deskmin2004_netboot2004cinnamon:    {len(deskmin2004_netboot2004cinnamon)} packages')
print(f'desk2004_deskmin2004:               {len(desk2004_deskmin2004)} packages')
print(f'desk2004_netboot2004cinnamon:       {len(desk2004_netboot2004cinnamon)} packages')
# print(f'dif_desk2004_min: {len(dif_deskmin2004)} packages')
# print(f'dif_min_desk2004: {len(dif_minimal_desk2004)} packages')

print(f'\deskmin1804_deskmin2004:\n{sorted(deskmin1804_deskmin2004)}')