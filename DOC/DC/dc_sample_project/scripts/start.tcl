set tech CRN28
set top_name "riscv_core"
set NAME_RES "/home/ikorchagin/Documents/tmp/ultraembedded/results"
set NAME "riscv_core"
set clock_name clk_i
set reset_name rst_i
set T_clk 1

source ./scripts/head.tcl

set path_CRN28  
set lib_logic 

set synth [getenv SYNOPSYS]/libraries/syn
set dw [getenv SYNOPSYS]/dw/sim_ver
set minpower [getenv SYNOPSYS]/minpower/syn

set search_path " ${path_CRN28} ${synth} ${dw} }"
# ${minpower}"
set target_library "${lib_logic}"
set link_library  "*  ${lib_logic}  dw_foundation.sldb"
# dw_minpower.sldb "
set synthetic_library {dw_foundation.sldb }
	#dw_minpower.sldb}

set skew 0.15
remove_design -all -quiet
sh rm -f ./work/*.pvl ./work/*.mr ./work/*.syn
set path_rtl ./core
##################################################
analyze  -f sverilog "${path_rtl}/module.v"
##################################################
elaborate $top_name 
link 
uniquify 
source ./scripts/setup_env.tcl
set library_cell tcbn28hpcplusbwp12t30p140lvtssg0p81vm40c
set inv GINVMCOD1BWP12T30P140LVT/I
set operating_condition ssg0p81vm40c
set flip_flop SDFD0BWP12T30P140LVT
set port_load [load_of ${library_cell}/${inv}]
set input_cap [expr (4*$port_load)]
set_max_capacitance $input_cap [all_inputs]
set_max_transition 0.4 [current_design]
set_max_fanout 16 [current_design]
set_load -pin_load 0.02 [all_outputs]
set_operating_conditions ${operating_condition}
set_driving_cell -no_design_rule -library ${library_cell}  -lib_cell ${flip_flop} [all_inputs]
create_clock ${clock_name} -period ${T_clk}
set_clock_uncertainty $skew [get_clock ${clock_name}]
set_input_delay  [expr ${T_clk}/4] -clock [get_clocks ${clock_name}] [remove_from_collection [all_inputs] ${clock_name}]
set_output_delay [expr ${T_clk}/4] -clock [get_clocks ${clock_name}] [all_outputs] 
