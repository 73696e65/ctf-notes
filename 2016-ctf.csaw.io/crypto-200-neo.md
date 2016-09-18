# Neo

Oracle Padding Attack, AES with block size = 16. 

```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

from paddingoracle import BadPaddingException, PaddingOracle
from base64 import b64encode, b64decode
from urllib import quote, unquote
from time import sleep

import requests
import socket

class PadBuster(PaddingOracle):
    def __init__(self, **kwargs):
        super(PadBuster, self).__init__(**kwargs)
        self.session = requests.Session()
        self.wait = kwargs.get('wait', 2.0)

    def oracle(self, data, **kwargs):
        somecookie = b64encode(data)
        payload = {'matrix-id': somecookie }

        print(repr('Data: ' + data))
        print(repr('Payload: ' + somecookie))

        while True:
            try:
                response = self.session.post('http://crypto.chal.csaw.io:8001', data = payload, stream=False, timeout=5, verify=False)
                break
            except (socket.error, requests.exceptions.RequestException):
                logging.exception('Retrying request in %.2f seconds...', self.wait)
                sleep(self.wait)
                continue

        self.history.append(response)

        if response.text.find("Caught exception during AES decryption...") == -1:
            logging.debug('No padding exception raised on %r', somecookie)
            return

        raise BadPaddingException


if __name__ == '__main__':
    import logging
    import sys

    if not sys.argv[1:]:
        print 'Usage: %s <somecookie value>' % (sys.argv[0], )
        sys.exit(1)

    logging.basicConfig(level=logging.INFO)

    encrypted_cookie = b64decode(unquote(sys.argv[1]))

    padbuster = PadBuster()
    cookie = padbuster.decrypt(encrypted_cookie, block_size=16)

    print('Decrypted somecookie: %s => %r' % (sys.argv[1], cookie))
```

Solution:

```
Decrypted somecookie: Wre7CkPi+rFZpTzV+TAtIHzHNtILVrx2XRdynvWoQVrK88FWdeMvn8QmM2RzWzuNbaIwf9m6RfMhwZKmzIqbQ+zMdSFLZ41Y4Db+q3JZOg0= => 
bytearray(b'flag{what_if_i_told_you_you_solved_the_challenge}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f')
```

References:

[https://github.com/mwielgoszewski/python-paddingoracle](https://github.com/mwielgoszewski/python-paddingoracle)
