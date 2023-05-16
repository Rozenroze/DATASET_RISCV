# DATASET_RISCV
Датасет реализаций процессорной архитектуры RISC-V.
## Методология пополнения датасета новыми реализациями
Датасет на данный момент состоит из 30 реализаций, однако для обучения нейронный сетей, набор данных должен быть многократно больше, чем он есть сейчас. Это означает, что необходимо разработать методологию, с помощью которой данный проект будет возможно продолжить другим исследователям. 
На основе характеристик и состава датасета, результатов синтеза и полученного в ходе практической работы опыта был выдвинут ряд критериев, по которым необходимо отбирать реализации для датасета:  

1.	Реализация взята из открытого источника (предпочтительнее GitHub).
2.	Допустимые языки описания аппаратуры: Verilog, SystemVerilog.
3.	Ядро должно быть написано без использования Python или C в коде.
4.	К реализации должно прилагаться рабочее тестовое окружение, заготовленное автором. Это включает в себя либо тест всего ядра, либо тесты его подмодулей по отдельности. 
5.	В структуре реализации должны присутствовать основные архитектурные модули и принципы RISC-V.
6.	Для реализаций, написанных на Verilog, перед синтезом в OpenLane необходимо проверить код на отсутствие циклов for без структуры generate, не синтезируемых конструкций языка и логических ошибок в блоках always.
7.	При отборе реализаций следует избегать проектов FPGA в силу того, что для успешной имплементации на ПЛИС зачастую используются особые конструкции определенного САПР. Их наличие приводит к невозможности синтеза под ASIC.
8.	В модулях верхнего уровня часто попадаются соединения с модулями отладки. Такого рода соединения следует удалить вручную. То же самое относится и к не синтезируемым конструкциям инициализации памяти.
9.	При отборе реализаций следует обращать внимания на сложность реализации. Чем технически сложнее и функциональнее ядро, тем лучше. 
 
В соответствии с нынешней структурой датасета, были разработаны следующие правила пополнения датасета новыми реализациями:  

1.	Реализация полностью соответствует первому набору критериев.
2.	Перед пополнением, необходимо синтезировать и выгрузить необходимые данные для каждого прогона по конфигурациям синтезатора. Если это реализация на SystemVerilog, то используется только Design Compiler, если на Verilog, то еще и OpenLane. Список необходимых данных включает в себя: отчет по задержкам, отчет по площади, отчет по энергопотреблению, netlist и sdf файлы.
3.	В зависимости от языка описания аппаратуры, реализация распределяется в нужный раздел (VERILOG/SYSTEMVERILOG).
4.	Для создания графического представления собранных статистических данных рекомендуется использовать готовые скрипты на Python. Они находятся по пути /DOC/scripts_for_stat.
5.	Второстепенной задачей является сбор отличительных архитектурных особенностей, показателей производительности и прочей полезной информации. Все данные оформляются в файле README.md по аналогии с уже добавленными реализациями.
6.	Отчеты, код и вся сопутствующая информация кладется в соответствующие разделы.  


## СОСТАВ ДАТАСЕТА
### VERILOG
| №                | РЕАЛИЗАЦИЯ          | АВТОР                                   |
|:-------------------------:|:--------------------:|:----------------------------------------------:|
| 1             | school_riscv                  | zhelnio    |
| 2               | ultraembedded_riscv                  | ultraembedded         |
| 3           | ultraembedded_biscv                  | ultraembedded          |
| 4        | ssrv                  | risclite                 |
| 5       | rv3n                  | risclite             |
| 6        | dark_riscv                  | darklife        |
| 7    | steel-core                  | rafaelcalcada       |
| 8 | vex_riscv                  | m-labs          |
| 9           | lemon_core                  | nmoroze       |
| 10         | picorv32a                  | YosysHQ                |
| ____________ | ________________________________________________ | ________________________________________________ |
### SYSTEMVERILOG
| №                | РЕАЛИЗАЦИЯ          | АВТОР                                   |
|:-------------------------:|:--------------------:|:----------------------------------------------:|
| 1             | swerv_eh1                  | westerndigital    |
| 2               | ibex                  | lowRISC         |
| 3           | simple_riscv                  | tilk          |
| 4        | nerv_core                  | YosysHQ                 |
| 5       | veer_eh1                  | chipsalliance             |
| 6        | rv32cpu                  | bwitherspoon        |
| 7    | muntjac                  | lowRISC       |
| 8 | cva5_core                  | openhwgroup         |
| 9           | drim_core                  | ic-lab-duth       |
| 10         | drims_core                | ic-lab-duth                |
| 11         | risc-v-vector                 | ic-lab-duth                |
| 12         | azadi_soc                 | merledu                 |
| 13         | wolv-z3                 | taneroksuz                |
| 14         | rsd_core                 | rsd-devel              |
| 15         | cv32e40x                 | openhwgroup                |
| 16         | kronos                 | SonalPinto                |
| 17         | andreili_riscv                 | andreili                 |
| 18         | diablo                 | skudlur                |
| 19         | cayde                 | skudlur                |
| 20        | soomrv                 | mathis-s                |
| ____________ | ________________________________________________ | ________________________________________________ |
