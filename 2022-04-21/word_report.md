



# work_report







## Kneser-Ney Smoothing



Kneser-ney smooth



### Absolute discounting 

subtracting a fixed discount $d$ from each count.

$P_{abs}(w_i|w_{i-1})=\frac{C(w_{i-1}w_i) -d}{\sum_v C(w_{i-1}v)} + \lambda(w_{i-1})P(w_i)$



$\lambda$ is a interpolation weight.



### Kneser-Ney discounting

统计$w$作为续接词的频率，

$P_{con}(w)=\frac{|v:C(vw)>0|}{v: C(vw')>0}$

$P_{KN}(w_i|w_{i-1})=\frac{max(C(w_{i-1}w_i)- d, 0)}{C(w_{i-1}) }+ \lambda(w_{i-1})P_{con}(w_i)$

和AD理念差不多



