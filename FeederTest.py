# import numpy as np
import pyomo.environ as pyo
import py_dss_interface as pdi
import re
import math
from collections import Counter
from _pu_y_ import g
from _pu_y_ import b

# OpenDSS Obj
dss = pdi.DSSDLL()
dss_file = r"C:\Users\AG3 SOLUTIONS\Desktop\FeederTest\Master.dss"
dss.text("compile [{}]".format(dss_file))  # corretor de formato, erro em "Program Files" no espaço
dss.text('New Line.NEWSOURCE phases=3 bus1=NEWSOURCE bus2=A length=1 unit=km !normamps=10')
dss.text("Set Mode=SnapShot")
dss.text("solve")

# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______dictionary_settings______
keys = ('SBase', 'Buses', 'PriBuses', 'Branches', 'Phases', 'BranchPhase', 'BusPhase',
        'SourceBus', 'DSSSourceBus', 'CapBus', 'PVBus', 'CapBusCont', 'RegBranch', 'RegGanged',
        'G', 'B', 'Pload', 'Qload', 'Pgen', 'Qgen', 'Qcap', 'Ppv', 'Qpv', 'Qinjinit', 'Vminit', 'Vainit',
        'Capinit', 'Tapinit', 'BranchIRat', 'BranchSRat', 'PVSrat', 'PVPlimit', 'Vsource', 'ANGsource',
        'Gsource', 'Bsource', 'Sourcebusphase', 'Pinjinit')

dictionary_ = {}
dictionary_[keys[0]] = 1.0
dictionary_[keys[1]] = dss.circuit_allbusnames()
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
h = dss.circuit_allbusnames()
i = 0
f1 = list()
f2 = list()
while i <= len(dss.circuit_allbusnames()) - 1:
    dss.circuit_setactivebus(h[i])
    Vln = dss.bus_vmagangle()
    Vll = 1.73205 * dss.bus_vmagangle()[0]  # VLL = raiz3. VLN
    if (1.73205 * abs(dss.bus_vmagangle()[0])) >= 1000:

        f1.append(dss.bus_name())
    else:
        f2.append(dss.bus_name())
    i += 1
dictionary_[keys[2]] = f1
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
d = list()
i_ = 0
while i_ <= len(dss.lines_allnames()) - 1:
    dss.circuit_setactiveclass('Line')
    dss.lines_write_name(dss.lines_allnames()[i_])
    d.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
              (''.join(x for x in dss.lines_read_bus2() if x.isalpha()))))
    i_ += 1
i_ = 0
while i_ <= len(dss.lines_allnames()) - 1:
    dss.circuit_setactiveclass('Line')
    dss.lines_write_name(dss.lines_allnames()[i_])
    d.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
              (''.join(x for x in dss.lines_read_bus1() if x.isalpha()))))
    i_ += 1
i_ = 0

while i_ <= len(dss.transformers_allNames()) - 1:
    dss.circuit_setactiveclass('Transformer')
    dss.transformers_write_name(dss.transformers_allNames()[i_])
    d.append(dss.cktelement_read_busnames())
    d.append((dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0]))
    i_ += 1
dictionary_[keys[3]] = d
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
dictionary_[keys[4]] = ['1', '2', '3']
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
b_ = list()
i_ = 0
while i_ <= len(dss.lines_allnames()) - 1:
    dss.circuit_setactiveclass('Line')
    dss.lines_write_name(dss.lines_allnames()[i_])
    bus1 = dss.lines_read_bus1().split('.')
    if len(dss.lines_read_bus1()) == 1:
        # sentido ij
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '1'))
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '2'))
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '3'))
        # sentido ji
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '1'))
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '2'))
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '3'))

    elif len(dss.lines_read_bus1()) == 9:  # to bus NEWSOURCE
        # sentido ij
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '1'))
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '2'))
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '3'))
        # sentido ji
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '1'))
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '2'))
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '3'))
    elif len(bus1) == 3 and (re.findall('1' + '+', dss.lines_read_bus1())) and (
            re.findall('2' + '+', dss.lines_read_bus1())):
        # sentido ij
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '1'))
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '2'))
        # sentido ji
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '1'))
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '2'))

    elif len(bus1) == 3 and (re.findall('2' + '+', dss.lines_read_bus1())) and (
            re.findall('3' + '+', dss.lines_read_bus1())):
        # sentido ij
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '2'))
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '3'))
        # sentido ji
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '2'))
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '3'))

    elif len(bus1) == 2 and (re.findall('1' + '+', dss.lines_read_bus1())):
        # sentido ij
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '1'))
        # sentido ji
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '1'))

    elif len(bus1) == 2 and (re.findall('2' + '+', dss.lines_read_bus1())):
        # sentido ij
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '2'))
        # sentido ji
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '2'))

    elif len(bus1) == 2 and (re.findall('3' + '+', dss.lines_read_bus1())):
        # sentido ij
        b_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '3'))
        # sentido ji
        b_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                   (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '3'))
    i_ += 1

i_ = 0
while i_ <= len(dss.transformers_allNames()) - 1:
    dss.circuit_setactiveclass('Transformer')
    dss.transformers_write_name(dss.transformers_allNames()[i_])
    busnames = dss.cktelement_read_busnames()
    # sentido ij
    b_.append((busnames[0], busnames[1], '1'))
    b_.append((busnames[0], busnames[1], '2'))
    b_.append((busnames[0], busnames[1], '3'))
    # sentido ji
    b_.append((busnames[1], busnames[0], '1'))
    b_.append((busnames[1], busnames[0], '2'))
    b_.append((busnames[1], busnames[0], '3'))
    i_ += 1
dictionary_[keys[5]] = b_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# 'BusPhase'
i = 0
f = list()
while i <= len(dss.circuit_allbusnames()) - 1:
    dss.circuit_setactivebus(dss.circuit_allbusnames()[i])
    if len(dss.bus_nodes()) == 1:
        f.append((dss.bus_name(), str(dss.bus_nodes()[0])))
    elif len(dss.bus_nodes()) == 2:
        f.append((dss.bus_name(), str(dss.bus_nodes()[0])))
        f.append((dss.bus_name(), str(dss.bus_nodes()[1])))
    elif len(dss.bus_nodes()) == 3:
        f.append((dss.bus_name(), str(dss.bus_nodes()[0])))
        f.append((dss.bus_name(), str(dss.bus_nodes()[1])))
        f.append((dss.bus_name(), str(dss.bus_nodes()[2])))
    i += 1
dictionary_[keys[6]] = f
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
dss.circuit_setactivebus('NEWSOURCE')
dictionary_[keys[7]] = [dss.bus_name()]
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
dss.circuit_setactivebus('A')
dictionary_[keys[8]] = dss.bus_name()
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
s = list()
i = 0
if dss.capacitors_allnames()[0] != 'NONE':
    while i <= len(dss.capacitors_allnames()) - 1:
        dss.circuit_setactiveclass('Capacitor')
        dss.capacitors_write_name(dss.capacitors_allnames()[i])
        s.append((dss.cktelement_read_busnames()[0])[0])
        i += 1
else:
    pass
dictionary_[keys[9]] = s
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
v = list()
i = 0
if dss.pvsystems_allnames()[0] != 'NONE':
    while i <= len(dss.pvsystems_allnames()) - 1:
        dss.circuit_setactiveclass('PVSystem')
        dss.pvsystems_write_name(dss.pvsystems_allnames()[i])
        v.append(dss.cktelement_read_busnames()[0])
        i += 1
else:
    pass
dictionary_[keys[10]] = v
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
r = list()
i = 0
if dss.capacitors_allnames()[0] != 'NONE':
    while i <= len(dss.capacitors_allnames()) - 1:
        dss.circuit_setactiveclass('Capacitor')
        dss.capacitors_write_name(dss.capacitors_allnames()[i])
        r.append((dss.cktelement_read_busnames()[0])[0])
        i += 1
else:
    pass
dictionary_[keys[11]] = r
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# 'RegBranch'
i_ = 0
u = list()
if dss.regcontrols_allnames()[0] != 'NONE':
    while i_ <= len(dss.regcontrols_allnames()) - 1:
        dss.circuit_setactiveclass('Regcontrol')
        dss.circuit_setactiveelement(dss.regcontrols_allnames()[i_])
        dss.circuit_setactiveelement('Transformer.{}'.format(dss.dssproperties_read_value('1')))
        # sentido ij
        u.append((dss.cktelement_read_busnames()[0], dss.cktelement_read_busnames()[1], '1'))
        u.append((dss.cktelement_read_busnames()[0], dss.cktelement_read_busnames()[1], '2'))
        u.append((dss.cktelement_read_busnames()[0], dss.cktelement_read_busnames()[1], '3'))
        # sentido ji
        # u.append((dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0], '1'))
        # u.append((dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0], '2'))
        # u.append((dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0], '3'))
        i_ += 1
else:
    pass
dictionary_[keys[12]] = u

# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# 'RegGanged'
i_ = 0
u_ = list()
if dss.regcontrols_allnames()[0] != 'NONE':
    while i_ <= len(dss.regcontrols_allnames()) - 1:
        dss.circuit_setactiveclass('Regcontrol')
        dss.circuit_setactiveelement(dss.regcontrols_allnames()[i_])
        dss.circuit_setactiveelement('Transformer.{}'.format(dss.dssproperties_read_value('1')))
        # sentido ij
        u_.append((dss.cktelement_read_busnames()[0], dss.cktelement_read_busnames()[1]))

        # sentido ji
        # u_.append((dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0]))
        i_ += 1
else:
    pass
