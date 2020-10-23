
clamp = lambda x : (int(x) & 0x1F)
def to5551(t):
	r = (t[0] / 255) * 31
	g = (t[1] / 255) * 31
	b = (t[2] / 255) * 31
	a = 1
	if len(t) == 4:
		if t[3] == 0:
			a = 0
	return ((clamp(r) << 11)) | (clamp(g) << 6) | (clamp(b) << 1) | a

u8 = lambda x : (x & 0xFF)

def to8888(t):
	return (u8(t[0]) << 24) | (u8(t[1]) << 16) | (u8(t[2]) << 8) | u8(t[3])



