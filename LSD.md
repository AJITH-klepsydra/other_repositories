# Sequential Logic circuits

## Flip-flops

sequential circuits are the circuits with memory element and the output of the current output depends on the present as well as the past inputs.
For the memory element we use flip-flops or latches, (initial ideology was to use cascaded not gates )
```mermaid
graph LR
A[Inputs] --> B[Comb circuits]
B -->C((Memory))
B-->D[Output]
C-->A
```

### SR latch
A latch is a sequential circuit that latches  0 or 1. But since we are latching it and if the inputs  are changing then the stored result will be lost, hence we use the clock. 
#### Nor Gate Implementation
![enter image description here](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5AvITcryF1aIatQvFfwMpCLRkMEqd89FnTQ&usqp=CAU) 

#### NAND gate implementation 

![enter image description here](https://circuits-diy.com/wp-content/uploads/2020/02/SR-Flip-Flop-Circuit-74HC00-Truth-Table.png)


// Invalid conditions Explanation

#### Clock
since in sequential circuits, outputs are depended upon the inputs, and we want to latch a certain term. We cannot let the inputs change randomly.
For this we are using a clock digital signal called clock that ensures that the inputs are changed only during
- When the clock is high.
- leading edge
-  falling edge
$$
Duty cycle = time:high/total 
$$

![enter image description here](https://qph.fs.quoracdn.net/main-qimg-b4aa2ddae3cd9567178e08465eb69c77)

#### Triggering methods in flip-flop
triggering is referring to the act of making changes to the input signal based on the clock pulse. Clock pulse is given to the memory element(Latch/ FlipFlop)
```mermaid
graph TB
A[Triggering] --> B(Level Triggering)
A -->C(Edge Triggering)
C-->D[Positive edge triggering]
C-->E[Negative edge triggering]
```
#### Latch and FlipFlop
level triggered/Enable --> Latch
Edge triggered --> Flip FLop
#### SR FLIP FLOP
in nand gate implementation of SR FF to accommodate clk we are introducing two more gates as per the figure, s* = S'+clk`, r*=  r'+clk' 
ie when the clock is low s=r=X s*=r*=1, ie for NAND gate it's a Unused state.
if clock is high then values will be that of set and reset.
![enter image description here](https://i.ibb.co/chX525Z/image.png)

![enter image description here](https://i.ibb.co/NpB2jyj/image.png)

![enter image description here](https://i.ibb.co/tbpktsZ/image.png)

$$
	Q_{n+1}= S+Q_nR'
$$
#### D FlipFlop
Principle behind D flipflop is that, in SR ff if clock is low then it will be memory condition and S is always opposite to R hence.
![enter image description here](https://i.ibb.co/KwYS2DG/image.png)

#### JK FLIPFLOP
![enter image description here](https://i.ibb.co/19tbLWp/image.png)

Making use of 1,1undetermined condition. ie here when J=k=1 occur values of Q and Q_n+1 toggles and racearound condition exists.
![enter image description here](https://i.ibb.co/qxbNT0s/image.png)
![enter image description here](https://i.ibb.co/X5M93zZ/image.png)

#### RACE AROUND CONDITION
// difference between race around and toggling.
![enter image description here](https://i.ibb.co/qpKPkFw/image.png)

#### How to Overcome the race around condition





, JK, T and D. - Master slave flip- flops, . Registers- register with parallel load. Counter design: Asynchronous counters- Binary and BCD counters, timing sequences and state diagrams. Synchronous counters- Binary Up- down counter, BCD counter.
