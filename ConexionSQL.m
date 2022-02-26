pkg load database
conn = pq_connect (setdbopts ('dbname','Parcial1','host','localhost', 'port','5432','user','javier','password','javier'))

N=pq_exec_params(conn, "insert into javierbarrios values ('Juan Ramon Hernandez Castro','201512779');")
N=pq_exec_params(conn, 'select * from javierbarrios;')