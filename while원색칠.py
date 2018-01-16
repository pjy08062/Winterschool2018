import turtle as t
t.speed(5)

color_list=['orange','light orange']
n=0
while n<2:
   t.fillcolor(color_list[n])
   t.begin_fill()
   t.circle(100)
   t.end_fill()
   fd(10)
   n=n+1
 



