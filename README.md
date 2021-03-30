Mongo cluster, deploying a ReplicaSet

### To connect mongo replicas from localhost
```
nano /etc/hosts

127.0.0.1   mongo1 mongo2 mongo3 mongo4

```

### To run the cluster:
``` sh
docker-compose up -d
```
### Connect to the primary node
```
docker-compose exec mongo1 mongo -u "catalog" -p "123456"
```

### Instantiate the replica set or force set primary
Primary is the highest priority.
```
var cfg = {"_id" : "rs0","members" : 
[{"_id" : 0,"host" : "mongo1:27017", "priority": 2},
{"_id" : 1,"host" : "mongo2:27017", "priority": 0},
{"_id" : 2,"host" : "mongo3:27017", "priority": 0},
{"_id" : 3,"host" : "mongo4:27017", "priority": 0}]}
rs.initiate(cfg, { force: true });
rs.reconfig(cfg, { force: true });
```

### Create a cluster admin
```
use admin;
db.createUser({user: "catalog",pwd: "password",roles: [ { role: "userAdminAnyDatabase", db: "admin" },  { "role" : "clusterAdmin", "db" : "admin" } ]});
db.auth("cluster_admin", "password");
```
### Create a collection on a database
```
use my_data;
db.createUser({user: "my_user",pwd: "password",roles: [ { role: "readWrite", db: "my_data" } ]});
db.createCollection('my_collection');
```
### Verify credentials
```
docker-compose exec mongo1 mongo -u "my_user" -p "password" --authenticationDatabase "my_data"
```
### Destory the cluster
```
docker-compose down
```