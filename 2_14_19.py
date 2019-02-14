print(SynthDefs)

p1 >> sawbass([(0, 2, 4), (0, 3, 5)], dur=4)
p2 >> play("x-o-")
p3 >> play("x-o{-=*}")
p4 >> play("x{-=*}{-=*}{-=*}{-=*}{-=*}")
p5 >> marimba([(0, 2, 4), (0, 3, 5)], dur=4)
p7 >> play("x-o   o{-=*}{-=*}")


p6 >> varsaw([(0, 2, 4), (0, 3, 5)], dur=4).stop()

p8 >> viola("x-o-")
