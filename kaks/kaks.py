def paki(arv):
	while '000' in arv: # Pakime nullid
		i = arv.find('000')
		n = 3
		while i+n < len(arv) and arv[i+n] == '0':
			n = n + 1
		if n < 16:
			arv = arv[:i] + 'B' + "{:1X}".format(n) + arv[i+n:]
		else:
			arv = arv[:i] + 'B0' + "{:2X}".format(n) + arv[i+n:]
	# Pakime arvu
	n = len(arv)
	if n < 16:
		arv = 'A' + "{:1X}".format(n) + arv
	else:
		arv = 'A0' + "{:2X}".format(n) + arv
	return arv

sis = open('kakssis.txt', 'rt')
val = open('kaksval.txt', 'wt')

arvud = sis.readline().split()[1:-1] # Eemaldame alguse ja lõpu sümbolid

# Lisame sõnumi alguse sümboli
v = 'E'

for a in arvud:
	v = v + paki(a)

# Lisame sõnumi lõpu sümboli
if len(v) % 2 == 0:
	v = v + 'FD'
else:
	v = v + 'F'

val.write('{0}\n'.format(v))

sis.close()
val.close()
