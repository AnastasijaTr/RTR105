#!/usr/bin/python
# -*- coding: utf-8 -*-
a = input("Cienījamais letotāj, lūdzu, ievadi skaitļi:")
# 3. python'ā visi input rezultāti ir ar str datu tipu
# tāpēc ievadītā lieluma datu tips vālāk ir jāparveido
a = int(a)

print("Liet., Tu esi ievadījis skaitļi: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))

