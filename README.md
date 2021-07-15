# ДЗ 1.2 Системы контроля версий
### 1) .gitignore
Будут проигнорированы:
* все файлы в папке .terraform, где бы она не находилась
* все файлы, заканчивающиеся на tfstate или имеющие в названии .tfstate.
* crash.log
* все файлы, оканчивающиеся на .tfvars
* override.tf
* override.tf.json
* все файлы, оканчивающиеся на _override.tf
* все файлы, оканчивающиеся на _override.tf.json
* .terraformrc
* terraform.rc