dictionary_[keys[13]] = u_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ____________________G____________________
dictionary_[keys[14]] = g
# # ______________________________________________________________________________________________
# # ______________________________________________________________________________________________
# # ______________________________________________________________________________________________
# # ______________________________________________________________________________________________
# # ____________________B____________________
dictionary_[keys[15]] = b
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# Loop para Pload formato ('A', 'a'): 0.0
i = 0
m_ = list()
ploadbuses = list()
if dss.loads_allnames()[0] != 'NONE':
    while i <= len(dss.loads_allnames()) - 1:
        dss.circuit_setactiveclass('Load')
        dss.loads_write_name(dss.loads_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        ploadbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para Carga Mono
        # Para Bus.1 Load.1 ou Bus.2 Load.2 ou Bus.3 Load.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', dss.loads_read_kw() / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '2', dss.loads_read_kw() / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '3', dss.loads_read_kw() / 1000))
                i += 1
            else:
                pass


        # Para Carga Mono
        # Para Bus.1.2 Load.1  ou Bus.1.3 Load.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                m_.append((dss.bus_name(), '1', dss.loads_read_kw() / 1000))
                m_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                m_.append((dss.bus_name(), '1', dss.loads_read_kw() / 1000))
                m_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.2 Load.1  ou Bus.2.3 Load.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                m_.append((dss.bus_name(), '1', '0.0'))
                m_.append((dss.bus_name(), '2', dss.loads_read_kw() / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                m_.append((dss.bus_name(), '2', dss.loads_read_kw() / 1000))
                m_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.3 Load.3  ou Bus.2.3 Load.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                m_.append((dss.bus_name(), '1', '0.0'))
                m_.append((dss.bus_name(), '3', dss.loads_read_kw() / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                m_.append((dss.bus_name(), '2', '0.0'))
                m_.append((dss.bus_name(), '3', dss.loads_read_kw() / 1000))
                i += 1
            else:
                pass


        # Para Carga Mono
        # Para Bus.1.2.3 Load.1, Load.2, Load.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', dss.loads_read_kw() / 1000))
                m_.append((dss.bus_name(), '2', '0.0'))
                m_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', '0.0'))
                m_.append((dss.bus_name(), '2', dss.loads_read_kw() / 1000))
                m_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', '0.0'))
                m_.append((dss.bus_name(), '2', '0.0'))
                m_.append((dss.bus_name(), '3', dss.loads_read_kw() / 1000))
                i += 1
            else:
                pass


        # Para Carga Bi
        # Para Bus.1.2 Load.1.2 ou Bus.2.2 Load.2.2 ou Bus.1.3 Load.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', (dss.loads_read_kw() / 2) / 1000))
                m_.append((dss.bus_name(), '2', (dss.loads_read_kw() / 2) / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '2', (dss.loads_read_kw() / 2) / 1000))
                m_.append((dss.bus_name(), '3', (dss.loads_read_kw() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', (dss.loads_read_kw() / 2) / 1000))
                m_.append((dss.bus_name(), '3', (dss.loads_read_kw() / 2) / 1000))
                i += 1
            else:
                pass


        # Para Carga Bi
        # Para Bus.1.2.3 Load.1.2 ou Bus.1.2.3 Load.2.3 ou Bus.1.2.3 Load.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', (dss.loads_read_kw() / 2) / 1000))
                m_.append((dss.bus_name(), '2', (dss.loads_read_kw() / 2) / 1000))
                m_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', '0.0'))
                m_.append((dss.bus_name(), '2', (dss.loads_read_kw() / 2) / 1000))
                m_.append((dss.bus_name(), '3', (dss.loads_read_kw() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                m_.append((dss.bus_name(), '1', (dss.loads_read_kw() / 2) / 1000))
                m_.append((dss.bus_name(), '2', '0.0'))
                m_.append((dss.bus_name(), '3', (dss.loads_read_kw() / 2) / 1000))
                i += 1
            else:
                pass


        # Para Carga Tri
        # Para Bus.1.2.3 Load.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            m_.append((dss.bus_name(), '1', (dss.loads_read_kw() / 3) / 1000))
            m_.append((dss.bus_name(), '2', (dss.loads_read_kw() / 3) / 1000))
            m_.append((dss.bus_name(), '3', (dss.loads_read_kw() / 3) / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem Loads________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(ploadbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem Loads a lista 'Qinjinit_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        m_.append((dss.bus_name(), '1', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        m_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        m_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        m_.append((dss.bus_name(), '1', '0.0'))
        m_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        m_.append((dss.bus_name(), '2', '0.0'))
        m_.append((dss.bus_name(), '3', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        m_.append((dss.bus_name(), '1', '0.0'))
        m_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 3:
        m_.append((dss.bus_name(), '1', '0.0'))
        m_.append((dss.bus_name(), '2', '0.0'))
        m_.append((dss.bus_name(), '3', '0.0'))
    i += 1
m_ = sorted(m_)
i_ = 0
n_ = list()
while i_ <= len(m_) - 1:
    kk = list(m_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_m_ = {}
while i_ <= len(m_) - 1:
    _m_[n_[i_]] = (m_[i_])[2]
    i_ += 1
dictionary_[keys[16]] = _m_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# Loop para Qload formato ('A', 'a'): 0.0
i = 0
q_ = list()
qloadbuses = list()
if dss.loads_allnames()[0] != 'NONE':
    while i <= len(dss.loads_allnames()) - 1:
        dss.circuit_setactiveclass('Load')
        dss.loads_write_name(dss.loads_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        qloadbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para Carga Mono
        # Para Bus.1 Load.1 ou Bus.2 Load.2 ou Bus.3 Load.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', dss.loads_read_kvar() / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '2', dss.loads_read_kvar() / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '3', dss.loads_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para Carga Mono
        # Para Bus.1.2 Load.1  ou Bus.1.3 Load.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                q_.append((dss.bus_name(), '1', dss.loads_read_kvar() / 1000))
                q_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                q_.append((dss.bus_name(), '1', dss.loads_read_kvar() / 1000))
                q_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.2 Load.1  ou Bus.2.3 Load.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                q_.append((dss.bus_name(), '1', '0.0'))
                q_.append((dss.bus_name(), '2', dss.loads_read_kvar() / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                q_.append((dss.bus_name(), '2', dss.loads_read_kvar() / 1000))
                q_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.3 Load.3  ou Bus.2.3 Load.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                q_.append((dss.bus_name(), '1', '0.0'))
                q_.append((dss.bus_name(), '3', dss.loads_read_kvar() / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                q_.append((dss.bus_name(), '2', '0.0'))
                q_.append((dss.bus_name(), '3', dss.loads_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para Carga Mono
        # Para Bus.1.2.3 Load.1, Load.2, Load.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', dss.loads_read_kvar() / 1000))
                q_.append((dss.bus_name(), '2', '0.0'))
                q_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', '0.0'))
                q_.append((dss.bus_name(), '2', dss.loads_read_kvar() / 1000))
                q_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', '0.0'))
                q_.append((dss.bus_name(), '2', '0.0'))
                q_.append((dss.bus_name(), '3', dss.loads_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para Carga Bi
        # Para Bus.1.2 Load.1.2 ou Bus.2.2 Load.2.2 ou Bus.1.3 Load.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', (dss.loads_read_kvar() / 2) / 1000))
                q_.append((dss.bus_name(), '2', (dss.loads_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '2', (dss.loads_read_kvar() / 2) / 1000))
                q_.append((dss.bus_name(), '3', (dss.loads_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', (dss.loads_read_kvar() / 2) / 1000))
                q_.append((dss.bus_name(), '3', (dss.loads_read_kvar() / 2) / 1000))
                i += 1
            else:
                pass


        # Para Carga Bi
        # Para Bus.1.2.3 Load.1.2 ou Bus.1.2.3 Load.2.3 ou Bus.1.2.3 Load.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', (dss.loads_read_kvar() / 2) / 1000))
                q_.append((dss.bus_name(), '2', (dss.loads_read_kvar() / 2) / 1000))
                q_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', '0.0'))
                q_.append((dss.bus_name(), '2', (dss.loads_read_kvar() / 2) / 1000))
                q_.append((dss.bus_name(), '3', (dss.loads_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                q_.append((dss.bus_name(), '1', (dss.loads_read_kvar() / 2) / 1000))
                q_.append((dss.bus_name(), '2', '0.0'))
                q_.append((dss.bus_name(), '3', (dss.loads_read_kvar() / 2) / 1000))
                i += 1
            else:
                pass


        # Para Carga Tri
        # Para Bus.1.2.3 Load.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            q_.append((dss.bus_name(), '1', (dss.loads_read_kvar() / 3) / 1000))
            q_.append((dss.bus_name(), '2', (dss.loads_read_kvar() / 3) / 1000))
            q_.append((dss.bus_name(), '3', (dss.loads_read_kvar() / 3) / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem Loads________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(qloadbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem Loads a lista 'q_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        q_.append((dss.bus_name(), '1', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        q_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        q_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        q_.append((dss.bus_name(), '1', '0.0'))
        q_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        q_.append((dss.bus_name(), '2', '0.0'))
        q_.append((dss.bus_name(), '3', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        q_.append((dss.bus_name(), '1', '0.0'))
        q_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 3:
        q_.append((dss.bus_name(), '1', '0.0'))
        q_.append((dss.bus_name(), '2', '0.0'))
        q_.append((dss.bus_name(), '3', '0.0'))
    i += 1
q_ = sorted(q_)
i_ = 0
n_ = list()
while i_ <= len(q_) - 1:
    kk = list(q_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_q_ = {}
while i_ <= len(q_) - 1:
    _q_[n_[i_]] = (q_[i_])[2]
    i_ += 1
dictionary_[keys[17]] = _q_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# pego todas as barras que tem geração  'Pgen'     formato ('A', 'a'): 0.0 em   WATTs
i = 0
f_ = list()
genbuses = list()
if dss.generators_allnames()[0] != 'NONE':
    while i <= len(dss.generators_allnames()) - 1:
        dss.circuit_setactiveclass('Generator')
        dss.generators_write_name(dss.loads_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        genbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para Gerador Mono
        # Para Bus.1 Gerador.1 ou Bus.2 Gerador.2 ou Bus.3 Gerador.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', dss.generators_read_kw() / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '2', dss.generators_read_kw() / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '3', dss.generators_read_kw() / 1000))
                i += 1
            else:
                pass


        # Para Gerador Mono
        # Para Bus.1.2 Gerador.1  ou Bus.1.3 Gerador.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                f_.append((dss.bus_name(), '1', dss.generators_read_kw() / 1000))
                f_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                f_.append((dss.bus_name(), '1', dss.generators_read_kw() / 1000))
                f_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.2 Gerador.1  ou Bus.2.3 Gerador.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                f_.append((dss.bus_name(), '1', '0.0'))
                f_.append((dss.bus_name(), '2', dss.generators_read_kw() / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                f_.append((dss.bus_name(), '2', dss.generators_read_kw() / 1000))
                f_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.3 Gerador.3  ou Bus.2.3 Gerador.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                f_.append((dss.bus_name(), '1', '0.0'))
                f_.append((dss.bus_name(), '3', dss.generators_read_kw() / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                f_.append((dss.bus_name(), '2', '0.0'))
                f_.append((dss.bus_name(), '3', dss.generators_read_kw() / 1000))
                i += 1
            else:
                pass


        # Para Gerador Mono
        # Para Bus.1.2.3 Gerador.1, Gerador.2, Gerador.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', dss.generators_read_kw() / 1000))
                f_.append((dss.bus_name(), '2', '0.0'))
                f_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', '0.0'))
                f_.append((dss.bus_name(), '2', dss.generators_read_kw() / 1000))
                f_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', '0.0'))
                f_.append((dss.bus_name(), '2', '0.0'))
                f_.append((dss.bus_name(), '3', dss.generators_read_kw() / 1000))
                i += 1
            else:
                pass


        # Para Gerador Bi
        # Para Bus.1.2 Gerador.1.2 ou Bus.2.2 Gerador.2.2 ou Bus.1.3 Gerador.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', (dss.generators_read_kw() / 2) / 1000))
                f_.append((dss.bus_name(), '2', (dss.generators_read_kw() / 2) / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '2', (dss.generators_read_kw() / 2) / 1000))
                f_.append((dss.bus_name(), '3', (dss.generators_read_kw() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', (dss.generators_read_kw() / 2) / 1000))
                f_.append((dss.bus_name(), '3', (dss.generators_read_kw() / 2) / 1000))
                i += 1
            else:
                pass


        # Para Gerador Bi
        # Para Bus.1.2.3 Gerador.1.2 ou Bus.1.2.3 Gerador.2.3 ou Bus.1.2.3 Gerador.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', (dss.generators_read_kw() / 2) / 1000))
                f_.append((dss.bus_name(), '2', (dss.generators_read_kw() / 2) / 1000))
                f_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', '0.0'))
                f_.append((dss.bus_name(), '2', (dss.generators_read_kw() / 2) / 1000))
                f_.append((dss.bus_name(), '3', (dss.generators_read_kw() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                f_.append((dss.bus_name(), '1', (dss.generators_read_kw() / 2) / 1000))
                f_.append((dss.bus_name(), '2', '0.0'))
                f_.append((dss.bus_name(), '3', (dss.generators_read_kw() / 2) / 1000))
                i += 1
            else:
                pass


        # Para Gerador Tri
        # Para Bus.1.2.3 Gerador.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            f_.append((dss.bus_name(), '1', (dss.generators_read_kw() / 3) / 1000))
            f_.append((dss.bus_name(), '2', (dss.generators_read_kw() / 3) / 1000))
            f_.append((dss.bus_name(), '3', (dss.generators_read_kw() / 3) / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem Gerador________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(genbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem Gerador a lista 'f_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        f_.append((dss.bus_name(), '1', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        f_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        f_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        f_.append((dss.bus_name(), '1', '0.0'))
        f_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        f_.append((dss.bus_name(), '2', '0.0'))
        f_.append((dss.bus_name(), '3', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        f_.append((dss.bus_name(), '1', '0.0'))
        f_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 3:
        f_.append((dss.bus_name(), '1', '0.0'))
        f_.append((dss.bus_name(), '2', '0.0'))
        f_.append((dss.bus_name(), '3', '0.0'))
    i += 1
f_ = sorted(f_)
i_ = 0
n_ = list()
while i_ <= len(f_) - 1:
    kk = list(f_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_f_ = {}
while i_ <= len(f_) - 1:
    _f_[n_[i_]] = (f_[i_])[2]
    i_ += 1
dictionary_[keys[18]] = _f_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# pego todas as barras que tem geração  'Qgen' formato ('A', 'a'): 0.0  (Var)
i = 0
ff_ = list()
qgenbuses = list()
if dss.generators_allnames()[0] != 'NONE':
    while i <= len(dss.generators_allnames()) - 1:
        dss.circuit_setactiveclass('Generator')
        dss.generators_write_name(dss.loads_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        qgenbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para Gerador Mono
        # Para Bus.1 Gerador.1 ou Bus.2 Gerador.2 ou Bus.3 Gerador.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', dss.generators_read_kvar() / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '2', dss.generators_read_kvar() / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '3', dss.generators_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para Gerador Mono
        # Para Bus.1.2 Gerador.1  ou Bus.1.3 Gerador.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                ff_.append((dss.bus_name(), '1', dss.generators_read_kvar() / 1000))
                ff_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                ff_.append((dss.bus_name(), '1', dss.generators_read_kvar() / 1000))
                ff_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.2 Gerador.1  ou Bus.2.3 Gerador.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                ff_.append((dss.bus_name(), '1', '0.0'))
                ff_.append((dss.bus_name(), '2', dss.generators_read_kvar() / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                ff_.append((dss.bus_name(), '2', dss.generators_read_kvar() / 1000))
                ff_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.3 Gerador.3  ou Bus.2.3 Gerador.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                ff_.append((dss.bus_name(), '1', '0.0'))
                ff_.append((dss.bus_name(), '3', dss.generators_read_kvar() / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                ff_.append((dss.bus_name(), '2', '0.0'))
                ff_.append((dss.bus_name(), '3', dss.generators_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para Gerador Mono
        # Para Bus.1.2.3 Gerador.1, Gerador.2, Gerador.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', dss.generators_read_kvar() / 1000))
                ff_.append((dss.bus_name(), '2', '0.0'))
                ff_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', '0.0'))
                ff_.append((dss.bus_name(), '2', dss.generators_read_kvar() / 1000))
                ff_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', '0.0'))
                ff_.append((dss.bus_name(), '2', '0.0'))
                ff_.append((dss.bus_name(), '3', dss.generators_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para Gerador Bi
        # Para Bus.1.2 Gerador.1.2 ou Bus.2.2 Gerador.2.2 ou Bus.1.3 Gerador.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', (dss.generators_read_kvar() / 2) / 1000))
                ff_.append((dss.bus_name(), '2', (dss.generators_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '2', (dss.generators_read_kvar() / 2) / 1000))
                ff_.append((dss.bus_name(), '3', (dss.generators_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', (dss.generators_read_kvar() / 2) / 1000))
                ff_.append((dss.bus_name(), '3', (dss.generators_read_kvar() / 2) / 1000))
                i += 1
            else:
                pass


        # Para Gerador Bi
        # Para Bus.1.2.3 Gerador.1.2 ou Bus.1.2.3 Gerador.2.3 ou Bus.1.2.3 Gerador.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', (dss.generators_read_kvar() / 2) / 1000))
                ff_.append((dss.bus_name(), '2', (dss.generators_read_kvar() / 2) / 1000))
                ff_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', '0.0'))
                ff_.append((dss.bus_name(), '2', (dss.generators_read_kvar() / 2) / 1000))
                ff_.append((dss.bus_name(), '3', (dss.generators_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                ff_.append((dss.bus_name(), '1', (dss.generators_read_kvar() / 2) / 1000))
                ff_.append((dss.bus_name(), '2', '0.0'))
                ff_.append((dss.bus_name(), '3', (dss.generators_read_kvar() / 2) / 1000))
                i += 1
            else:
                pass


        # Para Gerador Tri
        # Para Bus.1.2.3 Gerador.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            ff_.append((dss.bus_name(), '1', (dss.generators_read_kvar() / 3) / 1000))
            ff_.append((dss.bus_name(), '2', (dss.generators_read_kvar() / 3) / 1000))
            ff_.append((dss.bus_name(), '3', (dss.generators_read_kvar() / 3) / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem Gerador________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(qgenbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem Gerador a lista 'ff_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        ff_.append((dss.bus_name(), '1', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        ff_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        ff_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        ff_.append((dss.bus_name(), '1', '0.0'))
        ff_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        ff_.append((dss.bus_name(), '2', '0.0'))
        ff_.append((dss.bus_name(), '3', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        ff_.append((dss.bus_name(), '1', '0.0'))
        ff_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 3:
        ff_.append((dss.bus_name(), '1', '0.0'))
        ff_.append((dss.bus_name(), '2', '0.0'))
        ff_.append((dss.bus_name(), '3', '0.0'))
    i += 1
ff_ = sorted(ff_)
i_ = 0
n_ = list()
while i_ <= len(ff_) - 1:
    kk = list(ff_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_ff_ = {}
while i_ <= len(ff_) - 1:
    _ff_[n_[i_]] = (ff_[i_])[2]
    i_ += 1
dictionary_[keys[19]] = _ff_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# pego todas as barras que tem capacitores   'Qcap'  formato  ('A', 'a'): 0.0   (Var)
i = 0
cc_ = list()
capbuses = list()
if dss.capacitors_allnames()[0] != 'NONE':
    while i <= len(dss.capacitors_allnames()) - 1:
        dss.circuit_setactiveclass('Capacitor')
        dss.capacitors_write_name(dss.capacitors_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        capbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para capacitor Mono
        # Para Bus.1 capacitor.1 ou Bus.2 capacitor.2 ou Bus.3 capacitor.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', dss.capacitors_read_kvar() / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '2', dss.capacitors_read_kvar() / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '3', dss.capacitors_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para capacitor Mono
        # Para Bus.1.2 capacitor.1  ou Bus.1.3 capacitor.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                cc_.append((dss.bus_name(), '1', dss.capacitors_read_kvar() / 1000))
                cc_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                cc_.append((dss.bus_name(), '1', dss.capacitors_read_kvar() / 1000))
                cc_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.2 capacitor.1  ou Bus.2.3 capacitor.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                cc_.append((dss.bus_name(), '1', '0.0'))
                cc_.append((dss.bus_name(), '2', dss.capacitors_read_kvar() / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                cc_.append((dss.bus_name(), '2', dss.capacitors_read_kvar() / 1000))
                cc_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.3 capacitor.3  ou Bus.2.3 capacitor.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                cc_.append((dss.bus_name(), '1', '0.0'))
                cc_.append((dss.bus_name(), '3', dss.capacitors_read_kvar() / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                cc_.append((dss.bus_name(), '2', '0.0'))
                cc_.append((dss.bus_name(), '3', dss.capacitors_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para capacitor Mono
        # Para Bus.1.2.3 capacitor.1, capacitor.2, capacitor.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', dss.capacitors_read_kvar() / 1000))
                cc_.append((dss.bus_name(), '2', '0.0'))
                cc_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', '0.0'))
                cc_.append((dss.bus_name(), '2', dss.capacitors_read_kvar() / 1000))
                cc_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', '0.0'))
                cc_.append((dss.bus_name(), '2', '0.0'))
                cc_.append((dss.bus_name(), '3', dss.capacitors_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para capacitor Bi
        # Para Bus.1.2 capacitor.1.2 ou Bus.2.2 capacitor.2.2 ou Bus.1.3 capacitor.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', (dss.capacitors_read_kvar() / 2) / 1000))
                cc_.append((dss.bus_name(), '2', (dss.capacitors_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '2', (dss.capacitors_read_kvar() / 2) / 1000))
                cc_.append((dss.bus_name(), '3', (dss.capacitors_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', (dss.capacitors_read_kvar() / 2) / 1000))
                cc_.append((dss.bus_name(), '3', (dss.capacitors_read_kvar() / 2) / 1000))
                i += 1
            else:
                pass


        # Para capacitor Bi
        # Para Bus.1.2.3 capacitor.1.2 ou Bus.1.2.3 capacitor.2.3 ou Bus.1.2.3 capacitor.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', (dss.capacitors_read_kvar() / 2) / 1000))
                cc_.append((dss.bus_name(), '2', (dss.capacitors_read_kvar() / 2) / 1000))
                cc_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', '0.0'))
                cc_.append((dss.bus_name(), '2', (dss.capacitors_read_kvar() / 2) / 1000))
                cc_.append((dss.bus_name(), '3', (dss.capacitors_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                cc_.append((dss.bus_name(), '1', (dss.capacitors_read_kvar() / 2) / 1000))
                cc_.append((dss.bus_name(), '2', '0.0'))
                cc_.append((dss.bus_name(), '3', (dss.capacitors_read_kvar() / 2) / 1000))
                i += 1
            else:
                pass


        # Para capacitor Tri
        # Para Bus.1.2.3 capacitor.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            cc_.append((dss.bus_name(), '1', (dss.capacitors_read_kvar() / 3) / 1000))
            cc_.append((dss.bus_name(), '2', (dss.capacitors_read_kvar() / 3) / 1000))
            cc_.append((dss.bus_name(), '3', (dss.capacitors_read_kvar() / 3) / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem capacitor________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(capbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem capacitor a lista 'cc_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        cc_.append((dss.bus_name(), '1', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        cc_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        cc_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        cc_.append((dss.bus_name(), '1', '0.0'))
        cc_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        cc_.append((dss.bus_name(), '2', '0.0'))
        cc_.append((dss.bus_name(), '3', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        cc_.append((dss.bus_name(), '1', '0.0'))
        cc_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 3:
        cc_.append((dss.bus_name(), '1', '0.0'))
        cc_.append((dss.bus_name(), '2', '0.0'))
        cc_.append((dss.bus_name(), '3', '0.0'))
    i += 1
cc_ = sorted(cc_)
i_ = 0
n_ = list()
while i_ <= len(cc_) - 1:
    kk = list(cc_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_cc_ = {}
while i_ <= len(cc_) - 1:
    _cc_[n_[i_]] = (cc_[i_])[2]
    i_ += 1
dictionary_[keys[20]] = _cc_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# pego todas as barras que tem PVs   'Ppv' (watts)
i = 0
pp_ = list()
pvbuses = list()
if dss.pvsystems_allnames()[0] != 'NONE':
    while i <= len(dss.pvsystems_allnames()) - 1:
        dss.circuit_setactiveclass('PVSystem')
        dss.pvsystems_write_name(dss.pvsystems_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        pvbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para pvsystem Mono
        # Para Bus.1 pvsystem.1 ou Bus.2 pvsystem.2 ou Bus.3 pvsystem.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', dss.pvsystems_kw() / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '2', dss.pvsystems_kw() / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '3', dss.pvsystems_kw() / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Mono
        # Para Bus.1.2 pvsystem.1  ou Bus.1.3 pvsystem.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                pp_.append((dss.bus_name(), '1', dss.pvsystems_kw() / 1000))
                pp_.append((dss.bus_name(), '2', 0.0))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                pp_.append((dss.bus_name(), '1', dss.pvsystems_kw() / 1000))
                pp_.append((dss.bus_name(), '3', 0.0))
                i += 1
            # Para Bus.1.2 pvsystem.1  ou Bus.2.3 pvsystem.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                pp_.append((dss.bus_name(), '1', 0.0))
                pp_.append((dss.bus_name(), '2', dss.pvsystems_kw() / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                pp_.append((dss.bus_name(), '2', dss.pvsystems_kw() / 1000))
                pp_.append((dss.bus_name(), '3', 0.0))
                i += 1
            # Para Bus.1.3 pvsystem.3  ou Bus.2.3 pvsystem.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                pp_.append((dss.bus_name(), '1', 0.0))
                pp_.append((dss.bus_name(), '3', dss.pvsystems_kw() / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                pp_.append((dss.bus_name(), '2', 0.0))
                pp_.append((dss.bus_name(), '3', dss.pvsystems_kw() / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Mono
        # Para Bus.1.2.3 pvsystem.1, pvsystem.2, pvsystem.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', dss.pvsystems_kw() / 1000))
                pp_.append((dss.bus_name(), '2', 0.0))
                pp_.append((dss.bus_name(), '2', 0.0))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', 0.0))
                pp_.append((dss.bus_name(), '2', dss.pvsystems_kw() / 1000))
                pp_.append((dss.bus_name(), '3', 0.0))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', 0.0))
                pp_.append((dss.bus_name(), '2', 0.0))
                pp_.append((dss.bus_name(), '3', dss.pvsystems_kw() / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Bi
        # Para Bus.1.2 pvsystem.1.2 ou Bus.2.2 pvsystem.2.2 ou Bus.1.3 pvsystem.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', (dss.pvsystems_kw() / 2) / 1000))
                pp_.append((dss.bus_name(), '2', (dss.pvsystems_kw() / 2) / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '2', (dss.pvsystems_kw() / 2) / 1000))
                pp_.append((dss.bus_name(), '3', (dss.pvsystems_kw() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', (dss.pvsystems_kw() / 2) / 1000))
                pp_.append((dss.bus_name(), '3', (dss.pvsystems_kw() / 2) / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Bi
        # Para Bus.1.2.3 pvsystem.1.2 ou Bus.1.2.3 pvsystem.2.3 ou Bus.1.2.3 pvsystem.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', (dss.pvsystems_kw() / 2) / 1000))
                pp_.append((dss.bus_name(), '2', (dss.pvsystems_kw() / 2) / 1000))
                pp_.append((dss.bus_name(), '3', 0.0))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', 0.0))
                pp_.append((dss.bus_name(), '2', (dss.pvsystems_kw() / 2) / 1000))
                pp_.append((dss.bus_name(), '3', (dss.pvsystems_kw() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                pp_.append((dss.bus_name(), '1', (dss.pvsystems_kw() / 2) / 1000))
                pp_.append((dss.bus_name(), '2', 0.0))
                pp_.append((dss.bus_name(), '3', (dss.pvsystems_kw() / 2) / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Tri
        # Para Bus.1.2.3 pvsystem.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            pp_.append((dss.bus_name(), '1', (dss.pvsystems_kw() / 3) / 1000))
            pp_.append((dss.bus_name(), '2', (dss.pvsystems_kw() / 3) / 1000))
            pp_.append((dss.bus_name(), '3', (dss.pvsystems_kw() / 3) / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem pvsystem________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(pvbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem pvsystem a lista 'pp_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        pp_.append((dss.bus_name(), '1', 0.0))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        pp_.append((dss.bus_name(), '2', 0.0))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        pp_.append((dss.bus_name(), '3', 0.0))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        pp_.append((dss.bus_name(), '1', 0.0))
        pp_.append((dss.bus_name(), '2', 0.0))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        pp_.append((dss.bus_name(), '2', 0.0))
        pp_.append((dss.bus_name(), '3', 0.0))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        pp_.append((dss.bus_name(), '1', 0.0))
        pp_.append((dss.bus_name(), '3', 0.0))

    elif len(dss.bus_nodes()) == 3:
        pp_.append((dss.bus_name(), '1', 0.0))
        pp_.append((dss.bus_name(), '2', 0.0))
        pp_.append((dss.bus_name(), '3', 0.0))
    i += 1
pp_ = sorted(pp_)
i_ = 0
n_ = list()
while i_ <= len(pp_) - 1:
    kk = list(pp_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_pp_ = {}
while i_ <= len(pp_) - 1:
    _pp_[n_[i_]] = (pp_[i_])[2]
    i_ += 1
dictionary_[keys[21]] = _pp_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# pego todas as barras que tem PVs    'Qpv'       (Var)
i = 0
qpp_ = list()
qpvbuses = list()
if dss.pvsystems_allnames()[0] != 'NONE':
    while i <= len(dss.pvsystems_allnames()) - 1:
        dss.circuit_setactiveclass('PVSystem')
        dss.pvsystems_write_name(dss.pvsystems_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        qpvbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para pvsystem Mono
        # Para Bus.1 pvsystem.1 ou Bus.2 pvsystem.2 ou Bus.3 pvsystem.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', dss.pvsystems_read_kvar() / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '2', dss.pvsystems_read_kvar() / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '3', dss.pvsystems_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Mono
        # Para Bus.1.2 pvsystem.1  ou Bus.1.3 pvsystem.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                qpp_.append((dss.bus_name(), '1', dss.pvsystems_read_kvar() / 1000))
                qpp_.append((dss.bus_name(), '2', 0.0))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                qpp_.append((dss.bus_name(), '1', dss.pvsystems_read_kvar() / 1000))
                qpp_.append((dss.bus_name(), '3', 0.0))
                i += 1
            # Para Bus.1.2 pvsystem.1  ou Bus.2.3 pvsystem.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                qpp_.append((dss.bus_name(), '1', 0.0))
                qpp_.append((dss.bus_name(), '2', dss.pvsystems_read_kvar() / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                qpp_.append((dss.bus_name(), '2', dss.pvsystems_read_kvar() / 1000))
                qpp_.append((dss.bus_name(), '3', 0.0))
                i += 1
            # Para Bus.1.3 pvsystem.3  ou Bus.2.3 pvsystem.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                qpp_.append((dss.bus_name(), '1', 0.0))
                qpp_.append((dss.bus_name(), '3', dss.pvsystems_read_kvar() / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                qpp_.append((dss.bus_name(), '2', 0.0))
                qpp_.append((dss.bus_name(), '3', dss.pvsystems_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Mono
        # Para Bus.1.2.3 pvsystem.1, pvsystem.2, pvsystem.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', dss.pvsystems_read_kvar() / 1000))
                qpp_.append((dss.bus_name(), '2', 0.0))
                qpp_.append((dss.bus_name(), '2', 0.0))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', 0.0))
                qpp_.append((dss.bus_name(), '2', dss.pvsystems_read_kvar() / 1000))
                qpp_.append((dss.bus_name(), '3', 0.0))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', 0.0))
                qpp_.append((dss.bus_name(), '2', 0.0))
                qpp_.append((dss.bus_name(), '3', dss.pvsystems_read_kvar() / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Bi
        # Para Bus.1.2 pvsystem.1.2 ou Bus.2.2 pvsystem.2.2 ou Bus.1.3 pvsystem.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', (dss.pvsystems_read_kvar() / 2) / 1000))
                qpp_.append((dss.bus_name(), '2', (dss.pvsystems_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '2', (dss.pvsystems_read_kvar() / 2) / 1000))
                qpp_.append((dss.bus_name(), '3', (dss.pvsystems_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', (dss.pvsystems_read_kvar() / 2) / 1000))
                qpp_.append((dss.bus_name(), '3', (dss.pvsystems_read_kvar() / 2) / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Bi
        # Para Bus.1.2.3 pvsystem.1.2 ou Bus.1.2.3 pvsystem.2.3 ou Bus.1.2.3 pvsystem.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', (dss.pvsystems_read_kvar() / 2) / 1000))
                qpp_.append((dss.bus_name(), '2', (dss.pvsystems_read_kvar() / 2) / 1000))
                qpp_.append((dss.bus_name(), '3', 0.0))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', 0.0))
                qpp_.append((dss.bus_name(), '2', (dss.pvsystems_read_kvar() / 2) / 1000))
                qpp_.append((dss.bus_name(), '3', (dss.pvsystems_read_kvar() / 2) / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                qpp_.append((dss.bus_name(), '1', (dss.pvsystems_read_kvar() / 2) / 1000))
                qpp_.append((dss.bus_name(), '2', 0.0))
                qpp_.append((dss.bus_name(), '3', (dss.pvsystems_read_kvar() / 2) / 1000))
                i += 1
            else:
                pass


        # Para pvsystem Tri
        # Para Bus.1.2.3 pvsystem.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            qpp_.append((dss.bus_name(), '1', (dss.pvsystems_read_kvar() / 3) / 1000))
            qpp_.append((dss.bus_name(), '2', (dss.pvsystems_read_kvar() / 3) / 1000))
            qpp_.append((dss.bus_name(), '3', (dss.pvsystems_read_kvar() / 3) / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem pvsystem________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(qpvbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem pvsystem a lista 'qpp_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        qpp_.append((dss.bus_name(), '1', 0.0))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        qpp_.append((dss.bus_name(), '2', 0.0))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        qpp_.append((dss.bus_name(), '3', 0.0))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        qpp_.append((dss.bus_name(), '1', 0.0))
        qpp_.append((dss.bus_name(), '2', 0.0))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        qpp_.append((dss.bus_name(), '2', 0.0))
        qpp_.append((dss.bus_name(), '3', 0.0))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        qpp_.append((dss.bus_name(), '1', 0.0))
        qpp_.append((dss.bus_name(), '3', 0.0))

    elif len(dss.bus_nodes()) == 3:
        qpp_.append((dss.bus_name(), '1', 0.0))
        qpp_.append((dss.bus_name(), '2', 0.0))
        qpp_.append((dss.bus_name(), '3', 0.0))
    i += 1
qpp_ = sorted(qpp_)
i_ = 0
n_ = list()
while i_ <= len(qpp_) - 1:
    kk = list(qpp_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_qpp_ = {}
while i_ <= len(qpp_) - 1:
    _qpp_[n_[i_]] = (qpp_[i_])[2]
    i_ += 1
dictionary_[keys[22]] = _qpp_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o Qinjinit formato  {('A', 'a'): 0.0
i = 0
Qinjinit_ = list()
qinloadsbuses = list()
if dss.loads_allnames()[0] != 'NONE':
    while i <= len(dss.loads_allnames()) - 1:
        dss.circuit_setactiveclass('Load')
        dss.loads_write_name(dss.loads_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        qinloadsbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para Carga Mono
        # Para Bus.1 Load.1 ou Bus.2 Load.2 ou Bus.3 Load.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1


        # Para Carga Mono
        # Para Bus.1.2 Load.1  ou Bus.1.3 Load.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '2', 0.0))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '3', 0.0))
                i += 1
            # Para Bus.1.2 Load.1  ou Bus.2.3 Load.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                Qinjinit_.append((dss.bus_name(), '1', 0.0))
                Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '3', 0.0))
                i += 1
            # Para Bus.1.3 Load.3  ou Bus.2.3 Load.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                Qinjinit_.append((dss.bus_name(), '1', 0.0))
                Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                Qinjinit_.append((dss.bus_name(), '2', 0.0))
                Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1


        # Para Carga Mono
        # Para Bus.1.2.3 Load.1, Load.2, Load.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '2', 0.0))
                Qinjinit_.append((dss.bus_name(), '2', 0.0))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', 0.0))
                Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '3', 0.0))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', 0.0))
                Qinjinit_.append((dss.bus_name(), '2', 0.0))
                Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1


        # Para Carga Bi
        # Para Bus.1.2 Load.1.2 ou Bus.2.2 Load.2.2 ou Bus.1.3 Load.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1


        # Para Carga Bi
        # Para Bus.1.2.3 Load.1.2 ou Bus.1.2.3 Load.2.3 ou Bus.1.2.3 Load.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '3', 0.0))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', 0.0))
                Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
                Qinjinit_.append((dss.bus_name(), '2', 0.0))
                Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
                i += 1


        # Para Carga Tri
        # Para Bus.1.2.3 Load.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            Qinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[1] / 1000))
            Qinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[1] / 1000))
            Qinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[1] / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem Loads________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(qinloadsbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem Loads a lista 'Qinjinit_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        Qinjinit_.append((dss.bus_name(), 1, 0.0))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        Qinjinit_.append((dss.bus_name(), 2, 0.0))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        Qinjinit_.append((dss.bus_name(), 3, 0.0))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        Qinjinit_.append((dss.bus_name(), 1, 0.0))
        Qinjinit_.append((dss.bus_name(), 2, 0.0))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        Qinjinit_.append((dss.bus_name(), 2, 0.0))
        Qinjinit_.append((dss.bus_name(), 3, 0.0))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        Qinjinit_.append((dss.bus_name(), 1, 0.0))
        Qinjinit_.append((dss.bus_name(), 3, 0.0))

    elif len(dss.bus_nodes()) == 3:
        Qinjinit_.append((dss.bus_name(), 1, 0.0))
        Qinjinit_.append((dss.bus_name(), 2, 0.0))
        Qinjinit_.append((dss.bus_name(), 3, 0.0))
    i += 1
Qinjinit_ = sorted(Qinjinit_)
i_ = 0
n_ = list()
while i_ <= len(Qinjinit_) - 1:
    kk = list(Qinjinit_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_Qinjinit_ = {}
while i_ <= len(Qinjinit_) - 1:
    _Qinjinit_[n_[i_]] = (Qinjinit_[i_])[2]
    i_ += 1

dictionary_[keys[23]] = _Qinjinit_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o 'Vminit' formato  {('A', 'a'): 0.0
i = 0
vm_ = list()
while i <= len(dss.circuit_allbusnames()) - 1:
    dss.circuit_setactivebus(dss.circuit_allbusnames()[i])
    if len(dss.bus_nodes()) == 1:
        if dss.bus_nodes()[0] == 1:
            vm_.append((dss.bus_name(), '1', dss.bus_puvmagangle()[0]))
            i += 1
        elif dss.bus_nodes()[0] == 2:
            vm_.append((dss.bus_name(), '2', dss.bus_puvmagangle()[0]))
            i += 1
        elif dss.bus_nodes()[0] == 3:
            vm_.append((dss.bus_name(), '3', dss.bus_puvmagangle()[0]))
            i += 1
    elif len(dss.bus_nodes()) == 2:
        if dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
            vm_.append((dss.bus_name(), '1', dss.bus_puvmagangle()[0]))
            vm_.append((dss.bus_name(), '2', dss.bus_puvmagangle()[2]))
            i += 1
        elif dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
            vm_.append((dss.bus_name(), '2', dss.bus_puvmagangle()[0]))
            vm_.append((dss.bus_name(), '3', dss.bus_puvmagangle()[2]))
            i += 1
        elif dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
            vm_.append((dss.bus_name(), '1', dss.bus_puvmagangle()[0]))
            vm_.append((dss.bus_name(), '3', dss.bus_puvmagangle()[2]))
            i += 1

    elif len(dss.bus_nodes()) == 3:
        vm_.append((dss.bus_name(), '1', dss.bus_puvmagangle()[0]))
        vm_.append((dss.bus_name(), '2', dss.bus_puvmagangle()[2]))
        vm_.append((dss.bus_name(), '3', dss.bus_puvmagangle()[4]))
        i += 1
    else:
        i += 1
i_ = 0
n_ = list()
while i_ <= len(vm_) - 1:
    kk = list(vm_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_Vminit_ = {}
while i_ <= len(vm_) - 1:
    _Vminit_[n_[i_]] = (vm_[i_])[2]
    i_ += 1

dictionary_[keys[24]] = _Vminit_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o 'Vainit' formato  {('A', 'a'): 0.0  ÂNGULO
i = 0
va_ = list()
while i <= len(dss.circuit_allbusnames()) - 1:
    dss.circuit_setactivebus(dss.circuit_allbusnames()[i])
    if len(dss.bus_nodes()) == 1:
        if dss.bus_nodes()[0] == 1:
            va_.append((dss.bus_name(), '1', math.radians(dss.bus_puvmagangle()[1])))
            i += 1
        elif dss.bus_nodes()[0] == 2:
            va_.append((dss.bus_name(), '2', math.radians(dss.bus_puvmagangle()[1])))
            i += 1
        elif dss.bus_nodes()[0] == 3:
            va_.append((dss.bus_name(), '3', math.radians(dss.bus_puvmagangle()[1])))
            i += 1
    elif len(dss.bus_nodes()) == 2:
        if dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
            va_.append((dss.bus_name(), '1', math.radians(dss.bus_puvmagangle()[1])))
            va_.append((dss.bus_name(), '2', math.radians(dss.bus_puvmagangle()[3])))
            i += 1
        elif dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
            va_.append((dss.bus_name(), '2', math.radians(dss.bus_puvmagangle()[1])))
            va_.append((dss.bus_name(), '3', math.radians(dss.bus_puvmagangle()[3])))
            i += 1
        elif dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
            va_.append((dss.bus_name(), '1', math.radians(dss.bus_puvmagangle()[1])))
            va_.append((dss.bus_name(), '3', math.radians(dss.bus_puvmagangle()[3])))
            i += 1

    elif len(dss.bus_nodes()) == 3:
        va_.append((dss.bus_name(), '1', math.radians(dss.bus_puvmagangle()[1])))
        va_.append((dss.bus_name(), '2', math.radians(dss.bus_puvmagangle()[3])))
        va_.append((dss.bus_name(), '3', math.radians(dss.bus_puvmagangle()[5])))
        i += 1
    else:
        i += 1
i_ = 0
n_ = list()
while i_ <= len(va_) - 1:
    kk = list(va_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_Vainit_ = {}
while i_ <= len(va_) - 1:
    _Vainit_[n_[i_]] = (va_[i_])[2]
    i_ += 1

dictionary_[keys[25]] = _Vainit_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o 'Capinit' formato  {('A', 'a'): 0.0 (*acho q é nesse formato)
# atenção, não sei se o estado do cap é mesmo este que usei no loop !
i = 0
cstates_ = list()
capbus_ = list()
if dss.capacitors_allnames()[0] != 'NONE':
    while i <= len(dss.capacitors_allnames()) - 1:
        dss.circuit_setactiveclass('Capacitor')
        dss.capacitors_write_name(dss.capacitors_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        capbus_.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para capacitor Mono
        # Para Bus.1 capacitor.1 ou Bus.2 capacitor.2 ou Bus.3 capacitor.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
                i += 1
            else:
                pass


        # Para capacitor Mono
        # Para Bus.1.2 capacitor.1  ou Bus.1.3 capacitor.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.2 capacitor.1  ou Bus.2.3 capacitor.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                cstates_.append((dss.bus_name(), '1', '0.0'))
                cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            # Para Bus.1.3 capacitor.3  ou Bus.2.3 capacitor.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                cstates_.append((dss.bus_name(), '1', '0.0'))
                cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                cstates_.append((dss.bus_name(), '2', '0.0'))
                cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
                i += 1
            else:
                pass


        # Para capacitor Mono
        # Para Bus.1.2.3 capacitor.1, capacitor.2, capacitor.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '2', '0.0'))
                cstates_.append((dss.bus_name(), '2', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', '0.0'))
                cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', '0.0'))
                cstates_.append((dss.bus_name(), '2', '0.0'))
                cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
                i += 1
            else:
                pass


        # Para capacitor Bi
        # Para Bus.1.2 capacitor.1.2 ou Bus.2.2 capacitor.2.2 ou Bus.1.3 capacitor.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
                i += 1
            else:
                pass


        # Para capacitor Bi
        # Para Bus.1.2.3 capacitor.1.2 ou Bus.1.2.3 capacitor.2.3 ou Bus.1.2.3 capacitor.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '3', '0.0'))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', '0.0'))
                cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
                cstates_.append((dss.bus_name(), '2', '0.0'))
                cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
                i += 1
            else:
                pass


        # Para capacitor Tri
        # Para Bus.1.2.3 capacitor.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            cstates_.append((dss.bus_name(), '1', dss.capacitors_read_states()[0]))
            cstates_.append((dss.bus_name(), '2', dss.capacitors_read_states()[0]))
            cstates_.append((dss.bus_name(), '3', dss.capacitors_read_states()[0]))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem capacitor________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(capbus_)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem capacitor a lista 'cstates_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        cstates_.append((dss.bus_name(), '1', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        cstates_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        cstates_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 2:
        cstates_.append((dss.bus_name(), '1', '0.0'))
        cstates_.append((dss.bus_name(), '2', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[1] == 3:
        cstates_.append((dss.bus_name(), '2', '0.0'))
        cstates_.append((dss.bus_name(), '3', '0.0'))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[1] == 3:
        cstates_.append((dss.bus_name(), '1', '0.0'))
        cstates_.append((dss.bus_name(), '3', '0.0'))

    elif len(dss.bus_nodes()) == 3:
        cstates_.append((dss.bus_name(), '1', '0.0'))
        cstates_.append((dss.bus_name(), '2', '0.0'))
        cstates_.append((dss.bus_name(), '3', '0.0'))
    i += 1
cstates_ = sorted(cstates_)
i_ = 0
n_ = list()
while i_ <= len(cstates_) - 1:
    kk = list(cstates_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_cstates_ = {}
while i_ <= len(cstates_) - 1:
    _cstates_[n_[i_]] = (cstates_[i_])[2]
    i_ += 1
dictionary_[keys[26]] = _cstates_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# 'Tapinit'
i_ = 0
tap_ = {}
if dss.regcontrols_allnames()[0] != 'NONE':
    while i_ <= len(dss.regcontrols_allnames()) - 1:
        dss.circuit_setactiveclass('Regcontrol')
        dss.circuit_setactiveelement(dss.regcontrols_allnames()[i_])
        dss.circuit_setactiveelement('Transformer.{}'.format(dss.dssproperties_read_value('1')))
        # sentido ij
        tap_[dss.cktelement_read_busnames()[0], dss.cktelement_read_busnames()[1], '1'] = float(
            dss.dssproperties_read_value('8'))
        tap_[dss.cktelement_read_busnames()[0], dss.cktelement_read_busnames()[1], '2'] = float(
            dss.dssproperties_read_value('8'))
        tap_[dss.cktelement_read_busnames()[0], dss.cktelement_read_busnames()[1], '3'] = float(
            dss.dssproperties_read_value('8'))
        # sentido ji
        # tap_[dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0], '1'] = float(dss.dssproperties_read_value('8'))
        # tap_[dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0], '2'] = float(dss.dssproperties_read_value('8'))
        # tap_[dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0], '3'] = float(dss.dssproperties_read_value('8'))
        i_ += 1
else:
    pass

dictionary_[keys[27]] = tap_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o 'BranchIRat' formato  ('D', 'B'): 0
i, i_ = 0, 0
aa = list()
bb = list()
branchirat = list()
while i <= len(dss.lines_allnames()) - 1:
    dss.circuit_setactiveclass('Line')
    dss.lines_write_name(dss.lines_allnames()[i])
    while i_ <= len(dss.cktelement_currentsmagang()) - 1:
        aa.append(dss.cktelement_currentsmagang()[i_])
        i_ += 2
    branchirat.append(((dss.cktelement_read_busnames()[0]).split('.')[0],
                       (dss.cktelement_read_busnames()[1]).split('.')[0],
                       max(aa) / dss.cktelement_read_emergamps()))
    i += 1
i, i_ = 0, 0
while i <= len(dss.transformers_allNames()) - 1:
    dss.circuit_setactiveclass('Transformer')
    dss.transformers_write_name(dss.transformers_allNames()[i])
    while i_ <= len(dss.cktelement_currentsmagang()) - 1:
        bb.append(dss.cktelement_currentsmagang()[i_])
        i_ += 2
    branchirat.append(((dss.cktelement_read_busnames()[0]).split('.')[0],
                       (dss.cktelement_read_busnames()[1]).split('.')[0],
                       max(bb) / dss.cktelement_read_emergamps()))
    i += 1

i_ = 0
n_ = list()
while i_ <= len(branchirat) - 1:
    kk = list(branchirat[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_branchirat_ = {}
while i_ <= len(branchirat) - 1:
    _branchirat_[n_[i_]] = (branchirat[i_])[2]
    i_ += 1
dictionary_[keys[28]] = _branchirat_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o 'BranchSRat', formato ('D', 'B'): 0
oo_ = list()
i_ = 0
while i_ <= len(dss.lines_allnames()) - 1:
    dss.circuit_setactiveclass('Line')
    dss.lines_write_name(dss.lines_allnames()[i_])
    oo_.append(((''.join(x for x in dss.lines_read_bus1() if x.isalpha())),
                (''.join(x for x in dss.lines_read_bus2() if x.isalpha())), '0.0'))
    i_ += 1
i_ = 0
while i_ <= len(dss.lines_allnames()) - 1:
    dss.circuit_setactiveclass('Line')
    dss.lines_write_name(dss.lines_allnames()[i_])
    oo_.append(((''.join(x for x in dss.lines_read_bus2() if x.isalpha())),
                (''.join(x for x in dss.lines_read_bus1() if x.isalpha())), '0.0'))
    i_ += 1
i_ = 0

while i_ <= len(dss.transformers_allNames()) - 1:
    dss.circuit_setactiveclass('Transformer')
    dss.transformers_write_name(dss.transformers_allNames()[i_])
    oo_.append(
        (dss.cktelement_read_busnames()[0], dss.cktelement_read_busnames()[1], dss.transformers_read_kva() / 1000))
    oo_.append((dss.cktelement_read_busnames()[1], dss.cktelement_read_busnames()[0], '0.0'))
    i_ += 1

oo_ = sorted(oo_)
i_ = 0
n_ = list()
while i_ <= len(oo_) - 1:
    kk = list(oo_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_00_ = {}
while i_ <= len(oo_) - 1:
    _00_[n_[i_]] = (oo_[i_])[2]
    i_ += 1
dictionary_[keys[29]] = oo_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o 'PVSrat' formato {'C': 0.22}
i = 0
pvbus_ = list()
if dss.pvsystems_allnames()[0] != 'NONE':
    while i <= len(dss.pvsystems_allnames()) - 1:
        dss.circuit_setactiveclass('PVSystem')
        dss.pvsystems_write_name(dss.pvsystems_allnames()[i])
        pvbus_.append(
            ((dss.cktelement_read_busnames()[0]).split('.')[0], int(dss.dssproperties_read_value('11')) / 1000))
        i += 1
else:
    pass
pvbus_ = sorted(pvbus_)
i_ = 0
n_ = list()
while i_ <= len(pvbus_) - 1:
    kk = list(pvbus_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_pvbus_ = {}
while i_ <= len(pvbus_) - 1:
    _pvbus_[(n_[i_])[0]] = (pvbus_[i_])[1]
    i_ += 1
dictionary_[keys[30]] = _pvbus_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o 'PVPlimit' formato  {'C': 0.2}
i = 0
PVPlimit_ = list()
if dss.pvsystems_allnames()[0] != 'NONE':
    while i <= len(dss.pvsystems_allnames()) - 1:
        dss.circuit_setactiveclass('PVSystem')
        dss.pvsystems_write_name(dss.pvsystems_allnames()[i])
        PVPlimit_.append(
            ((dss.cktelement_read_busnames()[0]).split('.')[0], int(dss.dssproperties_read_value('5')) / 1000))
        i += 1
else:
    pass
PVPlimit_ = sorted(PVPlimit_)
i_ = 0
n_ = list()
while i_ <= len(PVPlimit_) - 1:
    kk = list(PVPlimit_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_PVPlimit_ = {}
while i_ <= len(PVPlimit_) - 1:
    _PVPlimit_[(n_[i_])[0]] = (PVPlimit_[i_])[1]
    i_ += 1
dictionary_[keys[31]] = _PVPlimit_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# dss.circuit_setactivebus('newsource')
# # Neste ponto crio uma lista com Tensões da barra Newsource
# _vsource = list()
# _vsource.append((dss.bus_name(), '1', dss.bus_puvmagangle()[0]))
# _vsource.append((dss.bus_name(), '2', dss.bus_puvmagangle()[2]))
# _vsource.append((dss.bus_name(), '3', dss.bus_puvmagangle()[4]))
#
# i_ = 0
# n_ = list()
# while i_ <= len(_vsource) - 1:
#     kk = list(_vsource[i_])
#     n_.append((kk[0], kk[1]))
#     i_ += 1
#
# i_ = 0
# _vsource_ = {}
# while i_ <= len(_vsource) - 1:
#     _vsource_[n_[i_]] = (_vsource[i_])[2]
#     i_ += 1
dictionary_[keys[32]] = 'NONE'
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# Neste ponto crio uma lista com ângulos da barra Newsource
# dss.circuit_setactivebus('newsource')
# _angsource = list()
# _angsource.append((dss.bus_name(), '1', math.radians(dss.bus_puvmagangle()[1])))
# _angsource.append((dss.bus_name(), '2', math.radians(dss.bus_puvmagangle()[3])))
# _angsource.append((dss.bus_name(), '3', math.radians(dss.bus_puvmagangle()[5])))
#
# i_ = 0
# n_ = list()
# while i_ <= len(_angsource) - 1:
#     kk = list(_angsource[i_])
#     n_.append((kk[0], kk[1]))
#     i_ += 1
#
# i_ = 0
# _angsource_ = {}
# while i_ <= len(_angsource) - 1:
#     _angsource_[n_[i_]] = (_angsource[i_])[2]
#     i_ += 1
dictionary_[keys[33]] = 'NONE'
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# dss.circuit_setactiveclass('Line')
# dss.lines_write_name('NEWSOURCE')
# dss.circuit_setactivebus('newsource')
# # Neste ponto crio uma lista com as Condutâncias em p.u. da barra Newsource
# _Gsource = list()
# _Gsource.append(('newsource', '1', ((dss.lines_read_yprim()[0])*(dss.bus_puvmagangle()[0])**2)/1e8))
# _Gsource.append(('newsource', '2', ((dss.lines_read_yprim()[0])*(dss.bus_puvmagangle()[2])**2)/1e8))
# _Gsource.append(('newsource', '3', ((dss.lines_read_yprim()[0])*(dss.bus_puvmagangle()[4])**2)/1e8))
#
# i_ = 0
# n_ = list()
# while i_ <= len(_Gsource) - 1:
#     kk = list(_Gsource[i_])
#     n_.append((kk[0], kk[1]))
#     i_ += 1
#
# i_ = 0
# _Gsource_ = {}
# while i_ <= len(_Gsource) - 1:
#     _Gsource_[n_[i_]] = (_Gsource[i_])[2]
#     i_ += 1
dictionary_[keys[34]] = 'NONE'
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# Neste ponto crio uma lista com as Condutâncias em p.u. da barra Newsource
# _Bsource = list()
# _Bsource.append(('newsource', '1', ((dss.lines_read_yprim()[1])*(dss.bus_puvmagangle()[0])**2)/1e8))
# _Bsource.append(('newsource', '2', ((dss.lines_read_yprim()[1])*(dss.bus_puvmagangle()[2])**2)/1e8))
# _Bsource.append(('newsource', '3', ((dss.lines_read_yprim()[1])*(dss.bus_puvmagangle()[4])**2)/1e8))
#
# i_ = 0
# n_ = list()
# while i_ <= len(_Bsource) - 1:
#     kk = list(_Bsource[i_])
#     n_.append((kk[0], kk[1]))
#     i_ += 1
#
# i_ = 0
# _Bsource_ = {}
# while i_ <= len(_Bsource) - 1:
#     _Bsource_[n_[i_]] = (_Bsource[i_])[2]
#     i_ += 1
# dictionary_[keys[35]] = _Bsource_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# sourcebusphase = (('newsource', '1'), ('newsource', '2'), ('newsource', '3'))
dictionary_[keys[36]] = 'NONE'
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# nesta etapa crio o Pinjinit formato  {('A', 'a'): 0.0
i = 0
Pinjinit_ = list()
pinloadsbuses = list()
if dss.loads_allnames()[0] != 'NONE':
    while i <= len(dss.loads_allnames()) - 1:
        dss.circuit_setactiveclass('Load')
        dss.loads_write_name(dss.loads_allnames()[i])
        dss.circuit_setactivebus((dss.cktelement_read_busnames()[0]).split('.')[0])
        pinloadsbuses.append((dss.cktelement_read_busnames()[0]).split('.')[0])
        # Para Carga Mono
        # Para Bus.1 Load.1 ou Bus.2 Load.2 ou Bus.3 Load.3
        if len(dss.bus_nodes()) == 1:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1


        # Para Carga Mono
        # Para Bus.1.2 Load.1  ou Bus.1.3 Load.1
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 2:
                Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '2', 0.0))
                i += 1
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '3', 0.0))
                i += 1
            # Para Bus.1.2 Load.1  ou Bus.2.3 Load.2
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                Pinjinit_.append((dss.bus_name(), '1', 0.0))
                Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1
            if re.findall('2' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[1] == 3:
                Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '3', 0.0))
                i += 1
            # Para Bus.1.3 Load.3  ou Bus.2.3 Load.3
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 1:
                Pinjinit_.append((dss.bus_name(), '1', 0.0))
                Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1
            if re.findall('3' + '+', str(dss.cktelement_read_busnames())) and dss.bus_nodes()[0] == 2:
                Pinjinit_.append((dss.bus_name(), '2', 0.0))
                Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1


        # Para Carga Mono
        # Para Bus.1.2.3 Load.1, Load.2, Load.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 3:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '2', 0.0))
                Pinjinit_.append((dss.bus_name(), '2', 0.0))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', 0.0))
                Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '3', 0.0))
                i += 1
            elif re.findall('3' + '+', str(dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', 0.0))
                Pinjinit_.append((dss.bus_name(), '2', 0.0))
                Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1


        # Para Carga Bi
        # Para Bus.1.2 Load.1.2 ou Bus.2.2 Load.2.2 ou Bus.1.3 Load.1.3
        elif len(dss.bus_nodes()) == 2 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1


        # Para Carga Bi
        # Para Bus.1.2.3 Load.1.2 ou Bus.1.2.3 Load.2.3 ou Bus.1.2.3 Load.1.3
        elif len(dss.bus_nodes()) == 3 and len(list(dss.cktelement_read_busnames()[0])) == 5:
            if re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('2' + '+', str(
                    dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '3', 0.0))
                i += 1
            elif re.findall('2' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', 0.0))
                Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1
            elif re.findall('1' + '+', str(dss.cktelement_read_busnames())) and re.findall('3' + '+', str(
                    dss.cktelement_read_busnames())):
                Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
                Pinjinit_.append((dss.bus_name(), '2', 0.0))
                Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
                i += 1


        # Para Carga Tri
        # Para Bus.1.2.3 Load.1.2.3
        elif (len(dss.cktelement_read_busnames()[0])) == 1:
            Pinjinit_.append((dss.bus_name(), '1', -1 * dss.cktelement_powers()[0] / 1000))
            Pinjinit_.append((dss.bus_name(), '2', -1 * dss.cktelement_powers()[0] / 1000))
            Pinjinit_.append((dss.bus_name(), '3', -1 * dss.cktelement_powers()[0] / 1000))
            i += 1

        else:
            i += 1

else:
    pass

# Loop para encontrar barras sem Loads________________________________________________________
diff__ = Counter(dss.circuit_allbusnames()) - Counter(pinloadsbuses)
diff__ = list(diff__.elements())
# ______________________________________________________________________________________________
# Loop para adicionar barras sem Loads a lista 'Pinjinit_'
i = 0
while i <= len(diff__) - 1:
    dss.circuit_setactivebus(diff__[i])
    bus_nodes = dss.bus_nodes()
    if len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 1:
        Pinjinit_.append((dss.bus_name(), 1, 0.0))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 2:
        Pinjinit_.append((dss.bus_name(), 2, 0.0))
    elif len(dss.bus_nodes()) == 1 and dss.bus_nodes()[0] == 3:
        Pinjinit_.append((dss.bus_name(), 3, 0.0))

    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[0] == 2:
        Pinjinit_.append((dss.bus_name(), 1, 0.0))
        Pinjinit_.append((dss.bus_name(), 2, 0.0))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 2 and dss.bus_nodes()[0] == 3:
        Pinjinit_.append((dss.bus_name(), 2, 0.0))
        Pinjinit_.append((dss.bus_name(), 3, 0.0))
    elif len(dss.bus_nodes()) == 2 and dss.bus_nodes()[0] == 1 and dss.bus_nodes()[0] == 3:
        Pinjinit_.append((dss.bus_name(), 1, 0.0))
        Pinjinit_.append((dss.bus_name(), 3, 0.0))

    elif len(dss.bus_nodes()) == 3:
        Pinjinit_.append((dss.bus_name(), 1, 0.0))
        Pinjinit_.append((dss.bus_name(), 2, 0.0))
        Pinjinit_.append((dss.bus_name(), 3, 0.0))
    i += 1
Pinjinit_ = sorted(Pinjinit_)
i_ = 0
n_ = list()
while i_ <= len(Pinjinit_) - 1:
    kk = list(Pinjinit_[i_])
    n_.append((kk[0], kk[1]))
    i_ += 1

i_ = 0
_Pinjinit_ = {}
while i_ <= len(Pinjinit_) - 1:
    _Pinjinit_[n_[i_]] = (Pinjinit_[i_])[2]
    i_ += 1
dictionary_[keys[37]] = _Pinjinit_
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________


# ______PYOMO_SETTINGS______
model = pyo.ConcreteModel()
# ___SETs___ 00:00 ~ 0:50 - (áudio 21.02.21)
# Barras
model.bus = pyo.Set(initialize=dictionary_['Buses'], ordered=True)
# Phases
model.Phases = pyo.Set(initialize=dictionary_['Phases'], ordered=True)

# Branch_domain
model.Branch_domain = pyo.Set(initialize=model.bus * model.bus, within=model.bus * model.bus, ordered=True)
# Seguimentos (Branches)
model.branches = pyo.Set(initialize=dictionary_['Branches'], domain=model.Branch_domain, ordered=True)

# BranchPhase_domain
model.BranchPhase_domain = pyo.Set(initialize=model.branches * model.Phases, within=model.branches * model.Phases,
                                   ordered=True)
# BranchPhase
model.BranchPhase = pyo.Set(initialize=dictionary_['BranchPhase'], within=model.BranchPhase_domain, ordered=True)

# BusPhase_domain
model.BusPhase_domain = pyo.Set(initialize=model.bus * model.Phases, within=model.bus * model.Phases, ordered=True)
# BusPhase
model.BusPhase = pyo.Set(initialize=dictionary_['BusPhase'], within=model.BusPhase_domain, ordered=True)

# Barras dos capacitores
model.CapBus = pyo.Set(initialize=dictionary_['CapBus'], within=model.bus, ordered=True)
# CapBusCont
model.CapBusCont = pyo.Set(initialize=dictionary_['CapBusCont'], within=model.CapBus, ordered=True)

# DSSSourceBus
model.DSSSourceBus = pyo.Set(initialize=dictionary_['DSSSourceBus'], within=model.bus, ordered=True)

# G_index
# model.G_index = pyo.Set(initialize=model.BusPhase*model.BusPhase, within=model.BusPhase*model.BusPhase, ordered=True)
# B_index
# model.B_index = pyo.Set(initialize=model.BusPhase*model.BusPhase, within=model.BusPhase*model.BusPhase, ordered=True)

# Barras de PVs
model.PVBus = pyo.Set(initialize=dictionary_['PVBus'], within=model.bus, ordered=True)
# PVBusCont
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# PriBus
model.PriBus = pyo.Set(initialize=dictionary_['PriBuses'], within=model.bus, ordered=True)

# Seguimentos reguladores
model.RegBranch = pyo.Set(initialize=dictionary_['RegBranch'], within=model.BranchPhase, ordered=True)
# RegBranchCont # ATENÇÃO: ESTE SET NÃO ESTÁ DESCRITO NOS SET'S DO PAULO / PORTANTO NÃO ESTÁ CONTEMPLADO NOS LOOPS
# model.RegBranchCont = pyo.Set(initialize=dictionary_['RegBranch'], within=model.RegBranch, ordered=True)

# RegGanged
model.RegGanged = pyo.Set(initialize=dictionary_['RegGanged'], within=model.branches, ordered=True)

# SourceBus
model.SourceBus = pyo.Set(initialize=dictionary_['SourceBus'], ordered=True)
# SourceVa_def_index
model.SourceVa_def_index = pyo.Set(initialize=model.SourceBus * model.Phases, within=model.SourceBus * model.Phases,
                                   ordered=True)

# ___PARAMs___ 00:50 ~ 01:45 - (áudio 21.02.21)
# Impedâncias dos seguimentos
model.G = pyo.Param(model.BusPhase, model.BusPhase, initialize=dictionary_['G'])
model.B = pyo.Param(model.BusPhase, model.BusPhase, initialize=dictionary_['B'])
# Corrente máxima dos seguimentos
model.branchirat = pyo.Param(model.branches, initialize=dictionary_['BranchIRat'])

# PVPlimit
# VERIFICAR SE PRECISA DISTO !
# PVSrat
# VERIFICAR SE PRECISA DISTO !

# Barras com geração P e Q
model.Pgen = pyo.Param(model.BusPhase, initialize=dictionary_['Pgen'], mutable=True)
model.Qgen = pyo.Param(model.BusPhase, initialize=dictionary_['Qgen'], mutable=True)

# Barras com cargas P e Q
model.Pload = pyo.Param(model.BusPhase, initialize=dictionary_['Pload'], mutable=True)
model.Qload = pyo.Param(model.BusPhase, initialize=dictionary_['Qload'], mutable=True)

# # Barras com capacitores Q
model.Qcap = pyo.Param(model.BusPhase, initialize=dictionary_['Qcap'], mutable=True)

# Max S do PV
model.PVSrat = pyo.Param(model.PVBus, initialize=dictionary_['PVSrat'])
# Max P do PV
model.PVPlimit = pyo.Param(model.PVBus, initialize=dictionary_['PVPlimit'])

# # Impedâncias da barra newsource (Atenção: Não tenho ctz deste param)
# model.Gsource = pyo.Param(model.sourcebusphase, initialize=dictionary_['Gsource'])
# model.Bsource = pyo.Param(model.sourcebusphase, initialize=dictionary_['Bsource'])
# # Tensões da barra newsource (Atenção: Não tenho ctz deste param)
# model.vsource_ = pyo.Param(model.sourcebusphase, initialize=dictionary_['Vsource'])
# # Ângulos da barra newsource (Atenção: Não tenho ctz deste param)
# model.angsource = pyo.Param(model.sourcebusphase, initialize=dictionary_['ANGsource'])


# ___VARs___
# Variáveis de estado
model.Pinj = pyo.Var(model.BusPhase, initialize=dictionary_['Pinjinit'])
model.Qinj = pyo.Var(model.BusPhase, initialize=dictionary_['Qinjinit'])


def __define_power_flow_init(dictionary_, model):
    # Cálculo do Pflowinit e Qflowinit
    i, j, p, d = 0, 0, 0, 0
    Pflowinit = {a: 0.0 for a in model.BranchPhase}
    Qflowinit = {a: 0.0 for a in model.BranchPhase}

    for i, j, p in Pflowinit:
        if (i, j, p) in dictionary_['RegBranch']:
            Pflowinit[i, j, p] = -sum(
            (dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
             math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d]) +
             dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
             math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d])) +
            (-dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
             math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d]) -
             dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
             math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d])) / dictionary_['Tapinit'][i, j, p] for
            d in dictionary_['Phases'] if (i, j, d) in dictionary_['BranchPhase'] and (i, p, j, d) in dictionary_['G'])

            Qflowinit[i, j, p] = -sum(
                (-dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d]) +
                 dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d])) +
                (dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d]) -
                 dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d])) / dictionary_['Tapinit'][i, j, p] for
                d in dictionary_['Phases'] if (i, j, d) in dictionary_['BranchPhase'] and (i, p, j, d) in dictionary_['G'])

        elif (j, i, p) in dictionary_['RegBranch']:
            Pflowinit[i, j, p] = -sum(
                (dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d]) +
                 dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d])) / dictionary_['Tapinit'][j, i, p] *
                dictionary_['Tapinit'][j, i, p] +
                (-dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d]) -
                 dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d])) / dictionary_['Tapinit'][j, i, p] for
                d in dictionary_['Phases'] if (i, j, d) in dictionary_['BranchPhase'] and (i, p, j, d) in dictionary_['G'])

            Qflowinit[i, j, p] = -sum(
                (-dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d]) +
                 dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d])) / dictionary_['Tapinit'][j, i, p] *
                dictionary_['Tapinit'][j, i, p] +
                (dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d]) -
                 dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d])) / dictionary_['Tapinit'][j, i, p] for
                d in dictionary_['Phases'] if (i, j, d) in dictionary_['BranchPhase'] and (i, p, j, d) in dictionary_['G'])
        else:
            Pflowinit[i, j, p] = -sum(
                (dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d]) +
                 dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d])) +
                (-dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d]) -
                 dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d]))
                for d in dictionary_['Phases'] if (i, j, d) in dictionary_['BranchPhase'] and (i, p, j, d) in dictionary_['G'])

            Qflowinit[i, j, p] = -sum(
                (-dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d]) +
                 dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][i, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][i, d])) +
                (dictionary_['B'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.cos(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d]) -
                 dictionary_['G'][(i, p), (j, d)] * dictionary_['Vminit'][i, p] * dictionary_['Vminit'][j, d] *
                 math.sin(dictionary_['Vainit'][i, p] - dictionary_['Vainit'][j, d]))
                for d in dictionary_['Phases'] if (i, j, d) in dictionary_['BranchPhase'] and (i, p, j, d) in dictionary_['G'])
    return Pflowinit, Qflowinit


Pflowinit, Qflowinit = __define_power_flow_init(dictionary_, model)
model.Pflow = pyo.Var(model.BranchPhase, initialize=Pflowinit)
model.Qflow = pyo.Var(model.BranchPhase, initialize=Qflowinit)

model.Vm = pyo.Var(model.BusPhase, initialize=dictionary_['Vminit'], bounds=(0.5, 1.5))
model.Va = pyo.Var(model.BusPhase, initialize=dictionary_['Vainit'])

# Variáveis de controle
model.CapState = pyo.Var(model.CapBus, initialize=dictionary_['Capinit'])
model.Tap = pyo.Var(model.RegBranch, initialize=dictionary_['Tapinit'],
                    bounds=(-16, 16))  # Verificar a relação entre tapMAx = 1.1, tapMAx = 0.9
model.Ppv = pyo.Var(model.BusPhase, initialize=dictionary_['Ppv'])
model.Qpv = pyo.Var(model.BusPhase, initialize=dictionary_['Qpv'])

# # Tensões
# model.Vm = pyo.Var(model.busphase, initialize=dictionary_['Vminit'], bounds=(0.5, 1.5))
# # angulos
# model.Va = pyo.Var(model.busphase, initialize=dictionary_['Vainit'], bounds=(-2.2, 2.2))
# # phases
# # model.Phase = pyo.Var(model.phases, initialize=dictionary_['Phases'])
# # Pinj
# model.Pinj = pyo.Var(model.busphase, initialize=dictionary_['Pinjinit'], bounds=(-0.5, 1.5))
# # Qinj
# model.Qinj = pyo.Var(model.busphase, initialize=dictionary_['Qinjinit'], bounds=(-0.5, 1.5))

# Pbranch
# model.Qflowinit = pyo.Var()

# Qbranch
# model.Qbranchflow = pyo.Var(model.regbranch, )


# Variáveis de controle
# Posição do regulador
# model.Qbranch = pyo.Var()
# Status do Cap
# model.Qbranch = pyo.Var()
# Potência das GDs
# model.Qbranch = pyo.Var()

# ___CONSTRAINTs___
# 1º Lei de kirchoff
# P
# Q


# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________
# ______________________________________________________________________________________________

# model.Pflowinit.pprint()
#
for key, value in Pflowinit.items():
    print(key, ":", value)

print('here')