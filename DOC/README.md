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

# После установки необходимо перелогиниться или перезагрузить машину

Скачиваем git-репозиторий с OpenLane:
mkdir -p ~/github
cd ~/github
git clone https://github.com/The-OpenROAD-Project/OpenLane.git
cd OpenLane
make

make test
```
3.	Запустить файловую косноль системы контейнера командой make mount и инициализировать проект с помощью команд -init_design configs и -add_to_designs.
```
make mount

# JSON Configuration File
./flow.tcl -design <design_name> -init_design_config -add_to_designs

# Tcl Configuration File
./flow.tcl -design <design_name> -init_design_config -add_to_designs -config_file config.tcl
```
5.	Переместиться в папку designs/<your_project>/src и положить туда все синтезируемые модули. Допускаются только файлы с расширением Verilog. Файлы тестов и дополнительных модулей по типу VGA.v, UART.v, LCD.v и т.д. не синтезируются.
6.	Далее следует открыть config.tcl в папке дизайна и скопировать в него единый шаблон конфигурации (приложение), в нем исправить строчки “DESIGN_NAME” указав название модуля топ уровня реализации, “CLOCK_PORT” и “CLOCK_NET” указав название тактирующего сигнала топ уровня. 
![image](https://github.com/Rozenroze/DATASET_RISCV/assets/131447538/383a92c6-8ed7-4c13-afb0-df8066c9de60)
8.	Установить необходимые параметры оптимизатора. 
9.	Запустить процесс синтеза с помощью команды ./flow.tcl.
```
./flow.tcl -design <design_name>
```
11.	Вся информация о процессе собирается в папке runs. Под новый запуск создается папка с датой в названии, в ней можно найти логи каждого инструмента маршрута, netlist и sdf файлы, и таблицу metrics.csv со всеми характеристиками синтезированного чипа.

