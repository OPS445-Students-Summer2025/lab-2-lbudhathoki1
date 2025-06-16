#!/usr/bin/env python3

# Author: Lalit Budhathoki
# Author ID: lbudhathoki
# Date Created: 2025/06/16
import sys
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3
while timer > 0:
    print(timer)
    timer -= 1
print('blast off!')
