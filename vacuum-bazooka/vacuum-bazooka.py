
# rectangle with 4 holes

# variables we might want to edit later
tube_rad = 36/2
width=2*tube_rad + 12
orad = width/2
top = 50
# add plane - xy is standard
# main class = camcam
# This is adding to camcam
# camcam understands planes - longer term is to add multiple planes - at the moment is has the xy plane - this contains the parts and layers
# layer has: thickness, material, and a z-offset from plane at z-zero (ignored at moment)
# part exists in it's own layer, and can modify other layers (ie part through top of baseboard will cut perspex). Multiple parts can exsist in the same layer. If you don't need to print it, it doesn't need to have its own layer e.g. a stepper motor is not something we can cut (yet), so it just needs to make holes in the layers it's mounted to or going through.
#
# camcam/path.py defines: planes, parts, path groups & paths & points, layers [core concepts]
# camcam/shapes.py defines: shapes (e.g. circles, holes, screws, bolts, polygons & modules
# camcam/parts.py defines: stepper  motors, inserts
# camcam/Milling.py defines: cutting modes (e.g. diagram, makespacerouter, laser...), bolt sizes, insert sizes, tools & materials [essentially a config files]


# add plane

plane = camcam.add_plane(Plane('xy', cutter='1/8_endmill'))
plane.add_layer('end', material = 'pvc', thickness = 6)

border = Path(closed=True, side='out')
border.add_point(V(orad,0))
border.add_point(V(orad,top))
border.add_point(V(-orad,top))
border.add_point(V(-orad,0))
border.add_point(PArc(V(0,0), radius=orad))

part=plane.add(Part(name = 'end', layer='end', border=Rect(V(0,0), centred=True, width=400, height=400)))
part.add(Hole(V(0,0), rad=tube_rad))
