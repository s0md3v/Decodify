# Decodify
It can detect and decode encoded strings, recursively. Its currently in beta phase.

Lets take this string : <b>teamultimate.in</b> and encode it with Hex, URL, Base64 and FromChar encoding, respectively.<br>
Now lets pass this encoded string to Decodify:

<img src='https://i.imgur.com/toXdaa1.png' />

Boom! Thats what <b>Decodify</b> does.

### Supported Encodings and Encryptions
- [x] Caesar ciphers
- [x] Binary
- [x] Hex
- [x] Decimal
- [x] Base64
- [x] URL
- [x] FromChar
- [x] MD5
- [x] SHA1
- [x] SHA2

##### Decoding Caesar Cipher
You can supply the offest by <b>--rot</b> option or you can tell Decodify to decode for 1-20 offest by using <b>--rot all</b>

<img src='https://i.imgur.com/uuoTgua.png' />

### Installing Decodify
Download Decodify with the following command:
```
git clone https://github.com/UltimateHackers/Decodify
```
Now switch to Decodify directory and run the installer with this command:
```
cd Decodify && chmod +x ./decodify.sh
```
Now you can run decodify by entering <b>dcode</b> in your terminal.<br>
Happy decoding!

### Please Contribute
Decodify needs huge improvements and bug fixes.<br>
If you encounter a valid encoded string which wasn't correctly processed by Decodfiy, please open an issue including the string.<br>
Also you can contribute by adding support for more encodings or by fixing my poorly writting code.
