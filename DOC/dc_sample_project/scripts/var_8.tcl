##################################################
set_cost_priority -delay
#set_max_area 0
#set_dynamic_optimization true
set_leakage_optimization true
set_host_options -max_cores 16
compile
report_qor >    $NAME_RES/8/report_qor.log
report_power >    $NAME_RES/8/report_power.log
report_area -hier >>   $NAME_RES/8/report_area.log
report_timing >> $NAME_RES/8/report_timing.log
write -hier -format verilog -output $NAME_RES/8/netlist.v 
write_sdf $NAME_RES/8/sdf.sdf
##################################################