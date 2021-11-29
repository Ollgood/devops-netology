#### 1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?
linux:
   ifconfig
   ip a
windows:
    ipconfig
    netsh
#### 2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?
протокол - LLDP
пакет - LLDPD
команда - lldpctl
#### 3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.
VLAN
пакет - vlan
команды - vconfig
```buildoutcfg
auto eth1.10
iface eth1.10 inet static
    address 10.0.0.1
    netmask 255.255.255.0
    vlan-raw-device eth1
```
#### 4. Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.
статический и динамический
возможно сделать с помощью бондинга (в Линукс, пакет ifenslave)
```buildoutcfg
auto bond0

iface bond0 inet static
    address 10.31.1.5
    netmask 255.255.255.0
    network 10.31.1.0
    gateway 10.31.1.254
    bond-slaves eth0 eth1
    bond-mode active-backup
    bond-miimon 100
    bond-downdelay 200
    bond-updelay 200
```
#### 5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.
6 ip адресов, 31 сети /29 можно получить из одной с маской /24. Примеры - 
Network:   10.10.10.8/29
HostMin:   10.10.10.9
HostMax:   10.10.10.14
Broadcast: 10.10.10.15

Network:   10.10.10.0/29
HostMin:   10.10.10.1
HostMax:   10.10.10.6
Broadcast: 10.10.10.7
#### 6. Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.
100.64.0.0/26
#### 7. Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?
ip neigh show в Линукс, arp -a в Windows
ip neigh flush all в Линукс, arp -d в Windows
ip neigh flush IP в Линукс, arp -d IP в Windows