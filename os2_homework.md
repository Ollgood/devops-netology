#### 1. На лекции мы познакомились с node_exporter. В демонстрации его исполняемый файл запускался в background. Этого достаточно для демо, но не для настоящей production-системы, где процессы должны находиться под внешним управлением. Используя знания из лекции по systemd, создайте самостоятельно простой unit-файл для node_exporter:
####  поместите его в автозагрузку,
#### предусмотрите возможность добавления опций к запускаемому процессу через внешний файл (посмотрите, например, на ```systemctl cat cron```),
#### удостоверьтесь, что с помощью systemctl процесс корректно стартует, завершается, а после перезагрузки автоматически поднимается.
```buildoutcfg
vagrant@vagrant:/home$ sudo reboot now
Connection to 127.0.0.1 closed by remote host.
Connection to 127.0.0.1 closed.
 ~/vagrant_cofings  vagrant ssh                                                                                               SIG(127) ↵  6633  21:09:18
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-80-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun 21 Nov 2021 06:09:33 PM UTC

  System load:  0.0               Processes:             123
  Usage of /:   3.0% of 61.31GB   Users logged in:       0
  Memory usage: 17%               IPv4 address for eth0: 10.0.2.15
  Swap usage:   0%


This system is built by the Bento project by Chef Software
More information can be found at https://github.com/chef/bento
Last login: Sun Nov 21 13:38:24 2021 from 10.0.2.2
vagrant@vagrant:~$ systemctl status node_exporter
● node_exporter.service - node exporter for Prometheus
     Loaded: loaded (/lib/systemd/system/node_exporter.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2021-11-21 18:09:30 UTC; 7s ago
   Main PID: 786 (node_exporter)
      Tasks: 4 (limit: 1071)
     Memory: 12.1M
     CGroup: /system.slice/node_exporter.service
             └─786 /usr/sbin/node_exporter

Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:115 level=info collector=thermal_zone
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:115 level=info collector=time
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:115 level=info collector=timex
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:115 level=info collector=udp_queues
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:115 level=info collector=uname
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:115 level=info collector=vmstat
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:115 level=info collector=xfs
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:115 level=info collector=zfs
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=node_exporter.go:199 level=info msg="Listening on" address=:9100
Nov 21 18:09:31 vagrant node_exporter[786]: ts=2021-11-21T18:09:31.045Z caller=tls_config.go:195 level=info msg="TLS is disabled." http2=false
```

unit-file:
```buildoutcfg
[Unit]
Description=node exporter for Prometheus
After=network-online.target

[Service]
User=root
Group=root
EnvironmentFile=-/etc/default/node_exporter
ExecStart=/usr/sbin/node_exporter $EXTRA_OPTS
[Install]
WantedBy=multi-user.target
```
#### 2. Ознакомьтесь с опциями node_exporter и выводом `/metrics` по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.
node_load1 0
node_load15 0
node_load5 0

node_memory_Active_file_bytes
node_memory_Buffers_bytes
node_memory_Cached_bytes
node_memory_SwapFree_bytes
node_memory_SwapTotal_bytes
process_cpu_seconds_total
node_vmstat_oom_kill

node_netstat_TcpExt_ListenDrops
node_netstat_TcpExt_TCPTimeouts

process_max_fds
process_open_fds

node_filesystem_free_bytes
node_filesystem_avail_bytes
node_filesystem_size_bytes
#### 4. Можно ли по выводу `dmesg` понять, осознает ли ОС, что загружена не на настоящем оборудовании, а на системе виртуализации?
Да, по выводу ```[    0.000000] DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006
[    0.000000] Hypervisor detected: KVM```
#### 5. Как настроен sysctl `fs.nr_open` на системе по-умолчанию? Узнайте, что означает этот параметр. Какой другой существующий лимит не позволит достичь такого числа (`ulimit --help`)?
1048576
это ограничение на количество открытых файлов для всех процессов.
ограничение в ```ulimit -n```, в настоящий момент - ```open files                      (-n) 1024```
#### 6. Запустите любой долгоживущий процесс (не `ls`, который отработает мгновенно, а, например, `sleep 1h`) в отдельном неймспейсе процессов; покажите, что ваш процесс работает под PID 1 через `nsenter`. Для простоты работайте в данном задании под root (`sudo -i`). Под обычным пользователем требуются дополнительные опции (`--map-root-user`) и т.д.
```buildoutcfg
root@vagrant:~# nsenter --target 1548 --pid --mount
root@vagrant:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   9828   592 pts/2    S    18:52   0:00 sleep 1h
root          13  0.0  0.4  11560  4032 pts/2    S    18:57   0:00 -bash
root          22  0.0  0.3  13216  3272 pts/2    R+   18:57   0:00 ps aux
```
#### 7. Найдите информацию о том, что такое `:(){ :|:& };:`. Запустите эту команду в своей виртуальной машине Vagrant с Ubuntu 20.04 (**это важно, поведение в других ОС не проверялось**). Некоторое время все будет "плохо", после чего (минуты) – ОС должна стабилизироваться. Вызов `dmesg` расскажет, какой механизм помог автоматической стабилизации. Как настроен этот механизм по-умолчанию, и как изменить число процессов, которое можно создать в сессии?
```buildoutcfg
[ 1795.353522] cgroup: fork rejected by pids controller in /user.slice/user-1000.slice/session-5.scope
[ 3510.585202] hrtimer: interrupt took 816281 ns
```
изменить число юзер процессов можно через ```ulimit -u```, либо изменив параметр в ```/usr/lib/systemd/system/user-.slice.d/10-defaults.conf```, где прописано, какой процент от общесистемного максимума может быть использовано пользователем