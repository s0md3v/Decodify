# Decodify
It can detect and decode encoded strings, recursively.\
Lets take this string : `s0md3v` and encode it in Base 64
```
czBtZDN2
```
Now lets encode it in hex
```
637a42745a444e32
```
And now again in Base 64
```
NjM3YTQyNzQ1YTQ0NGUzMg==
```
Now lets supply it **Decodify**

<img src='https://i.imgur.com/bsiEyiM.png' />

Boom! Thats what <b>Decodify</b> does. It automatically detects the encoding and decodes it and it does that recursively.

### Supported Encodings and Encryptions
- Caesar ciphers
- Hex
- Decimal
- Base64
- URL
- FromChar
- MD5
- SHA1
- SHA2

**Warning:** Decodify uses third party web services for MD5, SHA1 & SHA2 hash lookups. If you are dealing with sensitive data, you are advised to use the `-s` option which will prevent Decodify to use these services.

##### Decoding Caesar Cipher
You can supply the offest by `--rot` option or you can tell Decodify to decode for 1-20 offest by using `--rot all`

##### Reversing a String
You can reverse a string by using the `-rev` option.

### Usage
Download Decodify with the following command:
```
git clone https://github.com/UltimateHackers/Decodify
```
Now switch to Decodify directory and run the installer with this command:
```
cd Decodify && chmod +x setup.sh && ./setup.sh
```
Now you can run decodify by entering `dcode <string to decode>` in your terminal.

### Please Contribute
If you encounter a valid encoded string which wasn't correctly processed by Decodfiy, please open an issue including the string.<br>
Also you can contribute by adding support for more encodings or by fixing my poorly writting code.
