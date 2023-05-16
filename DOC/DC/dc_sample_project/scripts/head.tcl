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