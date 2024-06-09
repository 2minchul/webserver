import multiprocessing

workers = multiprocessing.cpu_count()

# bind - The server socket to bind
bind = '0.0.0.0:8000'

# backlog - The maximum number of pending connections
# Generally in range 64-2048
backlog = 2048

# worker_class - The type of workers to use
worker_class = 'gevent'

# worker_connections - The maximum number of simultaneous clients.
# This setting only affects the Eventlet and Gevent worker types.
worker_connections = 1000

# max_requests - The maximum number of requests a worker will process
# before restarting
# Any value greater than zero will limit the number of requests a work
# will process before automatically restarting. This is a simple method
# to help limit the damage of memory leaks.
max_requests = 0

# max_requests_jitter - The maximum jitter to add to the max-requests setting
# The jitter causes the restart per worker to be randomized by
# randint(0, max_requests_jitter). This is intended to stagger worker
# restarts to avoid all workers restarting at the same time.
max_requests_jitter = 1000

# timeout - Workers silent for more than this many seconds are killed
# and restarted
timeout = 120

# graceful_timeout - Timeout for graceful workers restart
# How max time worker can handle request after got restart signal.
# If the time is up worker will be force killed.
graceful_timeout = 10

# keep_alive - The number of seconds to wait for requests on a
# Keep-Alive connection
# Generally set in the 1-5 seconds range.
keep_alive = 4


# limit_request_line - The maximum size of HTTP request line in bytes
# Value is a number from 0 (unlimited) to 8190.
# This parameter can be used to prevent any DDOS attack.
limit_request_line = 0

# limit_request_fields - Limit the number of HTTP headers fields in a request
# This parameter is used to limit the number of headers in a request to
# prevent DDOS attack. Used with the limit_request_field_size it allows
# more safety.
# By default this value is 100 and can’t be larger than 32768.
limit_request_fields = 100

# limit_request_field_size - Limit the allowed size of an HTTP request
# header field.
# Value is a number from 0 (unlimited) to 8190.
limit_request_field_size = 0


# reload - Restart workers when code changes
reload = False

# spew - Install a trace function that spews every line executed by the server
spew = False

# check_config - Check the configuration
check_config = False

# preload_app - Load application code before the worker processes are forked
# By preloading an application you can save some RAM resources as well as
# speed up server boot times. Although, if you defer application loading to
# each worker process, you can reload your application code easily by
# restarting workers.
preload_app = False

# sendfile - Enables or disables the use of sendfile()
sendfile = False

# reuse_port - Set the SO_REUSEPORT flag on the listening socket.
reuse_port = True

# daemon - Daemonize the Gunicorn process.
# Detaches the server from the controlling terminal and enters the background.
daemon = False

# user - Switch worker processes to run as this user
# A valid user id (as an integer) or the name of a user that can be retrieved
# with a call to pwd.getpwnam(value) or None to not change the worker process
# user
user = None

# group - Switch worker process to run as this group.
# A valid group id (as an integer) or the name of a user that can be retrieved
# with a call to pwd.getgrnam(value) or None to not change the worker
# processes group.
group = None

# umask - A bit mask for the file mode on files written by Gunicorn
# Note that this affects unix socket permissions.
# A valid value for the os.umask(mode) call or a string compatible with
# int(value, 0) (0 means Python guesses the base, so values like “0”, “0xFF”,
# “0022” are valid for decimal, hex, and octal representations)
umask = 0

# initgroups - If true, set the worker process’s group access list with all of
# the groups of which the specified username is a member, plus the specified
# group id.
initgroups = False

# accesslog - The Access log file to write to.
# “-” means log to stdout.
accesslog = '-'

# access_log_format - The access log format
#
# Identifier  |  Description
# ------------------------------------------------------------
# h            ->  remote address
# l            -> ‘-‘
# u            -> user name
# t            -> date of the request
# r            -> status line (e.g. GET / HTTP/1.1)
# m            -> request method
# U            -> URL path without query string
# q            -> query string
# H            -> protocol
# s            -> status
# B            -> response length
# b            -> response length or ‘-‘ (CLF format)
# f            -> referer
# a            -> user agent
# T            -> request time in seconds
# D            -> request time in microseconds
# L            -> request time in decimal seconds
# p            -> process ID
# {header}i    -> request header
# {header}o    -> response header
# {variable}e  -> environment variable
# ---------------------------------------------------------------
#
# Use lowercase for header and environment variable names, and put {...}x names
# inside %(...)s. For example:
#
# %({x-forwarded-for}i)s
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# disable_redirect_access_to_syslog - Disable redirect access logs to syslog.
disable_redirect_access_to_syslog = False

# errorlog - The Error log file to write to.
# “-” means log to stderr.
errorlog = '-'

# loglevel - The granularity of Error log outputs.
# Valid level names are:
# 1. debug
# 2. info
# 3. warning
# 4. error
# 5. critical
loglevel = 'info'

# capture_output - Redirect stdout/stderr to specified file in errorlog.
capture_output = True

# syslog - Send Gunicorn logs to syslog
syslog = False

# proc_name - A base to use with setproctitle for process naming.
# This affects things like `ps` and `top`.
# It defaults to ‘gunicorn’.
proc_name = 'gunicorn'
