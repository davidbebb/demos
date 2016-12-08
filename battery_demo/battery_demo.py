
# add plane

plane = camcam.add_plane(Plane('xy', cutter='1/8_endmill'))
cutter = '1/8_endmill'

# Overall size of board
li_width = 480.0
li_height = 280.0
# wave amplitude
li_amp = 64.0/2/2/math.sqrt(2)
# wave wavelength
li_wl = 64.0/math.sqrt(2)
# depth to cut
li_depth = 8
# radius of ball
li_rad = 14.0/2
# offset for sine waves to cut a wider slot
li_off = (li_rad*2 + 1.5 - 8.0)/2
lib_depth = li_depth + 3


# radius of ball
k_rad=22.0/2
# depth to cut
k_depth = 12
# Overall size of board
k_height = 500.0
k_width =800.0
# wave amplitude
k_amp = 102.0/2/2/math.sqrt(2)
k_wl = 102.0/math.sqrt(2)
# how much the sine waves should be offset
k_off = (k_rad*2 - 8) /2 + 1
# depth to cut extra circle in middle of each joint
kb_depth = k_depth - 4

ball_offset = -53/k_wl

num_k = int(k_width/k_amp/2)-1
num_li = int(li_width/li_amp/2)-1

num_liy = int(li_height/li_amp/2)-1
num_ky = int(k_height/k_amp/2)-1

plane.add_layer('Lithium', material = 'plywood', thickness = 18)
plane.add_layer('Potassium', material = 'plywood', thickness = 18)
plane.add_layer('balls', material = 'plywood', thickness = 18)

# Draw balls to show how big they are
balls=plane.add(Part(name = 'balls', layer='balls', border=Rect(V(0,0), centred=True, width=k_width, height=k_height)))
# lithium board
lithium=plane.add(Part(name = 'Lithium', layer='Lithium', border=Rect(V(0,0), centred=True, width=li_width, height=li_height), ignore_border=True))
# potassium board
potassium=plane.add(Part(name = 'Potassium', layer='Potassium', border=Rect(V(0,0), centred=True, width=k_width, height=k_height), ignore_border=True))

# cut potassium
for i in range (0, num_k+1):
	x = -float(num_k)*k_amp +i * k_amp*2
#	x = -k_width/2+ i * 2* k_amp
	print "i="+str(i)+" x="+str(x)
	if i%2:
		phase = 0
	else:
		phase = math.pi
		for j in range(-1, num_ky/2+1):

			potassium.add(Circle(V(x-k_amp, k_height/2 - j*k_wl+ball_offset*k_wl), rad=k_rad),'balls')
			potassium.add(Circle(V(x+k_amp, k_height/2 - (0.5+j)*k_wl+ball_offset*k_wl), rad=k_rad), 'balls')
			# potassium.add(Hole(V(x-k_amp, k_height/2 - j*k_wl+ball_offset*k_wl), rad=k_rad/2, z1=-kb_depth, z0=-k_depth), 'Potassium')
			# potassium.add(Hole(V(x+k_amp, k_height/2 - (0.5+j)*k_wl+ball_offset*k_wl), z1=-kb_depth, rad=k_rad/2, z0=-k_depth), 'Potassium')

	potassium.add(Lines(SineWave(V(x, k_height/2), V(x, -k_height/2), amplitude=k_amp, wavelength=k_wl, phase=phase, step=1), z1=-k_depth))
	sine_wave = SineWave(V(x, k_height/2), V(x, -k_height/2), amplitude=k_amp, wavelength=k_wl, phase=phase, step=4.01)


	p = Lines(sine_wave, z1=-k_depth)
	p2 = copy.deepcopy(p)
	p3 = copy.deepcopy(p)
	potassium.add(p2.offset_path('left', k_off, {}))
	potassium.add(p3.offset_path('right', k_off, {}))

# cut lithium
for i in range (0, num_li+1):
	x = -float(num_li*li_amp)+i * li_amp*2
#	x = -li_width/2+ i * li_amp
	print "i="+str(i)+" x="+str(x)
	if i%2:
		phase = 0
	else:
		phase = math.pi
		for j in range(-1, num_liy/2+1):
			lithium.add(Circle(V(x-li_amp, li_height/2 - j*li_wl+ball_offset*li_wl), rad=li_rad),'balls')
			lithium.add(Circle(V(x+li_amp, li_height/2 - (0.5+j)*li_wl+ball_offset*li_wl), rad=li_rad),'balls')
			# lithium.add(Hole(V(x-li_amp, li_height/2 - j*li_wl+ball_offset*li_wl), rad=li_rad/2, z1=-lib_depth, z0=-li_depth))
			# lithium.add(Hole(V(x+li_amp, li_height/2 - (0.5+j)*li_wl+ball_offset*li_wl), z1=-lib_depth, rad=li_rad/2, z0=-li_depth))

	lithium.add(Lines(SineWave(V(x, li_height/2), V(x, -li_height/2), amplitude=li_amp, wavelength=li_wl, phase=phase, step=1), z1=-li_depth))

	p = Lines(SineWave(V(x, li_height/2), V(x, -li_height/2), amplitude=li_amp, wavelength=li_wl, phase=phase, step=2), z1=-li_depth)
	p2 = copy.deepcopy(p)

	lithium.add(p.offset_path('left', li_off, {}))
	lithium.add(p2.offset_path('right', li_off, {}))
