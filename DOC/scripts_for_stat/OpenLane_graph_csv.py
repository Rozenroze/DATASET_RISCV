import re
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd


def find_power(text_addr, str_val):
    with open(text_addr) as text:
        for line in text:
            if str_val in line:
                result = (re.findall(r'(\d+.\d+e-\d+)', line))
    return result


def find_value(text_addr, str_val, format):
    #  format:
    #       1 - float value
    #       0 - fixed value
    with open(text_addr) as text:
        for line in text:
            if str_val in line:
                if format == 1:
                    result = float(re.findall(r'(\d+.\d+)', line)[0])
                else:
                    result = int(re.findall(r'(\d+)', line)[0])
    return result




num_cores = 4
num_configs: int = 8
addr = np.array([]).astype(str)
folder_addr = "C:/Users/iliak/OneDrive/Рабочий стол/DATASET/"
addr = np.append(addr, "school_riscv")
addr = np.append(addr, "ultraembedded_riscv")
addr = np.append(addr, "ultraembedded_biriscv")
addr = np.append(addr, "ssrv")
plt.rcParams['figure.figsize'] = [15, 18]
for j in range(0, num_cores):
    core_area_array = np.array([])
    total_cell_array = np.array([])
    nonphyscell_array = np.array([])
    fillcell_array = np.array([])
    diodecell_array = np.array([])
    welltapcell_array = np.array([])
    decapcells_array = np.array([])
    tns_array = np.array([])
    wns_array = np.array([])
    internal_power_array = np.array([])
    switching_power_array = np.array([])
    total_power_array = np.array([])
    
    

    for i in range(1, num_configs + 1, +1):
        tmp = pd.read_csv(folder_addr + addr[j] + '/OpenLane/runs/' + str(i) + '/reports/metrics.csv')
        core_area_array = np.append(core_area_array, tmp['CoreArea_um^2'].tolist()[0])

        total_cell_array = np.append(total_cell_array, tmp['TotalCells'].tolist()[0])
        nonphyscell_array = np.append(nonphyscell_array, tmp['NonPhysCells'].tolist()[0])
        fillcell_array = np.append(fillcell_array, tmp['FillCells'].tolist()[0])
        diodecell_array = np.append(diodecell_array, tmp['DiodeCells'].tolist()[0])
        welltapcell_array = np.append(welltapcell_array, tmp['WelltapCells'].tolist()[0])
        decapcells_array = np.append(decapcells_array, tmp['DecapCells'].tolist()[0])
        tns_array = np.append(tns_array, abs(tmp['tns'].tolist()[0]))
        wns_array = np.append(wns_array, abs(tmp['wns'].tolist()[0]))
    print(core_area_array)

    ########### AREA_GRAPH ##########
    area = plt.subplot2grid((3, 2), (0, 0), colspan=1)
    X_AXIS = np.arange(1, num_configs + 1, 1)
    bw = 0.2
    area.set_title('AREA', fontsize=20)
    area.bar(X_AXIS, core_area_array, color='b', label='CoreArea_um^2')
    area.set_xticks(X_AXIS, X_AXIS.astype(str))
    area.legend(loc='best', ncol=4, fancybox=True, shadow=True,
                fontsize='xx-small')
    area.set_xlabel('Номер вариации параметров')
    area.set_ylabel('Квадратные микрометры')

    ########### LEAF_CELL_GRAPH ##########
    bw = 0.15
    cell = plt.subplot2grid((3, 2), (0, 1), colspan=2)
    cell.set_title('CELL COUNT', fontsize=20)
    cell.bar(X_AXIS, total_cell_array, bw, color='firebrick', label='TotalCells')
    cell.bar(X_AXIS + 1 * bw, nonphyscell_array, bw, color='saddlebrown', label='NonPhysCells')
    cell.bar(X_AXIS + 2 * bw, welltapcell_array, bw, color='orange', label='WelltapCells')
    cell.bar(X_AXIS + 3 * bw, fillcell_array, bw, color='forestgreen', label='FillCells')
    cell.bar(X_AXIS + 4 * bw, diodecell_array, bw, color='chocolate', label='DiodeCells')
    cell.bar(X_AXIS + 5 * bw, decapcells_array, bw, color='olive', label='DecapCells')
    cell.set_xticks(X_AXIS + 2 * bw, X_AXIS.astype(str))
    cell.legend(loc='best', ncol=6, fancybox=True, shadow=True,
                fontsize='xx-small')
    cell.set_xlabel('Номер вариации параметров')
    cell.set_ylabel('Количество логических элементов')

    ########## TIMING_GRAPH ##########
    timing_tns = plt.subplot2grid((3, 2), (1, 0), colspan=1)
    timing_tns.set_title('TNS', fontsize=20)
    timing_tns.bar(X_AXIS, tns_array, bw, color='r', label='TNS')
    timing_tns.set_xticks(X_AXIS + 1 * bw, X_AXIS.astype(str))
    timing_tns.set_xlabel('Номер вариации параметров')
    timing_tns.set_ylabel('Наносекунды')
    timing_wns = plt.subplot2grid((3, 2), (1, 1), colspan=1)
    timing_wns.set_title('WNS', fontsize=20)
    timing_wns.bar(X_AXIS + bw, wns_array, bw, color='y', label='WNS')
    timing_wns.set_xticks(X_AXIS + 1 * bw, X_AXIS.astype(str))
    timing_wns.set_xlabel('Номер вариации параметров')
    timing_wns.set_ylabel('Наносекунды')

    ########## POWER_GRAPH ##########
    for i in range(1, num_configs + 1, +1):
        tmp = find_power(folder_addr + addr[j] + '/OpenLane/runs/' + str(i) + '/reports/synthesis/2-syn_sta.power.rpt', 'Total')
        internal_power_array = np.append(internal_power_array, tmp[0])
        switching_power_array = np.append(switching_power_array, tmp[1])
        total_power_array = np.append(total_power_array, tmp[3])

    power = plt.subplot2grid((3, 2), (2, 0), colspan=2)
    power.set_title('POWER', fontsize=20)
    power.bar(X_AXIS, total_power_array.astype(float)*10**6, bw, color='b', label='Total power')
    power.bar(X_AXIS + bw, internal_power_array.astype(float)*10**6, bw, color='y', label='Internal power')
    power.bar(X_AXIS + 2 * bw, switching_power_array.astype(float)*10**6, bw, color='g', label='Switching power')
    power.set_xticks(X_AXIS + 1 * bw, X_AXIS.astype(str))
    power.legend(loc='best', ncol=4, fancybox=True, shadow=True,
                 fontsize='xx-small')
    power.set_xlabel('Номер вариации параметров')
    power.set_ylabel('МикроВатты')
    addr_arr = addr[j].split("/")
    name_core = addr_arr[len(addr_arr) - 2]
    plt.savefig('openlane_graph_' + addr[j] + '.png')
    plt.show()


    
