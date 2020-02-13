import microbit
import sinobit

pads = [ microbit.pad5, microbit.pad4, microbit.pad3, microbit.pad0, microbit.pad1, microbit.pad2 ]

while True:
    for x,p in enumerate(pads):
        for i in range(0,(3*p.read_analog()-800)//200):
            sinobit.display.set_pixel(i,x*2+1,True)

    sinobit.display.write()
    microbit.sleep(100)
    sinobit.display.clear()

