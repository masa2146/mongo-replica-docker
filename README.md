Mongo cluster, deploying a ReplicaSet

### To run the cluster:
``` sh
docker-compose up
```
### Connect to the primary node
```
docker-compose exec blt-mongo-primary mongo -u "root" -p "password"
```

### Instantiate the replica set
```
rs.initiate({"_id" : "rs0","members" : [{"_id" : 0,"host" : "mongo1:27017"},{"_id" : 1,"host" : "mongo2:27017"},{"_id" : 2,"host" : "mongo3:27017"},{"_id" : 3,"host" : "mongo4:27017"}]});
```
### Set the priority of the master over the other nodes
```
conf = rs.config();
conf.members[0].priority = 2;
rs.reconfig(conf);
```

### Create a cluster admin
```
use admin;
db.createUser({user: "cluster_admin",pwd: "password",roles: [ { role: "userAdminAnyDatabase", db: "admin" },  { "role" : "clusterAdmin", "db" : "admin" } ]});
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
docker-compose exec blt-mongo-primary mongo -u "my_user" -p "password" --authenticationDatabase "my_data"
```
### Destory the cluster
```
docker-compose down
```

### To connect mongo replicas from localhost
```
nano /etc/hosts

127.0.0.1   mongo1
127.0.0.1   mongo2
127.0.0.1   mongo3
127.0.0.1   mongo4

```