# Move CWD into the server dir
cd server

: << -
Start the flask debug server with
our 'app' variable from the main
Python file. Note that the '--debug'
flag here has nothing to do with the
fact that this is a debug server.
Flask on its own *ONLY* has a debug
server builtin. The '--debug' flag
allows reloading when the python
files change on disk, among others.
-

# Start the app
flask --app main:app run --debug