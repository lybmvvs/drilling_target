import numpy as np
import pandas as pd
import datetime
import random
import missingno as msno
import statistics
import numpy as np
import matplotlib.pyplot as plt

cordinates = pd.read_excel('new_well_info.xlsx',header=[0],index_col=[0])
cordinates=cordinates.drop(['Thickness, meters','Effective thickness, meters','Depth, meters'],axis=1)

inj_wells = pd.read_excel('new_injection_td.xlsx',header=[0],index_col=[0])

inj_wells.reset_index(inplace=True)

inj_wells_new=inj_wells.groupby(by=['Well']).sum()

inj_wells_new.reset_index(inplace=True)

inj_cord = inj_wells_new.merge(cordinates, on='Well')
w_inj=inj_cord['Well'].tolist()
w_inj_x=inj_cord['Coordinate X'].tolist()
w_inj_y=inj_cord['Coordinate Y'].tolist()
w_inj_names=inj_cord['Well'].tolist()

prod_wells_cord = pd.read_excel('DIPLOM_first_step.xlsx',header=[0],index_col=[0])

w_prod_names=prod_wells_cord['Well'].tolist()
w_prod_x=prod_wells_cord['Coordinate X'].tolist()
w_prod_y=prod_wells_cord['Coordinate Y'].tolist()

fig,ax=plt.subplots()
ax.scatter(w_prod_x, w_prod_y,color = 'black', label = "prod")


ax.scatter(w_inj_x,w_inj_y,color = 'blue', label = "inj")

w_new_BP12_names=['BP12_1','BP12_2','BP12_3']
w_new_x_BP12=[596281.73637649, 591121.25968044, 592512.84890185]
w_new_y_BP12=[7094619.5894348, 7088038.5320753, 7083283.9355688]
ax.scatter(w_new_x_BP12,w_new_y_BP12,color = 'red', label = "new_BP12")
for i, txt in enumerate(w_new_BP12_names):
    ax.annotate(txt, (w_new_x_BP12[i], w_new_y_BP12[i]))

w_new_BP17_name=['BP17_1']
w_new_x_BP17=[588844.34789335]
w_new_y_BP17=[7068075.6849254]
ax.scatter(w_new_x_BP17,w_new_y_BP17,color = 'green', label = "new_BP17")
for i, txt in enumerate(w_new_BP17_name):
    ax.annotate(txt, (w_new_x_BP17[i], w_new_y_BP17[i]))

w_new_U1_names=['U1_1','U1_2']
w_new_x_U1=[592659.08047875,591033.60099798]
w_new_y_U1=[7087608.954304,7070152.4103242]
ax.scatter(w_new_x_U1,w_new_y_U1,color = 'yellow', label = "new_U1")
for i, txt in enumerate(w_new_U1_names):
    ax.annotate(txt, (w_new_x_U1[i], w_new_y_U1[i]))

w_new_BP_names=['BP_11_0_1','BP_11_1_1']
w_new_BP_names_1=['BP_11_0_2','BP_11_1_2']
new_x_BPfirst,new_y_BPfirst=[591466.6283196,592455.91310057],[7089237.0322519,7088876.4521449]
new_x_BPsecond,new_y_BPsecond=[591040.60037612,591106.11354923],[7077819.4833667,7078078.0557343]
ax.plot(new_x_BPfirst,new_y_BPfirst,new_x_BPsecond,new_y_BPsecond,marker='o',color = 'orange',label = "new_BP")
for i, txt in enumerate(w_new_BP_names):
    ax.annotate(txt, (new_x_BPfirst[i], new_y_BPfirst[i]))
for i, txt in enumerate(w_new_BP_names_1):
    ax.annotate(txt, (new_x_BPsecond[i], new_y_BPsecond[i]))

plt.legend()
plt.show()
