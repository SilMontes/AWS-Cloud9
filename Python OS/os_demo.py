import os
print(os.listdir('/home/ec2-user/environment'))
os.rmdir('newOsFolder')
print(os.listdir())