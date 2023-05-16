set library_cell 
set inv 
set operating_condition 
set flip_flop 

set port_load [load_of ${library_cell}/${inv}]
set input_cap [expr (4*$port_load)]
set_max_capacitance $input_cap [all_inputs]
set_max_transition 0.4 [current_design]
set_max_fanout 16 [current_design]
set_load -pin_load 0.02 [all_outputs]
set_operating_conditions ${operating_condition}
set_driving_cell -no_design_rule -library ${library_cell}  -lib_cell ${flip_flop} [all_inputs]

