
#prefix for binary input is "0b", prifix for hex input is "0x", no need for prefix for decimal numbers

rawKeyInput = 0 #put value here!!


#********************************************************************************************
import base58
import hashlib
rawKeyBinary = bin(rawKeyInput)
rawKeyLen = len(rawKeyBinary)-2
if rawKeyBinary[2]=="0":
	print "key not valid!"
elif rawKeyLen>256:
	print "key value too big!"
else:
	preppendZero=(256-rawKeyLen)*"0"
	keyBody = "10000000"+str(preppendZero) +str(rawKeyBinary[2:len(rawKeyBinary)])+"00000001"
	keyBodyHex = hex(int(keyBody,2))
	keyBodyHexClean = keyBodyHex[2:len(keyBodyHex)-1]
	decodeKey = keyBodyHexClean.decode('hex')
	shaRound1 = hashlib.new('sha256',decodeKey).digest()
	shaRound2 = hashlib.new('sha256',shaRound1).digest()
	checksum = shaRound2.encode('hex')[0:8]
	bodyAndChecksum = str(keyBodyHexClean)+str(checksum)
	preBase58 = bodyAndChecksum.decode('hex')
	WIFcompressed = base58.b58encode(preBase58)
	print "your input value is: " + str(rawKeyInput)
	print "your bitcoin private key in WIF compressed Format is: " +str(WIFcompressed)