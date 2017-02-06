# CR3: What is this encryption?

With `rsatool`, we can easily derive the private key: 

```
root@kali64:~$ git clone https://github.com/ius/rsatool
Cloning into 'rsatool'...
cd rsremote: Counting objects: 33, done.
remote: Total 33 (delta 0), reused 0 (delta 0), pack-reused 33
Unpacking objects: 100% (33/33), done.

root@kali64:~$ cd rsatool/
root@kali64:~/rsatool on master $
```

```
root@kali64:~/rsatool on master $ ./rsatool.py -p 0xa6055ec186de51800ddd6fcbf0192384ff42d707a55f57af4fcfb0d1dc7bd97055e8275cd4b78ec63c5d592f567c66393a061324aa2e6a8d8fc2a910cbee1ed9 -q 0xfa0f9463ea0a93b929c099320d31c277e0b0dbc65b189ed76124f5a1218f5d91fd0102a4c8de11f28be5e4d0ae91ab319f4537e97ed74bc663e972a4a9119307
Using (p, q) to initialise RSA instance

n =
a22b591571af4e0d465774b82ccd9952eb479fdfdd551800c2940b1c114e25414fc62c60086563df
6cba2fc164cafd0db253299dddfa57d8c4e87af9f271ef9e0cb10ab85139e5cf52ae39ff7f833380
fbf3439e374c31ea26b2224b2d18cb194e3b3bb13cd6409c978e3e8ff35794ed4cf8cad0305b2b05
b2ee66c09ca272ef

e = 65537 (0x10001)

d =
52a28a135e49b9191495edf9078380b47b059556ea9eb8cb725b23ca1a9b5a6a8c6eec1fc7477afb
d7988c4b1cc43eec62c8f3b4e8eeef229b3be7a643bf811c914f7cc7b01c369346991a8fad3e6969
7f26dc30ed2f7a4fb52867da022806252bcd670bb9b7a181e11853e203c75c06f6511b7fd062e042
ceb5c62d99f5da31

p =
a6055ec186de51800ddd6fcbf0192384ff42d707a55f57af4fcfb0d1dc7bd97055e8275cd4b78ec6
3c5d592f567c66393a061324aa2e6a8d8fc2a910cbee1ed9

q =
fa0f9463ea0a93b929c099320d31c277e0b0dbc65b189ed76124f5a1218f5d91fd0102a4c8de11f2
8be5e4d0ae91ab319f4537e97ed74bc663e972a4a9119307

Saving PEM as priv.key
```

We can compute 'd' also manually using sage:

```
p=0xa6055ec186de51800ddd6fcbf0192384ff42d707a55f57af4fcfb0d1dc7bd97055e8275cd4b78ec63c5d592f567c66393a061324aa2e6a8d8fc2a910cbee1ed9
q=0xfa0f9463ea0a93b929c099320d31c277e0b0dbc65b189ed76124f5a1218f5d91fd0102a4c8de11f28be5e4d0ae91ab319f4537e97ed74bc663e972a4a9119307
e=0x6d1fdab4ce3217b3fc32c9ed480a31d067fd57d93a9ab52b472dc393ab7852fbcb11abbebfd6aaae8032db1316dc22d3f7c3d631e24df13ef23d3b381a1c3e04abcc745d402ee3a031ac2718fae63b240837b4f657f29ca4702da9af22a3a019d68904a969ddb01bcf941df70af042f4fae5cbeb9c2151b324f387e525094c41
c=0x7fe1a4f743675d1987d25d38111fae0f78bbea6852cba5beda47db76d119a3efe24cb04b9449f53becd43b0b46e269826a983f832abb53b7a7e24a43ad15378344ed5c20f51e268186d24c76050c1e73647523bd5f91d9b6ad3e86bbf9126588b1dee21e6997372e36c3e74284734748891829665086e0dc523ed23c386bb520

N = p * q
phi_n = (p-1) * (q-1)
d = inverse_mod(e, phi_n)

decrypted = Mod(c, N) ** d
flag = hex(Integer(decrypted)).decode('hex')
print(flag)
```

```
$ /Applications/SageMath/sage rsa.sage
ALEXCTF{RS4_I5_E55ENT1AL_T0_D0_BY_H4ND}
```