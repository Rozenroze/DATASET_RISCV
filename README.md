# DATASET_RISCV
Датасет реализаций процессорной архитектуры RISC-V.
	|№|РЕАЛИЗАЦИЯ|АВТОР| 
	| ------------------------- |:--------------------:| ---------------------------------------------- |
	| 1| school_riscv| zhelnio|
	| 2| ultraembedded_riscv| ultraembedded | 
	| 3| ultraembedded_biscv| ultraembedded |
	| 4| ssrv| risclite|
	| 5| rv3n| risclite|
	| 6| dark_riscv| darklife|
	| 7| steel-core| rafaelcalcada |
	| 8| vex_riscv| m-labs|
	| 9| lemon_core| nmoroze |
	| 10| picorv32a| YosysHQ |
	
#### Configuration

| Param Name                | Valid Range          | Description                                   |
| ------------------------- |:--------------------:| ----------------------------------------------|
| SUPPORT_SUPER             | 1/0                  | Enable supervisor / user privilege levels.    |
| SUPPORT_MMU               | 1/0                  | Enable basic memory management unit.          |
| SUPPORT_MULDIV            | 1/0                  | Enable HW multiply / divide (RV-M).           |
| SUPPORT_DUAL_ISSUE        | 1/0                  | Support superscalar operation.                |
| SUPPORT_LOAD_BYPASS       | 1/0                  | Support load result bypass paths.             |
| SUPPORT_MUL_BYPASS        | 1/0                  | Support multiply result bypass paths.         |
| SUPPORT_REGFILE_XILINX    | 1/0                  | Support Xilinx optimised register file.       |
| SUPPORT_BRANCH_PREDICTION | 1/0                  | Enable branch prediction structures.          |
| NUM_BTB_ENTRIES           | 2 -                  | Number of branch target buffer entries.       |
| NUM_BTB_ENTRIES_W         | 1 -                  | Set to log2(NUM_BTB_ENTRIES).                 |
| NUM_BHT_ENTRIES           | 2 -                  | Number of branch history table entries.       |
| NUM_BHT_ENTRIES_W         | 1 -                  | Set to log2(NUM_BHT_ENTRIES_W).               |
| BHT_ENABLE                | 1/0                  | Enable branch history table based prediction. |
| GSHARE_ENABLE             | 1/0                  | Enable GSHARE branch prediction algorithm.    |
| RAS_ENABLE                | 1/0                  | Enable return address stack prediction.       |
| NUM_RAS_ENTRIES           | 2 -                  | Number of return stack addresses supported.   |
| NUM_RAS_ENTRIES_W         | 1 -                  | Set to log2(NUM_RAS_ENTRIES_W).               |
| EXTRA_DECODE_STAGE        | 1/0                  | Extra decode pipe stage for improved timing.  |
| MEM_CACHE_ADDR_MIN        | 32'h0 - 32'hffffffff | Lowest cacheable memory address.              |
| MEM_CACHE_ADDR_MAX        | 32'h0 - 32'hffffffff | Highest cacheable memory address.             |	


 	 | -----------------SYSTEMVERILOG------------ |
	| 1		| swerv_eh1	           | westerndigital|
	| 2		| ibex	               | lowRISC       |
	| 3		| simple_riscv	       | tilk          |
	| 4		| nerv_core	           | YosysHQ       |
	| 5		| veer_eh1	           | chipsalliance |
	| 6		| rv32cpu	             | bwitherspoon  |
	| 7		| muntjac	             | lowRISC       |
	| 8		| cva5_core	           | openhwgroup   |
	| 9		| drim_core	           | ic-lab-duth   |
	| 10	|	drims_core	         | ic-lab-duth   |
	| 11	|	risc-v-vector	       | ic-lab-duth   |
	| 12	|	azadi_soc	           | merledu       |
	| 13	|	wolv-z3	             | taneroksuz    |
	| 14	|	rsd_core	           | rsd-devel     |
	| 15	|	cv32e40x	           | openhwgroup   |
	| 16	|	kronos	             | SonalPinto    |
	| 17	|	andreili_riscv	     | andreili      |
	| 18	|	diablo	             | skudlur       | 
	| 19	|	cayde	               | skudlur       | 
	| 20	|	soomrv	             | mathis-s      |
