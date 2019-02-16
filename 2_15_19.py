print(SynthDefs)

p1 >> glass([(0, 2, 4), (0, 3, 5)], dur=4)
p4 >> play("x{-=*}{-=*}{-=*}{-=*}{-=*}")
p4 >> play("x-o{-=*}{-=*}{-=*}{-=*}{-=*}")

p5 >> marimba([(0, 2, 4), (0, 3, 5)], dur=4)
p7 >> play("x-o   o{-=*}{-=*}")


p6 >> varsaw([(0, 2, 4), (0, 3, 5)], dur=4).stop()
d1 >> play("x-o-", hpf=linvar([0,2000],32))

p8 >> viola([3,4,3,4], dur=8)

d1 >> play("x-o-").every(4, "stutter", 4, dur=1, pan=(-1,1), rate=(4, 1/2)).stop()
d2 >> gong([0, 4], dur=[3/4, 3/4, 1/2]).every(3, "offadd", 2).stop()
d3 >> charm([0,1,3,4], dur=1/2).every(5, "offadd", 4, 3/4).stop()

d4 >> pads(dur=4, vib=4, vibdepth=1).stop()

d5 >> play("X O ", crush=4, bits=4).stop()
p1 >> play("x o ", room=0.8, mix=0.8).stop()
d1 >> play("x-o-").every(6.5, "jump", cycle=8).stop()
p1 >> saw([7, 0, 3, 1, 7, 4, 5, 2], dur=1/4, oct=4).slider().stop()
x1 >> marimba([4,3,2,1], dur=8)

z1 >> play("x-o  x-o- x o{-=*}{-=*}{-=*}{-=*}{-=*}{-=*}{-=*}")
p6 >> varsaw([(0, 2, 4), (0, 3, 5)], dur=4).stop()
z8 >> pluck(dur=4, slide=0.5, bend=0.5).stop()

p4.bpm=220
