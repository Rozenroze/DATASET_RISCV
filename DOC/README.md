# ДОКУМЕНТАЦИЯ ДАТАСЕТА
Данный раздел включает в себя техническое описание датасета, а так же полезные руководства и скрипты для синтеза.

## СИНТЕЗ С ПОМОЩЬЮ OPENLANE 
Для того, чтобы синтезировать реализацию необходимо пошагово выполнить следующие этапы:
1.	Клонировать репозиторий, предварительно установив необходимые утилиты (Docker, Python 3.6, make). Проверить корректность работы всех инструментов с помощью make test. 
```
sudo apt install git
sudo apt install make
sudo apt install build-essential python3 python3-venv python3-pip 
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install \
      ca-certificates \
      curl \
      gnupg \
      lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o
/etc/apt/keyrings/docker.gpg
echo \
 "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg]
https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo usermod -aG docker $USER
# После установки необходимо перелогиниться или перезагрузить машину!!!
Скачиваем git-репозиторий с OpenLane:
mkdir -p ~/github
cd ~/github
git clone https://github.com/The-OpenROAD-Project/OpenLane.git
cd OpenLane
make
После заверешния установки нужно провести тестовый запуск:
make test
```
3.	Перейти в Docker командой make mount и инициализировать проект с помощью команд -init_design configs и -add_to_designs.
4.	Переместиться в папку designs/<your_project>/src и положить туда все синтезируемые модули. Допускаются только файлы с расширением Verilog. Файлы тестов и дополнительных модулей по типу VGA.v, UART.v, LCD.v и т.д. не синтезируются.
5.	Далее следует открыть config.tcl в папке дизайна и скопировать в него единый шаблон конфигурации (приложение), в нем исправить строчки “DESIGN_NAME” указав название модуля топ уровня реализации, “CLOCK_PORT” и “CLOCK_NET” указав название тактирующего сигнала топ уровня. 
6.	Установить необходимые параметры оптимизатора. 
7.	Запустить процесс синтеза с помощью команды ./flow.tcl.
8.	Вся информация о процессе собирается в папке runs. Под новый запуск создается папка с датой в названии, в ней можно найти логи каждого инструмента маршрута, netlist и sdf файлы, и таблицу metrics.csv со всеми характеристиками синтезированного чипа.



## Features
* 32-bit RISC-V ISA CPU core.
* Superscalar (dual-issue) in-order 6 or 7 stage pipeline.
* Support RISC-V’s integer (I), multiplication and division (M), and CSR instructions (Z) extensions (RV32IMZicsr).
* Branch prediction (bimodel/gshare) with configurable depth branch target buffer (BTB) and return address stack (RAS).
* 64-bit instruction fetch, 32-bit data access.
* 2 x integer ALU (arithmetic, shifters and branch units).
* 1 x load store unit, 1 x out-of-pipeline divider.
* Issue and complete up to 2 independent instructions per cycle.
* Supports user, supervisor and machine mode privilege levels.
* Basic MMU support - capable of booting Linux with atomics (RV-A) SW emulation.
* Implements base ISA spec [v2.1](docs/riscv_isa_spec.pdf) and privileged ISA spec [v1.11](docs/riscv_privileged_spec.pdf).
* Verified using [Google's RISCV-DV](https://github.com/google/riscv-dv) random instruction sequences using cosimulation against [C++ ISA model](https://github.com/ultraembedded/exactstep).
* Support for instruction / data cache, AXI bus interfaces or tightly coupled memories.
* Configurable number of pipeline stages, result forwarding options, and branch prediction resources.
* Synthesizable Verilog 2001, Verilator and FPGA friendly.
* Coremark:  **4.1 CoreMark/MHz**
* Dhrystone: **1.9 DMIPS/MHz** ('legal compile options' / 337 instructions per iteration)
