Write a small report on which you study possible models and approaches to take when controlling the car having in account the following specifications.

Wheelbase: 1550mm

Mass: ~270 kg

Weight distributions front/back: ~50/50

Steering angle limits: ±40°

Steering ratio: 2.25

I suck at fisics but here we go:
---

I will be basing my research on [this paper](https://www.researchgate.net/figure/Sideslip-angle_fig1_259632108) as i only have 12º Grade education worth of fisics and i studied mostly projectiles, and other "inanimate objects"

Also as addendum i will be using latex like formatting for math so that according to this it renders properly on github i hope(i dont have a lot of experience on this kind of formatting)

## Steering Wheel Turning

First assuming that the car is being drived by a person with the ability to react instantly, we can say that the wheel that controls the car is able to spin 90º each way(which now that i remember i think thats precisely how much the prototype car wheelhandle spins).

The steering ratio is calculated as such(according to [wikipedia](https://en.wikipedia.org/wiki/Steering_ratio) the free encyclopedia):
	$( sr = { \pm tal \over \pm sal } )$

Where $sr$ represents the steering ratio, $tal$ represents the positive and negative maximum turn angles of the steering wheel and $sal$ represents the maximum and minimum angle that the actual front wheels can turn.  

As said previously we can just: 
	$( \pm tal = { sr * \pm sal } )$
Arriving at the aforementioned $( \pm 90º )$.

## Yaw, Torque and Avoiding under-steering and over-steering

We can presuppose that the objective a autonomous driving automata will follow most of the time is to at the very least keep the vehicle inside the road or some inside of some kind of bounds that the automata is to perceive as a path.

We start by simplifying the scenario and saying that the car somehow is in a state where the velocity is constant and will remain so unless otherwise stated. This will make the Yaw acceleration denoted by the $\ddot\psi$ 0 and the sideslip velocity 0 ie: $(\dot\beta)=0$. Im also gonna assume the steering of the vehicle is controlled only by the front wheels and the traction is made by its back wheel

(_off note, anotação matemática com isto e bue fácil e percetível devia ter pesquisado isto mais cedo_)

As also said in the paper we can arrive at the torque equation like so:
$$(F_{Lf}l=ma_yl_r)$$

Basically $F_{Lf}$ represents the lateral direction force on the front of the car
, $l$ represents represents the distance in meters from the center of the back tire to the respective center of the front tire in the same side, then $ma_y$ represents the centrifugal force that is exerted on the center of the car lastly we have $l_r$ which represents the length from the center of the rear tires to the center of mass

We can first yeet the $l$ to the other side like so:
$$(F_{Lf}=ma_y{l_r\over l})$$
If i havent made it obvious im gonna try to get rid of the l's im guessing that this line:
```
Weight distributions front/back: ~50/50
```
is telling us that the center of mass is well centered that is lr= lf, if $lr+lf=l$ then we get
$$(F_{Lf}={ma_y\over 2})$$

Now we can just 
$$ c_{\alpha f}*\alpha_f={ma_y\over 2}$$

Where the alfa thingie represents the angle that the front wheel makes in relation to its respective back wheel. Now we just fetch some details from the paper and get to:

$$( c_{\alpha f}*({\delta +\beta -{l_f*\psi \over v}})={ma_y\over 2} )$$

We want the $\delta$ or the steering angle so im just gonna skip a few steps because this notation is takes time. Im also gonna plug $v=$, which describes the velocity related to the radius and velocity of yaw

$$( {\delta}={ma_y\over 2*c_{\alpha f}}-\beta+ -{l_f*\bcancel{\dot\psi} \over \bcancel{\dot\psi}*r} )$$

This gives is a very rough model i would use to check what angle should the wheels be in when turning. to make shure we dont overturn $\Delta\alpha$ must be equal to 0 we can add $$(\Delta\alpha= \delta-{l \over r})$$

(also dont forget that the steering wheel turn $\neq$ the actual degree of the wheel so supposing that the car is always uniquely controlled by the steering wheel we would have to multiply by the steering ratio as previously mentioned)

To the former to garantee we arent doing weird stuff.Its not the best model as im still a bit unshure on what exaclty is the difference between slippage velocity and yaw velocity along with other variables(does drifting count as slippage?)

With this i modestly ask to not be in charge of finding out what the model is. Regardless i hope that the exercises i made show that im interested in the project.

