# nptu_db

### Start service:

```sh
$ docker-compose up -d
```
### Start service ONLY FIRST TIME:
```sh
$  docker exec -it rs1 bash
/  mongo rs1:27041
> cfg =  {
		"_id" : "RS",
		members : [
					{
						"_id" : 0,
						"host" : "rs1:27041"
					},
					{
						"_id" : 1,
						"host" : "rs2:27042"
					},
					{
						"_id" : 2,
						"host" : "rs3:27043"
					},
		]
		
	}
>  rs.initiate(cfg);
RS:SECONARY>  rs.status()
RS:PRIMARY>  exit
/  exit
```
### Service:
*Your IP/myapp        Read Service content
*Your IP/list_user    List User
*Your IP/login        Login Page
*Your IP/myapp/del    Delete Service content
*Your IP/myapp/add    Add Service content
*Your IP/myapp/upd    Update Service content
*Your IP/create_user  Create User



### Stop service:

```sh
$ docker-compose down
```
