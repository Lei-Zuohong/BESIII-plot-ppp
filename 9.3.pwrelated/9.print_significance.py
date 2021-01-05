# -*- coding: UTF-8 -*-
# Public package

# Private package
import headpy.hfile as hfile

a = hfile.pkl_read('output_nomial/2.1250.pkl')
b = a.significance

print(b)


