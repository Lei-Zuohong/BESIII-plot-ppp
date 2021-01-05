# -*- coding: UTF-8 -*-
# Public package

# Private package
import headpy.hfile as hfile
import headpy.hscreen.hprint as hprint


detail_pwa = hfile.pkl_read('5.python_efficiency_factor/data/nominal.pkl')
detail_2d = hfile.pkl_read('5.python_efficiency_factor/data/reweight2d.pkl')
detail_3d = hfile.pkl_read('5.python_efficiency_factor/data/reweight3d.pkl')
table = hprint.TABLE()
table.add_dict(detail_2d, key1='Energy')
table.platex()
