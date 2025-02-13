# CONFIGURE PROJECT
### Replace all files in hadoop, node_exporter, prometheus and spark with respective file from conf directory
Start prometheus with `./prometheus --config.file=prometheus.yml`
Start master with `start-master -h <your ip address>`
Change all uri with your ip
Start node exporter with `./node_exporter`
start prometheus with `./prometheus --config.file=prometheus.yml`
submit task with `spark-submit --master spark://10.58.94.45:7077  master.py`
