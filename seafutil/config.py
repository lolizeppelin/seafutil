from oslocfg import cfg

# ----------------- server opts -------------------
location_opts = [
    cfg.StrOpt('cfgdir',
               default='/etc/seafile',
               help='Seafile config path'),
    cfg.StrOpt('logdir',
               default='/var/log/seafile',
               help='Seafile log path'),
    cfg.StrOpt('datadir',
               required=True,
               regex='',
                help='Seafile server data path'),
]

ccnet_opts = [
    cfg.StrOpt('name',
               required=True,
               regex=r'^[a-zA-Z0-9_\-]{3,15}$',
               help='Seafile server name'),
    cfg.StrOpt('external',
               default='127.0.0.1',
               required=True,
               regex=r'^[^.].+\..+[^.]$',
               help='Seafile server ip or domain name'),
]

seahub_opts = [
    cfg.StrOpt('seahub',
               help='Seahub app root path'),
    cfg.StrOpt('hubkey',
               required=True,
               secret=True,
               max_length=20,
               help='Seahub secret key')
]
# ----------------- server opts -------------------

# options for server-luanch
luanch_opts = [
    cfg.StrOpt('action',
               required=True,
               choices=['seafile', 'ccnet'],
               help='Seafile luanch type'),
    cfg.StrOpt('config',
               short='c',
               required=True,
               help='Seafile luanch config file'),
    cfg.StrOpt('pidfile',
               required=True,
               help='Process pid file'),
    cfg.IntOpt('timeout',
               short='t',
               default=5,
               min=1, max=30,
               help='Seafile controller luanch timeout'),

]

# options for init script
base_init_opts = [
    cfg.StrOpt('user',
               default='seafile',
               help='seafile process running user'),
    cfg.StrOpt('group',
               default='seafile',
               help='seafile process running group'),
]

admin_init_opts = [
    cfg.StrOpt('email',
               required=True,
               regex=r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b",
               help='Admin email address'),
    cfg.StrOpt('passwd',
               max_length=16,
               required=True,
               help='Admin password'),
]

database_init_opts = [
    cfg.StrOpt('engine',
               default='mysql',
               choices=['mysql'],
               # choices=['mysql', 'postgresql'],
               help='database engine'),
    cfg.StrOpt('dbhost',
               short='o',
               default='127.0.0.1',
               help='database host'),
    cfg.PortOpt('dbport',
                short='P',
                default=3306,
                help='database listen port'),
    # cfg.StrOpt('unix-socket', short='u',
    #            help='database unix socket'
    #            ),
    cfg.StrOpt('dbuser', short='u',
               required=True,
               help='Database user name'),
    cfg.StrOpt('dbpass', short='p',
               secret=True,
               required=True,
               help='Database user password'),
    cfg.StrOpt('scope',
               default='127.0.0.1',
               help='Database user name scope'),
    cfg.StrOpt('rname',
               default='root',
               help='Database root name'),
    cfg.StrOpt('rpass',
               secret=True,
               help='Database root password'),
    cfg.BoolOpt('create',
                default=True,
                help='create new database schema or use existing database schema'),
    cfg.BoolOpt('debug',
                default=False,
                help='connect database use debug mode'),
]

ccnet_init_opts = [
    cfg.PortOpt('port',
                default=10001,
                help='Ccnet server listen port'),
    cfg.StrOpt('dbname',
               default='ccnet',
               help='ccnet database name'),
]

seafile_init_opts = [
    cfg.PortOpt('port',
                default=8082,
                help='Seafile file server public port'),
    cfg.PortOpt('iport',
                default=12001,
                choices=[12001],
                help='Seafile server internal port'),
    cfg.StrOpt('dbname',
               default='seafile',
               help='Seafile database name'),
    cfg.BoolOpt('develop',
                default=False,
                help='Seafile enable development api'),
    cfg.PortOpt('devport',
                default=8080,
                help='Seafile development port')
]

seahub_init_opts = [
    cfg.StrOpt('dbname',
               default='seahub',
               help='seahub database name'),
    cfg.BoolOpt('memcache',
                default=True,
                help='use memcahced as cache'),
]

# -----------------gc opts -------------------
gc_opts = [
    cfg.StrOpt('config',
               short='c',
               default='/etc/seafile.conf',
               help='Seafile luanch config file'),
    cfg.StrOpt('ccent',
               default='/run/seafile/ccnet-server.pid',
               help='Ccnet pid file'),
    cfg.StrOpt('seafile',
               default='/run/seafile/seafile-server.pid',
               help='Seafile pid file'),
    cfg.BoolOpt('remove',
                short='r',
                default=False,
                help='use --rm-deleted remove garbaged repos if true else use --dry-run to show'
                ),
    cfg.BoolOpt('verbose',
                short='v',
                default=False,
                help='verbose output messages'
                ),
    cfg.ListOpt('repos',
                default=[],
                # item_type=types.Integer(),
                help='target repos id list'
                ),
]
# -----------------gc opts -------------------


def list_server_opts():
    return ccnet_opts + location_opts + seahub_opts