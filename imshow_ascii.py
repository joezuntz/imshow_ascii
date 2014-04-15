import numpy as np

COLORS = ['black', 'blue', 'cyan', 'green', 'yellow', 'red', 'magenta', 'white']
NCOLOR = len(COLORS)

COLOR_CODES = dict(
        list(zip([
            'grey',
            'red',
            'green',
            'yellow',
            'blue',
            'magenta',
            'cyan',
            'white',
            ],
            list(range(40, 48))
            ))
        )
COLOR_CODES = {c:'\033[%dm'%COLOR_CODES[c] for c in COLOR_CODES}
COLOR_CODES['black'] = ''
BLOCK = unichr(0x2588)
RESET = '\033[0m'

def value_to_color(value, minval, maxval):
	x = (value-1.0*minval) / (maxval-minval)
	#x in range(0,1)
	x = int(x*NCOLOR)
	if x==NCOLOR: x-=1
	c = COLORS[x]
	return c

def color_string_for_value(v, zmin, zmax):
	c = value_to_color(v, zmin, zmax)
	return [COLOR_CODES[c] + ' ' + RESET]

def color_string_for_array(z):
	zmin = z.min()
	zmax = z.max()
	nx, ny = z.shape

	s = []
	for i in xrange(ny):
		for j in xrange(nx):
			v = z[i,j]
			s += color_string_for_value(v, zmin, zmax)
		s.append('\n')
	return ''.join(s)

def main():
	x, y = np.mgrid[0.:50.:1, 0.:50.:1]
	z = (x-25.)**2 + (y-25.)**2
	s = color_string_for_array(z)
	print s

if __name__ == '__main__':
	main()