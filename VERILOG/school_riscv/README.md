# ULTRAEMBEDDED RISC-V Core
## Описание
32-битное RISC-V ядро, написанное на языке Verilog, и симулятор набора инструкций, поддерживающий RV32IM.  
Это ядро было протестировано и отработано на ПЛИС.  

* 32-разрядное процессорное ядро RISC-V ISA.
* Поддержка RISC-V целочисленных (I), умножения и деления (M) и расширения инструкций CSR (Z) (RV32IMZicsr).
* Поддержка уровней привилегий пользователя, супервизора и машинного режима.
* Базовая поддержка MMU - возможность загрузки Linux с атомической эмуляцией (RV-A).
* Реализация базовой спецификации ISA [v2.1](https://github.com/ultraembedded/riscv/tree/master/doc/riscv_isa_spec.pdf) и привилегированной спецификации ISA [v1.11](https://github.com/ultraembedded/riscv/tree/master/doc/riscv_privileged_spec.pdf).
* Верификация с помощью [Google's RISCV-DV](https://github.com/google/riscv-dv) случайных последовательностей инструкций с использованием косимуляции [C++ ISA](https://github.com/ultraembedded/exactstep).
* Поддержка кэша инструкций/данных, интерфейсов шины AXI или тесно связанной памяти.
* Настраиваемое количество стадий конвейера и опции пересылки результатов.
* Синтезируемый Verilog 2001, совместимый с Verilator и FPGA.
* Coremark:  **2.94 CoreMark/МГц**.
* Dhrystone: **1.25 DMIPS/МГц**.  

Ссылка на авторский репозитарий [тут](https://github.com/ultraembedded/riscv/)  
    
## Принципиальная схема
![image](https://github.com/Rozenroze/DATASET_RISCV/assets/131447538/b965c022-f0ab-498d-a976-6de3e46be0bf)

Данные синтеза доступны по ссылке на [Яндекс диск](https://disk.yandex.ru/d/WoJWMWOvAvWjBQ) 

## Метрики синтеза OpenLane
![openlane_graph_ultraembedded_riscv](https://github.com/Rozenroze/DATASET_RISCV/assets/131447538/a6b62bb4-b956-4f38-8b7a-95424dd46fef)
## Метрики синтеза Design Compiler
![dc_graph_ultraembedded_riscv](https://github.com/Rozenroze/DATASET_RISCV/assets/131447538/c194735a-bd77-4c0c-832c-b4ac76fe0932)
