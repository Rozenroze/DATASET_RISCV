import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def find_point(text_addr, str_val, format):
    #  format:
    #       1 - float value
    #       0 - fixed value
    with open(text_addr) as text:
        for line in text:
            if str_val in line:
                result = (re.findall(r'(\w+)', line)[5])
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


num_cores = 7
num_configs_dc: int = 11
addr = np.array([]).astype(str)
addr = np.append(addr, "C:/Users/iliak/OneDrive/Рабочий стол/DATASET/ultraembedded_biriscv/DC")
addr = np.append(addr, "C:/Users/iliak/OneDrive/Рабочий стол/DATASET/ultraembedded_riscv/DC")
addr = np.append(addr, "C:/Users/iliak/OneDrive/Рабочий стол/DATASET/school_riscv/DC")
addr = np.append(addr, "C:/Users/iliak/OneDrive/Рабочий стол/DATASET/dark_riscv/DC")
addr = np.append(addr, "C:/Users/iliak/OneDrive/Рабочий стол/DATASET/ssrv/DC")
addr = np.append(addr, "C:/Users/iliak/OneDrive/Рабочий стол/DATASET/steel_core/DC")
addr = np.append(addr, "C:/Users/iliak/OneDrive/Рабочий стол/DATASET/vex_riscv/DC")
plt.rcParams['figure.figsize'] = [15, 18]
for j in range(0, num_cores):
    area = plt.subplot2grid((3, 2), (0, 0), colspan=1)
    ########### AREA_GRAPH ##########                                                                                                                                                                                                             
    total_cell_area_array = np.array([])
    comb_area_array = np.array([])
    seq_area_array = np.array([])
    buff_area_array = np.array([])

    str_total_cell_area = 'Total cell area:'
    str_comb_area = 'Combinational area:'
    str_seq_area = 'Noncombinational area:'
    str_buff_area = 'Buf/Inv area:'

    for i in range(1, num_configs_dc + 1, +1):
        total_cell_area_array = np.append(total_cell_area_array,
                                          find_value(addr[j] + '/' + str(i) + '/report_area.log', str_total_cell_area,
                                                     1))
        comb_area_array = np.append(comb_area_array,
                                    find_value(addr[j] + '/' + str(i) + '/report_area.log', str_comb_area, 1))
        seq_area_array = np.append(seq_area_array,
                                   find_value(addr[j] + '/' + str(i) + '/report_area.log', str_seq_area, 1))
        buff_area_array = np.append(buff_area_array,
                                    find_value(addr[j] + '/' + str(i) + '/report_area.log', str_buff_area, 1))
    print(total_cell_area_array)
    print((22571.471907-17450.159763)/22571.471907)

    X_AXIS = np.arange(1, num_configs_dc + 1, 1)
    # print(X_AXIS.astype(str))
    bw = 0.2
    area.set_title('AREA', fontsize=20)
    area.bar(X_AXIS, total_cell_area_array, bw, color='b', label=str_total_cell_area)
    area.bar(X_AXIS + bw, comb_area_array, bw, color='y', label=str_comb_area)
    area.bar(X_AXIS + 2 * bw, seq_area_array, bw, color='r', label=str_seq_area)
    area.bar(X_AXIS + 3 * bw, buff_area_array, bw, color='g', label=str_buff_area)
    area.set_xticks(X_AXIS + 1 * bw, X_AXIS.astype(str))
    area.legend(loc='best', ncol=4, fancybox=True, shadow=True,
                fontsize='xx-small')
    area.set_xlabel('Номер вариации параметров')
    area.set_ylabel('Квадратные микрометры')
    ########### LEAF_CELL_GRAPH ##########
    leaf_cell_count_array = np.array([])
    comb_cell_count_array = np.array([])
    seq_cell_count_array = np.array([])
    buff_cell_count_array = np.array([])

    str_leaf_cell_count = 'Leaf Cell Count:'
    str_buff_cell_count = '  Buf/Inv Cell Count:'
    str_comb_cell_count = 'Combinational Cell Count:'
    str_seq_cell_count = 'Sequential Cell Count:'

    for i in range(1, num_configs_dc + 1, +1):
        leaf_cell_count_array = np.append(leaf_cell_count_array,
                                          find_value(addr[j] + '/' + str(i) + '/report_qor.log', str_leaf_cell_count,
                                                     0))
        comb_cell_count_array = np.append(comb_cell_count_array,
                                          find_value(addr[j] + '/' + str(i) + '/report_qor.log', str_comb_cell_count,
                                                     0))
        seq_cell_count_array = np.append(seq_cell_count_array,
                                         find_value(addr[j] + '/' + str(i) + '/report_qor.log', str_seq_cell_count, 0))
        buff_cell_count_array = np.append(buff_cell_count_array,
                                          find_value(addr[j] + '/' + str(i) + '/report_qor.log', str_buff_cell_count,
                                                     0))
    # print(leaf_cell_count_array)
    cell = plt.subplot2grid((3, 2), (0, 1), colspan=1)
    cell.set_title('CELL COUNT', fontsize=20)
    cell.bar(X_AXIS, leaf_cell_count_array, bw, color='b', label=str_leaf_cell_count)
    cell.bar(X_AXIS + bw, comb_cell_count_array, bw, color='y', label=str_comb_cell_count)
    cell.bar(X_AXIS + 2 * bw, seq_cell_count_array, bw, color='r', label=str_seq_cell_count)
    cell.bar(X_AXIS + 3 * bw, buff_cell_count_array, bw, color='g', label=str_buff_cell_count)
    cell.set_xticks(X_AXIS + 1 * bw, X_AXIS.astype(str))
    cell.legend(loc='best', ncol=4, fancybox=True, shadow=True,
                fontsize='xx-small')
    cell.set_xlabel('Номер вариации параметров')
    cell.set_ylabel('Количество логических элементов')
    ########### TIMING_GRAPH ##########
    tns_array = np.array([])
    wns_array = np.array([])

    str_tns = 'Total Hold Violation:'
    str_wns = 'Worst Hold Violation:'
    str_slack = 'slack (MET)'

    for i in range(1, num_configs_dc + 1, +1):
        tns_array = np.append(tns_array,
                              find_value(addr[j] + '/' + str(i) + '/report_qor.log', str_tns,
                                         1))
        wns_array = np.append(wns_array,
                              find_value(addr[j] + '/' + str(i) + '/report_qor.log', str_wns, 1))

    timing_tns = plt.subplot2grid((3, 2), (1, 0), colspan=1)
    timing_tns.set_title('TNS', fontsize=20)
    timing_tns.bar(X_AXIS, tns_array, bw, color='r', label=str_tns)
    timing_tns.set_xticks(X_AXIS + 1 * bw, X_AXIS.astype(str))
    timing_tns.set_xlabel('Номер вариации параметров')
    timing_tns.set_ylabel('Наносекунды')
    timing_wns = plt.subplot2grid((3, 2), (1, 1), colspan=1)
    timing_wns.set_title('WNS', fontsize=20)
    timing_wns.bar(X_AXIS + bw, wns_array, bw, color='y', label=str_wns)
    timing_wns.set_xticks(X_AXIS + 1 * bw, X_AXIS.astype(str))
    timing_wns.set_xlabel('Номер вариации параметров')
    timing_wns.set_ylabel('Наносекунды')
    
    ########### POWER_GRAPH ##########
    internal_power_array = np.array([])
    switching_power_array = np.array([])
    total_power_array = np.array([])

    str_total_power = 'Total Dynamic Power'
    str_internal_power = 'Cell Internal Power'
    str_switching_power = 'Net Switching Power'

    for i in range(1, num_configs_dc + 1, +1):
        point = find_point(addr[j] + '/' + str(i) + '/report_power.log', str_total_power, 0)
        tmp = find_value(addr[j] + '/' + str(i) + '/report_power.log', str_total_power, 1)
        if point == 'mW':
            tmp = tmp*10**3
        elif point == 'nW':
            tmp = tmp/10**3
        elif point == 'uW':
            tmp = tmp
        total_power_array = np.append(total_power_array, tmp)

        point = find_point(addr[j] + '/' + str(i) + '/report_power.log', str_internal_power, 0)
        tmp = find_value(addr[j] + '/' + str(i) + '/report_power.log', str_internal_power, 1)
        if point == 'mW':
            tmp = tmp*10**3
        elif point == 'nW':
            tmp = tmp/10**3
        elif point == 'uW':
            tmp = tmp
        internal_power_array = np.append(internal_power_array, tmp)

        point = find_point(addr[j] + '/' + str(i) + '/report_power.log', str_switching_power, 0)
        tmp = find_value(addr[j] + '/' + str(i) + '/report_power.log', str_switching_power, 1)
        if point == 'mW':
            tmp = tmp*10**3
        elif point == 'nW':
            tmp = tmp/10**3
        elif point == 'uW':
            tmp = tmp
        switching_power_array = np.append(switching_power_array, tmp)                                                       

    power = plt.subplot2grid((3, 2), (2, 0), colspan=2)
    power.set_title('POWER', fontsize=20)
    power.bar(X_AXIS, leaf_cell_count_array, bw, color='b', label=str_total_power)
    power.bar(X_AXIS + bw, internal_power_array, bw, color='y', label=str_internal_power)
    power.bar(X_AXIS + 2 * bw, switching_power_array, bw, color='g', label=str_switching_power)
    power.set_xticks(X_AXIS + 1 * bw, X_AXIS.astype(str))
    power.legend(loc='best', ncol=4, fancybox=True, shadow=True,
                 fontsize='xx-small')
    power.set_xlabel('Номер вариации параметров')
    power.set_ylabel('МикроВатты')
    addr_arr = addr[j].split("/")
    name_core = addr_arr[len(addr_arr) - 2]
    plt.savefig('dc_graph_' + str(name_core) + '.png')
    print(total_cell_area_array.shape)
    print(pd.array(np.arange(1, 12, 1).astype(str)))
    df = pd.DataFrame({'total_cell_area': total_cell_area_array,
                       'comb_area': comb_area_array,
                       'seq_area': seq_area_array,
                       'buff_area': buff_area_array,
                       'leaf_cell_count': leaf_cell_count_array,
                       'comb_cell_count': comb_cell_count_array,
                       'seq_cell_count': seq_cell_count_array,
                       'buff_cell_count': buff_cell_count_array,
                       'tns': tns_array,
                       'wns': wns_array,
                       'total_power': total_power_array,
                       'internal_power': internal_power_array,
                       'switching_power': switching_power_array
                       }, index=pd.array(np.arange(1, 12, 1).astype(str)))
    print(df.T)
    df_t = df.T
    df_t.to_csv('metrics_dc.csv', index = True, header=True)

    plt.show()