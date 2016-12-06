
# add plane

plane = camcam.add_plane(Plane('xy', cutter='8mm_endmill'))
cutter = '1/8_endmill'



li_width = 64.0
li_height = 480.0
li_amp = 64.0/2/2/math.sqrt(2)
li_wl = 64.0/math.sqrt(2)
li_depth = 3
li_rad = 14/2

k_rad=22/2

k_depth = 6.12

k_width = 105.0
k_height =480.0
k_amp = 102.0/2/2/math.sqrt(2)
k_wl = 102.0/math.sqrt(2)

ball_offset = -54/k_wl

num_k = int(k_width/k_amp/2)-1
num_li = int(li_width/li_amp/2)-1

num_liy = int(li_height/li_wl/2)-1
num_ky = int(k_height/k_wl/2)-1

plane.add_layer('Lithium', material = 'plywood', thickness = 18)
plane.add_layer('Potassium', material = 'plywood', thickness = 18)
plane.add_layer('balls', material = 'plywood', thickness = 18)

balls=plane.add(Part(name = 'balls', layer='balls', border=Rect(V(0,0), centred=True, width=k_width, height=k_height)))
lithium=plane.add(Part(name = 'Lithium', layer='Lithium', ignore_border=True))
pottassium=plane.add(Part(name = 'Potassium', layer='Potassium', ignore_border=True))#V(0,0), centred=True, width=k_width, height=k_height)))


for i in range (0, num_k+1):
	x = -float(num_k*k_amp)+i * k_amp*2
#	x = -k_width/2+ i * 2* k_amp
	print "i="+str(i)+" x="+str(x)
	if i%2:
		phase = 0
	else:
		phase = math.pi
		for j in range(-1, num_ky+1):
			pottassium.add(Circle(V(x-k_amp, k_height/2 - j*k_wl+ball_offset*k_wl), rad=k_rad),'balls')
			pottassium.add(Circle(V(x+k_amp, k_height/2 - (0.5+j)*k_wl+ball_offset*k_wl), rad=k_rad), 'balls')
			pottassium.add(Hole(V(x-k_amp, k_height/2 - j*k_wl+ball_offset*k_wl), rad=k_rad/2, z1=-k_depth), 'Potassium')
			pottassium.add(Hole(V(x+k_amp, k_height/2 - (0.5+j)*k_wl+ball_offset*k_wl), z1=-k_depth, rad=k_rad/2), 'Potassium')
	pottassium.add(Lines(SineWave(V(x, k_height/2), V(x, -k_height/2), amplitude=k_amp, wavelength=k_wl, phase=phase, step=1), z1=-k_depth))


for i in range (0, num_li+1):
	x = -float(num_li*li_amp)+i * li_amp*2
#	x = -li_width/2+ i * li_amp
	print "i="+str(i)+" x="+str(x)
	if i%2:
		phase = 0
	else:
		phase = math.pi
		for j in range(-1, num_liy):
			lithium.add(Circle(V(x-li_amp, li_height/2 - j*li_wl+ball_offset*li_wl), rad=li_rad),'balls')
			lithium.add(Circle(V(x+li_amp, li_height/2 - (0.5+j)*li_wl+ball_offset*li_wl), rad=li_rad),'balls')
			lithium.add(Hole(V(x-li_amp, li_height/2 - j*li_wl+ball_offset*li_wl), rad=li_rad/2, z1=-li_depth))
			lithium.add(Hole(V(x+li_amp, li_height/2 - (0.5+j)*li_wl+ball_offset*li_wl), z1=-li_depth, rad=li_rad/2))
	lithium.add(Lines(SineWave(V(x, li_height/2), V(x, -li_height/2), amplitude=li_amp, wavelength=li_wl, phase=phase, step=1), z1=-li_depth))


