# Consul

Quick & Dirty solution in gdb:

```gdb
b main
display /x *0x601360

r
set $rip=0x400A6A
step

set $rip=real_help
b *0x400B15
c
step

set $rip=help
b *0x0400B3C
c
step


set $rip=dont_call_me
b *0x400AB1
c
step

set $rip=fake_help
b *0x0400AD8
c

define loop_c1
b *0x400891
set $total=55
set $i = 0
  while($i<$total)
  set $i = $i + 1
  set $rip=c1
  c
  end
end

loop_c1

set $rip=c8
c
q
```

```
$ gdb -x script.gdb consul.dcdcdac48cdb5ca5bc1ec29ddc53fb554d814d12094ba0e82f84e0abef065711 | grep flag
R11: 0x6030f0 ("flag{write_in_bernie!}")
```
