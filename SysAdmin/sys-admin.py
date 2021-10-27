import os
import subprocess


os.system("ls -la")
subprocess.run(["ls","-l"]) #this uses a list of arguments separated by (,)
subprocess.run(["ls","-l","README.md"]) # show information just about the README file

'''
    Though os.system() is simple to use because it takes a string argument, it is recommended that you use the
    more powerful subprocess.run() function. You can use the subprocess module to spawn new processes, 
    connect to input/output/error pipes, and obtain error codes. The subprocess.run() function can take many new arguments, 
    but those additional arguments are optional.
'''

'''
    The subprocess.run() function is powerful because you can use it to run any Bash command. 
    In this exercise, you will call the uname command to get system information.
'''

command="uname" # it is used to have information about the system
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument]) #we can use variables

command="ps" # this brings information about the active processes
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

print('---------------------------------------------------\n')
print('\n')

#Popen: atakes arguments to set up the new process so the parent can communicate with it via pipes
# PIPE: to send data to or receive data from a program being run as a subprocess
comm = subprocess.Popen(["ls","-la"], stdout=subprocess.PIPE) 
comm2 = subprocess.Popen(["grep","Py"],stdin=comm.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
comm.stdout.close() # close the command 
out, err = comm2.communicate() # to communicate the uotput and the error of the command 2
print(out)
print(err)